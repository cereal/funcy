import sys
from funcy.objects import *


### @cached_property

def test_set_cached_property():
    class A(object):
        @cached_property
        def prop(self):
            return 7

    a = A()
    assert a.prop == 7

    a.prop = 42
    assert a.prop == 42


### Monkey tests

def test_monkey():
    class A(object):
        def f(self):
            return 7

    @monkey(A)
    def f(self):
        return f.original(self) * 6

    assert A().f() == 42


def test_monkey_property():
    class A(object):
        pass

    @monkey(A)
    @property
    def prop(self):
        return 42

    assert A().prop == 42


def f(x):
    return x

def test_monkey_module():
    this_module = sys.modules[__name__]

    @monkey(this_module)
    def f(x):
        return f.original(x) * 2

    assert f(21) == 42
