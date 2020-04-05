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
let materialSelected;

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
      setItem(x, y, materialSelected)
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
      setItem(x, y, materialSelected);
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
  // default selected material to first in the list
  materialSelected = Object.keys(materials)[0]
  // show palette of materials
  draw.listMaterials();
  draw.highlightSelectedMaterial();
}

function xyFromMouse(mx, my) {
  return [Math.floor(mx/cellWidth), Math.floor(my/cellHeight)];
}

function getCell(x, y) {
  if (items[x] == null) {
    return null;
  } else if (items[x][y] == null) {
    return null;
  } else {
    return items[x][y];
  }
}

function getCellItem(x, y) {
  let cell = getCell(x, y);
  if (cell == null) {
    return null
  } else {
    return cell[0];
  }
}

function getCellIcon(x, y) {
  let cell = getCell(x, y);
  if (cell == null) {
    return " "
  } else {
    return cell[1];
  }
}

function setItem(x, y, value) {
  if (x >= mapWidth || y >= mapHeight) {
    return;
  }
  if (items[x] == null) {
    items[x] = [];
  }
  items[x][y] = [value, materials[value].icon]
}

function select(x0, y0, x1, y1) {
  if (x1 == undefined || y1 == undefined)
  {
    select(x0, y0, x0, y0);
    return;
  }
  selected = [Math.min(x0, x1), Math.min(y0, y1), Math.max(x0, x1), Math.max(y0, y1)];
}

function selectMaterial(materialName) {
  materialSelected = materialName;
  draw.highlightSelectedMaterial();
}

start();
