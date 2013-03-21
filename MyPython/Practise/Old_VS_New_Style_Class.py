__author__ = 'epq_008'
# old-style classes are created like this (no superclass):
class OldStyle: pass

# new-style classes include the superclass in parentheses, like this:
class NewStyle(object): pass

# new-style classes are much more "OOPy" (they have a more complete object model).
# For example, new-style classes are types, and their instances are of that type:

obj = NewStyle()
print isinstance(obj, NewStyle) # True
print type(obj) == NewStyle     # True
print type(obj)                 # <class 'NewStyle'>

# old-style classes do not work the same way:

obj = OldStyle()
print isinstance(obj, OldStyle) # True
print type(obj) == OldStyle     # False!
print type(obj)                 # <type 'instance'>