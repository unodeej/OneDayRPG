import display
import numpy

class Popup:
    x = display.width//4
    y = display.height//4
    width = display.width//2
    border = 2
    textPerLine = width - 2*border

    def __init__(self, text, buttons, centeredOnScreen=True, x=0, y=0, z=-1000):
        self.text = text
        self.buttons = buttons
        borderSymbol = "░"

        self.z = z
        if not centeredOnScreen:
            self.x = x
            self.y = y

        self.data = []
        self.data.append([borderSymbol] * self.width) # first line is a border
        for line in self.splitTextIntoLines():
            nextLine = [borderSymbol, " "]
            nextLine += list(line)
            nextLine += [' '] * (self.width - len(nextLine) - 1) + [borderSymbol] # pad the right of the line
            self.data.append(nextLine)

        self.data.append([borderSymbol] + [' '] * (self.width - 2) + [borderSymbol])
        for button in buttons:
            nextLine = [borderSymbol, " ", ">", ">", " ", "[", *(button.hotkey.lower()) ,"]", " ", ]
            nextLine += button.text
            nextLine += [' '] * (self.width - len(nextLine) - 1) + [borderSymbol] # pad the right of the line
            self.data.append(nextLine)

        self.data.append([borderSymbol] * self.width) # last line is a border

    def show(self):
        self.viewport = display.addViewport(self.x, self.y, self.data, self.z)

    def hide(self):
        # display.clearViewports()
        if hasattr(self, 'viewport'):
            display.removeViewport(self.viewport)
            del self.viewport

    def splitTextIntoLines(self):
        for i in range(0, len(self.text), self.textPerLine):
            # break up self.text into chunks of text with max length == self.textPerLine
            a = self.text[i:i + self.textPerLine]
            for line in a.split("\n"): # \n splits the text into a new line
                yield line

class Button():
    def __init__(self, text, hotkey):
        self.text = text
        self.hotkey = hotkey

def demo():
    p = Popup(
        text="There once was a man from Kentucky. With cars, he was not very lucky.  When his truck broke down, the mechanic skipped town, for he and the man's wife did fuck(y)",
        buttons = [Button(text="okay", hotkey="o"), Button(text="whatever", hotkey="w")]
    )
    p.show()
    display.render()

if __name__ == "__main__":
    demo()
