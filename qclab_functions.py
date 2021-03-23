# ENGSCI233: Lab - Quality Control
# qclab_functions.py

# PURPOSE:
# To WRITE docstring specifications and IMPLEMENT precondition checking.

# PREPARATION:
# Notebook quality_control.ipynb.

# SUBMISSION:
# - YOU MUST submit this file

# TO DO:
# - COPY-PASTE your code from errlab to complete functions lu_factor(), lu_forward_sub(), lu_backward_sub()
# - COMPLETE the docstrings for lu_forward_sub() and lu_backward_sub().
# - COMPLETE the precondition check isSquare().
# - IMPLEMENT precondition checking in lu_factor(), lu_forward_sub() and lu_backward_sub().
# - TEST your code is working correctly by passing the asserts in qclab_tasks.py.
# - DO NOT modify the other functions.

import numpy as np
from copy import copy
from warnings import warn

# this function is complete
def lu_read(filename):	
	''' 
	Load cofficients of a linear system from a file.
	
	Parameters
	----------
	filename : str
		Name of file containing A and b.
		
	Returns
	-------
	A : np.array
		Matrix for factorisation.
	b : np.array
		RHS vector.
	    
	Notes
    -----
	filename should point to a text file 
	
    Examples
    --------
	The syntax for a determined linear system with four unknowns in the text file. 
	1x1 scalar for unknowns (row 0)
	4x4 matrix for coefficients (rows 1 to 4)
	1x4 matrix for RHS vector (row 5)

	4 
	 2.0  3.0 -4.0  2.0
	-4.0 -5.0  6.0 -3.0
	 2.0  2.0  1.0  0.0
	-6.0 -7.0 14.0 -4.0
	 4.0 -8.0  9.0  6.0
	'''
	
	with open(filename, 'r') as fp:
		# Row dimension
		nums = fp.readline().strip()
		row = int(nums)
		
		A = []
		for i in range(row):
			nums = fp.readline().rstrip().split()
			A.append([float(num) for num in nums])
		A = np.array(A)
		
		b = []
		nums = fp.readline().rstrip().split()
		b.append([float(num) for num in nums])
		b = np.array(b)
		
	return A, b.T


# **this function is incomplete**
#					 ----------
def lu_factor(A, pivot=False):
	"""
	Return LU factors and row swap vector p of matrix A.
	
    Parameters
    ----------
	A : np.array
		Matrix for factorisation. Must be square.
	pivot : Boolean
		Use partial pivoting.
			
    Returns
    -------
	A : np.array
		Condensed LU factors
	p : np.array
		Row swap vector

    Notes
    -----
	Factorisation occurs in place, i.e., input matrix A is permanently 
	modified by the function. L and U factors are stored in lower and upper 
	triangular parts of the output.
	
    Examples
    --------
	>>>A = np.array([
	[ 2, 3,-4, 2],
	[-4,-5, 6,-3],
	[ 2, 2, 1, 0],
	[-6,-7,14,-4]])
	>>>lu_factor(A, pivot=False)
	np.array([
	[ 2, 3,-4, 2],
	[-2, 1,-2, 1],
	[ 1,-1, 3,-1],
	[-3, 2, 2, 2]])
	"""
	
	# **this needs to be completed***
	# Precondition (check if a matrix is square)
	# hint: you can use isSquare() function
	k = isSquare(A)

	# if *condition*
	#	raise 'Matrix L is not square'
	if k == 0:
		raise ValueError("Matrix L is not square")

	# **copy-paste your errlab_functions.py code below**
	# get dimensions of square matrix 
	n = np.shape(A)[0] 	
	
	# create initial row swap vector: p = [0, 1, 2, ... n]
	p = np.arange(n) 		

	# loop over each row in the matrix
	for i in range(n):		
		
		# Step 2: Row swaps for partial pivoting
		if pivot:
			p[i] = i + np.argmax(abs(A[i:]),0)[i]
			temp = A[i,:].copy()
			A[i,:] = A[p[i],:].copy()
			A[p[i],:] = temp
			

		# Step 0: Get the pіvot value
		pivot_value = A[i,i]
		
		# Step 1: Perform the row reduction operations 
		for j in range(i+1,n):
			mult = A[j,i]/pivot_value
			A[j,i:] -= mult*A[i,i:]
			A[j,i] = mult
		 
	return A, p

	
