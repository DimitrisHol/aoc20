def part1(goal):

    for i in data: 

        remaining = goal - int(i)
        if remaining in data : 
            print("Found" , i , remaining ,  "summing to " , goal , remaining * i)

            return remaining , i 


# Fix 1 number in place , then use the part1 algorithm
def part2():
    goal = 2020

    for i in data:
        remaining = goal -int(i)
        # Now find 2 numbers in the array that sum up to the remainder

        numbers = part1(remaining)
        if numbers is not None : 
            if numbers[0] + numbers[1] + i == goal:

                print (numbers[0] * numbers[1] * i)
                break


# Reading the data in a fancy way
data = [int(x) for x in open("input.txt").read().rstrip().split()]
goal = 2020

print ( "Part 1 :")
part1(goal)
print ( "Part 2 :")
part2()


