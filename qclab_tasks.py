# ENGSCI233: Lab - Quality Control
# qclab_tasks.py

# PURPOSE:
# - CREATE a github code repository.
# - WRITE a specification (docstring).
# - IMPLEMENT a precondition.
# - WRITE a unit test.

# SUPPORTING MATERIAL (SP):
# SP1. GitHub introduction video on Canvas
# SP2. Pytest introduction video : https://www.youtube.com/watch?v=l32bsaIDoWk

# SUBMISSION:
# Personal GitHub repository (URL) containing:
# - qclab_functions.py
# - qclab_tasks.py
# - test_qclab_functions.py

# imports
from qclab_functions import*

# EXERCISE 1: Git repository
# Follow the lab instructions to create a GitHub repository and add some files. 

# TO DO:
#   - Watch SP1.
#   - Register a GitHub account.
#	- Create a new PRIVATE repository.
#   - Clone the repository to the ENGSCI233 folder on your H: drive.
#   - Add this file, qclab_functions.py, qclab_tasks.py and test_qclab_functions.py to the repository.
#   - Ensure that you COMMIT and PUSH all changes when you have finished the lab.
#   - USE sensible, informative commit messages.


# EXERCISE 2: Specification (docstring)
# Write function specifications using the standard Python format. 

# TO DO:
#   - COPY your code from the previous lab into qclab_functions.py
#   - Inspect the docstring for lu_factor()
#   - Write docstrings for lu_forward_sub and lu_backward_sub functions.
#   - ADD and then COMMIT your changes to the LOCAL repository. 
#   - PUSH your changes up to the REMOTE repository. 


# EXERCISE 3: Preconditions 
# Write a function that evaluates the "squareness" of a matrix and use this to evaluate a 
# "squareness" precondition in lu_factor().

# 3.1 TO DO:
# 	- In qclab_functions.py, complete the function isSquare() (hint: read the dosctring provided).
#   - Pass the asserts below.
#   - (optional) Use print statements or debugging to explain what the commands np.zeros, np.ones, 
#     np.eye and np.random.rand return.

Asquare1 = np.array([[1,2],[3,4]])
Asquare2 = np.zeros((8,8))
Asquare3 = np.random.rand(22,22)

Anotsquare1 = np.array([[1,2],[3,4],[5,6]])
Anotsquare2 = np.array([[1,3,5],])
Anotsquare3 = np.ones((4,12))
Anotsquare4 = np.eye(9,7)

for Asquare in [Asquare1, Asquare2, Asquare3]:
	assert isSquare(Asquare) is True

for Anotsquare in [Anotsquare1, Anotsquare2, Anotsquare3, Anotsquare4]:
	assert isSquare(Anotsquare) is False

# 3.2 TO DO:
#   - In qclab_functions.py, use isSquare to check the "squareness" precondition in lu_factor().
#   - Raise a ValueError if precondition is not met.
#   - Pass the assert below.
#   - ADD and then COMMIT your changes to the LOCAL repository. 
#   - PUSH your changes up to the REMOTE repository.  

# *do not modify the code block below*
try:
	lu_factor(Anotsquare)
except ValueError:
	# if you are raising the correct error, we will catch it here, 
	# tell Python to ignore it, and continue with the code
	pass

print('you have passed all tests in qclab_tasks.py - go to EXERCISE 4')
 
# EXERCISE 4: Unit tests
# Use the pytest python library to write and run unit tests.

# TO DO:
#   - In errlab_practice.py, inspect the assert test under EXERCISE 1.
#   - In test_qclab_functions.py, inspect the code for test_lu_factor().
#   - Open a command prompt and run 'pytest -v' in the directory containing test_qclab_functions.py
#   - Modify test_lu_factor() so that it tests partial pivoting functionality, and more than one matrix. 
#   - Implement unit tests for lu_forward_sub(), lu_backward_sub() and isSquare() using APPROPRIATELY NAMED test functions .
#   - ADD and then COMMIT your changes to the LOCAL repository. 
#   - PUSH your changes up to the REMOTE repository. 


# FINAL SUBMISSION:
#   - PUSH all changes to the repository.
#   - Make sure you add bryan-ruddy as a collaborator on your repository on GitHub.
#   - Submit to CANVAS the file qclab_repository.txt, with the address of your PRIVATE repository.