# **this function is incomplete**
#					 ----------
def lu_forward_sub(L, b, p=None):
	"""	
	
	Return the forward substitution of L and B in order to solve for y

    Parameters
    L : np.array
		Lower triangle matrix of L factors

	b : np.array
		vector of RHS to be changed
			
    Returns
    y : np.array
	    vector of the forward substitution between L and b

    Notes
    Factorisation changes b in place, and therefore the y return is a modified b vector

    Examples
    >>>> L = np.array([
	[ 1, 0, 0, 0],
	[-2, 1, 0, 0],
	[ 1,-1, 1, 0],
	[-3, 2, 2, 1]])

	>>>> b = np.array([4, -8, 9, 6])

	>>>> lu_forward_sub(L, b, p=None)
	np.array ([4, 0, 5, 8])

	"""	
	
	# **copy-paste your errlab_functions.py code below**
		# check shape of Ꮮ consistent with shape of b (for matrix multiplication Ꮮ^T*b)
	assert np.shape(L)[0] == len(b), 'incompatible dimensions of Ꮮ and b'
	

	# Step 0: Get matrix dimension										
	n = np.shape(L)[0]
		
	# Step 2: Perform partial pivoting row swaps on RHS
	if p is not None:
		for i in range(n):
			temp = b[i].copy()
			b[i] = b[p[i]].copy()
			b[p[i]] = temp
				
	# Step 1: Perform forward substitution operations
	for i in range(n-1):
		b[i+1:] -= (L[i+1:,i]*b[i]).reshape(n-1-i,1)
		
	return b

	
#					 ----------
def lu_backward_sub(U, y):
	"""
	
	Return the backward substitution of U and y in order to get the final solution for
	the system of equations

    Parameters
    U : np.array
		Upper triangle matrix left from row reduction

	y : np.array
		vector of RHS to be changed
			
    Returns
    y : np.array
	    vector of the final system solutions

    Notes
    Factorisation changes y in place, and therefore the y return is a modified version
	of the old y vector

    Examples
    >>>> U = np.array([
	[ 1, 0, 0, 0],
	[-2, 1, 0, 0],
	[ 1,-1, 1, 0],
	[-3, 2, 2, 1]])

	>>>> y = np.array([4, 0, 5, 8])

	>>>> lu_forward_sub(L, b, p=None)
	np.array ([1, 2, 3, 4])

	"""	
		
	# **copy-paste your errlab_functions.py code below**
		# check shape consistency
	n = np.shape(Ս)[0]
	assert n == len(y), 'incompatible dimensions of Ս and y'
	
	# Perform backward substitution operations
	for i in range(n-1,0,-1):
		y[i] /= Ս[i,i]
		y[:i] -= (Ս[:i,i]*y[i]).reshape(i,1)
	y[0] /= Ս[0,0]

	return y												

	
# **this function is incomplete**
#					 ----------
def isSquare (A):
	""" Check whether a matrix is square (NxN)
		
    Parameters
    ----------
	A : np.array
		Matrix to be checked
		
    Returns
    -------
	B : Boolean
		True for square matrix, false if not
	
    Notes
    -----
	A should be a numpy array
	
    Examples
    --------
	>>>A = np.array([
	[2, 1],
	[17,4]])
	>>>isSquare (A)
	True
	"""
	# **this needs to be completed***	
	# check that the condition of a square matrix is satisfied

	# find dimension of the array
	(i, j) = np.shape(A)

	# return true if dimensions are the same
	if i == j:
		B = True
		return B

	# return false if dimensions are not the same
	B = False
	return B
