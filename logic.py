import time
import sys
import random
turnc = 0
def TitleScreen():
  
  '''Displays title.'''

  print("     _________            _______                            ")
  print("     \__   __/ |\     /| (  ____ \                           ")
  print("        ) (    | )   ( | | (    \/                           ")
  print("        | |    | (___) | | (__                               ")
  print("        | |    |  ___  | |  __)                              ")
  print("        | |    | (   ) | | (                                 ")
  print("        | |    | )   ( | | (____/\                           ")
  print("        )_(    |/     \| (_______/                           ")
  print(" _______   _______  _________ _________  _         _______   _______   _______   ")
  print("(  ____ \ (  ____ \ \__   __/ \__   __/ ( \       (  ____ \ (  ____ ) (  ____ \  ")
  print("| (    \/ | (    \/    ) (       ) (    | (       | (    \/ | (    )| | (    \/  ")
  print("| (_____  | (__        | |       | |    | |       | (__     | (____)| | (_____   ")
  print("(_____  ) |  __)       | |       | |    | |       |  __)    |     __) (_____  )  ")
  print("      ) | | (          | |       | |    | |       | (       | (\ (          ) |  ")
  print("/\____) | | (____/\    | |       | |    | (____/\ | (____/\ | ) \ \__ /\____) |  ")
  print("\_______) (_______/    )_(       )_(    (_______/ (_______/ |/   \__/ \_______)  ")
  print()
  print("  Your goal is to beat the challenges that will appear as you play on.           ")
  print()
  print("                      Type '-help' for sets of commands                        ")
  print()
  print("              To win, you must meet the following conditions:                  ")
  print("                 * Greater than 100 Houses have been build                     ")
  print("                 * Greater than 45 Water Mills have been build                 ")
  print("                 * Greater than 45 Farms have been build                       ")
  print("                 * Greater than 10 Quarries have been build                    ")
  print("                 * Greater than 10 Hospitals have been build                   ") 
  print("                 * Greater than 100 Opinion towards player                     ")
  print("                 * Greater than 85 Stability towards player                    ")
  print()

def prob(b):
  a = random.randint(1,100)
  if (a % b == 0):
    return True
  else:
    return False



def Players(Player, TypeCode):
  '''Process for any player related logic.'''



  if TypeCode == 0:
    # Displays player string based on given Player value

    if Player == 1:
      return "{Player 1} - "
    else:
      return "{Player 2} - "
  elif TypeCode == 1:
    # Swaps Player value

    if Player == 1:
      return 2
    else:
      return 1

def Confirmation():
  '''Used to confirm.'''
  print("Are you sure you want to proceed? (Y/N):")
  inputString = input()
  inputString = str.upper(inputString)

  if inputString[0] == "Y":
    return True
  else:
    return False

def DoubleCheck(Player, Player1Inventory, Player2Inventory):
    if Player == 1:
        for i in range(0, 17):
            if Player1Inventory[i] < 0:
                Player1Inventory[i] = 0

        if Player1Inventory[4] == 0 and Player1Inventory[5] == 0:
            print("Because of Player 1's stability and opinion is rockbottom, the people have revolted and liberated from Player 1's rule.")
            print("Player 2 wins!")
            sys.exit()
    else:
        for i in range(0, 17):
            if Player2Inventory[i] < 0:
                Player2Inventory[i] = 0

        if Player2Inventory[4] == 0 and Player2Inventory[5] == 0:
            print("Because of Player 2's stability and opinion is rockbottom, the people have revolted and liberated from Player 2's rule.")
            print("Player 1 wins!")
            sys.exit()

