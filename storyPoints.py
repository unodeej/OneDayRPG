class StoryPoint():
	def __init__(self, startAction, arg, choices):
		self.startAction = startAction
		self.arg = arg
		self.choices = choices

	def Run(self):
		self.startAction(self.arg)
		cond = self.choices[0].conditionFunc();
		for c in self.choices:
			if cond == c.conditionVal:
				c.processResponse(c.responseAction())
				return story_points.get(c.link)
		# if none of the choices fired
		return self


class Choice():
	def __init__(self, conditionFunc, conditionVal, responseAction, processResponse, link):
		#self.trigger = trigger
		self.conditionFunc = conditionFunc
		self.conditionVal = conditionVal
		self.responseAction = responseAction
		self.processResponse = processResponse
		self.link = link

game = None

def dialogue(msg):
	print(msg)

def isTrue():
	return True

def doNothing(arg = ""):
	return None

def wait():
	try:
	    input("Press enter to continue")
	except SyntaxError:
	    pass

def getInputStr(msg = ""):
	return raw_input(msg)
	
def getInputInt(msg = ""):
	c = input(msg)
	try:
	   val = int(c)
	   return val
	except ValueError:
	  try:
	    val = float(user_input)
	    print("Please input a whole number")
	    return getInputInt(msg)
	  except ValueError:
	      print("Please input a number")
	      return getInputInt(msg)

def assignName(name):
	game.player.Name = name

def waitForEvent(arg = ''):
	if game.eventTrigger == True:
		game.eventTrigger = False
		return True
	else:
		print("FAIL")
		return waitForEvent()

story_points = {
	'intro1': StoryPoint(dialogue, "Welcome to One Day RPG!",
		[ Choice(isTrue, True, wait, doNothing, 'intro2' ) ] ),

	'intro2': StoryPoint(dialogue, "What is your name?",
		[ Choice(isTrue, True, getInputStr, assignName, 'intro3') ] ),

	'intro3': StoryPoint(dialogue, "Who's your favorite dev? (1) Kam (2) DJ (3) Brandon",
		[ Choice(getInputInt, 1, doNothing, doNothing, 'introKam'),
		  Choice(None, 2, doNothing, doNothing, 'introDJ'),
		  Choice(None, 3, doNothing, doNothing, 'introBran') ] ),

	'introKam': StoryPoint(dialogue, "Sick, Kam is a homie",
		[ Choice(isTrue, True, wait, doNothing, 'intro4') ] ),

	'introDJ': StoryPoint(dialogue, "That's the correct choice, DJ rules",
		[ Choice(isTrue, True, wait, doNothing, 'intro4') ] ),

	'introBran': StoryPoint(dialogue, "Awesome, Brandon is lit yo",
		[ Choice(isTrue, True, wait, doNothing, 'intro4') ] ),

	'intro4': StoryPoint(dialogue, "Please walk to the end of the hall",
		[ Choice(isTrue, True, doNothing, doNothing, 'intro5') ] ),

	'intro5': StoryPoint(waitForEvent, "",
		[ Choice(isTrue, True, doNothing, doNothing, None) ] ),


	}

