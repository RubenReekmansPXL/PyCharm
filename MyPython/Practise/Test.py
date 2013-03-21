__author__ = 'epq_008'
# print __eq__.__doc__
# Test Methods
# Q: If you write a method C.foo(), should you write a test method C.testFoo()?
# A: Yes.
# Q: But then how do you call the test method?  Do you create an instance of C on which to call that test method?
# A: No.  You make the test method an @classmethod.
# Q: Then should you also have a C.testAll() method?
# A: Yes.  That's a fine idea.  Then you can call this single method (also an @classmethod) from outside the class to run all your test methods inside the class.