# MPSGDreamDictionary

I created this simple script with the intention of concatenating two dictionaries together all inclusively, such as adding a dictionary of first names to a dictionary of last names to create a dictionary of full names.

Creates a dictionary from two .txt files.
- inputFirst - first input file (ex: first names)
- inputLast - last input file (ex: last names)
- delimiter - delimiter added between the first and last dictionaries (Currently Supports . or exclude this option for none)
- outputFile - output file

Example:
- Create fullname dictionary with periods between first and last name
    
        MPSGDreamDictionary.py -inputFirst FirstNames.txt -inputLast LastNames.txt -delimiter '.' -outputFile Dictionary_FirstNameDotLastName.txt

            Input First: .TXT
            Input Last: .TXT
            Delimiter: '.' or exclude for none
            Output File: .TXT
