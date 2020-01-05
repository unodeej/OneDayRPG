import popup
import time
import display

class UI():
	def __init__(self):
		self.p = popup.Popup(
			text = "",
			buttons = []
			)

	def CreatePopup(self, msg, buttons):
		self.p = popup.Popup(
			text = msg,
			buttons = buttons
			)

		self.p.show()
		popup.display.render()

	def HidePopup(self):
		self.p.hide()

ui = UI()

# This isn't working yet! how to unload a room, @kam?
def clearMap():
	floorDisplay.unloadRoom()

def auto(msg):
	ui.CreatePopup(msg, [])

def dialogue(msg):
	ui.CreatePopup(msg, [popup.Button(text="enter", hotkey=" ")] )

def question(msg):
	i = 0
	newMsg = msg

	while(True):
		findMe = "(" + str(i+1) + ")"
		if findMe in msg:
			if i == 0:
				newMsg = msg[0:msg.find(findMe)]
			i += 1

		else:
			break

	buttonText = ""
	myButtons = []
	for j in range(1, i+1):
		if j == i:
			findMe = "(" + str(j) + ")"
			buttonText = msg[(msg.find(findMe) + len(findMe) ):]
		else:
			findMeFront =  "(" + str(j) + ")"
			findMeEnd =  "(" + str(j+1) + ")"
			buttonText = msg[(msg.find(findMeFront) + len(findMe) ):msg.find(findMeEnd) ]
		myButtons.append(popup.Button(text=buttonText, hotkey=str(j)))

	ui.CreatePopup(newMsg, myButtons)

def message(msg):
	dialogue(msg)
	wait()

	

def OneSec():
	time.sleep(1)
	return True

def wait():
	try:
	    input("")
	    ui.HidePopup()
	except SyntaxError:
	    pass

def getInputStr(msg = ""):
	m = input(msg)
	ui.HidePopup()
	return str(m)

def getInputIntHelper(c):
	try:
		ui.HidePopup()
		val = int(c)

		return val
	except ValueError:
		print("Please input a number")
		return getInputInt(c)
	
def getInputInt(msg = ""):
	c = input(msg)
	return getInputIntHelper(c)
	

def getInputAnyInt():
	c = input()
	return getInputIntHelper(c)

