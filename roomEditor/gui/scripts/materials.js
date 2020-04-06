const LinkMode = {
  none: 0,     // no linking
  two:  1,     // like one continuous pipe, with no splits
  four: 2,     // can link with any number of sides like redstone
}

const LinkedIconIndex = { // Order of Linked Icons in any linkedIcons array
  DownAndRight      : 0,
  Horizontal        : 1,
  DownAndLeft       : 2,
  Vertical          : 3,
  UpAndLeft         : 4,
  UpAndRight        : 5,

  HorizontalAndDown : 6,
  VerticalAndLeft   : 7,
  HorizontalAndUp   : 8,
  VerticalAndRight  : 9,
  All               : 10,
}

// Unlinked Icons can be something like `▓` or it can be multiple alternatives like `─` and `│`

class Material {
  constructor(name, solid, moveable, linking, unlinkedIcons, linkedIcons) {
    this.name = name;
    this.solid = solid;
    this.moveable = moveable;
    this.linking = linking
    this.unlinkedIcons = unlinkedIcons;
    this.linkedIcons = linkedIcons;
    this.icon = unlinkedIcons[0];
  }
}

materials = {
  Erasor: new Material("Erasor", false, false, LinkMode.none, " "),
  Wall: new Material("Wall", true, false, LinkMode.none, "▓"),
  Bumble: new Material("Bumble", false, true, LinkMode.none, "B"),
  Pipe: new Material("Pipe", false, false, LinkMode.four, ["│", "─"], ["┌", "─", "┐", "│", "┘", "└", "┬", "┤", "┴", "├", "┼"]),
}
