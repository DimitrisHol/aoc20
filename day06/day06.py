def part1(groups) : 


	totalAnswers = 0 
	for group in groups :


		# Group answer = ['ab', 'ac']
		groupAnswer = group.split("\n")
		groupDict = {}

		#	answers =['ab']
		for answers in groupAnswer :

			# answer = ["a" ,"b"]
			for answer in answers:


				groupDict[answer] = True

		

		totalAnswers += len(groupDict)

	print("Part 1 : " , totalAnswers)



def part2 (groups):
	totalAnswers = 0 
	for group in groups :


		# Group answer = ['ab', 'ac']
		groupAnswer = group.split("\n")
		groupDict = {}

		#	answers =['ab']
		for answers in groupAnswer :

			# answer = ["a" ,"b"]
			for answer in answers:

				# Initialize
				groupDict[answer] = 0

		for answers in groupAnswer :

			for answer in answers:

				#Populate the answers
				groupDict[answer] += 1



		for key in groupDict: 

			if groupDict[key] == len(groupAnswer) : 

				totalAnswers +=1

			# print (key , groupDict[key], len(groupAnswer)) 


		# print ( "-------------------")



	print("Part 2 : " , totalAnswers)



groups = [x for x in open("input.txt").read().rstrip().split("\n\n")]



part1(groups)
part2(groups)