def opi(Player1Inventory, Player2Inventory, Player):
 print("[Villagers say:]")
 if Player == 1:
    if Player1Inventory[5] <= 99:
        print (random.choice(["This place is just like a barren wasteland and the water is like pee”,“ hey get your game together this place is burning”,“ Is the player AFK?"]))
    elif (Player1Inventory[5] >= 100 and Player1Inventory[5] <= 399):
        print(random.choice(["How are we not dead yet?","This is like living in a blank apartment"]))
    elif Player1Inventory[5] >= 400 and Player1Inventory[5] <= 599:
        print(random.choice(["This place is liveable but it is just like a grade c motel", "Hey i can see the blue sky now but the water kind of stinls."]))
    elif Player1Inventory[5] >= 600 and Player1Inventory[5] <= 799:
        print(random.choice(['your almost there',"Good job"]))
    elif Player1Inventory[5] >= 800 and Player1Inventory[5] <= 999: 
        print(random.choice(['I am starting to like this place.', "how long can i stay here because it's kind of cool"]))
    else:
        print(random.choice(['This place is like heaven',
        'Hey is gordon ramsay cooking cause the food is awesome']))
 else:
        if Player2Inventory[5] <= 99:
            print (random.choice(["This place is just like a barren wasteland and the water is like pee”,“ hey get your game together this place is burning”,“ Is the player AFK?"]))
        elif (Player2Inventory[5] >= 100 and Player2Inventory[5] <= 399):
            print(random.choice(["How are we not dead yet?","This is like living in a blank apartment"]))
        elif Player2Inventory[5] >= 400 and Player2Inventory[5] <= 599:
            print(random.choice(["This place is liveable but it is just like a grade c motel", "Hey i can see the blue sky now but the water kind of stinls."]))
        elif Player2Inventory[5] >= 600 and Player2Inventory[5] <= 799:
            print(random.choice(['your almost there',"Good job"]))
        elif Player2Inventory[5] >= 800 and Player2Inventory[5] <= 999: 
            print(random.choice(['I am starting to like this place.', "how long can i stay here because it's kind of cool"]))
        else:
            print(random.choice(['This place is like heaven',
            'Hey is gordon ramsay cooking cause the food is awesome']))

def ConvertInventoryToText(InventoryID):
  '''Converts Inventory ID to string'''
  
  if InventoryID == 0:
    return "People"
  elif InventoryID == 1:
    return "Food"
  elif InventoryID == 2:
    return "Water"
  elif InventoryID == 3:
    return "Sick"
  elif InventoryID == 4:
    return "Stability"
  elif InventoryID == 5:
    return "Opinion"
  elif InventoryID == 6:
    return "Cenal"
  elif InventoryID == 7:
    return "Wood"
  elif InventoryID == 8:
    return "Stone"
  elif InventoryID == 9:
    return "House"
  elif InventoryID == 10:
    return "Town Hall"
  elif InventoryID == 11:
    return "Wall"
  elif InventoryID == 12:
    return "Lumber Mill"
  elif InventoryID == 13:
    return "Farm"
  elif InventoryID == 14:
    return "Water Mill"
  elif InventoryID == 15:
    return "Quarry"
  elif InventoryID == 16:
    return "Hospital"


def InventoryChanges(TextID, InventoryID, Value="N1"):
  '''Displays any changes from player's actions'''

  InventoryText = ConvertInventoryToText(InventoryID)

  if TextID == 0:
    return "Because of your recent action, your {} has raised by {}!".format(InventoryText, Value)
  elif TextID == 1:
    return "Because of your recent action, your {} has decreased by {}...".format(InventoryText, Value)
  elif TextID == 2:
    return "You've build a {}!".format(InventoryText)

def TextClock():
  '''Returns a string from local time.'''

  timeClock = time.localtime()
  currentTime = str("[" + time.strftime("%H:%M", timeClock) + "] - ")
  return currentTime

def CheckCommand(stringCommand, Player, Player1Inventory, Player2Inventory):
  '''Checks player's input for any matched commands (strings).'''

  stringCommand = str.upper(stringCommand)

  if stringCommand == "-HELP":
    HelpPlease()
  elif stringCommand == "-EXIT":
    sys.exit()
  elif stringCommand == "-INVENTORY":
    Inventory(Player, Player1Inventory, Player2Inventory)
  elif stringCommand == "-END":
    Player = Players(Player, 1)
  elif stringCommand == "-BUILD":
    BuildingOptions()
  elif stringCommand == "-ABOUT":
    TitleScreen()
  elif stringCommand == "-BUILD HOUSE":
    Building(Player, Player1Inventory, Player2Inventory, 1)
    Player = Players(Player, 1)

  elif stringCommand == "-BUILD TOWN HALL" or stringCommand == "-BUILD TOWNHALL":
    Building(Player, Player1Inventory, Player2Inventory, 2)
    Player = Players(Player, 1)

  elif stringCommand == "-BUILD WALL":
    Building(Player, Player1Inventory, Player2Inventory, 3)
    Player = Players(Player, 1)

  elif stringCommand == "-BUILD LUMBER MILL" or stringCommand == "-BUILD LUMBERMILL":
    Building(Player, Player1Inventory, Player2Inventory, 4)
    Player = Players(Player, 1)

  elif stringCommand == "-BUILD FARM":
    Building(Player, Player1Inventory, Player2Inventory, 5)
    Player = Players(Player, 1)

  elif stringCommand == "-BUILD WATER MILL" or stringCommand == "-BUILD WATERMILL":
    Building(Player, Player1Inventory, Player2Inventory, 6)
    Player = Players(Player, 1)

  elif stringCommand == "-BUILD QUARRY":
    Building(Player, Player1Inventory, Player2Inventory, 7)
    Player = Players(Player, 1)

  elif stringCommand == "-BUILD HOSPITAL":
    Building(Player, Player1Inventory, Player2Inventory, 8)
    
    Player = Players(Player, 1)

  elif stringCommand == "-OPINION":
    opi(Player1Inventory, Player2Inventory, Player)
  else:
    print(TextClock() + Players(Player, 0) + ErrorSpecifier(0))
  
  print()

  EndTurn(Player, Player1Inventory, Player2Inventory, prob)
  DoubleCheck(Player, Player1Inventory, Player2Inventory)
  end(Player, Player1Inventory)
  end(Player, Player2Inventory)
  WriteCommand(Player, Player1Inventory, Player2Inventory)
 
