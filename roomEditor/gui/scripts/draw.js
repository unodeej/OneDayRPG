// constants
const cellWidth = 10;
const cellHeight = 20;

// colors
const c_bg = "#000000";
const c_lines = "#444";
const c_highlight = "#1060F050";
const c_text = "#fff";

const draw = {
  ////////////////////////////////////////////////////
  /// update all visuals
  ///
  update: () => {
    draw.reset();
    draw.text();
    draw.highlight(selected)
  },

  ////////////////////////////////////////////////////
  /// reset canvas to black background with grid
  ///
  reset: () => {
    // make background black
    ctx.beginPath();
    ctx.fillStyle = c_bg;
    ctx.rect(0, 0, canvas.width, canvas.height);
    ctx.fill();

    // draw grid
    draw.grid()
  },

  ////////////////////////////////////////////////////
  /// draw the grid
  ///
  grid: () => {
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
  text: () => {
    ctx.fillStyle = c_text;
    ctx.font = '16.5px monospace';
    ctx.textBaseline = "bottom";
    for (let i = 0; i < mapWidth; i++) {
      for (let j = 0; j < mapHeight; j++) {
        ctx.fillText(getItem(i, j), (i) * cellWidth, (j+1) * cellHeight);
      }
    }
  },

  ////////////////////////////////////////////////////
  /// highlight some number of cell
  ///
  highlight: (selected) => {
    [x0, y0, x1, y1] = selected
    x1++; y1++;
    x0 *= cellWidth;
    y0 *= cellHeight;
    x1 *= cellWidth;
    y1 *= cellHeight;

    ctx.beginPath();
    ctx.rect(x0, y0, x1 - x0, y1 - y0)
    ctx.fillStyle = c_highlight;
    ctx.fill();
  },
}

// highlight: (x0, y0, x1, y1) => {
//   console.log("HI")
//   cellx0 = Math.floor(x0 / cellWidth) * cellWidth
//   celly0 = Math.floor(y0 / cellHeight) * cellHeight
//   cellx1 = Math.ceil(x1 / cellWidth) * cellWidth
//   celly1 = Math.ceil(y1 / cellHeight) * cellHeight
//
//   ctx.beginPath();
//   ctx.rect(cellx0, celly0, cellx1 - cellx0, celly1 - celly0)
//   ctx.fillStyle = c_highlight;
//   ctx.fill();
// },
