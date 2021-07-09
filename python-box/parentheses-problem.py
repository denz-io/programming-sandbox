# Python3 program to count the number of pairs
# of balanced parentheses
import math as mt

# Function to count the number of pairs
def countPairs(bracks, num):

	# Hashing function to count the
	# opening and closing brackets
	openn=dict()
	close=dict()

	cnt = 0

	# Traverse for all bracket sequences
	for i in range(num):

		# Get the string
		s = bracks[i]

		l = len(s)

		# Counts the opening and closing required
		op,cl = 0,0

		# Traverse in the string
		for j in range(l):
			# If it is a opening bracket
			if (s[j] == '('):
				op+=1
			else: # Closing bracket
			

				# If openings are there, then close it
				if (op):
					op-=1
				else: # Else increase count of closing
					cl+=1
			
		

		# If requirements of openings
		# are there and no closing
		if (op and cl==0):
			if op in openn.keys():
				openn[op]+=1
			else:
				openn[op]=1
				

		# If requirements of closing
		# are there and no opening
		if (cl and op==0):
			if cl in openn.keys():
				close[cl]+=1
			else:
				close[cl]=1
			

		# Perfect
		if (op==0 and cl==0):
			cnt+=1
	

	# Divide by two since two
	# perfect makes one pair
	cnt = cnt //2

	# Traverse in the open and find
	# corresponding minimum
	for it in openn:
		cnt += min(openn[it], close[it])

	return cnt


# Driver Code
bracks= [")())", ")", "((", "((", "(", ")", ")" ]

print(len(bracks))

num = len(bracks)

print(countPairs(bracks, num))

#This code is contributed by Mohit kumar 29