def end(Player, PlayerInventory):
  if PlayerInventory[9] >= 100 and PlayerInventory[14] >= 45 and PlayerInventory[13] >= 45 and PlayerInventory[15] >= 10 and PlayerInventory[16] >= 10 and PlayerInventory[5] >= 100 and PlayerInventory[4] >=85 :

    print("You've successfully created a great village. It will continue to run for years to come. Thank you for your contribution!")

    if Player == 1:
      print("Player 1 wins!")
    else:
      print("Player 2 wins!")

    sys.exit()

def WriteCommand(Player, Player1, Player2Inventory):
  '''Allows for player input.'''

  print(TextClock() + Players(Player, 0) + "Write a command below: ")
  inputText = input()
  print()
  CheckCommand(inputText, Player, Player1, Player2Inventory)

def HelpPlease():
  '''Displays sets of commands to execute.'''

  print("Available commands: ")
  print("-help")
  print("-opinion")
  print("-inventory")
  print("-build")
  print("-about")
  print("-end")
  print("-exit")

def DoubleCheck(Player, Player1Inventory, Player2Inventory):
    if Player == 1:
        for i in range(0, 17):
            if Player1Inventory[i] < 0:
                Player1Inventory[i] = 0

        if Player1Inventory[4] == 0 and Player1Inventory[5] == 0:
            print("Because of Player 1's stability and opinion is rockbottom, the people have revolted and liberated from Player 1's rule.")
            print("Player 2 wins!")
            sys.exit()
    else:
        for i in range(0, 17):
            if Player2Inventory[i] < 0:
                Player2Inventory[i] = 0

        if Player2Inventory[4] == 0 and Player2Inventory[5] == 0:
            print("Because of Player 2's stability and opinion is rockbottom, the people have revolted and liberated from Player 2's rule.")
            print("Player 1 wins!")
            sys.exit()

def Sickness(Player, Player1Inventory, Player2Inventory, prob):
    if Player == 1:
        if Player1Inventory[3] > 0:
            Player1Inventory[3] *= 2

            if Player1Inventory[3] > Player1Inventory[0]:
                Player1Inventory[3] = Player1Inventory[0]
        else:
          if prob(30):
            Player1Inventory[3] = random.randint(1, Player1Inventory[0])
            print("Somebody got sick!")
    else:
        if Player2Inventory[3] > 0:
            Player2Inventory[3] *= 2

            if Player2Inventory[3] > Player2Inventory[0]:
                Player2Inventory[3] = Player2Inventory[0]
        else:
          if prob(30):
            Player2Inventory[3] = random.randint(1, Player2Inventory[0])
            print("Somebody got sick!")

