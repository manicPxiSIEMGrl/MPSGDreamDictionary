#!/usr/bin/env python

# Name Dictionary Creator - Creates a dictionary from provided first and last names.
#
# Description:
#   Creates a text file of names from provided lists of 
#   first and last names for checking against email or user
#   accounts.
#
# Author:
#   Jessa (@manicPxiSIEMGirl)
#
#	Version 1.0
#	Updated: 3/26/24
#
###########################################################

###########################################################
#
# To Do:
#  1)
#
###########################################################

import codecs
import sys
import argparse

class create:
	def __init__(self, inputFirst, inputLast, delimiter, outputFile):
		self.__inputFirst = inputFirst
		self.__inputLast = inputLast
		self.__delimiter = delimiter
		self.__outputFile = outputFile

	def create(self):
		try:
			fName = open(self.__inputFirst,"r")
			fName.close()
		except:
			print("First name input file not found. Please ensure the file is a valid .txt file stored in ",self.__inputFirst)
			sys.exit(1)
		try:
			lName = open(self.__inputLast,"r")
			lName.close()
		except:
			print("Last name input file not found. Please ensure the file is a valid .txt file stored in ",self.__inputLast)
			sys.exit(1)

		try:
			#create
			if self.__delimiter is None:
				fName = open(self.__inputFirst,"r")
				for i in fName.readlines():
					print(str(i))
					lName = open(self.__inputLast,"r")
					for j in lName.readlines():
						outputSTR = str(i).strip()+str(j).strip()+"\n"
						o = open(self.__outputFile,"a")
						o.write(outputSTR)
						o.close()
					lName.close()
				fName.close()

			else:
				fName = open(self.__inputFirst,"r")
				for i in fName.readlines():
					print(str(i))
					lName = open(self.__inputLast,"r")
					for j in lName.readlines():
						outputSTR = str(i).strip()+str(self.__delimiter).strip()+str(j).strip()+"\n"
						o = open(self.__outputFile,"a")
						o.write(outputSTR)
						o.close()
					lName.close()
				fName.close()
		except:
			print("Failed to create output files")
			sys.exit(1)

# Process command-line arguments.
if __name__ == '__main__':
	# Explicitly changing the stdout encoding format
	if sys.stdout.encoding is None:
		# Output is redirected to a file
		sys.stdout = codecs.getwriter('utf8')(sys.stdout)
	argParser = argparse.ArgumentParser(add_help = True, description = "Creates a dictionary from two .txt files.")
	argParser.add_argument('-inputFirst', action='store', help='first input file (ex: first names)')
	argParser.add_argument('-inputLast', action='store', help='last input file (ex: last names)')
	argParser.add_argument('-delimiter', choices=['','.'], help='delimiter added between the first and last dictionaries. Exclude this option for none.')
	argParser.add_argument('-outputFile', action='store' , help='output file')

	#Error check empty expected items
	if len(sys.argv)==1:
		argParser.print_help()
		sys.exit(1)
	options = argParser.parse_args()
	if options.inputFirst is None or options.inputLast is None:
		print("Both input files must be specified. This file should be a .txt file.")
		sys.exit(1)
	if options.outputFile is None:
		print("An output file must be specified. This file should be a .txt file.")
		sys.exit(1)

	#Append and handle file extensions and directory traversal
	if not(str(options.outputFile).endswith(".txt")):
		options.outputFile = options.outputFile + ".txt"
	
    #Create
	createDictionary = create(options.inputFirst,options.inputLast,options.delimiter,options.outputFile)
	try:
		createDictionary.create()
	except:
		print("Creation of the dictionary failed. This is due to a series of deeper failures. Maybe brush some salt into it?")
		sys.exit(1)
