let ground;
let level = 1;
let speed = 10,
  maxspeed = 5,
  speeduprate = 0.3;
let jumpheight = 2;
let dirmoving = 0;
let run1, run2, idle, jump;
let runstate, idlestate, jumpstate; 
let debugtoggle = 0;
let bosshealth = 150;
let bossx = 0;
let bossy = 0;
let frames = 0;
let playerhp = 100;
let song = new Audio();
// music taken from https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1200067&Search=Search
song.src = "assets/music/boss.mp3";
function preload() {
  spritee = loadImage("assets/idle.png");
  flint = loadFont("assets/dynapuff.ttf");
  fry = loadImage("assets/sonic-fry.png");
  bg = loadImage("assets/bg.gif");
  gemimg = loadImage("assets/gem.png");
  win = loadImage("assets/win.png");
  lose = loadImage("assets/lost.png");
}
function setup() {
  idle = loadImage("assets/idle.png");
  jump = loadImage("assets/idle.png");
  run = loadImage("assets/run.gif");
  sonic = loadImage("assets/boss.png");

  createCanvas(800, 800);
  player = new Sprite(spritee, 0, 0, 1);
  sonic = new Sprite(sonic, 0, 0, 1);
  fry = new Sprite(fry, 0, 0, 1);
  gem = new Sprite(gemimg, 0, 0, 1);
  fry.width = 150;
  fry.height = 150;
  ground = new Sprite(window.width / 2, window.height - 20, 1000, 100);
  ground.color = "rgb(0,233,255)";
  ground.collider = "static";
  player.vel.x = 0;
  player.shape = "box";
  fry.collider = "none";
  gem.collider = "none";
  player.width = 42;
  player.height = 175.7;
  let fr = frameRate().toFixed(1) * 4;
}
function draw() {

    song.play();

  if (playerhp <= 0) {

    background(lose);

    noLoop();
  } else if (bosshealth <= 0) {

    background(win);

    playerhp = 10000000000000000000000;
  } else {

    tint(80.5);
    background(bg);
    noTint();
  }

  frameRate(120);
  if (debugtoggle == 1) {
    player.debug = true;
  }
  if (debugtoggle == 0) {
    player.debug = false;
  }
  player.rotation = 0;

  let oldx = player.x;
  let oldy = player.y;

  let speedcounter = player.vel.x.toFixed(3);
  fill(0, 0, 244);

  text("Speed: " + speedcounter, 10, 40);
  textFont(flint);
  textSize(36);
  fill(119, 221, 119);
  textFont(flint);
  textSize(36);

  text("Terminal Crawler", 470, 40);
  fill(255, 0, 0);

  if (playerhp >= 70) {

    fill(0, 240, 0);
    text("Player Hp: " + playerhp, 10, 120);
  } else if (playerhp < 70 && playerhp >= 40) {

    fill(255, 254, 122);
    text("Player Hp: " + playerhp, 10, 120);
  } else if (playerhp < 39) {

    fill(255, 0, 0);
    text("Player Hp: " + playerhp, 10, 120);
  }
  fill(255, 0, 0);

  textFont(flint);
  textSize(36);

  text(bossbarupdate(), 10, 80);

  animationUpdate();

  player.shape = "box";

  fry.collider = "none";
  sonic.collider = "none";

  movementCheck();

  moveboss();

  playerattack();


  if (dist(fry.x, fry.y, player.x, player.y) <= 50) {

    fry.visible = false;

    playerhp -= Math.floor(Math.random() * 20);

    fry.x = 900;
    fry.y = 900;
  } else {

    fry.visible = true;
  }
}

