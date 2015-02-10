# -*- coding: utf-8 -*-
from di import DependencyInjector
import pytest


class OneClass(object):
    def one_method_that_returns_6(self):
        return 6


class AnotherClass(object):
    def another_method_that_returns_4(self):
        return 4


di = DependencyInjector()


def test_class_initialization():

    child_di = di(OneClass, AnotherClass)

    class EmptyClass(child_di.OneClass, child_di.AnotherClass):
        pass

    e = EmptyClass()

    assert e.one_method_that_returns_6() + e.another_method_that_returns_4() == 10
