

raw_data = ["apple:5" , "orange:6"]


# Convert into a dictionary

fruitDictionary = {}
for record in raw_data : 

	# Parse into list : 

	fruits = record.split(":")

	# print ( fruits)

	fruitDictionary[fruits[0]] = fruits[1]

print(fruitDictionary)


print ( fruitDictionary["apple"])


# Pattern : 


'''

^ : start of the line 

[a-z0-9] : what should be included

{} how many characters long

'''



hairColourList = ["#123abc" , "#123abz" , "123abc"]


import re 
for hairColour in hairColourList : 
	x = re.findall("^[#a-f0-9]{7}", hairColour)
	if not x : 

		print ( "Non Valid")
	else : 
		print ( "Valid")



heights = [x for x in open("test.txt").read().rstrip().split()]


for height in heights: 

	print ( height[:2])
