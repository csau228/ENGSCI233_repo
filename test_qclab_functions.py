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


	# test 2
	[A2, b2] = lu_read('test2.txt')						# read a matrix and RHS vector
	LU2,p2 = lu_factor(A2)   								# change display to False when LU_FACTOR working
	LU_soln2 = np.array([
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
	assert norm(LU2 - LU_soln2) < 1.e-10

# test LU factorization function (w partial pivot)
# **write your function here**

# test forward substitution function
# **this function is incomplete**
def test_lu_forward_sub():
	""" *you don't need to write docstrings for these functions*
	"""	
	# test 1
	L = np.array([
		[ 2, 3,-4, 2],
		[-2, 1,-2, 1],
		[ 1,-1, 3,-1],
		[-3, 2, 2, 2]])	

	b = np.array([4, -8, 9, 6])

	y = lu_forward_sub(L, b) 		
	y_soln = np.array([4,0,5,8])						# correct output of LU_FORWARD_SUB
	assert norm(y - y_soln) < 1.e-10

	# test 2
	L2 = np.array([
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

	b2 = np.array ([[1.01], [-0.99], [-0.99], [-0.99], [-0.99], [-0.99], [-0.99], [-0.99], [-0.99], [-0.99], [0.]])

	y2 = lu_forward_sub(L2, b2) 		
	y_soln2 = np.array([1.01, -101.99, 98.01, 98.01, 98.01, 98.01, 98.01, 98.01, 98.01, 98.01, 99])						# correct output of LU_FORWARD_SUB
	assert norm(y2 - y_soln2) < 1.e-10
	

	



# test backward substitution function
# **write your function here**
def test_lu_backward_sub():
	# test 1
	LU = np.array([
		[ 2, 3,-4, 2],
		[-2, 1,-2, 1],
		[ 1,-1, 3,-1],
		[-3, 2, 2, 2]])	
	y = np.array([4, 0, 5, 8])

	x = lu_backward_sub(LU, y) 	
	x_soln = np.array([1, 2, 3, 4])						# correct output of LU_BACKWARD_SUB
	assert norm(x - x_soln) < 1.e-10

	# test 2
	LU2 = np.array([
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

	y2 = np.array([1.01, -101.99, 98.01, 98.01, 98.01, 98.01, 98.01, 98.01, 98.01, 98.01, 99])	

	x = lu_backward_sub(LU2, y2) 	
	x_soln = np.array([1, 2, 3, 4])						# correct output of LU_BACKWARD_SUB
	assert norm(x - x_soln) < 1.e-10


# test isSquare function
# **write your function here**

def test_isSquare():
	# test 1
	LU = np.array([
		[ 2, 3,-4, 2],
		[-2, 1,-2, 1],
		[ 1,-1, 3,-1],
		[-3, 2, 2, 2]])

	z = isSquare(LU)
	z_soln = True
	assert z == z_soln

	# test 2
	LU2 = np.array([
		[ 2, 3,-4, 2],
		[-2, 1,-2, 1],
		[ 1,-1, 3,-1]])

	z = isSquare(LU2)
	z_soln = False
	assert z == z_soln
	