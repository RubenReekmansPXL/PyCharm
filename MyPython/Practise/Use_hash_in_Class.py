__author__ = 'epq_008'
class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return (self.name == other.name) and (self.age == other.age)

    def __hash__(self):
        # replace hashables tuple with instance data attributes for your own class
        hashables = (self.name, self.age)
        # Then just use the code below unmodified.
        # It is based on Bernstein's hash function, which is
        # simple enough but works well enough
        result = 0
        for value in hashables:
            result = 33*result + hash(value)
        return hash(result)

pet1 = Dog("marceau", 10)
s = set()
s.add(pet1)

pet2 = Dog("marceau", 10)
print pet2 == pet1 # prints True
print pet1 in s    # prints True
print pet2 in s    # prints True (huzzah!)  if we don't use __hash__, then this will return false