example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. You are free to choose and design any 
#   data structure you would like to use to manage the information.
# 
# Arguments: 
#   string_input: block of text containing the network information
#
#   You may assume that for all the test cases we will use, you will be given the 
#   connections and games liked for all users listed on the right-hand side of an
#   'is connected to' statement. For example, we will not use the string 
#   "A is connected to B.A likes to play X, Y, Z.C is connected to A.C likes to play X."
#   as a test case for create_data_structure because the string does not 
#   list B's connections or liked games.
#   
#   The procedure should be able to handle an empty string (the string '') as input, in
#   which case it should return a network with no users.
# 
# Return:
#   The newly created network data structure

# name=''
# network = {}
# network[name] = [[],[]]

def filter(string_input):
	comma = 0
	values = []
	s = string_input
	while ',' in s:
		comma = s.find(',')
		values.append(s[:comma])
		s = s[comma + 2:]
	if len(s) > 0:
		values.append(s)
	return values


def create_data_structure(string_input):
	network = {}
	s = string_input
	while '.' in s:
		name = ''
		connections, games = '', ''
		phrases = s[:s.find('.')]
		name = phrases[0:phrases.find(' ')]
		if 'connect' in phrases:
			if name not in network:
				network[name] = [[],[]]
			connections = filter(phrases[phrases.find('connected to')+13:])
			network[name][0] = connections
		if 'play' in phrases:
			if name not in network:
				network[name] = [[],[]]
			games = filter(phrases[phrases.find('play')+5:])
			network[name][1] = games
		s = s[s.find('.')+1:]
	return network

# ----------------------------------------------------------------------------- #
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        #
# ----------------------------------------------------------------------------- #

# -----------------------------------------------------------------------------
# get_connections(network, user):
#   Returns a list of all the connections that user has
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return:
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.

def get_connections(network, user):
	if user in network:
		return network[user][0]
	return None


# -----------------------------------------------------------------------------
# get_games_liked(network, user):
#   Returns a list of all the games a user likes
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return:
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.
def get_games_liked(network, user):
	if user in network:
		return network[user][1]
	return None


# -----------------------------------------------------------------------------
# add_connection(network, user_A, user_B):
#   Adds a connection from user_A to user_B. Make sure to check that both users
#   exist in network.
#
# Arguments:
#   network: the gamer network data structure
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return:
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.

# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: the gamer network data structure 
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return: 
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.
def add_connection(network, user_A, user_B):
	if user_B and user_A in network:
		if user_B in network[user_A][0]:
			return	network
		else: 
			return[user_A].append(user_B)
			return network
	else:
		return network


# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. The new user 
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's game preferences)
def add_new_user(network, user, games):
    if user not in network: 
    	network[user] = [[],[]]
    	network[user][1] = games
    else:
    	return "network *UNCHANGED*"
    return network
		

# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections (i.e. connections of connections) of a 
#   given user.
# 
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.
def get_secondary_connections(network, user):
	if user in network:
		primary = network[user][0]
		secondary = []
		for i in primary:
			if i in network:
				for s in network[i][0]:
					if s not in secondary:
						secondary.append(s)
		return secondary
	return None



# ----------------------------------------------------------------------------- 	
# count_common_connections(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return: 
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.
def count_common_connections(network, user_A, user_B):
    count = 0
    if user_A and user_B in network:
    	for i in network[user_A][0]:
    		for s in network[user_B][0]:
    			if i == s: 
    				count += 1
    	return count
    return False



# ----------------------------------------------------------------------------- 
# find_path_to_friend(network, user_A, user_B): 
#   Finds a connections path from user_A to user_B. It has to be an existing 
#   path but it DOES NOT have to be the shortest path.
#   
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#
# Sample output:
#   >>> print find_path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.
# 
# NOTE:
#   You must solve this problem using recursion!
# 
# Hints: 
# - Be careful how you handle connection loops, for example, A is connected to B. 
#   B is connected to C. C is connected to B. Make sure your code terminates in 
#   that case.
# - If you are comfortable with default parameters, you might consider using one 
#   in this procedure to keep track of nodes already visited in your search. You 
#   may safely add default parameters since all calls used in the grading script 
#   will only include the arguments network, user_A, and user_B.
# def find_path_to_friend(network, user_A, user_B):
# 	checked = []
	
# 	if user_B in checked:
# 		return checked
# 	else:
# 		depth = 7
# 		while depth != 0:
# 			connections = get_connections(network, user_A)
# 			for connection in connections:
# 				if connection not in checked:
# 					checked.append(connection)
# 					find_path_to_friend(network, connection, user_B)

# 			depth = depth - 1


	









# if user_A connection in user_B connection = True

def find_path_to_friend(network, user_A, user_B):
	explored = []
	queue = [user_A]
	while queue:
		if user_B in explored:
			return explored
		else:
			node = queue.pop(0)
			if node not in explored:
				explored.append(node)
				neighbours = network[node][0]
				for neighbour in neighbours:
					queue.append(neighbour)
	return explored

	
	# your RECURSIVE solution here!

# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
# Your MYOP should either perform some manipulation of your network data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.

# Replace this with your own procedure! You can also uncomment the lines below
# to see how your code behaves. Have fun!

def get_stats(network):
	users = 0
	connections = 0
	games = 0
	users = users + len(network)
	for i in network:
		temp = []
		# games = games + (sum(network[i][1])/len(network[i][1]))
		# connections = connections + (sum(temp)/len(temp))

	print('Your social network Data:')
	print('Users = {}' '\n' 'Connections = {}' '\n' 'Games = {}'.format(users, connections, games))


net = create_data_structure(example_input)
print(net)
print(get_connections(net, "Debra"))
print(get_connections(net, "Mercedes"))
print(get_games_liked(net, "John"))
print(add_connection(net, "John", "Freda"))
print(add_new_user(net, "Debra", []) )
print(add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]))
print(get_secondary_connections(net, "Mercedes"))
print(count_common_connections(net, "Mercedes", "John"))
print(find_path_to_friend(net, "John", "Ollie"))
print(get_stats(net))