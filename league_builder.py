import csv

if __name__ == '__main__':

	# List where players will be stored
	players_list = []
	
	# Team List
	Sharks = []
	Raptors = []
	Dragons = []

	# Gives me a list with the players from the CSV File
	def create_player_list():
	 	
	 	players_list = []

	 	# Reads CSV Files and create a List with Players
		with open("soccer_players.csv", "rb") as csvfile:
			players_file = csv.DictReader(csvfile)
			for player in players_file:
				players_list.append(player)

		return players_list

	# Function to get experienced players
	def get_players(players_list, exp = "YES"):

		players = []

		# Returns Experienced Players
		for player in players_list:
			if player["Soccer Experience"] == exp:
				players.append(player)

		# Sorts out the Experienced players list
		players.sort()

		return players

	def assign_players(players):
		# Assigns the experienced players to player lists
		count = 0
		for player in players:
			if count < 3:
				Sharks.append(player)
			elif count < 6:
				Raptors.append(player)
			else:
				Dragons.append(player)
			count += 1

	def create_teams_file():
		# Opens teams.txt file 
		teams_file = open("teams.txt", "a")

		teams_file.write("TEAMS!\n=========================================================\n \n")
		teams_file.write("Sharks\n---------------------------------------------------------\n")

		for shark in Sharks:
			teams_file.write("{}, {}, {}".format(shark["Name"], shark["Soccer Experience"], shark["Guardian Name(s)"])+"\n")

		teams_file.write("\n\nRaptors\n---------------------------------------------------------\n")

		for raptor in Raptors:
			teams_file.write("{}, {}, {}".format(raptor["Name"], raptor["Soccer Experience"], raptor["Guardian Name(s)"])+"\n")

		teams_file.write("\n\nDragons\n---------------------------------------------------------\n")

		for dragon in Dragons:
			teams_file.write("{}, {}, {}".format(dragon["Name"], dragon["Soccer Experience"], dragon["Guardian Name(s)"])+"\n")

		# Closes teams.txt file
		teams_file.close()

	def extra_credit():
		for shark in Sharks:
			file_name = shark["Name"].lower().replace(" ", "_")
			file = open(file_name+".txt", "a")
			file.write("Dear {},\n\n".format(shark["Guardian Name(s)"]))
			file.write("We are proud to announce that {} has been accepted on team Sharks, and date & time of first practice will be February 12 at 3:00pm.\nLooking forward on start practices!\n\nMy Best Regards,\nThe Coach".format(shark["Name"]))
			file.close()

		for raptor in Raptors:
			file_name = raptor["Name"].lower().replace(" ", "_")
			file = open(file_name+".txt", "a")
			file.write("Dear {},\n\n".format(raptor["Guardian Name(s)"]))
			file.write("We are proud to announce that {} has been accepted on team Raptors, and date & time of first practice will be February 12 at 3:00pm.\nLooking forward on start practices!\n\nMy Best Regards,\nThe Coach".format(raptor["Name"]))
			file.close()

		for dragon in Dragons:
			file_name = dragon["Name"].lower().replace(" ", "_")
			file = open(file_name+".txt", "a")
			file.write("Dear {},\n\n".format(dragon["Guardian Name(s)"]))
			file.write("We are proud to announce that {} has been accepted on team Dragons, and date & time of first practice will be February 12 at 3:00pm.\nLooking forward on start practices!\n\nMy Best Regards,\nThe Coach".format(dragon["Name"]))
			file.close()

	# Creates the Players List
	players_list = create_player_list()

	# Gets the players from experience variable
	experienced_players = get_players(players_list)
	rookie_players = get_players(players_list, "NO")
	
	# Assigns Players to Teams
	assign_players(experienced_players)
	assign_players(rookie_players)

	# Sorts out the teams (Let's not hurt the rookies feelings)
	Sharks.sort()
	Raptors.sort()
	Dragons.sort()

	# Creates the teams.txt file
	create_teams_file()

	# Extra Creadit
	extra_credit()



	




