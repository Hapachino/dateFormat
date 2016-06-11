#! python3
# dateFormat: Finds all file names in a folder, revises American-style dates to European-style dates

import os, re, shutil

# Create a regex that can identify the text pattern of American-style dates.

dateRegex = re.compile(r'''
			(0[1-9]|1[0-2])                  # Month 
			-
			(10|20|[0-2][1-9]|3[01])         # Day - instead of [0-2][0-9]|3[01] to avoid 00 as a match
			-
			((198[0-9]|20(0[0-9]|1[0-6])'''  # Year - matches 1980 - 2016
			, re.VERBOSE)


# Call os.listdir() to find all the files in the working directory.

os.listdir(os.getcwd())


# Loop over each filename, using the regex to check whether it has a date.

# If it has a date, rename the file with shutil.move().

