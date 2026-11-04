let ground;
let level = 1;
// speed control varibles
let speed = 10,
  maxspeed = 5,
  speeduprate = 0.3;
let jumpheight = 2;
// directional positioning value
let dirmoving = 0;
// animation control variables
let run1, run2, idle, jump;
// variables to determine current movement state
let runstate, idlestate, jumpstate; 
let debugtoggle = 0;
let bosshealth = 150;
let bossx = 0;
let bossy = 0;
let frames = 0;
let playerhp = 100;
song = new Audio();
song.src = "song.mp3";
function preload() {
  spritee = loadImage("idle.png");
  flint = loadFont("dynapuff.ttf");
  fry = loadImage("sonic-fry.png");
  bg = loadImage("bg.gif");
  gemimg = loadImage("gem.png");
  win = loadImage("win.png");
  lose = loadImage("lost.png");
}
function setup() {
  // loading the idle state image
  idle = loadImage("idle.png");
  // loading the jump state image
  jump = loadImage("jump.png");
  // loading the run state image
  run = loadImage("sonic-running.gif");
  // loading the temu sonic image
  sonic = loadImage("boss.png");

  // setting the canvas to the windows sizings
  createCanvas(800, 800);
  // declaring the player sprite
  player = new Sprite(spritee, 0, 0, 1);
  // declaring the boss sprite
  sonic = new Sprite(sonic, 0, 0, 1);
  // declaring the boss attack item sprite
  fry = new Sprite(fry, 0, 0, 1);
  // declaring the gem player sprite item to attack the boss
  gem = new Sprite(gemimg, 0, 0, 1);
  // setting the fry hitbox
  fry.width = 150;
  fry.height = 150;
  // ground sprite
  ground = new Sprite(window.width / 2, window.height - 20, 1000, 100);
  // setting the ground stuff
  // set the ground color
  ground.color = "rgb(0,233,255)";
  // set the ground collider
  ground.collider = "static";
  // player hitbox stuff
  player.vel.x = 0;
  // setting the player hitbox
  player.shape = "box";
  // setting the fry/gem hitbox types to none so it dosent push around the boss/player
  fry.collider = "none";
  gem.collider = "none";
  // hitbox stuff
  player.width = 42;
  player.height = 175.7;
  // set the framerate for the timer
  let fr = frameRate().toFixed(1) * 4;
}
function draw() {
  // play audio x2
    song.play();
  // win check
  if (playerhp <= 0) {
    // switch background to lose if the player lost the game
    background(lose);
    // stop the game
    noLoop();
  } else if (bosshealth <= 0) {
    // change the background to win if the player win the game
    background(win);
    // set the health to a commicaly high number so the player dosent die after wining
    playerhp = 10000000000000000000000;
  } else {
    // set the background to defualt if the player hasnt won/lost
    tint(80.5); // setting the tint so that its blured
    background(bg); // setting the defualt bg
    noTint(); // removing the tint off of other objects
  }
  // temp debug toggle for hitboxes
  frameRate(120);
  if (debugtoggle == 1) {
    player.debug = true; // enable debug mode so that you can easily view hitboxes via =
  }
  if (debugtoggle == 0) {
    player.debug = false; // disable if equal is pressed again
  }
  player.rotation = 0;
  // coloisons
  let oldx = player.x;
  let oldy = player.y;
  // speed text
  let speedcounter = player.vel.x.toFixed(3);
  fill(0, 0, 244); // text color
  // text
  text("Speed: " + speedcounter, 10, 40); // speed text
  textFont(flint); // set the font to dynapuff
  textSize(36); // text size
  fill(119, 221, 119); // set the color
  textFont(flint);
  textSize(36);
  // text
  text("Sonic Vs Temu Sonic", 420, 40);
  fill(255, 0, 0);
  // set the color of the player hp text depending on h[]
  if (playerhp >= 70) {
    // set to green if above or equal to 70hp
    fill(0, 240, 0);
    text("Player Hp: " + playerhp, 10, 120);
  } else if (playerhp < 70 && playerhp >= 40) {
    // set to yellow if hp is in the range of 69-40
    fill(255, 254, 122);
    text("Player Hp: " + playerhp, 10, 120);
  } else if (playerhp < 39) {
    // set to red if the hp is anything under 39
    fill(255, 0, 0);
    text("Player Hp: " + playerhp, 10, 120);
  }
  fill(255, 0, 0);
  // bosbar health
  textFont(flint);
  textSize(36);
  // function to create the boss bar text
  text(bossbarupdate(), 10, 80);
  // calling important functions
  animationUpdate();
  // collider stuff
  player.shape = "box";
  // reset the colliders
  fry.collider = "none";
  sonic.collider = "none";
  // movement script
  movementCheck();
  // script to move boss
  moveboss();
  // script for attacking player
  playerattack();
  // script to calc if the player is touching the fry
  // if the distance between the boss attack item and player is under 50
  if (dist(fry.x, fry.y, player.x, player.y) <= 50) {
    // set the visibily to none if touching the player
    fry.visible = false;
    // remove a random amount of hp
    playerhp -= Math.floor(Math.random() * 20);
    // go off screen to avoid double damage
    fry.x = 900;
    fry.y = 900;
  } else {
    // show if not touching the player
    fry.visible = true;
  }
}
// important functions for checking
function movementCheck() {
  // code to add friction
  if (!kb.pressing("a") && !kb.pressing("d")) {
    player.vel.x *= 0.9;
    // prevent speeding to mach one
    if (abs(player.vel.x) < 0.1) {
      player.vel.x = 0;
    }
  }
  // debug toggle inorder to see hitboxes
  if (kb.pressing("-") && debugtoggle == 0) {
    // set the debug toggle to one
    debugtoggle = 1;
  }
  if (kb.pressing("=") && debugtoggle == 1) {
    debugtoggle = 0;
  }
  // prevent going off screen
  if (player.x + player.width / 2 > width) player.x = 0;
  if (player.x - player.width / 2 < 0) player.x = 100;
  if (player.y + player.height / 2 > height) player.y = 100;
  if (player.y - player.height / 2 < 0) player.y = 100;
  if (player.vel.x > 10) player.vel.x = 10;
  if (player.vel.x < -10) player.vel.x = -10;
  // movement stuff
  if (kb.pressing("w")) {
    // increase speed
    speed = 12;
    player.vel.y -= speeduprate;
  } else {
    speed = 10;
  }
  if (player.colliding(ground)) {
    // dont do anything if the player is touching the ground before jumping
    player.vel.y = 0;
  } else {
    // otherwise jump
    player.vel.y += 1;
  }
  // jump controls
  // check if the player is pressing space or w and touching the ground before starting a jump
  if ((kb.pressing("w") || kb.pressing("space")) && player.colliding(ground)) {
    // jump
    player.vel.y = -18;
    // set jump state for anims
    jumpstate = 1;
    // set running state to 0
    runstate = 0;
  }
  // running left and right controls
  if (kb.pressing("a")) {
    speed = 13;
    // decrease x velocity by speed up rate
    player.vel.x -= speeduprate;
    // flip player image to show going the correct direction
    player.mirror.x = true;
    // set the state to running for the anims
    runstate = 1;
    // dont set the jump state
    jumpstate = 0;
  } else if (kb.pressing("d")) {
    speed = 13;
    // increase x velocity by speed up rate
    player.vel.x += speeduprate;
    // flip player image to show going the correct direction
    player.mirror.x = false;
    // set the state to running for the anims
    runstate = 1;
    // dont set the jump state
    jumpstate = 0;
  } else {
    speed = 10;
    // disable run state if no movement is present
    runstate = 0;
  }
  // add speed limits
  if (player.vel.x > maxspeed) player.vel.x = maxspeed; // if player is above the max speed on postive, then cap it at 5
  if (player.vel.x < -maxspeed) player.vel.x = -maxspeed; // if player is above the max speed on negative, then cap it at -5
  if (player.vel.x == 0 && player.vel.y == 0) {
    // if the player isnt moving, set both of the states to 0 so it defualts to idle anims
    runstate = 0;
    jumpstate = 0;
  }
}
function animationUpdate() {
  // idle anim
  if (jumpstate == 0 && runstate == 0 && player.colliding(ground)) {
    // set hitbox
    player.width = 42;
    player.height = 175.7;
    // set the idle image
    player.img = idle;
  }
  // jump anim
  if (jumpstate == 1 && runstate == 0 && !player.colliding(ground)) {
    // set hitbox
    player.width = 145;
    player.height = 140;
    // set the jumo image
    player.img = jump;
  }
  //running anim
  if (jumpstate == 0 && runstate == 1) {
    // set hitbox
    player.width = 145;
    player.height = 140;
    // set the run image
    player.img = run;
  }
}
function bossbarupdate() {
  // update the bossbar text
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
  // log boss health
  console.log(bosshealth);
}
function moveboss() {
  // gets a random x value to move the boss
  // the random works by mupltying the math.random value (between 0 - 1.0) to get a new value,
  // its 601 because other wise it would generate in the range of 100 to 599
  bossx = Math.floor(Math.random() * 601) + 100; // add one hundered to prevent touching the edge
  // timer system
  if (frames == 0) {
    sonic.x = bossx;
  }
  if (frames == 0) {
    // reset timer if its 0
    frames = frameRate().toFixed(0) * 5;
    // send the fry attack to the player
    bossattack1();
  }
  // set a constant y value
  sonic.y = 175;
  // decrease the timer
  frames -= 1;
}
function bossattack1() {
  // boss attack checker
  fry.x = sonic.x;
  fry.y = sonic.y;
  // move to player
  fry.moveTo(player, 10);
}
function playerattack() {
  // player attack code for r
  if (kb.pressing("r")) {
    gem.x = player.x;
    gem.y = player.y;
    // direct the gem to the boss (sonic)
    gem.moveTo(sonic, 10);
    // have tha werid rotating animation
    gem.rotateTowards(sonic, 10);
  }
  // code to check if boss is touching gem
  // if the distacne between the player gem attack and the boss is under 50
  if (dist(gem.x, gem.y, sonic.x, sonic.y) <= 50) {
    // set to be invisible
    gem.visible = false;
    // remove health
    bosshealth -= 10;
    // go offscreen
    gem.x = 900;
    gem.y = 900;
  } else {
    // keep gem visible if it misses
    gem.visible = true;
  }
}
