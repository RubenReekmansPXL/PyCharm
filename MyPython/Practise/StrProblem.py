
#Working Solution #3:  Use __repr__ with %r
class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return (self.name == other.name) and (self.age == other.age) #solution for equal problem

   # def __str__(self):
    #    return "Dog(%s, %s)" % (self.name, self.age)
    # when print [pet1] will  prints [<__main__.Dog object at 0x0000000002308CC0>]

    def __repr__(self):
        return "Dog(%r, %r)" % (self.name, self.age)

   # def __repr__(self):
    #    return "Dog(%s, %s)" % (self.name, self.age)  this will cause NameError: name 'marceau' is not defined
    #                                                       When you wanna use eval


pet1 = Dog("marceau", 10)
print pet1   # prints Dog('marceau', 10)
print [pet1] # prints [Dog('marceau', 10)]
pet2 = eval(repr(pet1))
print pet2 == pet1  # prints True (huzzah!)