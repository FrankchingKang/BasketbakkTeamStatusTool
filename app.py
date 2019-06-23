import constants
import os

def clear_screen():
  os.system("cls" if os.name == "nt" else "clear")

def conver_height(Players):
  for player in Players:
    l_height = player['height'].split()
    player['height'] = int(l_height[0])

  return Players


def conver_experience(Players):
  for player in Players:
    if player['experience'] == "YES":
      player['experience'] = True
    else:
      player['experience'] = False
  return Players


def conver_guardians(Players):  
  for player in Players:
    guardians = player['guardians'].split()
    player['guardians'] = []
    try:
      guardians.remove("and")
      # have "and"
      player['guardians'].append(" ".join(guardians[:2]))
      player['guardians'].append(" ".join(guardians[2:]))
      
    except ValueError:
      # no "and"
      player['guardians'].append(" ".join(guardians))

      
  return Players


def divide_players(Players):
  ExPlayers = []
  NoExPlayers = []
  for player in Players:
    if player['experience'] == True:
      ExPlayers.append(player)
    else:
      NoExPlayers.append(player)
      
  return ExPlayers, NoExPlayers

  
def assign_players_to_three_teams(Players):
  # divide experienced player and non experienced player
  ExPlayers, NoExPlayers = divide_players(Players)
  
  Sortedplayers = ExPlayers + NoExPlayers
  TeamOne, TeamTwo, TeamThree = [], [], [];
  
  while Sortedplayers != []:
    if len(Sortedplayers) % 3 == 0:
      TeamOne.append(Sortedplayers.pop())
    elif len(Sortedplayers) % 3 == 1:
      TeamTwo.append(Sortedplayers.pop())
    else:
      TeamThree.append(Sortedplayers.pop())
  
  return TeamOne, TeamTwo, TeamThree


def total_experienced_players(Players):
  count = 0
  for player in Players:
    if player['experience'] == True:
      count += 1
    
  return count


def total_inexperienced_players(Players):
  count = 0
  for player in Players:
    if player['experience'] == False:
      count += 1
    
  return count


def average_height(Players):
  TotalHeight = 0
  for player in Players:
    TotalHeight += player['height']

  return TotalHeight / len(Players)

def show_players_info(Players):
  print("Total players: {}".format(len(Players)))
  print("Experience Players: {}".format(total_experienced_players(Players)))
  print("Inexperience Players: {}".format(total_inexperienced_players(Players)))
  print("Average height of the team: {}".format(average_height(Players)))
  print("\nPlayers on Team:")
  PlayerName = [player['name'] for player in Players]
  print("{}".format(", ".join(PlayerName)))
  print("\nGuardians of all Players on Team:")
  GuardiansOfPlayers = [guardian for player in Players for guardian in player['guardians']]
  print(", ".join(GuardiansOfPlayers))
  

if __name__ == "__main__":
  
  # get date from constants.py
  Teams = [team for team in constants.TEAMS]
  Players = [player for player in constants.PLAYERS]
  
  # conver height of Players to int 
  Players = conver_height(Players)
  
  # conver experience to Boolean
  Players = conver_experience(Players)
  
  # conver guardians string to list and delete "and"
  Players = conver_guardians(Players)
  
  # assign player to three teams 
  league = {team: player for team, player in zip(Teams, assign_players_to_three_teams(Players))}
  
  while True:
    clear_screen()
    print("Here are your choices:")
    print("1) Display Team Stats")
    print("2) Quit")
    action = input("Enter an option > ")
    if action.upper == "QUIT" or action.lower() == "quit" or action == "2":
      break
    elif action == "1":
      print("1) Panthers")
      print("2) Bandits")
      print("3) Warriors")
      action = int(input("Enter an option > "))
      if 1 <= action and action <=3:
        clear_screen()
        TeamSelected = Teams[action-1]
        PlayersOfTeam = league[TeamSelected]
        print("\nTeam: {} status:".format(TeamSelected))
        print("-"*50)
        show_players_info(PlayersOfTeam)
        print("-"*50)
      else:
        
        continue
    else:
      clear_screen()
      print("Please enter 1 or 2 to select your action. Thanks")
      
      
    
    input("Press enter to continue > ")
    
    
