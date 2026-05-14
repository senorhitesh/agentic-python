class TeaLeaf:

    def __init__(self, age):
        self.age = age   # use setter

    @property
    def age(self):
        return self._age 

    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError('Your Kid is Too Big in age')


leaf = TeaLeaf(30)
print(leaf.age);

 