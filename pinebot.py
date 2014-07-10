import praw




def main_menu():
	# initialize
	user_agent = ("Pinebot user analyzer by /u/pinebender")
	r = praw.Reddit(user_agent=user_agent)
	thing_limit = 50
	user = None
	run_program = True
	
	while run_program == True:
		print("""
Reddit User Analyzer
1. Enter User
2. Retrieve Karma Information
3. Search User Comments for Keywords
4. Exit
			""")
		prompt = raw_input("> ")

		if prompt == "1":
			user = set_user(r)
			print("\n")

		elif prompt == "2":
			# check for user
			if user == None:
				print ("Invalid user or user not set. Please set a valid user.")
				print("\n")
			else:
				get_karma(user, r, thing_limit)
				print("\n")

		elif prompt == "3":
			if user == None:
				print("Invalid user or user not set. Please set a valid user.")
				print("\n")
			else:
				get_keywords(user, r, thing_limit)
				print("\n")

		elif prompt == "4":
			run_program = False
			print("\n")

		else:
			print("Please enter a valid option (1-4).")
			print("\n")



def set_user(r):
	user_name = raw_input("Reddit user to be analyzed: ")
	try:
		user = r.get_redditor(user_name)
	except:
		user = None

	return user
	#return r.get_redditor(user_name)
	
def get_karma(user, r, thing_limit):
	

	# link karma (turn these into a function)
	print("Link karma: " + str(user.link_karma))

	# comment karma
	print("Comment karma: " + str(user.comment_karma))

	# get karma by subreddit (turn this into a function)
	gen = user.get_submitted(limit = thing_limit)

	karma_by_subreddit = {}
	for thing in gen:
		subreddit = thing.subreddit.display_name
		karma_by_subreddit[subreddit] = (karma_by_subreddit.get(subreddit, 0) + thing.score)

	for key in karma_by_subreddit:
		print(str(key) + ": " + str(karma_by_subreddit[key]))

# analyze for a word (turn this into a function)

def get_keywords(user, r, thing_limit):
	search_term = raw_input("Please enter a search string: \n")
	comments_gen = user.get_comments(limit=thing_limit)
	tally = 0
	for comment in comments_gen:	
		if str(search_term) in comment.body:
			print("Word mentioned in /r/" + str(comment.subreddit.display_name) + ": ")
			print(comment.body)
			print("\n")
			tally += 1

	print("Search string mentioned: " + str(tally) + " times.")

main_menu()