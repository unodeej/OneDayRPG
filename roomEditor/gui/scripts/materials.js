// Unlinked Icons can be something like `▓` or it can be multiple alternatives like `─` and `│`

// Order of Linked Icons:
  // topleft
  // top
  // topright
  // right
  // bottomright
  // bottom
  // bottomleft
  // left
  //
  // topleftright
  // topbottomright
  // bottomleftright
  // topbottomleft
  // all

const LinkMode = {
  none: 0,     // no linking
  two:  1,     // like one continuous pipe, with no splits
  four: 2,     // can link with any number of sides like redstone
}

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
  Wall: new Item("Wall", true, false, LinkMode.none, "Q"),
  Bumble: new Item("Bumble", false, true, LinkMode.none, "B"),
  Pipe: new Item("Pipe", false, false, LinkMode.two, ["|", "─"], ["┌", "─", "┐", "│", "┘", "─", "└", "│"]),
}