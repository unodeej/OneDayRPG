class Entity():
	def __init__(self, maxHP, attack, defense):
		self.maxHP = maxHP
		self.attack = attack
		self.defense = defense

		self.HP = self.maxHP

	def Heal(self, amt):
		self.HP += amt
		if (self.HP > self.maxHP):
			self.HP = self.maxHP

	def Damage(self, amt):
		self.HP -= amt
		if (self.HP <= 0):
			self.HP = 0

	def Attack(self, other):
		dmg = self.attack - other.defense
		if (dmg < 0):
			dmg = 0
		other.Damage(dmg)


class Player(Entity):
	def __init__(self, maxHP, attack, defense):
		self.name = "Sanpel"
		Entity.__init__(self, maxHP, attack, defense)

class Enemy(Entity):
	def __init__(self, name, maxHP, attack, defense):
		self.name = name
		Entity.__init__(self, maxHP, attack, defense)