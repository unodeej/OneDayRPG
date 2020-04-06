// constants
const cellWidth = 9;
const cellHeight = 18;
const cellCursor = document.querySelector("#cell-cursor")

// colors
const c_bg = "#000000";
const c_lines = "#444";
const c_highlight = "#1060F050";
const c_text = "#fff";
const c_tool = "#00436f";

// html elements
const palette = document.getElementById("palette");
const toolbox = document.getElementById("toolbox");

const draw = {
  ////////////////////////////////////////////////////
  /// update all visuals
  ///
  update: () => {
    draw.reset();
    draw.text();
    draw.highlight();
  },

  ////////////////////////////////////////////////////
  /// reset canvas to black background with grid
  ///
  reset() {
    // make background black
    ctx.beginPath();
    ctx.fillStyle = c_bg;
    ctx.rect(0, 0, canvas.width, canvas.height);
    ctx.fill();

    draw.grid()
  },

  ////////////////////////////////////////////////////
  /// draw the grid
  ///
  grid() {
    ctx.strokeStyle = c_lines;
    ctx.lineWidth = 1;
    ctx.beginPath();
    // columns
    for (i = 0; i <= canvas.width; i+= cellWidth) {
      ctx.moveTo(i, 0);
      ctx.lineTo(i, canvas.height);
    }
    // rows
    for (i = 0; i <= canvas.height; i+= cellHeight) {
      ctx.moveTo(0, i);
      ctx.lineTo(canvas.width, i);
    }
    ctx.stroke();
  },

  ////////////////////////////////////////////////////
  /// write in all of the text
  ///
  text() {
    ctx.fillStyle = c_text;
    ctx.font = '16.5px monospace';
    ctx.textBaseline = "bottom";
    for (let i = 0; i < mapWidth; i++) {
      for (let j = 0; j < mapHeight; j++) {
        ctx.fillText(getCellIcon(i, j), (i) * cellWidth, (j+1) * cellHeight);
      }
    }
  },

  ////////////////////////////////////////////////////
  /// highlight some number of cell
  ///
  highlight() {
    [x0, y0, x1, y1] = selected
    x0 *= cellWidth;
    y0 *= cellHeight;
    x1 *= cellWidth;
    y1 *= cellHeight;

    ctx.beginPath();
    ctx.rect(x0, y0, x1 - x0, y1 - y0)
    ctx.fillStyle = c_highlight;
    ctx.fill();
  },

  ////////////////////////////////////////////////////
  /// list all available materials
  ///
  listMaterials : () => {
    // get the template element:
    let template = document.getElementById("mat-template");
    // get the div element representing the whole material
    let materialDiv = template.content.querySelector("div");

    // for each material, display the material in the HTML
    Object.values(materials).forEach(function (m) { // m is a material
      // clone the template
      let clone = document.importNode(materialDiv, true);
      // put the clone in the html
      palette.appendChild(clone);
      // modify the clone's html to fit the material
      clone.querySelector(".mat-name").innerHTML = m.name;
      clone.querySelector(".mat-icon").innerHTML = m.unlinkedIcons[0];
      clone.querySelector(".mat-solid").innerHTML = m.solid ? "Yes" : "No";
      clone.querySelector(".mat-moveable").innerHTML = m.moveable ? "Yes" : "No";

      // demo a few tiles in a row using the material
      let demo;
      if (m.linking == LinkMode.none) {
        demo = m.unlinkedIcons[0]
        demo = demo + demo + demo + " " + demo + demo + demo
      } else {
        demo = m.linkedIcons[1]
        demo = m.linkedIcons[0] + demo + m.linkedIcons[2] + " " + demo + demo + demo
      }
      clone.querySelector(".mat-demo").innerHTML = demo;

      // Add click event listener
      clone.onclick = () => {setPrimaryMaterial(m.name)};
    });
  },

  ////////////////////////////////////////////////////
  /// Highlight currently selected material
  ///
  highlightSelectedMaterial() {
    // For each material in the palette:
    palette.querySelectorAll(".material").forEach((mat, i) => {
      let matName = mat.querySelector(".mat-name").innerHTML;
      if (matName == materialsSelected[0]) {
        mat.classList.add("selected");
      } else {
        mat.classList.remove("selected");
      }
    });
  },

  ////////////////////////////////////////////////////
  /// Highlight currently selected tool
  ///
  highlightSelectedTool() {
    toolbox.querySelectorAll(".tool").forEach((tool) => {
      // reset tools to their default html settings
      tool.style.backgroundColor = "#00000000";
      tool.classList.remove("selected");
      // highlight current mode, including override
      if (getModeWithOverride() == Mode[(tool.id.substring(1))]) { // if current tool's id matches the current mode
        tool.style.backgroundColor = c_tool;
      }
      // add "selected" class to current mode, excluding override
      if (mode == Mode[(tool.id.substring(1))]) { // if current tool's id matches the current mode
        tool.classList.add("selected");
      }
    });
  },

  ////////////////////////////////////////////////////
  /// Highlight currently selected material
  ///
  highlightHoveredCell(left, top, cellX, cellY) {
    cellCursor.style.left = left + (cellX * cellWidth) + 1 + "px";
    cellCursor.style.top = top + (cellY * cellHeight) + 1 + "px";
  },

  ////////////////////////////////////////////////////
  /// The canvas uses a different mouse cursor in some modes
  /// This function updates the css to set the cursor.
  ///
  showModeCursor() {
    switch (getModeWithOverride()) {
      case Mode.select:
        canvas.style.cursor = "crosshair";
        break;
      default:
        canvas.style.cursor = "cell";
        break;
    }
  },
}
