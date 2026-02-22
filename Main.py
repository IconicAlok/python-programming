# variable scope = where a variable is visible and accessable
# scopr resulation = (LEGB) Local -> Enclosed -> Global -> Build in


def func1():
    # a = 1
    print(x)

def func2():
    # b = 2
    print(x)
    # print(a)          # name error variable a is not define

x = 3
func1()
func2()

from math import e
def func3():
    print(e)
e = 3
func3()