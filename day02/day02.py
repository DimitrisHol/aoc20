def part1Validation(password , character , minRange , maxRange):

	validPasswords = 0 

	count = 0 
	for c in password: 

		if c == character: 
			count +=1 
	if count >= int(minRange) and count <= int(maxRange):
		validPasswords +=1

	return validPasswords



with open("input.txt") as file : 

	data = file.read().rstrip().split()


	validPasswordsPart1 = 0
	validPasswordsPart2 = 0

	# Parser
	for index in range(0, len(data) -1, 3):

		# 1. get the range
		rangePolicy = data[index].split("-")

		minRange = int(rangePolicy[0])
		maxRange = int(rangePolicy[1])

		# 2. get the character
		character = data[index+1][0]


		# 3. get the password
		password = data[index+2]

		if part1Validation (password , character , minRange , maxRange) : 
			validPasswordsPart1 +=1

		if ((character == password[minRange-1]) ^ (character == password[maxRange-1])):

			validPasswordsPart2 +=1	

	print ( "Part 1 : " ,validPasswordsPart1 )

	print ( "Part 2 : " ,validPasswordsPart2 )