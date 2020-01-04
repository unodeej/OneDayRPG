import popup

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

def dialogue(u, msg):
	u.CreatePopup(msg, [popup.Button(text="enter", hotkey=" ")] )

def question(u, msg):
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

	u.CreatePopup(newMsg, myButtons)

def message(msg):
	dialogue(ui, msg)
	wait()

def OneSec():
	time.sleep(1)
	return True

def wait():
	try:
	    input("")
	except SyntaxError:
	    pass

def getInputStr(msg = ""):
	return str(input(msg))
	
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