function movementCheck() {

  if (!kb.pressing("a") && !kb.pressing("d")) {
    player.vel.x *= 0.9;

    if (abs(player.vel.x) < 0.1) {
      player.vel.x = 0;
    }
  }

  if (kb.pressing("-") && debugtoggle == 0) {

    debugtoggle = 1;
  }
  if (kb.pressing("=") && debugtoggle == 1) {
    debugtoggle = 0;
  }

  if (player.x + player.width / 2 > width) player.x = 0;
  if (player.x - player.width / 2 < 0) player.x = 100;
  if (player.y + player.height / 2 > height) player.y = 100;
  if (player.y - player.height / 2 < 0) player.y = 100;
  if (player.vel.x > 10) player.vel.x = 10;
  if (player.vel.x < -10) player.vel.x = -10;

  if (kb.pressing("w")) {

    speed = 12;
    player.vel.y -= speeduprate;
  } else {
    speed = 10;
  }
  if (player.colliding(ground)) {

    player.vel.y = 0;
  } else {

    player.vel.y += 1;
  }


  if ((kb.pressing("w") || kb.pressing("space")) && player.colliding(ground)) {

    player.vel.y = -18;

    jumpstate = 1;

    runstate = 0;
  }

  if (kb.pressing("a")) {
    speed = 13;

    player.vel.x -= speeduprate;

    player.mirror.x = true;

    runstate = 1;

    jumpstate = 0;
  } else if (kb.pressing("d")) {
    speed = 13;

    player.vel.x += speeduprate;

    player.mirror.x = false;

    runstate = 1;

    jumpstate = 0;
  } else {
    speed = 10;

    runstate = 0;
  }

  if (player.vel.x > maxspeed) player.vel.x = maxspeed;
  if (player.vel.x < -maxspeed) player.vel.x = -maxspeed;
  if (player.vel.x == 0 && player.vel.y == 0) {

    runstate = 0;
    jumpstate = 0;
  }
}
function animationUpdate() {

  if (jumpstate == 0 && runstate == 0 && player.colliding(ground)) {

    player.width = 42;
    player.height = 175.7;

    player.img = idle;
  }

  if (jumpstate == 1 && runstate == 0 && !player.colliding(ground)) {

    player.width = 145;
    player.height = 140;

    player.img = jump;
  }

  if (jumpstate == 0 && runstate == 1) {

    player.width = 145;
    player.height = 140;

    player.img = run;
  }
}
function bossbarupdate() {

  if (bosshealth == 150) {
    return "HP: ■■■■■■■■■■■■■■■";
  }
  if (bosshealth == 140) {
    return "HP: ■■■■■■■■■■■■■■";
  }
  if (bosshealth == 130) {
    return "HP: ■■■■■■■■■■■■■";
  }
  if (bosshealth == 120) {
    return "HP: ■■■■■■■■■■■■";
  }
  if (bosshealth == 110) {
    return "HP: ■■■■■■■■■■■";
  }
  if (bosshealth == 100) {
    return "HP: ■■■■■■■■■■";
  }
  if (bosshealth == 90) {
    return "HP: ■■■■■■■■■";
  }
  if (bosshealth == 80) {
    return "HP: ■■■■■■■■";
  }
  if (bosshealth == 70) {
    return "HP: ■■■■■■■";
  }
  if (bosshealth == 60) {
    return "HP: ■■■■■■";
  }
  if (bosshealth == 50) {
    return "HP: ■■■■■";
  }
  if (bosshealth == 40) {
    return "HP: ■■■■";
  }
  if (bosshealth == 30) {
    return "HP: ■■■";
  }
  if (bosshealth == 20) {
    return "HP: ■■";
  }
  if (bosshealth == 10) {
    return "HP: ■";
  }
  if (bosshealth <= 0) {
    return "■■■ YOU WIN ■■■";
  }

  console.log(bosshealth);
}
function moveboss() {



  bossx = Math.floor(Math.random() * 601) + 100;

  if (frames == 0) {
    sonic.x = bossx;
  }
  if (frames == 0) {

    frames = frameRate().toFixed(0) * 5;

    bossattack1();
  }

  sonic.y = 175;

  frames -= 1;
}
function bossattack1() {

  fry.x = sonic.x;
  fry.y = sonic.y;

  fry.moveTo(player, 10);
}
function playerattack() {

  if (kb.pressing("r")) {
    gem.x = player.x;
    gem.y = player.y;

    gem.moveTo(sonic, 10);

    gem.rotateTowards(sonic, 10);
  }


  if (dist(gem.x, gem.y, sonic.x, sonic.y) <= 50) {

    gem.visible = false;

    bosshealth -= 10;

    gem.x = 900;
    gem.y = 900;
  } else {

    gem.visible = true;
  }
}
