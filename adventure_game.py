from sys import exit


def moat_room():
	print "You approach a moat that extends far North of you, but you can see your castle in the distance!  Should you try to use your aquatic skills and swim, or should you try to use your air-born awesomeness and fly!"
	moat_room = False
	
	while True:
		choice = raw_input("> ")
		
		if choice == "swim":
			print "You take off your clothing so it doesn't weigh you down.  You get into the water and swim for a long, long time until you feel something rub against your legs.  It's a massive and horrific shark!"
			dead("The shark eats your face off, sorry... Try again!")
		elif choice == "fly":
			dead("You remember what Gandalf said once in Lord of the Rings. \"Fly you fools\" as he fell down into the pit during \'The Fellowship of the Ring\' and you turn to see an Eagle soaring high above you.  Pulling Gandalf's staff straight outta yo ass, you summon the Eagle to fly you to your castle, good job!")
			moat_room = True
		else:
			print "That is not an option, try again."

		
def cave_room():
	print "Now that you have come to the cave, you can either turn back or push on."
	cave_room = False
	
	while True:
		choice = raw_input("> ")
	
		if choice == "turn back":
			print "Smart move, you avoided death."
			moat_room()
		elif choice == "push on":
			dead("You frantically move into the cave when suddenly you hear a screech.  A giant bat with ferocious wings flies above you and grabs with with its claws.  It flies you to the farthest point in the cave and eats you.  Yuck.")
			cave_room = True	
		else:
		    print "Type\'turn back\' or \'push on\'."
	

def wizard_room():
	print "You approach a mystical Wizard.  He is wearing a tall pointed grey hat, a long grey cloak, and a silver scarf.  He has a long white beard and bushy eyebrows that stick out beyond the brim of his hat."
	print "You\'re curious, yet you are also cautious as you do not know what he is capable of."
	print "The Wizard turns to you and says, \'A boy who is taking a break from his homework to play a game is wandering through the forest, he sees the road forks both left and right.  Which road does he take?"
	
	choice = raw_input("> ")
	
	if choice == "left":
		print "The Wizard gazes deeply into your eyes and sighs..."
		print "\"That is wrong\", he says."
		print "The Wizard Kamehameha's you, but thanks to the fact that you are watching Dragon Ball, you dodge it and run towards a cave."
		cave_room()
	elif choice == "right":
		print "The Wizard creepily smiles at you and waves you to continue on through the wood."	
		moat_room()
	else:
		print "That isn't an option, stupid."

		
def troll_room():
	print "Off in the distance you see a campfire."
	print ".\n" * 10
	print "Once you get closer you see that a group of trolls is cooking supper."
	print "It appears they have a precious green jewel with them.  Do you take the jewel or run away?"
	
	choice = raw_input("> ")
	
	if choice == "take the jewel":
		print "You stupidly try to take on a goup of trolls, you realize they had been planning on cooking YOU for supper.  R.I.P"
		dead("They rip you to shreds!")
	elif choice == "run away":
		print "You notice a cloak to the side of the camp.  It's an invisibility cloak! You put it on and sneak past the hungry trolls and hear one of them say, \"What's for dinner?\""
		moat_room()
	else:
		print "Type \'take the jewel\' or \'run away\'. Any other choice is just plain silly."

		
def dead(why):
	print why, "Dumbass!"
	exit(0)


def start():
	print "You are a handsome prince who is in a forest far, far away.  You need to get back to your castle to marry the beautiful princess Bulma."
	print "As you move through the trees, you notice a road."
	print "There is a fork in the road."
	print "Which way do you go, left or right?"

	choice = raw_input("> ")
	
	if choice == "left":
		troll_room()
	elif choice == "right":
		wizard_room()
	else:
		dead("You are dumb for not typing \'left\' or \'right\'. You die.")
		
start()