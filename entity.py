class Entity():
	def __init__(self, maxHP, attack, defense):
		self.maxHP = maxHP
		self.attack = attack
		self.defense = defense

		self.HP = self.maxHP

		self.buffs = []

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

	def UseBuff(self, buff):
		if (buff.stat == "maxHP"):
			self.maxHP += buff.amt
		elif (buff.stat == "currentHP"):
			self.HP += buff.amt
		elif (buff.stat == "attack"):
			self.attack += buff.amt
		elif (buff.stat == "defense"):
			self.defense += buff.amt
		else:
			print("The buff had no effect!")

		self.buffs.append(buff)

	def ExpireBuff(self, buff):
		if (buff.stat == "maxHP"):
			self.maxHP -= buff.amt
		elif (buff.stat == "currentHP"):
			self.HP -= buff.amt
		elif (buff.stat == "attack"):
			self.attack -= buff.amt
		elif (buff.stat == "defense"):
			self.defense -= buff.amt
		else:
			print("The buff had no effect!")

		self.buffs.remove(buff)

class Player(Entity):
	def __init__(self, maxHP, attack, defense):
		self.name = "Sanpel"
		Entity.__init__(self, maxHP, attack, defense)

class Enemy(Entity):
	def __init__(self, name, maxHP, attack, defense, flavorText, attackText):
		self.name = name
		self.flavorText = flavorText
		self.attackText = attackText
		Entity.__init__(self, maxHP, attack, defense)

class Buff():
	def __init__(self, stat, amt, duration):
		self.stat = stat
		self.amt = amt
		self.duration = duration