import re 

def part1() : 

	validPassports = 0

	# Take the batch file and split it to each passport
	for rawPassport in data : 

		passportEntry = rawPassport.split()
		# passportEntry : ['ecl:gry', 'pid:860033327']

		passportFields = []
		# Take each passport take the names of the fields
		for field in passportEntry :
			fields = field.split(":")

			passportFields.append(fields[0])

		# passPortFields = ['ecl', 'pid']

		# Validation : does the passport have all the required fields?

		valid = True 
		for field in allFields : 

			if field not in passportFields : 
				valid = False	
				break
		if valid : 
			validPassports +=1
	return validPassports

def part2() : 

	validPassports = 0
	allPassports = 0


	validPassportData = {}


	# Take the batch file and split it to each passport
	for rawPassport in data : 

		passportEntry = rawPassport.split()
		# passportEntry : ['ecl:gry', 'pid:860033327']
		allPassports +=1

		passportFields = [] # For Validation
		fieldDictionary = {} # For Validation part 2
		# Take each passport take the names of the fields
		for field in passportEntry :
			fields = field.split(":")

			# Validation Part 1 
			passportFields.append(fields[0])

			# Validation Part 2 

			fieldDictionary[fields[0]] = fields[1]

		# Pass passportEntry to dictionary

		# passPortFields = ['ecl', 'pid']

		valid = True 

		# Validation Part 1 : does the passport have all the required fields?
		for field in allFields : 

			if field not in passportFields : 
				valid = False	
				break

 		# Validation Part 2: do the passport values checkout ?

 		# fields [0] key, fields[1] : value

 		# Check if it passed the previous validation 

		if valid : 



			# Birth Year (BYR) :

			if int(fieldDictionary["byr"]) < 1920 or int(fieldDictionary["byr"]) > 2002:

				valid = False	
				continue


			if int(fieldDictionary["iyr"]) < 2010 or int(fieldDictionary["iyr"]) > 2020:

				valid = False	
				continue

			if int(fieldDictionary["eyr"]) < 2020 or int(fieldDictionary["eyr"]) > 2030:

				valid = False
				continue	 



			if "cm" in fieldDictionary["hgt"]:

				# Some trouble for values under 100cm (2characters instead of 3)
				if int(fieldDictionary["hgt"][:len(fieldDictionary["hgt"])-2]) < 150 or int(fieldDictionary["hgt"][:len(fieldDictionary["hgt"])-2]) > 193 :

					valid = False
					continue	

			elif "in" in fieldDictionary["hgt"]:

				if int(fieldDictionary["hgt"][:2]) < 59 or int(fieldDictionary["hgt"][:2]) > 76 :

					valid = False
					continue	

			else :
				valid = False 
				continue

			validEyeColours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

			if fieldDictionary["ecl"] not in validEyeColours : 

				valid = False
				continue

			# Pattern : 
			'''
			^ : start of the line 
			[a-z0-9] : what should be included
			{7} how many characters long

			'''
			validHairColour = re.findall("^[#a-f0-9]{7}", fieldDictionary["hcl"])
			
			if not validHairColour : 

				valid = False
				continue	

			# There was value with 10 numbers, regex matches it and passes only the 9
			# digits so also do this :) 

			if len(fieldDictionary["pid"]) != 9: 
				valid = False
				continue

			validPassportId = re.findall("^[0-9]{9}" , fieldDictionary["pid"])

			if not validPassportId :

				valid = False
				continue	


		if valid :
			validPassports +=1
	return validPassports 


data = [x for x in open("input.txt").read().split("\n\n")]

# cid is optional so we don't put it in
allFields = ["byr" , "iyr" , "eyr" , "hgt" , "hcl", "ecl" , "pid"] 

print("Part 1 : " , part1())
print("Part 2 : " , part2())


# Maybe more refactoring to have puzzle() and part1() part2()? 
# Or put part1() inside part2(), but too much hassle.