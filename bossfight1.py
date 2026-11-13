import json 
from logging import Handler
import mimetypes
import os
import threading
import time
import urllib.parse
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

# vars
start_timeout = 120 # seconds to wait before the page loads
ping_timeout = 15 # seconds without a ping before assuiming that tge tab closed

# this part was asisted with ai

# this is the part that detects if the bossfight has finished and if the player has won or lost and the js that 
# alerts the server

BRIDGE_TEMPLATE = """
<script>
(function () {
  var CFG = __CFG__;
  var sent = false;
 
  // reads top-level var / let / const by name
  function read(name) {
    try { return (0, eval)(name); } catch (e) { return undefined; }
  }
 
  function snapshot() {
    var out = {};
    CFG.watch.forEach(function (n) { out[n] = read(n); });
    return out;
  }
 
  function send(won, extra) {
    if (sent) return;
    sent = true;
    fetch("/__result", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ won: !!won, vars: snapshot(), extra: extra || {} })
    }).catch(function () {});
  }
 
  window.bossFightEnd = function (won, extra) { send(won, extra); };
 
  setInterval(function () {
    if (sent) return;
    if (CFG.win && read(CFG.win)) send(true);
    else if (CFG.lose && read(CFG.lose)) send(false);
  }, 300);
 
  setInterval(function () {
    if (!sent) fetch("/__ping").catch(function () {});
  }, 2000);
  fetch("/__ping").catch(function () {});
})();
</script>
"""

class _shared: 
    def __init__(self):
        self.result = None
        self.last_ping = None
        self.done = threading.Event()

    def _make_handler(shared, root, entry, bridge):
        root = os.path.realpath(root)

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def _send(self, code, body=b"", ctype="text/plain"):
                # pasted from ai
                self.send_response(code)
                self.send_header("Content-Type", ctype)
                self.send_header("Content-Length", str(len(body)))
                self.send_header("Cache-Control", "no-store")
                self.end_headers()
                if body:
                    self.wfile.write(body)

            def _resolve(self, url_path):
                rel = urllib.parse.unquote(urllib.parse.urlparse(url_path).path)
                rel = rel.lstrip("/") or entry
                full = os.path.realpath(os.path.join(root, rel))
                # block paths outside the folder
                if os.path.commonpath([root, full]) != root:
                    return None
                if os.path.isdir(full):
                    full = os.path.join(full, "index.html")
                return full if os.path.isfile(full) else None
 
            def do_GET(self):
                if self.path.startswith("/__ping"):
                    shared.last_ping = time.time()
                    self._send(204)
                    return
 
                full = self._resolve(self.path)
                if full is None:
                    self._send(404, b"Not found")
                    return
 
                with open(full, "rb") as f:
                    data = f.read()
 
                ctype = mimetypes.guess_type(full)[0] or "application/octet-stream"
                if full.lower().endswith((".html", ".htm")):
                    text = data.decode("utf-8", errors="replace")
                    idx = text.lower().rfind("</body>")
                    if idx == -1:
                        text += bridge
                    else:
                        text = text[:idx] + bridge + text[idx:]
                    data = text.encode("utf-8")
                    ctype = "text/html; charset=utf-8"
                elif ctype.startswith("text/") or ctype in (
                    "application/javascript", "application/json"
                ):
                    ctype += "; charset=utf-8" if "charset" not in ctype else ""
                self._send(200, data, ctype)
 
            def do_POST(self):
                if self.path != "/__result":
                    self._send(404, b"Not found")
                    return
                try:
                    length = int(self.headers.get("Content-Length", 0))
                    shared.result = json.loads(self.rfile.read(length) or b"{}")
                except (ValueError, json.JSONDecodeError):
                    self._send(400, b"Bad request")
                    return
                self._send(200, b"ok")
                shared.done.set()
 
        return Handler
    # end of pasted from ai segment
def startbossfight1(folder, entry="index.html", win_var=None, lose_var=None, watch_vars=(), open_browser=True):
    """
     folder      path to the boss fight folder
    entry       html file to open (default index.html)
    win_var     JS variable name. When truthy, the fight is a win.
    lose_var    JS variable name. When truthy, the fight is a loss.
    watch_vars  JS variable names to read back when the fight ends.
    """
    """
    folder      path to your boss fight folder
    entry       HTML file to open (default index.html)
    win_var     JS variable name. When truthy, the fight is a win.
    lose_var    JS variable name. When truthy, the fight is a loss.
    watch_vars  JS variable names to read back when the fight ends.
 
    Returns: {"won": bool, "vars": {...}, "extra": {...}}
    If the tab closes early: {"won": False, "abandoned": True, "vars": {}}
    """
    folder = os.path.abspath(folder)
    if not os.path.isfile(os.path.join(folder, entry)):
        raise FileNotFoundError(f"{entry} not found in {folder}")
 
    cfg = {"win": win_var, "lose": lose_var, "watch": list(watch_vars)}
    bridge = BRIDGE_TEMPLATE.replace("__CFG__", json.dumps(cfg).replace("</", "<\\/"))
 
    shared = _shared()
    handler = _shared._make_handler(shared, folder, entry, bridge)
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)  # port 0 = free port
    url = f"http://127.0.0.1:{server.server_address[1]}/"
 
    threading.Thread(target=server.serve_forever, daemon=True).start()
 
    print(f"Boss fight is live at {url}")
    if open_browser:
        webbrowser.open(url)
    print("Waiting for the fight to finish...")
 
    abandoned = {"won": False, "abandoned": True, "vars": {}, "extra": {}}
    started = time.time()
    result = None
    try:
        while not shared.done.wait(1):
            now = time.time()
            if shared.last_ping is None and now - started > start_timeout:
                result = abandoned
                break
            if shared.last_ping is not None and now - shared.last_ping > ping_timeout:
                result = abandoned
                break
        if result is None:
            result = shared.result
    except KeyboardInterrupt:
        result = abandoned
    finally:
        server.shutdown()
        server.server_close()
 
    return result
if __name__ == "__main__":
    print(startbossfight1("bossfight", watch_vars=["playerHP", "bossHP"]))