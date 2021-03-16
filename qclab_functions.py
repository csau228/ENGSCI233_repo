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
	#
	# if *condition*
	#	raise 'Matrix L is not square'
	
	# **copy-paste your errlab_functions.py code below**
	pass

	
# **this function is incomplete**
#					 ----------
def lu_forward_sub(L, b, p=None):
	"""
	**this needs to be completed***	
	
    Parameters
    ----------
			
    Returns
    -------

    Notes
    -----

    Examples
    --------

	"""	
	
	# **copy-paste your errlab_functions.py code below**
	pass

	
# **this function is incomplete**
#					 ----------
def lu_backward_sub(U, y):
	"""
	**this needs to be completed***	

	"""	
		
	# **copy-paste your errlab_functions.py code below**
	pass												

	
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
	B = False
	return B
