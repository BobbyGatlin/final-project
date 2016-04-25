import random

def msg(room):
    if room['msg'] == '':
        return "You have entered the " + room['name'] + '.'
    else:
        return room['msg']

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
    
def main():
    dirs = (0,0,0,0)

    livingroom = {'name':'Living Room','directions':dirs,'msg':''}
    kitchen = {'name':'Kitchen and Dining Room','directions':dirs,'msg':''}
    hall = {'name':'Hall','directions':dirs,'msg':''}
    bathroom = {'name':'Bathroom','directions':dirs,'msg':''}
    bedrooma = {'name':'Bedroom #1','directions':dirs,'msg':''}
    bedroomb = {'name':'Bedroom #2','directions':dirs,'msg':''}

    livingroom['directions'] = (kitchen,0,0,0)
    kitchen['directions'] = (hall,0,livingroom,bedrooma)
    hall['directions'] = (0,bathroom,kitchen,bedroomb)
    bathroom['directions'] = (0,0,0,hall)
    bedrooma['directions'] = (bedroomb,kitchen,0,0)
    bedroomb['directions'] = (0,hall,bedrooma,0)

    rooms = [kitchen,hall,bathroom,bedrooma,bedroomb]
    room_with_necronomicon = random.choice(rooms)
    necronomicon_found = False
    room = livingroom
    print('Welcome to Hell once again, Ash. \n' +
          'You swore you would never step foot into this God-Forsaken cabin ever again but here you are. \n' +
          'All because somebody screwed up and brought hell back to town by reading a passage out of that cursed Book of the Dead, the Necronomicon Ex Mortis. \n' +
          'Now, you and your trusty Boomstick have to send those damn Deadites back to where they came from. \n' +
          'So find the book, say the passage (Klattu Barada Nikto), and end this for good this time.')

    while True:
        if necronomicon_found and room['name'] == 'Living Room':
            print('As you step into the room with the book in hand, you can\'t help but to feel the overwhelming presence of evil. \n' +
            'The whispers of the Deadites, coming to consume every thing you are, is deafening. "We\'ll swallow your soul..We\'ll swallow your soul..." \n' +
            'You open the book and say the words... Wait, what were those words again... "Klattu Barada Necktie, Nectarine, Nhhhmmmm... \n' +
            'You cough out a noise that slightly resembles the sound that you can vaguely remember. \n' +
            'And just like that, everything is quiet. \n' +
            'You did it Ash. You can now leave this Cabin, seal away the Necronomicon, and never return. \n' +
            '"Hail to the King, baby!" \n'
            'The End...or is it?')
            break;
        elif not necronomicon_found and room['name'] == room_with_necronomicon['name']:
              necronomicon_found = True
              print(msg(room) + 'There it is. The damn book that started this thing... \n' +
                    'The Necronomicon Ex Mortis...Book of the Dead. Inked in human blood and bound in human flesh, \n' +
                    'This book has ruined your life since the first time you saw it. \n'+
                    'Here\'s your chance to finish this. Get the book to the living room and recite the passage.')
              room['msg'] = ('You are back in the ' + room['name'] +
                         '! You already have the book. ' +
                         'Hurry and get back to the living room before more deadites come!')
        else:
          print(msg(room))
          room['msg'] = 'You are back in the ' +room['name']

        stuck = True
        while stuck:
              dir = input("Which way are you gonna go Ash: N,E,S, or W? ")
              choice = get_choice(room,dir)
              if choice == -1:
                  print("So you're a wise guy, eh? Please enter N,E,S, or W? ")
              elif choice == 4:
                  print("Nope. Can't go that way.")
              else:
                  room = room['directions'][choice]
                  stuck = False

main()
          
          
          
          

          
          
        
              

              

              
        
        
        
        