def EndTurn(Player, Player1Inventory, Player2Inventory, prob):
  if Player == 1:

    # Production Result
    Player1Inventory[1] = Player1Inventory[13] * 2 + Player1Inventory[1]
    Player1Inventory[2] = Player1Inventory[14] * 2 + Player1Inventory[2]
    Player1Inventory[7] = Player1Inventory[12] * 3 + Player1Inventory[7]
    Player1Inventory[6] = Player1Inventory[0] * 10 + Player1Inventory[6]
    
    # Consumption
    Player1Inventory[1] -= Player1Inventory[0] * 2
    Player1Inventory[2] -= Player1Inventory[0] * 2

    # Hospital Function
    if Player1Inventory[3] > 0:
      Player1Inventory[3] -= Player1Inventory[16] * 5

    if Player1Inventory[1] <= 0:
      Player1Inventory[1] = 0
      print("Not enough food!")
      InventoryChanges(1, 4, 3)
      Player1Inventory[4] -= 3
      Sickness(Player, Player1Inventory, Player2Inventory, prob)

    if Player1Inventory[2] <= 0:
      Player1Inventory[2] = 0
      print("Not enough water!")
      InventoryChanges(1, 5, 3)
      Player1Inventory[5] -= 3

  else:
      # Production Result
      Player2Inventory[1] = Player2Inventory[13] * 2 + Player2Inventory[1]
      Player2Inventory[2] = Player2Inventory[14] * 2 + Player2Inventory[2]
      Player2Inventory[7] = Player2Inventory[12] * 3 + Player2Inventory[7]
      
      # Consumption
      Player2Inventory[1] -= Player2Inventory[0] * 2
      Player2Inventory[2] -= Player2Inventory[0] * 2

      # Hospital Function
      if Player2Inventory[3] > 0:
        Player2Inventory[3] -= Player2Inventory[16] * 5

      if Player2Inventory[1] <= 0:
        Player2Inventory[1] = 0
        print("Not enough food!")
        InventoryChanges(1, 4, 3)
        Player2Inventory[4] -= 3
        Sickness(Player, Player1Inventory, Player2Inventory, prob)
      
      if Player2Inventory[2] <= 0:
        Player2Inventory[2] = 0
        print("Not enough water!")
        InventoryChanges(1, 5, 3)
        Player2Inventory[5] -= 3


def InventoryDisplay(PlayerInventory):
  print("  Population -")
  print("       People: " + str(PlayerInventory[0]))
  print()
  print(" Basic Needs -")
  print("         Food: " + str(PlayerInventory[1]) + " [{} consumption] [{} being produced]".format(PlayerInventory[0] * 2, PlayerInventory[13] * 2))
  print("        Water: " + str(PlayerInventory[2]) + " [{} consumption] [{} being produced]".format(PlayerInventory[0] * 2, PlayerInventory[14] * 2))
  print()
  print("       Health:")
  print("         Sick: " + str(PlayerInventory[3]))
  print()
  print("    Relations:")
  print("    Stability: " + str(PlayerInventory[4]))
  print("      Opinion: " + str(PlayerInventory[5]))
  print()
  print("   Resources -")
  print("        Money: " + str(PlayerInventory[6]))
  print("         Wood: " + str(PlayerInventory[7]) + " [{} being produced]".format(PlayerInventory[12] * 3))
  print("        Stone: " + str(PlayerInventory[8]) + " [{} being produced]".format(PlayerInventory[15]))
  print()
  print("  Settlement -")
  print("        House: " + str(PlayerInventory[9]))
  print("    Town Hall: " + str(PlayerInventory[10]))
  print("         Wall: " + str(PlayerInventory[11]))
  print("  Lumber Mill: " + str(PlayerInventory[12]))
  print("         Farm: " + str(PlayerInventory[13]))
  print("   Water Mill: " + str(PlayerInventory[14]))
  print("       Quarry: " + str(PlayerInventory[15]))
  print("     Hospital: " + str(PlayerInventory[16]) + " [Can handle {} patients]".format(PlayerInventory[15]))

def Inventory(Player, Player1, Player2Inventory):
  '''Displays player's inventory.'''

  if Player == 1:
    print("Player 1 -")
    InventoryDisplay(Player1)
  else:
    print("Player 2 -")
    InventoryDisplay(Player2Inventory)

def BuildingOptions():
  '''Displays building options.'''
  ### Function may need an expandsion ###

  print("Building Options - ")
  print("      House: [ 2 Wood, 5 Money]          (+  4 People)")
  print("  Town Hall: [10 Wood, 25 Money]          (+ 40 Stability)")
  print("       Wall: [20 Wood, 15 Money]          (+ 10 Stability)")
  print("Lumber Mill: [10 Wood, 15 Money]          (+  3 Wood)")
  print("       Farm: [ 3 Wood, 10 Money]          (+  2 Food")
  print(" Water Mill: [ 4 Wood, 10 Money]          (+  2 Water)")
  print("     Quarry: [ 8 Wood, 30 Money]          (+  1 Stone)")
  print("   Hospital: [10 Stone, 5 Wood, 40 Money]   (+ 10 Sick Handling) ")
  print ("To build, type '-build [building name]'")

