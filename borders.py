class Border:
    topleft: str
    top: str
    topright: str
    right: str
    bottomright: str
    bottom: str
    bottomleft: str
    left: str

    def __init__(self, topleft, top, topright, right, bottomright, bottom, bottomleft, left):
        self.topleft = topleft
        self.top = top
        self.topright = topright
        self.right = right
        self.bottomright = bottomright
        self.bottom = bottom
        self.bottomleft = bottomleft
        self.left = left

blockLight      = Border("░", "░", "░", "░", "░", "░", "░", "░")
blockMedium     = Border("▒", "▒", "▒", "▒", "▒", "▒", "▒", "▒")
blockBold       = Border("▓", "▓", "▓", "▓", "▓", "▓", "▓", "▓")
blockSolid      = Border("█", "█", "█", "█", "█", "█", "█", "█")
halfBlockSolid  = Border("█", "▀", "█", "▐", "█", "▄", "█", "▌")
lineSingle      = Border("┌", "─", "┐", "│", "┘", "─", "└", "│")
lineDouble      = Border("╔", "═", "╗", "║", "╝", "═", "╚", "║")
scroll          = Border("⌠", "═", "⌠", "│", "⌡", "═", "⌡", "│")
dots            = Border("·", "·", "·", ":", "·", "·", "·", ":")
