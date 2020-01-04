import UI

def getInputInt():
	c = input()
	try:
	   val = int(c)
	   return val
	except ValueError:
	  try:
	    val = float(user_input)
	    UI.message("Invalid input.")
	    return getInputInt(msg)
	  except ValueError:
	      UI.message("Invalid input.")
	      return getInputInt(msg)

def question(msg):
	return UI.question(UI.ui, msg)

class Battle():
	def __init__(self, player, enemies):
		self.player = player
		self.enemies = enemies

	def Start(self):
		self.PlayerTurn()

	def IsBattleOver(self):
		if self.player.HP <= 0:
			UI.message("You died!")
			return True
		for e in self.enemies:
			if e.HP > 0:
				return False
		UI.message("You win!")
		return True

	def PlayerTurn(self):
		player = self.player
		enemies = self.enemies

		question("It's your turn. (1) Attack (2) Guard (3) Item (4) Run")
		inp = getInputInt()
		if (inp == 1):
			# Attack
			i = 1
			msg = ""
			for e in enemies:
				msg += "(" + str(i) + ") " + e.name + " [" + str(e.HP) + "/" + str(e.maxHP) + "] "
				i += 1
			question(msg)

			msg = ""
			inp = getInputInt()
			for j in range(1, i):
				if inp == j:
					target = enemies[j-1]
					if (target.HP <= 0):
						msg += "You attack the corpse of " + target.name + ", for some reason! "
					else:
						msg += "You attack " + target.name + "! "
					player.Attack(target)
			for e in enemies:
				msg += e.name + ": [" + str(e.HP) + "/" + str(e.maxHP) + "] "
			UI.message(msg)

		elif (inp == 2):
			# Guard
			UI.message("You guard.")
		elif (inp == 3):
			# Item
			UI.message("You have no items, nerd.")
		elif (inp == 4):
			# Run
			UI.message("There's nowhere to run, nerd.")
		else:
			UI.message("Invalid input.")
			self.PlayerTurn()

		if not self.IsBattleOver():
			self.EnemyTurn()

	def EnemyTurn(self):
		player = self.player
		enemies = self.enemies

		UI.message("Enemy Turn.")

		msg = ""
		for e in enemies:
			if (e.HP <= 0):
				continue
			# Attack
			msg += e.name + " attacks! "
			e.Attack(player)
			msg += player.name + ": [" + str(player.HP) + "/" + str(player.maxHP) + "] "
		UI.message(msg)


		if not self.IsBattleOver():
			self.PlayerTurn()