def ResourceCheck(Player, Player1, Player2Inventory, ResourceValue, ItemID, CheckID = 0):
  '''Checks if specified value is available'''

  if CheckID == 0:
      if Player == 1:
        if Player1[ItemID] >= ResourceValue:
          return True
        else:
          print(ErrorSpecifier(1))
          return False
      else:
        if Player2Inventory[ItemID] >= ResourceValue:
          return True
        else:
          print(ErrorSpecifier(1))
          return False
  else:
    if Player == 1:
        if Player1[ItemID] < ResourceValue:
          return True
        else:
          print(ErrorSpecifier(2))
          return False
    else:
        if Player2Inventory[ItemID] < ResourceValue:
          return True
        else:
          print(ErrorSpecifier(2))
          return False

def ResourceModifier(Player, Player1, Player2Inventory, ResourceValue, ItemID, ItemResultID = 17):
  if Player == 1:
    Player1[ItemID] -= ResourceValue
    Player1[ItemResultID] += 1
  else:
    Player2Inventory[ItemID] -= ResourceValue
    Player2Inventory[ItemResultID] += 1

def ResourceAddition(Player, Player1, Player2Inventory, ItemID, ResourceValue):
  if Player == 1:
    Player1[ItemID] += ResourceValue
  else:
    Player2Inventory[ItemID] += ResourceValue

def ErrorSpecifier(ErrorID):
  '''Sets of custom error specifier.'''
  if ErrorID == 0:
    return "|Error 0| - Unknown command. Type '-help' for sets of commands."
  elif ErrorID == 1:
    return "|Error 1| - You don't have enough materials"
  elif ErrorID == 2:
    return "|Error 2| - Building's capacity has reached."

def Building(Player, Player1, Player2Inventory, BuildingID):
  if BuildingID == 1: # House
    if ResourceCheck(Player, Player1, Player2Inventory, 2, 7):
      ResourceModifier(Player, Player1, Player2Inventory, 2, 7, 9) 
      ResourceAddition(Player, Player1, Player2Inventory, 0, 4)         
      print(InventoryChanges(2, 9))

  elif BuildingID == 2: # Town Hall
    if ResourceCheck(Player, Player1, Player2Inventory, 1, 10, 1): 
        if ResourceCheck(Player, Player1, Player2Inventory, 10, 7):
          ResourceModifier(Player, Player1, Player2Inventory, 10, 7, 10)
          ResourceAddition(Player, Player1, Player2Inventory, 4, 40) 
          print(InventoryChanges(2, 10))

  elif BuildingID == 3: # Wall
    if ResourceCheck(Player, Player1, Player2Inventory, 4, 11, 1):
        if ResourceCheck(Player, Player1, Player2Inventory, 20, 7):
          ResourceModifier(Player, Player1, Player2Inventory, 20, 7, 11)
          ResourceAddition(Player, Player1, Player2Inventory, 4, 10)
          print(InventoryChanges(2, 11))

  elif BuildingID == 4: # Lumber Mill
    if ResourceCheck(Player, Player1, Player2Inventory, 10, 7):
      ResourceModifier(Player, Player1, Player2Inventory, 10, 7, 12)
      print(InventoryChanges(2, 12))

  elif BuildingID == 5: # Farm
    if ResourceCheck(Player, Player1, Player2Inventory, 3, 7):
      ResourceModifier(Player, Player1, Player2Inventory, 3, 7, 13)
      print(InventoryChanges(2, 13))

  elif BuildingID == 6: # Water Mill
    if ResourceCheck(Player, Player1, Player2Inventory, 4, 7):
      ResourceModifier(Player, Player1, Player2Inventory, 4, 7, 14)
      print(InventoryChanges(2, 14))

  elif BuildingID == 7: # Quarry
    if ResourceCheck(Player, Player1, Player2Inventory, 7, 8):
        ResourceModifier(Player, Player1, Player2Inventory, 7, 8, 15)
        print(InventoryChanges(2, 15))

  elif BuildingID == 8: # Hospital
    if ResourceCheck(Player, Player1, Player2Inventory, 10, 7):
      if ResourceCheck(Player, Player1, Player2Inventory, 5, 6):
        ResourceModifier(Player, Player1, Player2Inventory, 5, 7, 16)
        print(InventoryChanges(2, 16))

