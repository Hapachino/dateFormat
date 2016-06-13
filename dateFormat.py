#! python3
# dateFormat: Finds all file names in cwd, revises American-style dates (MM-DD-YYYY) to European-style (DD-MM-YYYY)

import os, re, shutil

# regex that can identify the text pattern of American-style dates.

dateRegex = re.compile(r'''
			^(.*?)?		# Text Before
			((0|1)\d)	# Month
			-		
			((0|1|2|3)\d)	# Day
			-
			((19|20)\d\d)	# Year
			(.*?)?$		# Text After
			''', re.VERBOSE)

''' 
Numeric representation of the mo.groups:

			^(1)?		# Text Before
			(2(3))		# Month
			-		
			(4(5))		# Day
			-
			(6(7))		# Year
			(8)?$		# Text After
'''

# Loop over each filename in current working directory, using the regex to check whether it has an American date 

for filename in os.listdir('.'):
	mo = dateRegex.search(filename)
	if mo == None
		continue

# if match found, create variales of the mo.groups:

	textBefore = mo.group(1)
	month = mo.group(2)
	day = mo.group(4)
	year = mo.group(6)
	textAfter = mo.group(8)
	
# create European style filename using mo.group variables
	
	europeanFile = textBefore + month + '-' + day + '-' + year + textAfter

# find the American and Euroepan absolute filepaths and rename with shutil.move(): comment out and use print first!

	cwd = os.path.abspath('.')
	europeanPath = os.path.join(cwd, europeanFile)
	americanPath = os.path.join(cdw, filename)
	# shutil.move(americanPath, europeanPath) 	# uncomment after testing
	print('Renaming "%s" to "%s"...' % (americanPath, europeanPath))
	




