def getInputInt():
	c = input()
	try:
	   val = int(c)
	   return val
	except ValueError:
	  try:
	    val = float(user_input)
	    print("Invalid input.")
	    return getInputInt(msg)
	  except ValueError:
	      print("Invalid input.")
	      return getInputInt(msg)

class Battle():
	def __init__(self, player, enemies):
		self.player = player
		self.enemies = enemies

	def Start(self):
		self.PlayerTurn()

	def IsBattleOver(self):
		if self.player.HP <= 0:
			print("You died!")
			return True
		for e in self.enemies:
			if e.HP > 0:
				return False
		print("You win!")
		return True

	def PlayerTurn(self):
		player = self.player
		enemies = self.enemies

		print("It's your turn. (1) Attack (2) Guard (3) Item (4) Run")
		inp = getInputInt()
		if (inp == 1):
			# Attack
			i = 1
			for e in enemies:
				print("(" + str(i) + ") " + e.name + " [" + str(e.HP) + "/" + str(e.maxHP) + "]")
				i += 1
			inp = getInputInt()
			for j in range(1, i):
				if inp == j:
					target = enemies[j-1]
					if (target.HP <= 0):
						print("You attack the corpse of " + target.name + ", for some reason!")
					else:
						print("You attack " + target.name + "!")
					player.Attack(target)
			for e in enemies:
				print(e.name + ": [" + str(e.HP) + "/" + str(e.maxHP) + "]")

		elif (inp == 2):
			# Guard
			print("You guard.")
		elif (inp == 3):
			# Item
			print("You have no items, nerd.")
		elif (inp == 4):
			# Run
			print("There's nowhere to run, nerd.")
		else:
			print ("Invalid input.")
			self.PlayerTurn()

		if not self.IsBattleOver():
			self.EnemyTurn()

	def EnemyTurn(self):
		player = self.player
		enemies = self.enemies

		print("Enemy Turn.")

		for e in enemies:
			if (e.HP <= 0):
				continue
			# Attack
			print(e.name + " attacks!")
			e.Attack(player)
			print(player.name + ": [" + str(player.HP) + "/" + str(player.maxHP) + "]")


		if not self.IsBattleOver():
			self.PlayerTurn()
