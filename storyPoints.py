import time
import battle as BATTLE
import entity
import UI

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


def battle(enemies):
	batt = BATTLE.Battle(game.player, enemies)

	batt.Start()

def isTrue():
	return True

def doNothing(arg = ""):
	return None



def assignName(name):
	game.player.name = name

def PauseStory(arg = ''):
	# Create a listener in Game
	game.storyPaused = True
	game.pausedStoryPoint = arg
	game.Update()

def ResumeStory():
	game.storyPaused = False
	game.pausedStoryPoint = None

def TriggerEvent(mapName, xPos, yPos, char):
	x = str(xPos)
	y = str(yPos)
	print(mapName + ' ' + x + "." + y)
	story_points.get(mapName + ' ' + x + "." + y).Run()
	# while(True):
	# 	print(mapName + char + x + "." + y)

def dialogue(msg):
	return UI.dialogue(msg)

def exitMap(msg):
	UI.clearMap()
	ResumeStory()
	return UI.dialogue(msg)

def question(msg):
	return UI.question(msg)

def questionWithName(msg):
	return UI.dialogue(game.player.name + msg)



story_points = {
	'intro1': StoryPoint(dialogue, "Welcome to One Day RPG!",
		[ Choice(isTrue, True, UI.wait, doNothing, 'intro6' ) ] ),

	'intro2': StoryPoint(dialogue, "What is your name?",
		[ Choice(isTrue, True, UI.getInputStr, assignName, 'intro2.1') ] ),
	'intro2.1': StoryPoint(questionWithName, ": That's your name? (1) Yes (2) No",
		[ Choice(UI.getInputInt, 1, doNothing, doNothing, 'intro3.1'),
		  Choice(True, 2, doNothing	, doNothing, 'intro2') ] ),

	'intro3.1': StoryPoint(UI.auto, ".",
		[ Choice(UI.OneSec, True, doNothing, doNothing, 'intro3.2') ] ),
	'intro3.2': StoryPoint(UI.auto, ".",
		[ Choice(UI.OneSec, True, doNothing, doNothing, 'intro3.3') ] ),
	'intro3.3': StoryPoint(UI.auto, ".",
		[ Choice(UI.OneSec, True, doNothing, doNothing, 'intro3.4') ] ),

	'intro3.4': StoryPoint(dialogue, "7:00 A.M.",
		[ Choice(isTrue, True, UI.wait, doNothing, 'intro3.5') ] ),
	'intro3.5': StoryPoint(UI.auto, "Zzzzzzzzz.....",
		[ Choice(UI.OneSec, True, doNothing, doNothing, 'intro3.6') ] ),
	'intro3.6': StoryPoint(UI.auto, "Zzzzzzzzzzzzzz........",
		[ Choice(UI.OneSec, True, doNothing, doNothing, 'intro4.1') ] ),

	'intro4.1': StoryPoint(question, "You hear a blaring alarm clock. (1) Turn off the alarm (2) Let it ring",
		[ Choice(UI.getInputInt, 1, doNothing, doNothing, 'intro4.2'),
		  Choice(None, 2, doNothing, doNothing, 'intro4.1.1') ] ),

	'intro4.1.1': StoryPoint(question, "The alarm gets louder. (1) Turn off the alarm (2) Let it ring",
		[ Choice(UI.getInputInt, 1, doNothing, doNothing, 'intro4.2'),
		  Choice(None, 2, doNothing, doNothing, 'intro4.1.2') ] ),

	'intro4.1.2': StoryPoint(question, "It gets even louder. (1) Turn off the alarm (2) Let it ring",
		[ Choice(UI.getInputInt, 1, doNothing, doNothing, 'intro4.2'),
		  Choice(None, 2, doNothing, doNothing, 'intro4.1.2') ] ),

	'intro4.2': StoryPoint(question, "You turn off the alarm. It's so cold that you don't want to get out of bed. (1) Look around (2) Get out of bed",
		[ Choice(UI.getInputInt, 1, doNothing, doNothing, 'intro4.2.1'),
		  Choice(None, 2, doNothing, doNothing, 'intro4.2.2') ] ),

	'intro4.2.1': StoryPoint(question, "You look around your room. There's a desk with a bunch of papers and a computer on it, a dresser with all the drawers half open and clothes spilling out of it onto the floor, and a window with gray drapes hung at the sides. It’s barely light outside. (1) Get out of bed",
		[ Choice(UI.getInputInt, 1, doNothing, doNothing, 'intro4.2.2') ] ),

	'intro4.2.2': StoryPoint(question, "You try to get out of bed. But your limbs are all tangled up in the blankets. (1) Stare up at the ceiling (2) Struggle",
		[ Choice(UI.getInputInt, 1, doNothing, doNothing, 'intro4.2.3'),
		  Choice(None, 2, doNothing, doNothing, 'intro4.2.4') ] ),

	'intro4.2.3': StoryPoint(question, "You gaze listlessly at the ceiling, wondering if it’s worth it to even try to get out of bed. From downstairs, you hear MOM’s angry voice asking if you’re awake. (1) Yell back at MOM (2) Remain silent",
		[ Choice(UI.getInputInt, 1, doNothing, doNothing, 'intro4.2.5'),
		  Choice(None, 2, doNothing, doNothing, 'intro4.2.6') ] ),

	'intro4.2.4': StoryPoint(question, "You thrash back and forth, trying to squirm out of bed, but you can’t seem to escape from the bundle of blankets enveloping you. From downstairs, you hear MOM call your name. (1) Scream for help (2) Accept your fate",
		[ Choice(UI.getInputInt, 1, doNothing, doNothing, 'intro4.2.5'),
		  Choice(None, 2, doNothing, doNothing, 'intro4.2.6') ] ),

	'intro4.2.5': StoryPoint(question, "You open your mouth, but before you can make a sound, blankets wrap around your throat and fill your mouth, gagging you with the smell of clean detergent. (1) Fight",
		[ Choice(UI.getInputInt, 1, doNothing, doNothing, 'intro5') ] ),

	'intro4.2.6': StoryPoint(question, "You sink deeper into the mattress, a sense of sleepiness descending upon you as you accept a life bound to eternal slumber. But then you are gripped with a sudden sense of determination, as you realize you are too young to die here in this bed. (1) Fight",
		[ Choice(UI.getInputInt, 1, doNothing, doNothing, 'intro5') ] ),

	'intro5': StoryPoint(battle, [ entity.Enemy("BED", 1000, 1, 0,
												["BED stares at you enticingly, tempting you to dive into its sheets.",
												 "BED reminds you of all the years you spent together.",
												 "BED’s sheets rustle ominously.",
												 "BED creaks under its own massive weight."],
												["BED's Blankets wrap around your throat!",
												 "The pain from BED's attacks feels too real to be a bad dream!",
												 "BED's Pillows smother you, making it hard to breathe!",
												 "The overwhelming scent of BED's fabric softener makes you gag!",] ) ],
		[ Choice(isTrue, True, doNothing, doNothing, 'intro6') ] ),

	'intro6': StoryPoint(dialogue, "You get up to walk around your room.",
		[ Choice(isTrue, True, doNothing, doNothing, 'intro7') ] ),

	'intro7': StoryPoint(PauseStory, 'intro7',
		[ Choice(isTrue, False, doNothing, doNothing, 'intro8') ] ),

	'floor1 2.2': StoryPoint(dialogue, 'The bed DOES look enticing, but you are late :(',
		[ Choice(isTrue, True, UI.wait, doNothing, None) ] ),
	'floor1 2.3': StoryPoint(dialogue, 'The bed DOES look enticing, but you are late :(',
		[ Choice(isTrue, True, UI.wait, doNothing, None) ] ),
	'floor1 3.2': StoryPoint(dialogue, 'The bed DOES look enticing, but you are late :(',
		[ Choice(isTrue, True, UI.wait, doNothing, None) ] ),
	'floor1 3.3': StoryPoint(dialogue, 'The bed DOES look enticing, but you are late :(',
		[ Choice(isTrue, True, UI.wait, doNothing, None) ] ),

	'floor1 17.1': StoryPoint(dialogue, 'Your desk is cluttered, but you can clean it later...',
		[ Choice(isTrue, True, UI.wait, doNothing, None) ] ),
	'floor1 17.2': StoryPoint(dialogue, 'Your desk is cluttered, but you can clean it later...',
		[ Choice(isTrue, True, UI.wait, doNothing, None) ] ),
	'floor1 17.3': StoryPoint(dialogue, 'Your desk is cluttered, but you can clean it later...',
		[ Choice(isTrue, True, UI.wait, doNothing, None) ] ),
	'floor1 17.4': StoryPoint(dialogue, 'Your desk is cluttered, but you can clean it later...',
		[ Choice(isTrue, True, UI.wait, doNothing, None) ] ),
	'floor1 18.1': StoryPoint(dialogue, 'Your desk is cluttered, but you can clean it later...',
		[ Choice(isTrue, True, UI.wait, doNothing, None) ] ),
	'floor1 19.1': StoryPoint(dialogue, 'Your desk is cluttered, but you can clean it later...',
		[ Choice(isTrue, True, UI.wait, doNothing, None) ] ),
	'floor1 20.1': StoryPoint(dialogue, 'Your desk is cluttered, but you can clean it later...',
		[ Choice(isTrue, True, UI.wait, doNothing, None) ] ),
	'floor1 20.2': StoryPoint(dialogue, 'Your desk is cluttered, but you can clean it later...',
		[ Choice(isTrue, True, UI.wait, doNothing, None) ] ),
	'floor1 20.3': StoryPoint(dialogue, 'Your desk is cluttered, but you can clean it later...',
		[ Choice(isTrue, True, UI.wait, doNothing, None) ] ),
	'floor1 20.4': StoryPoint(dialogue, 'Your desk is cluttered, but you can clean it later...',
		[ Choice(isTrue, True, UI.wait, doNothing, None) ] ),
	'floor1 18.4': StoryPoint(dialogue, 'Your desk is cluttered, but you can clean it later...',
		[ Choice(isTrue, True, UI.wait, doNothing, None) ] ),
	'floor1 19.4': StoryPoint(dialogue, 'Your desk is cluttered, but you can clean it later...',
		[ Choice(isTrue, True, UI.wait, doNothing, None) ] ),


    'floor1 30.7': StoryPoint(exitMap, 'Time to go!',
		[ Choice(isTrue, True, UI.wait, doNothing, 'intro2') ] ),
	'floor1 31.7': StoryPoint(exitMap, 'Time to go!',
		[ Choice(isTrue, True, UI.wait, doNothing, 'intro2') ] ),


	'introx3': StoryPoint(dialogue, "Who's your favorite dev? (1) Kam (2) DJ (3) Brandon",
		[ Choice(UI.getInputInt, 1, doNothing, doNothing, 'introKam'),
		  Choice(None, 2, doNothing, doNothing, 'introDJ'),
		  Choice(None, 3, doNothing, doNothing, 'introBran') ] ),

	'introKam': StoryPoint(dialogue, "Sick, Kam is a homie",
		[ Choice(isTrue, True, UI.wait, doNothing, 'intro4') ] ),

	'introDJ': StoryPoint(dialogue, "That's the correct choice, DJ rules",
		[ Choice(isTrue, True, UI.wait, doNothing, 'intro4') ] ),

	'introBran': StoryPoint(dialogue, "Awesome, Brandon is lit yo",
		[ Choice(isTrue, True, UI.wait, doNothing, 'intro4') ] ),

	'introx4': StoryPoint(dialogue, "Please walk to the end of the hall",
		[ Choice(isTrue, True, doNothing, doNothing, 'intro5') ] ),

	'introx5': StoryPoint(PauseStory, 'intro6',
		[ Choice(isTrue, False, doNothing, doNothing, 'intro6') ] ),

	'introx6': StoryPoint(dialogue, "Yayyy you made it!",
		[ Choice(isTrue, True, doNothing, doNothing, None) ] )

	}
