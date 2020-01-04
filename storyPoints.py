class StoryPoint():
	def __init__(self, startAction, arg, choices):
		self.startAction = startAction
		self.arg = arg
		self.choices = choices

	def Run(self):
		self.startAction(self.arg)
		for c in self.choices:
			if c.conditionFunc() == c.conditionVal:
				c.processResponse(c.responseAction())
				return story_points.get(c.link)


class Choice():
	def __init__(self, conditionFunc, conditionVal, responseAction, processResponse, link):
		#self.trigger = trigger
		self.conditionFunc = conditionFunc
		self.conditionVal = conditionVal
		self.responseAction = responseAction
		self.processResponse = processResponse
		self.link = link

class Player():
	def __init__(self):
		self.name = ""

player = Player()

def dialogue(msg):
	print(msg)

def true():
	return true

def doNothing(arg):
	return

def wait():
	try:
	    input("Press enter to continue")
	except SyntaxError:
	    pass

def getInput(msg = ""):
	return raw_input(msg)

def assignName(name):
	player.Name = name

story_points = {
	'intro1': StoryPoint(dialogue, "Welcome to One Day RPG!",
		[ Choice(true, true, wait, doNothing, 'intro2' ) ] ),

	'intro2': StoryPoint(dialogue, "What is your name?",
		[ Choice(true, true, getInput, assignName, 'intro3') ] ),

	'intro3': StoryPoint(dialogue, "Who's your favorite dev? (1) Kam (2) DJ (3) Brandon",
		[ Choice(getInput, 1, "Nice Choice", dialogue, None) ] )

	}

