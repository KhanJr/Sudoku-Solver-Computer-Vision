def sudokuSolAlgo():
	size = 9

	#function to print solved sudoku grid

	def print_grid(arr):
	    for i in range(9):
	        print(arr[i])

	# checking empty location that means 0 position in grid
	     
	def empty(arr,l):
	    for row in range(9):
	        for col in range(9):
	            if(arr[row][col]==0):
	                l[0]=row
	                l[1]=col
	                return False
	    return True

	#checking possibilty of a no in a row

	def checkrow(arr,row,num):
	    for i in range(9):
	        if(arr[row][i] == num):
	            return False
	    return True

	#checking possibilty of no in column
	 
	def checkcol(arr,col,num):
	    for i in range(9):
	        if(arr[i][col] == num):
	            return False
	    return True
	#checking possibilities of a no in 3x3 sudoku grid

	def checkbox(arr,row,col,num):
	    for i in range(3):
	        for j in range(3):
	            if(arr[i+row][j+col] == num):
	                return False
	    return True

	# this check the possibilties of a no in a particular place by calling checkrow(),checkcol(),checkbox() functions 
	def safe(arr,row,col,num):
	    return checkrow(arr,row,num) and checkcol(arr,col,num) and checkbox(arr,row - (row%3),col - (col%3),num)

	#this function check the possibilties of all no and produce a solution
	def solve_sudoku(arr):
	#use of recursive backtracking algorithm        
	    l=[0,0]
	#calling function for free space
	    if(empty(arr,l)):
	        return True
	     
	   
	    row=l[0]
	    col=l[1]
	     
	 #checking possiblities of all digits   
	    for num in range(1,10):
	    	if(safe(arr,row,col,num)):
	             
	  	# if there is possibility we keep that no          
		        arr[row][col]=num
			    
		#moving towards next grid          
		        if(solve_sudoku(arr)):
		            return True

		#if not possible it will backtrack 
		        arr[row][col] = 0
	             
	            
	    return False
	 
	#ssolver function is check wheather a solution exist or not
	def ssolver(board):
	 
	    #printing sudoku  
	    
	    if(solve_sudoku(board)):
	       print_grid(board)
	    else:
	        print ("No solution exists")


