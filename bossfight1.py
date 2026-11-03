import json 
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

bridge = """
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
      root = os.path.readpath(root)
      
    