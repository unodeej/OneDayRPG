# import importlib
import storyPoints
import cliInput
import display as dis
import floorDisplay
import entity
import battle



class Game():
	def __init__(self, firstStoryPoint):
		
		self.firstStoryPoint = firstStoryPoint
		self.storyPaused = False
		self.pausedStoryPoint = None

		self.player = entity.Player(5, 2, 0)

		self.mapEvent = False

		storyPoints.game = self
		floorDisplay.room.game = self

	def StartGame(self):
		self.ReadStoryPoint(self.firstStoryPoint)

	def ReadStoryPoint(self, story_point):
		nextStoryPoint = story_point.Run()
		if nextStoryPoint != None:
			self.ReadStoryPoint(nextStoryPoint)

	def Battle(player, enemies):
		battle = Battle(player, enemies)


	def TriggerMapEvent(self, mapName, xPos, yPos, char):
		self.mapEvent = True
		storyPoints.TriggerEvent(mapName, xPos, yPos, char)

	def Update(self):
		entityViewport = floorDisplay.room.loadRoom("floor1.txt")
		while(self.storyPaused == True):
			floorDisplay.room.Update()


game = Game(storyPoints.story_points.get('intro1'))
game.StartGame()





