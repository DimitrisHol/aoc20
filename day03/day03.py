# Pass data into 2D array : 

forest = [x for x in open("input.txt").read().split("\n")]


# Length of forest is the way down 
# Length of forest[X] is the way right

# Part 1 : Right 3 , Down 1 

def descend (right , down ): 

	treesHit = 0 
	positionX = 0
	positionY = 0
	rowLength = len(forest[0]) 

	for i in range (len(forest) -1):

		positionX = (positionX + right) % rowLength
		positionY += down

		if positionY > len(forest)-1 : 
			break

		# print ( positionY , positionX ,forest[positionY][positionX])

		if forest[positionY][positionX] == "#":
			treesHit +=1

	print (right , down , treesHit)

	return treesHit


i1 = descend(1, 1)
i2 = descend(5, 1)
i3 = descend(3, 1)
i4 = descend(7, 1)
i5 = descend(1, 2)

print (i1 * i2 * i3 * i4 * i5)