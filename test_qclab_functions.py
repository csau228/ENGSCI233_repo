# ENGSCI233: Lab - Quality Control
# test_qclab_tasks.py

from qclab_functions import *
import numpy  as np
from numpy.linalg import norm

# CURRENTLY WRITING TEST 2 IN THE FUNCTION TEST_LU_FORWARD-SUB (TASK 4.1)

# test LU factorization function (w/o partial pivot)
# **this function is incomplete**
def test_lu_factor():
	"""
	Test if function lu_factor is working properly by comparing it with a known result.

	Tests should be expanded to include two different matrices, as well as partial pivoting functionality.
	"""
	#[A, b] = lu_read('test1.txt')
	# it is poor form to read an external file into a test function, as above
	A = np.array([
		[ 2.,  3., -4.,  2.],
		[-4., -5.,  6., -3.],
		[ 2.,  2.,  1.,  0.],
		[-6., -7., 14., -4.]])	
	LU,p = lu_factor(A, pivot=False)
	LU_soln = np.array([
		[ 2, 3,-4, 2],
		[-2, 1,-2, 1],
		[ 1,-1, 3,-1],
		[-3, 2, 2, 2]])	
	assert norm(LU - LU_soln) < 1.e-10	


# test LU factorization function (w partial pivot)
# **write your function here**

# test forward substitution function
# **this function is incomplete**
def test_lu_forward_sub():
	""" *you don't need to write docstrings for these functions*
	"""	
	# test 1
	[A, b] = lu_read('test1.txt')						# read a matrix and RHS vector
	LU,p = lu_factor(A)   								# change display to False when LU_FACTOR working
	LU_soln = np.array([
		[ 2, 3,-4, 2],
		[-2, 1,-2, 1],
		[ 1,-1, 3,-1],
		[-3, 2, 2, 2]])									# correct output of LU_FACTOR
	assert norm(LU - LU_soln) < 1.e-10
 

	# test 2
	[A, b] = lu_read('test2.txt')						# read a matrix and RHS vector
	LU,p = lu_factor(A)   								# change display to False when LU_FACTOR working
	LU_soln = np.array([
		 [0.01, 0., 0., 0., 0., 0., 0., 0., 0., 0., 1],
		 [-100., 0.01, 0., 0., 0., 0., 0., 0., 0., 0., 100],
		 [0., -100., 0.01, 0., 0., 0., 0., 0., 0., 0., 10000],
		 [0., 0., -100., 0.01, 0., 0., 0., 0., 0., 0., 1000000],
		 [0., 0., 0., -100., 0.01, 0., 0., 0., 0., 0., 100000000],
		 [0., 0., 0., 0., -100., 0.01, 0., 0., 0., 0., 10000000000],
		 [0., 0., 0., 0., 0., -100., 0.01, 0., 0., 0., 1000000000000],
		 [0., 0., 0., 0., 0., 0., -100., 0.01, 0., 0., 100000000000000],
		 [0., 0., 0., 0., 0., 0., 0., -100., 0.01, 0., 10000000000000000],
		 [0., 0., 0., 0., 0., 0., 0., 0., -100, 0.01, 1000000000000000000],
		 [0., 0., 0., 0., 0., 0., 0., 0., 0., -100., 100000000000000000000]])
	assert norm(LU - LU_soln) < 1.e-10	



# test backward substitution function
# **write your function here**
def test_lu_backward_sub():


# test isSquare function
# **write your function here**

