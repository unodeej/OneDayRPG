import importlib
import storyPoints

#importlib.import_module(storyPoints.py)

class Game():
	def __init__(self, firstStoryPoint):
		self.firstStoryPoint = firstStoryPoint

	def StartGame(self):
		self.ReadStoryPoint(self.firstStoryPoint)

	def ReadStoryPoint(self, story_point):
		nextStoryPoint = story_point.Run()
		if nextStoryPoint != None:
			self.ReadStoryPoint(nextStoryPoint)

game = Game(storyPoints.story_points.get('intro1'))
game.StartGame()






# class Player():
# 	maxHP = 5
# 	HP = maxHP
# 	def heal(self, amt):
# 		self.HP += amt
# 		if (self.HP > self.maxHP)
# 			self.HP = self.maxHP