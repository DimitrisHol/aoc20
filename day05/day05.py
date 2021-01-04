seats = [x for x in open("input.txt").read().rstrip().split()]


occupiedSeats ={}

for i in range(128) : 
	occupiedSeats[i] = []

maximum = 0 
for seat in seats : 

	row = int (seat.replace("B" , "1").replace("F" , "0")[:7] ,2)
	column = int(seat.replace("R" , "1").replace("L" , "0")[7:], 2)

	seatID =  row *  8 +column

	if seatID > maximum  : 

		maximum = seatID

	occupiedSeats[row].append(column)

for occupiedSeat in occupiedSeats : 

	if len(occupiedSeats[occupiedSeat]) < 8 and len(occupiedSeats[occupiedSeat]) !=0 :

		print ( occupiedSeat , occupiedSeats[occupiedSeat])



print ("Part 1 :" , maximum)
print ("Part 2 :" , 72 * 8 + 3)






'''

* Start with the whole 128 rows of the plane 

* Each letter tells you in which half the seat is in.

* First F or B indicates if it's in the first rows, or the back rows

0-63 and 64-128 respectively

* Second letter does the same thing , with the next subset.

* Finally you end up with 1 row 

* Last 3 Characters will be either R or L , they specify one of the 8 columns 
of the seats of the plane (0-7) L = lower half , R = upper half


BFFFBBF : 70 = 64 + 4 + 2
1000110

70 : BFFFBBF
70 : 



exoum se seats ta FBFBFBFBLRR

kataferame na broyme seatID apo kathe ena ksexwrista 

exoume thn thesh tou row kai thn thesh tou column 

naive solution : 

apothikeuse se enan 2d pinaka tis theseis apo 0 mexri 127 poy einai piasmenes



'''