import display

def splitTextIntoLines(text, textPerLine):
    for i in range(0, len(text), textPerLine):
        # break up self.text into chunks of text with max length == self.textPerLine
        a = text[i:i + textPerLine]
        for line in a.split("\n"): # \n splits the text into a new line
            yield line

class Feed:
    viewport = None
    messages = []
    data = []
    def __init__(self, x, y, width, height, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.maxMessages = height
        self.generateDisplayData()

    def push(self, message):
        for line in splitTextIntoLines(message, self.width):
            self.messages.append(line)
            if len(self.messages) > self.maxMessages:
                self.messages.pop(0)
        self.generateDisplayData()

    def generateDisplayData(self):
        self.data = []
        for message in self.messages:
            nextLine = list(message)
            nextLine += [' '] * (self.width - len(message)) # pad right side of message
            self.data.append(nextLine)
        self.data = [[' '] * self.width] * (self.height - len(self.data)) + self.data # pad top of feed
        if self.viewport is not None:
            self.viewport.replaceData(self.data)

    def show(self):
        self.viewport = display.addViewport(self.x, self.y, self.data, self.z)

    def hide(self):
        if self.viewport is not None:
            display.removeViewport(self.viewport)

def demo():
    import time
    f = Feed(x=20, y=0, width=60, height=35, z=1)
    f.show()
    display.render()
    time.sleep(.3)
    f.push("Alas, poor Yorick! I knew him, Horatio: a fellow of infinite jest, of most excellent fancy: he hath borne me on his back a thousand times; and now, how abhorred in my imagination it is!")
    display.render()
    time.sleep(.3)
    f.push("my gorge rims at it. Here hung those lips that I have kissed I know not how oft. Where be your gibes now? your gambols? your songs? your flashes of merriment, that were wont to set the table on a roar?")
    display.render()
    time.sleep(.3)
    f.push("Not one now, to mock your own grinning? quite chap-fallen? Now get you to my lady’s chamber, and tell her, let her paint an inch thick, to self favour she must come; make her laugh at that.")
    display.render()
