// constants
const canvas = document.getElementById("editor");
const ctx = canvas.getContext("2d");
const Mode = {
  select: 0,
  drawFree: 1,
}
const Sides = {
  up: 1,
  right: 2,
  down: 4,
  left: 8,
}

// helper variables
let cells = [] // each cell in cells is an array containing [material_name, icon]
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
      setCell(x, y, materialSelected)
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
      setCell(x, y, materialSelected);
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
  if (hasCell(x, y)) {
    return cells[x][y];
  } else {
    return undefined;
  }
}

function hasCell(x, y) {
  if (cells[x] == undefined) {
    return false;
  } else if (cells[x][y] == undefined) {
    return false;
  } else {
    return true;
  }
}

function getCellMaterialID(x, y) {
  let cell = getCell(x, y);
  if (cell == undefined) {
    return undefined
  } else {
    return cell[0];
  }
}

function getCellIcon(x, y) {
  let cell = getCell(x, y);
  if (cell == undefined) {
    return " "
  } else {
    return cell[1];
  }
}

function setCell(x, y, value) {
  if (x >= mapWidth || y >= mapHeight) {
    return;
  }
  if (cells[x] == undefined) {
    cells[x] = [];
  }
  cells[x][y] = [value, getAppropriateIcon(x, y, materials[value])]
  updateAllNeighbors(x, y)
}

function updateAllNeighbors(x,y) {
  updateNeighbor(x, y-1) // top neighbor
  updateNeighbor(x, y+1) // bottom neighbor
  updateNeighbor(x-1, y) // left neighbor
  updateNeighbor(x+1, y) // right neighbor
}

function updateNeighbor(x, y) {
  if (hasCell(x, y)) {
    let c = cells[x][y]
    c[1] = getAppropriateIcon(x, y, materials[c[0]])
  }
}

function getAppropriateIcon(x, y, mat) {
  if (mat.linking == LinkMode.none) {
    return mat.unlinkedIcons[0];
  }
  // get list of neighboring cells of the same material type
  let sides = 0;
  sides += (mat == materials[getCellMaterialID(x, y-1)]) * Sides.up
  sides += (mat == materials[getCellMaterialID(x-1, y)]) * Sides.left
  sides += (mat == materials[getCellMaterialID(x, y+1)]) * Sides.down
  sides += (mat == materials[getCellMaterialID(x+1, y)]) * Sides.right
  // select the appropriate icon based on which sides we have
  switch (sides) {
    case Sides.up + Sides.left:
      return mat.linkedIcons[LinkedIconIndex.UpAndLeft];
    case Sides.up:
      return mat.linkedIcons[LinkedIconIndex.Vertical]; // bottomright, bottomleft, and left also work
    case Sides.up + Sides.right:
      return mat.linkedIcons[LinkedIconIndex.UpAndRight];
    case Sides.right:
      return mat.linkedIcons[LinkedIconIndex.Horizontal]; // top also works
    case Sides.down + Sides.right:
      return mat.linkedIcons[LinkedIconIndex.DownAndRight];
    case Sides.down:
      return mat.linkedIcons[LinkedIconIndex.Vertical]; // topright, DownAndRight, and left also work
    case Sides.down + Sides.left:
      return mat.linkedIcons[LinkedIconIndex.DownAndLeft];
    case Sides.left:
      return mat.linkedIcons[LinkedIconIndex.Horizontal]; // top also works
    case Sides.left + Sides.right:
      return mat.linkedIcons[LinkedIconIndex.Horizontal]; // top also works
    case Sides.up + Sides.down:
      return mat.linkedIcons[LinkedIconIndex.Vertical]; // left also works
    case 0: // no sides
      return mat.unlinkedIcons[0];
  }

  if (mat.linking == LinkMode.four) {
    switch (sides) {
      case Sides.left + Sides.up + Sides.right:
        return mat.linkedIcons[LinkedIconIndex.HorizontalAndUp]; // all also works
      case Sides.up + Sides.right + Sides.down:
        return mat.linkedIcons[LinkedIconIndex.VerticalAndRight]; // all also works
      case Sides.left + Sides.down + Sides.right:
        return mat.linkedIcons[LinkedIconIndex.HorizontalAndDown]; // all also works
      case Sides.up + Sides.down + Sides.left:
        return mat.linkedIcons[LinkedIconIndex.VerticalAndLeft]; // all also works
      case Sides.up + Sides.left + Sides.right + Sides.down:
        return mat.linkedIcons[LinkedIconIndex.All];
    }
  }
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
