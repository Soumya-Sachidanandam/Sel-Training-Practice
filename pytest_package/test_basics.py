# def login():
#     print("login executing")
#
# def logout():
#     print("logout executing")
#
# login()
# logout()

## To execute the class, we should create the object and call the attributes
#################################################################################################################################

# def test_login():
#     print("login executing")
#
# def test_logout():
#     print("logout executing")
    #
    # collected
    # 2
    # items
    #
    # test_basics.py::test_login
    # login
    # executing
    # PASSED
    # test_basics.py::test_logout
    # logout
    # executing
    # PASSED
###################################################################################################################################

# def test_login():
#     print("login executing")
#
# def signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#here signup wont get executed by pytest since it is not defined as per the rules

# ###############################################################################################################################
# def test_login():
#     print("login executing")
#     def test_signup():
#         print("signup executing")




#so pytest will recognize only outer test function


#################################################################################################################################


# def test_login():
#     raise Exception
#
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")

'''
Though there is error in first test case, next two tests are getting executed which is an advantage of pytest
'''

'''
test_basics.py::test_login FAILED
test_basics.py::test_signup signup executing
PASSED
test_basics.py::test_logout logout executing
PASSED
'''

################################################################################################################################
# def test_login():
#     print("login executing")
#
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# test_login()
# test_signup()
# test_logout()

'''
collecting ... login executing
signup executing
logout executing
collected 3 items                                                                                                                             

test_basics.py::test_login login executing
PASSED
test_basics.py::test_signup signup executing
PASSED
test_basics.py::test_logout logout executing
PASSED
'''
'''

No need to give function call in pytest.Even if we give it wont throw error rather the execution happens twice.
'''

##################################################################################################################################

#
# def test_add(a, b):
#     print(a + b)

'''
E       fixture 'a' not found
'''

'''
We cannot pass formal parameters in function through pytest(There is other way though). We can use in general way in function call.
'''

# ##########################################################################################################################################
# def test_add(a, b):
#     print(a + b)
#
# test_add(1, 2)

'''
collecting ... 3
collected 1 item                                                                                                                              

test_basics.py::test_add ERROR
'''

'''
Through func call it is getting executed where as through pytest is throwing error
'''
###################################################################################################################################

# def test_login():
#     print("hello world")
#
# def test_login():
#     print("hello universe")


'''
collected 2 items                                                                                                                             

test_basics.py::test_add ERROR
test_basics.py::test_login hello universe
PASSED
'''
#--------------doubt---output differs from ramya mam--------------------###################################################


# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")

'''
collected 3 items                                                                                                                             

test_basics.py::TestSample::test_login login executing
PASSED
test_basics.py::TestSample::test_signup signup executing
PASSED
test_basics.py::TestSample::test_logout logout executing
PASSED
'''

###################################################################################################################################

# class Sample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")



'''
collected 0 items
'''

'''Class name is not following rules'''
#############################################################################################################


# class TestSample:
#
#     def login(self):
#         print("login executing")
#
#     def signup(self):
#         print("signup executing")
#
#     def logout(self):
#         print("logout executing")

'''
collected 0 items 
'''

'''
Attributes are not following the rules
'''

###########################################################################################################################

# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# s = TestSample()
# s.test_login()
# s.test_signup()
# s.test_logout()

'''

collecting ... login executing
signup executing
logout executing
collected 3 items                                                                                                                             

test_basics.py::TestSample::test_login login executing
PASSED
test_basics.py::TestSample::test_signup signup executing
PASSED
test_basics.py::TestSample::test_logout logout executing
PASSED
'''


'''
Execution happens twice
'''

##################################################################################################################################

#
# class TestSample:
#
#     def test_login(self, name):
#         print("login executing")


'''
paramaters passing is not allowed.There is someother way
'''

##############################################################################################################################


class TestSample:

    def __init__(self):
        pass

    def test_login(self):
        print("login executing")

    def test_signup(self):
        print("signup executing")

    def test_logout(self):
        print("logout executing")













