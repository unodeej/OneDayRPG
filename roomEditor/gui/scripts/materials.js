const LinkMode = {
  none: 0,     // no linking
  two:  1,     // like one continuous pipe, with no splits
  four: 2,     // can link with any number of sides like redstone
}

const LinkedIconIndex = { // Order of Linked Icons in any linkedIcons array
  topleft         : 0,
  top             : 1,
  topright        : 2,
  right           : 3,
  bottomright     : 4,
  bottom          : 5,
  bottomleft      : 6,
  left            : 7,

  topleftright    : 8,
  topbottomright  : 9,
  bottomleftright : 10,
  topbottomleft   : 11,
  all             : 12,
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
  Wall: new Material("Wall", true, false, LinkMode.none, "Q"),
  Bumble: new Material("Bumble", false, true, LinkMode.none, "B"),
  Pipe: new Material("Pipe", false, false, LinkMode.two, ["│", "─"], ["┌", "─", "┐", "│", "┘", "─", "└", "│"]),
  Erasor: new Material("Erasor", false, false, LinkMode.none, " "),
}
