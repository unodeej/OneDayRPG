// constants
const canvas = document.getElementById("editor");
const ctx = canvas.getContext("2d");
const Mode = {
  select: 0,
  drawFree: 1,
}

// helper variables
let items = []
let previousClick
let selected = [] // x0, y0, x1, y1
let mode = Mode.drawFree;
let mapWidth = 0;
let mapHeight = 0;

canvas.onmousedown = function(event) {
  draw.reset()
  rect = canvas.getBoundingClientRect()
  let x, y;
  [x,y] = xyFromMouse(event.clientX - rect.left, event.clientY - rect.top);
  previousClick = [x, y]

  switch (mode) {
    case Mode.select:
      select(x, y)
      break;
    case Mode.drawFree:
      setItem(x, y, "B")
      break;
  }
  draw.update()
}

canvas.onmousemove = function(event) {
  if (event.buttons == 0)
    return;
  rect = canvas.getBoundingClientRect();
  [x,y] = xyFromMouse(event.clientX - rect.left, event.clientY - rect.top);

  switch (mode) {
    case Mode.select:
      select(previousClick[0], previousClick[1], x, y)
      break;
    case Mode.drawFree:
      setItem(x, y, "B");
      break;
  }
  draw.update()
}

function start() {
  // make canvas the width of the window
  mapWidth = Math.floor((window.innerWidth - 24) / cellWidth);
  mapHeight = Math.floor(canvas.height / cellHeight);
  canvas.width = mapWidth * cellWidth
  // initialize grid
  draw.reset();
}

function xyFromMouse(mx, my) {
  return [Math.floor(mx/cellWidth), Math.floor(my/cellHeight)];
}

function getItem(x, y) {
  if (items[x] == null) {
    return " ";
  } else if (items[x][y] == null) {
    return " ";
  } else {
    return items[x][y];
  }
}

function setItem(x, y, value) {
  if (x >= mapWidth || y >= mapHeight) {
    return;
  }
  if (items[x] == null) {
    items[x] = [];
  }
  items[x][y] = value
}

function select(x0, y0, x1, y1) {
  if (x1 == undefined || y1 == undefined)
  {
    select(x0, y0, x0, y0);
    return;
  }
  selected = [Math.min(x0, x1), Math.min(y0, y1), Math.max(x0, x1), Math.max(y0, y1)];
}

start();
