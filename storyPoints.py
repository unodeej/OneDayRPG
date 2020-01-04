import time

class StoryPoint():
	def __init__(self, startAction, arg, choices, trigger = None):
		self.startAction = startAction
		self.arg = arg
		self.choices = choices
		self.trigger = trigger

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

def battle(arg = ''):
	return True

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
	return input(msg)
	
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

def PauseStory(arg = ''):
	# Create a listener in Game
	game.storyPaused = True
	game.pausedStoryPoint = arg
	game.Update()

def ResumeStory():
	game.storyPaused = False
	game.pausedStoryPoint = None

def OneSec():
	time.sleep(1)
	return True


story_points = {
	'intro1': StoryPoint(dialogue, "Welcome to One Day RPG!",
		[ Choice(isTrue, True, wait, doNothing, 'intro4.2.6' ) ] ),

	'intro2': StoryPoint(dialogue, "What is your name?",
		[ Choice(isTrue, True, getInputStr, assignName, 'intro3.1') ] ),

	'intro3.1': StoryPoint(dialogue, ".",
		[ Choice(OneSec, True, doNothing, doNothing, 'intro3.2') ] ),
	'intro3.2': StoryPoint(dialogue, ".",
		[ Choice(OneSec, True, doNothing, doNothing, 'intro3.3') ] ),
	'intro3.3': StoryPoint(dialogue, ".",
		[ Choice(OneSec, True, doNothing, doNothing, 'intro3.4') ] ),

	'intro3.4': StoryPoint(dialogue, "7:00 A.M.",
		[ Choice(isTrue, True, doNothing, doNothing, 'intro3.5') ] ),
	'intro3.5': StoryPoint(dialogue, "Zzzzzzzzz.....",
		[ Choice(isTrue, True, doNothing, doNothing, 'intro3.6') ] ),
	'intro3.6': StoryPoint(dialogue, "Zzzzzzzzzzzzzz........",
		[ Choice(isTrue, True, doNothing, doNothing, 'intro4.1') ] ),

	'intro4.1': StoryPoint(dialogue, "You hear a blaring alarm clock. \n(1) Turn off the alarm (2) Let it ring",
		[ Choice(getInputInt, 1, doNothing, doNothing, 'intro4.2'),
		  Choice(None, 2, doNothing, doNothing, 'intro4.1.1') ] ),

	'intro4.1.1': StoryPoint(dialogue, "The alarm gets louder. \n(1) Turn off the alarm (2) Let it ring",
		[ Choice(getInputInt, 1, doNothing, doNothing, 'intro4.2'),
		  Choice(None, 2, doNothing, doNothing, 'intro4.1.2') ] ),

	'intro4.1.2': StoryPoint(dialogue, "It gets even louder. \n(1) Turn off the alarm (2) Let it ring",
		[ Choice(getInputInt, 1, doNothing, doNothing, 'intro4.2'),
		  Choice(None, 2, doNothing, doNothing, 'intro4.1.2') ] ),

	'intro4.2': StoryPoint(dialogue, "You turn off the alarm. It's so cold that you don't want to get out of bed. \n(1) Look around (2) Get out of bed",
		[ Choice(getInputInt, 1, doNothing, doNothing, 'intro4.2.1'),
		  Choice(None, 2, doNothing, doNothing, 'intro4.2.2') ] ),

	'intro4.2.1': StoryPoint(dialogue, "You look around your room. There's a desk with a bunch of papers and a computer on it, a dresser with all the drawers half open and clothes spilling out of it onto the floor, and a window with gray drapes hung at the sides. It’s barely light outside. \n(1) Get out of bed",
		[ Choice(getInputInt, 1, doNothing, doNothing, 'intro4.2.2') ] ),

	'intro4.2.2': StoryPoint(dialogue, "You try to get out of bed. But your limbs are all tangled up in the blankets. \n(1) Stare up at the ceiling (2) Struggle",
		[ Choice(getInputInt, 1, doNothing, doNothing, 'intro4.2.3'),
		  Choice(None, 2, doNothing, doNothing, 'intro4.2.4') ] ),

	'intro4.2.3': StoryPoint(dialogue, "You gaze listlessly at the ceiling, wondering if it’s worth it to even try to get out of bed. From downstairs, you hear MOM’s angry voice asking if you’re awake. \n(1) Yell back at MOM (2) Remain silent",
		[ Choice(getInputInt, 1, doNothing, doNothing, 'intro4.2.5'),
		  Choice(None, 2, doNothing, doNothing, 'intro4.2.6') ] ),

	'intro4.2.4': StoryPoint(dialogue, "You thrash back and forth, trying to squirm out of bed, but you can’t seem to escape from the bundle of blankets enveloping you. From downstairs, you hear MOM call your name. \n(1) Scream for help (2) Accept your fate",
		[ Choice(getInputInt, 1, doNothing, doNothing, 'intro4.2.5'),
		  Choice(None, 2, doNothing, doNothing, 'intro4.2.6') ] ),

	'intro4.2.5': StoryPoint(dialogue, "You open your mouth, but before you can make a sound, blankets wrap around your throat and fill your mouth, gagging you with the smell of clean detergent. \n(1) Fight",
		[ Choice(getInputInt, 1, doNothing, doNothing, 'intro5') ] ),

	'intro4.2.6': StoryPoint(dialogue, "You sink deeper into the mattress, a sense of sleepiness descending upon you as you accept a life bound to eternal slumber. But then you are gripped with a sudden sense of determination, as you realize you are too young to die here in this bed. \n(1) Fight",
		[ Choice(getInputInt, 1, doNothing, doNothing, 'intro5') ] ),

	'intro5': StoryPoint(battle, "",
		[ Choice(isTrue, True, doNothing, doNothing, 'intro6') ] ),

	'intro6': StoryPoint(dialogue, "You get up to walk around your room.",
		[ Choice(isTrue, True, doNothing, doNothing, 'intro7') ] ),

	'intro7': StoryPoint(PauseStory, 'intro7',
		[ Choice(isTrue, False, doNothing, doNothing, 'intro8') ] ),



	'introx3': StoryPoint(dialogue, "Who's your favorite dev? (1) Kam (2) DJ (3) Brandon",
		[ Choice(getInputInt, 1, doNothing, doNothing, 'introKam'),
		  Choice(None, 2, doNothing, doNothing, 'introDJ'),
		  Choice(None, 3, doNothing, doNothing, 'introBran') ] ),

	'introKam': StoryPoint(dialogue, "Sick, Kam is a homie",
		[ Choice(isTrue, True, wait, doNothing, 'intro4') ] ),

	'introDJ': StoryPoint(dialogue, "That's the correct choice, DJ rules",
		[ Choice(isTrue, True, wait, doNothing, 'intro4') ] ),

	'introBran': StoryPoint(dialogue, "Awesome, Brandon is lit yo",
		[ Choice(isTrue, True, wait, doNothing, 'intro4') ] ),

	'introx4': StoryPoint(dialogue, "Please walk to the end of the hall",
		[ Choice(isTrue, True, doNothing, doNothing, 'intro5') ] ),

	'introx5': StoryPoint(PauseStory, 'intro6',
		[ Choice(isTrue, False, doNothing, doNothing, 'intro6') ] ),

	'introx6': StoryPoint(dialogue, "Yayyy you made it!",
		[ Choice(isTrue, True, doNothing, doNothing, None) ] )

	}

