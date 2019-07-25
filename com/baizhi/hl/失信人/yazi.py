class A():
    def fly(self):
        print('1号李佳伟')

class B():
    def fly(self):
        print('2号李佳伟')


def flyfly(animals):
    animals.fly()

Bird1=A()
Bird1.fly()
Bird2=B()
Bird2.fly()


