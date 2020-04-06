// constants
const canvas = document.getElementById("editor");
const ctx = canvas.getContext("2d");
const Mode = {
  none: 0,
  select: 1,
  drawFree: 2,
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
let selected = [] // x0, y0, x1, y1 - lower bounds (x0, x1) are inclusive. Upper bounds are exclusive.
let mode = Mode.drawFree;
let overrideMode = Mode.none;
let desiredOverrideMode = Mode.none; // We need this because you can't update overrideMode at all times
let mapWidth = 160; // same as One Day RPG
let mapHeight = 35; // "   "      "     "
let materialsSelected = [];
let materialSelectedIndex; // 0 for primary, 1 for alt
let mouseButtons; // bit flag of current mouse buttons, updated at onmousedown, onmouseup, and onmousemove

canvas.oncontextmenu = function(event) {
  event.preventDefault();
}

document.onkeydown = function(event) {
  switch(event.keyCode) {
    case 16:  // shift
      desiredOverrideMode = Mode.select
      break;
    // 17 == control
    // 18 == alt
    // 32 == space
    case 46: // delete
    case 8:  // backspace
      deleteSelection();
      break;
  }
  draw.update();
}

document.onkeyup = function(event) {
  switch(event.keyCode) {
    case 16:
      desiredOverrideMode = Mode.none
      break;
  }
}

canvas.onmousedown = function(event) {
  UpdateOverrideModeIfPossible();
  mouseButtons = event.buttons;
  draw.reset()
  rect = canvas.getBoundingClientRect()
  let x, y;
  [x,y] = xyFromMouse(event.clientX - rect.left, event.clientY - rect.top);
  previousClick = [x, y]

  switch (getModeWithOverride()) {
    case Mode.select:
      select(x, y);
      break;
    case Mode.drawFree:
      deselectAll();
      useAlternateMaterial(event.button == 2) // use alt material if the right mouse button was clicked
      setCell(x, y, getSelectedMaterial())
      break;
  }
  draw.update()
}

canvas.onmousemove = function(event) {
  mouseButtons = event.buttons;
  if (event.buttons == 0)
    return;
  rect = canvas.getBoundingClientRect();
  [x,y] = xyFromMouse(event.clientX - rect.left, event.clientY - rect.top);

  switch (getModeWithOverride()) {
    case Mode.select:
      select(previousClick[0], previousClick[1], x, y)
      break;
    case Mode.drawFree:
      setCell(x, y, getSelectedMaterial());
      break;
  }
  draw.update()
}

canvas.onmouseup = function(event) {
    mouseButtons = event.buttons;
    UpdateOverrideModeIfPossible();
}

function start() {
  // resize the canvas
  canvas.width = mapWidth * cellWidth;
  canvas.height = mapHeight * cellHeight;
  // initialize grid
  draw.reset();
  // default selected material to first in the list (not the erasor)
  materialsSelected[0] = Object.keys(materials)[1]
  materialsSelected[1] = Object.keys(materials)[0]
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

function updateNeighbor(x, y) {
  if (hasCell(x, y)) {
    let c = cells[x][y]
    c[1] = getAppropriateIcon(x, y, materials[c[0]])
  }
}

function updateAllNeighbors(x,y) {
  updateNeighbor(x, y-1) // top neighbor
  updateNeighbor(x, y+1) // bottom neighbor
  updateNeighbor(x-1, y) // left neighbor
  updateNeighbor(x+1, y) // right neighbor
}

function getModeWithOverride() {
  if (overrideMode == Mode.none) {
    console.log(mode)
    return mode;
  } else {
    return overrideMode;
  }
}

////////////////////////////////////////////////////
/// Check if there are no reasons that we shouldn't update overrideMode
/// e.g., certain mouse buttons being held down.
/// If it's fine to update overrideMode, do so
/// (OverrideMode is used for using shift/other keypresses to temporarily
/// override the base mode)
///
function UpdateOverrideModeIfPossible() {
  if (mouseButtons == 0)
    overrideMode = desiredOverrideMode;
}

function swapMaterials() {
  materialsSelected = [materialsSelected[1], materialsSelected[0]]
}

function useAlternateMaterial(trueOrFalse) {
  if (trueOrFalse == true) {
    materialSelectedIndex = 1;
  } else {
    materialSelectedIndex = 0;
  }
}

function getSelectedMaterial() {
  return materialsSelected[materialSelectedIndex]
}

// function getPrimaryMaterial() {}

function setPrimaryMaterial(materialName) {
  materialsSelected[0] = materialName
  draw.highlightSelectedMaterial();
}

function setAlternateMaterial(materialName) {
  materialsSelected[1] = materialName
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
  selected = [Math.min(x0, x1), Math.min(y0, y1), Math.max(x0, x1) + 1, Math.max(y0, y1) + 1];
}

function deselectAll() {
  selected = [];
}

function deleteSelection() {
  for (let i = selected[0]; i < selected[2]; i++) { // iterate through columns
    if (cells[i] == undefined) {
      continue;
    }
    for (let j = selected[1]; j < selected[3]; j++) { // iterate through rows
      if (cells[i][j] == undefined) {
        continue;
      }
      setCell(i, j, materialsSelected[1])
    }
  }
}

start();