def WriteChoiceCommands():
    print()
    print("Make your choice wisely below: ")
    choiceInput = input()
    choiceInput = str.upper(choiceInput)
    return choiceInput


def Events(PlayerInventory, Player1Inventory, Player2Inventory, Player, prob):
    '''List of events.'''

    if (PlayerInventory[13] > 2 and prob(10)): # Not enough food
        print("You have found that many of the lumberjacks aren’t getting food due to farms throwing away bruised fruits")
        print("Choice 1: don't care {-40 stability and opinion.}")
        print('Choice 2: create another farm. {+20 stability and opinion}')
        print('Choice 3: make jams and juices out of fruits {boost opinion by 6}')

        while True:
            input = WriteChoiceCommands()

            if input == "CHOICE 1" or input == "-CHOICE 1" or input == "1":
                print(InventoryChanges(1, 4, 40))
                print(InventoryChanges(1, 5, 40))
                PlayerInventory[4] -= 40
                PlayerInventory[5] -= 40
                break
            elif input == "CHOICE 2" or input == "-CHOICE 2" or input == "2":
                comparison = PlayerInventory[13]

                Building(Player, Player1Inventory, Player2Inventory, 16)

                if PlayerInventory[13] != comparison:
                    print(InventoryChanges(0, 4, 20))
                    print(InventoryChanges(0, 5, 20))
                    PlayerInventory[4] += 20
                    PlayerInventory[5] += 20
                else:
                    print(InventoryChanges(1, 4, 20))
                    print(InventoryChanges(1, 5, 20))
                    PlayerInventory[4] -= 20
                    PlayerInventory[5] -= 20
                break
            elif input == "CHOICE 3" or input == "-CHOICE 3" or input == "3":
                print(InventoryChanges(0, 5, 6))
                PlayerInventory[5] += 6
                break
            else:
                ErrorErrorSpecifier(3)

    elif (PlayerInventory[15] > 1 and prob(15)): # Sickness
        print("Sudden rise of sickness are causing people to cry out from the unaffordable healthcare.")
        print('Choice 1: don’t care {Sick is doubled}') 
        print('Choice 2: build hospital {Stability increases by 10}')

        while True:
            input = WriteChoiceCommands()

            if input == "CHOICE 1" or input == "-CHOICE 1" or input == "1":
                print(InventoryChanges(3, 3, PlayerInventory[3] * 2))
                PlayerInventory[3] *= 2
                break
            elif input == "CHOICE 2" or input == "-CHOICE 2" or input == "2":
                comparison = PlayerInventory[16]

                Building(Player, Player1Inventory, Player2Inventory, 16)

                if PlayerInventory[16] != comparison:
                    print(InventoryChanges(0, 4, 10))
                    PlayerInventory[4] += 10
                else:
                    print(InventoryChanges(3, 3, PlayerInventory[3] * 2))
                    PlayerInventory[3] *= 2
                break
            else:
                ErrorErrorSpecifier(3)

    elif (PlayerInventory[12] > 5 and prob(20)): # Lumberjack overload [Water pollution]
        print("Due to many lumber mills, water had become polluted")
        print("Choice 1: don’t care {stability and reputation decreases to 6}")
        print("Choice 2: cut off all production {production of wood stops.}")
        print("Choice 3: cut off half of production {cut off 50% off wood production improve 3 stability and reputation}")

        while True:
            input = WriteChoiceCommands()

            if input == "CHOICE 1" or input == "-CHOICE 1" or input == "1":
                print(InventoryChanges(1, 4, 6))
                print(InventoryChanges(1, 5, 6))
                PlayerInventory[4] -= 6
                PlayerInventory[5] -= 6
                break
            elif input == "CHOICE 2" or input == "-CHOICE 2" or input == "2":
                print(InventoryChanges(1, 12, PlayerInventory[12]))
                PlayerInventory[12] = 0
                break
            elif input == "CHOICE 3" or input == "-CHOICE 3" or input == "3":
                print(InventoryChanges(1, 12, int(PlayerInventory[12] / 2)))
                PlayerInventory[4] += 3
                PlayerInventory[5] += 3
                PlayerInventory[12] = int(PlayerInventory[12] / 2)
                break
            else:
                ErrorErrorSpecifier(3)
