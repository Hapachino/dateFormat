#! python3
# dateFormat: Finds all file names in current working directory, revises American-style dates (MM-DD-YYYY) to European-style (DD-MM-YYYY)

import os, re, shutil

# Create a regex that can identify the text pattern of American-style dates.

dateRegex = re.compile(r'''(\d{2})	# Month
			   -
			   (\d{2})	# Day
			   -
			   (\d{4})'''	# Year
			   , re.VERBOSE)

# Loop over each filename in current working directory, using the regex to check whether it has a American date 
# and rename with Shutil.move():

for filename in os.listdir(os.getcwd()):
	if dateRegex.search(filename) != None:
		shutil.move(filename, dateRegex.sub('\2-\1-\3', filename))
		


