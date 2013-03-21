class Monster(object):
    def sayBoo(self):
        print "boo!"

class SeaMonster(Monster):
    def swim(self):
        print "glug glug!"

m1 = SeaMonster()
m2 = Monster()

print type(m1) == Monster     # False
print type(m2) == Monster     # True
print type(m1) == SeaMonster  # True
print type(m2) == SeaMonster  # False

print isinstance(m1, Monster)    # True (differs from (type(m1) == Monster) above!)
print isinstance(m2, Monster)    # True
print isinstance(m1, SeaMonster) # True
print isinstance(m2, SeaMonster) # False