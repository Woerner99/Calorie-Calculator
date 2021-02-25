#====================================================================
# Profile.py
# author: Sean-Michael Woerner

# contains all profile related functions: creating, deleting, etc.
#====================================================================

#====================================================================
#Imports:
#====================================================================
import os
import BMR


#====================================================================
# Subroutines
#====================================================================
# Boolean function to determine whether or not to save the profile of user
# 1 means save, else do nothing
def doWeSave(bmr):
	save = int(input("Would you like to save this entry?\n(1) YES\n(2) NO\n"))
	if (save == 1):
		name = input("Enter your name: ")
		saveProfile(name, bmr)
		print("Profile has been saved in profiles.txt as user: " + name)

# Save portfolio of to text file, writes person's name and BMR
def saveProfile(name, bmr):
	f = open("profiles.txt","a")
	f.write(name+" "+str(bmr)+"\n")
	f.close()
# Erases profiles.txt if it exists in the project folder
def eraseProfiles():
	if os.path.exists("profiles.txt"):
		os.remove("profiles.txt")
	else:
		print("There are no profiles saved...")
		back = input("Press ENTER to return...\n")