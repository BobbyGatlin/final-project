#First off let's just say I'm a huge Evil Dead fan. When I had the opportunity to choose to develop my own game and write a small story featuring Ash, I was all about it.
#This is my design document to explain what went into designing this game.



import random
#I had to import random so later I could make the room the necronomicon is hidden in random.

def msg(room):
    if room['msg'] == '':
        return "\nYou have entered the " + room['name'] + '.'
    else:
        return room['msg']
# This function is the message that reads when you enter a room along with the room name

def get_choice(room,dir):
    if dir=='N':
        choice = 0
    elif dir=='E':
        choice = 1
    elif dir=='S':
        choice = 2
    elif dir=='W':
        choice = 3
    else:
        return -1

    if room['directions'][choice] == 0:
        return 4
    else:
        return choice
#This function defines what directions will be used for choices in the ruple I made to define the names

    
def main():
    dirs = (0,0,0,0)
#This tuple is the foundation for all directional choices (N,E,S,W). 

    livingroom = {'name':'Living Room \nYou swear everything is laughing as you. \nYou feel your own sanity breaking as you bust into laughter along with the sofa and mounted deer head','directions':dirs,'msg':''}
    kitchen = {'name':'Kitchen and Dining Room \nThe room where you had to cut off your own hand after it went bad. \nAt least now you have your trusty chainsaw hand','directions':dirs,'msg':''}
    hall = {'name':'Hall \nYou start to feel the darkness overtake you as if possessing your very soul. \nYou regain your senses and shake it off','directions':dirs,'msg':''}
    bathroom = {'name':'Bathroom \nDefinitely the scariest room in the whole damn place. \nWhoever last used the john didn\'t flush ','directions':dirs,'msg':''}
    bedrooma = {'name':'Bedroom #1 \nYou pull out your boomstick and lay the smack down on a nasty deadite waiting for an ambush. \nYou then decapitate it with your chainsaw hand','directions':dirs,'msg':''}
    bedroomb = {'name':'Bedroom #2 \nMemories of your beloved Linda playing the piano flood into your mind. \nThat was before you had to cut her head off in the woodshed..','directions':dirs,'msg':''}
#This is defining the room names along with the flavor text that I added that comes into play when you enter a room. In my first commit I didn't have the flavor text, but I found that boring.

    livingroom['directions'] = (kitchen,0,0,0)
    kitchen['directions'] = (hall,0,livingroom,bedrooma)
    hall['directions'] = (0,bathroom,kitchen,bedroomb)
    bathroom['directions'] = (0,0,0,hall)
    bedrooma['directions'] = (bedroomb,kitchen,0,0)
    bedroomb['directions'] = (0,hall,bedrooma,0)
#This is defining which room you enter when you input a direction. For instance,(kitchen,0,0,0) means that the kitchen is to the N and every other direction is blocked. 

    rooms = [kitchen,hall,bathroom,bedrooma,bedroomb]
    room_with_necronomicon = random.choice(rooms)
    necronomicon_found = False
    room = livingroom
    print('Welcome to Hell once again, Ash.' +
          '\nYou swore you would never step foot into this God-Forsaken cabin ever again but here you are.' +
          '\nAll because somebody screwed up and brought hell back to town by reading a passage out of that cursed Book of the Dead, the Necronomicon Ex Mortis.' +
          '\nNow, you and your trusty Boomstick have to send those damn Deadites back to where they came from.' +
          '\nSo find the book, say the passage (Klattu Barada Nikto), and end this for good this time.')
#This states that the Necronomicon can be found in every room but the entrance and that it will be hidden randomly. This is why I had to import random in the beginning.

    while True:
        if necronomicon_found and room['name'] == 'Living Room \nYou swear everything is laughing as you. \nYou feel your own sanity breaking as you bust into laughter along with the sofa and mounted deer head':
            print('\nAs you step into the room with the book in hand, you can\'t help but to feel the overwhelming presence of evil.' +
            '\nThe whispers of the Deadites, coming to consume every thing you are, is deafening. "We\'ll swallow your soul..We\'ll swallow your soul..."' +
            '\nYou open the book and say the words... Wait, what were those words again... "Klattu Barada Necktie, Nectarine, Nhhhmmmm...' +
            '\nYou cough out a noise that slightly resembles the sound that you can vaguely remember.' +
            '\nAnd just like that, everything is quiet.' +
            '\nYou did it Ash. You can now leave this Cabin, seal away the Necronomicon, and never return.' +
            '\n"Hail to the King, baby!"' +
            '\n'''
            '\nThe End...or is it?\n')
            break;
#This is what happens after you have found the Necronomicon and you enter the Living Room. 

        elif not necronomicon_found and room['name'] == room_with_necronomicon['name']:
              necronomicon_found = True
              print(msg(room) + '\n''\nThere it is. The damn book that started this whole mess... \n' +
                    'The Necronomicon Ex Mortis...Book of the Dead. Inked in human blood and bound in human flesh, \n' +
                    'This book has ruined your life since the first time you saw it. \n'+
                    'Here\'s your chance to finish this. Get the book to the living room and recite the passage.')
              room['msg'] = ('You are back in the ' + room['name'] +
                         '! You already have the book. ' +
                         'Hurry and get back to the living room before more deadites come!')
#This is what happens when you find the Necronomicon              

        else:
          print(msg(room))
          room['msg'] = 'You are back in the ' +room['name']
#This is what happens when you reenter a room after being in it once.

        stuck = True
        while stuck:
              dir = input("\nWhich way are you gonna go Ash: N,E,S, or W? ")
              choice = get_choice(room,dir)
              if choice == -1:
                  print("So you're a wise guy, eh? Please enter N,E,S, or W? ")
              elif choice == 4:
                  print("Nope. Can't go that way.")
              else:
                  room = room['directions'][choice]
                  stuck = False
#This ask the user to pick a direction and defines what happens if you enter an invalid choice or a direction you can't go.

main()

k=input("Press close to exit")
#I added this so if ran in the command window it wouldn't just exit before you could read the ending.          
          
          
          

          
          
        
              

              

              
        
        
        
        
