# -*- coding: utf-8 -*-
from di import DependencyInjector

di = DependencyInjector()
di.register_dependency('list_summer_upper', sum)


class SpecialClass(object):
    @di
    def the_sum_of_a_list(self, list_of_ints, list_summer_upper):
        return list_summer_upper(list_of_ints)

    @di
    def the_sum_of_a_list__reversed_args(self, list_summer_upper, list_of_ints):
        return list_summer_upper(list_of_ints)


class AwkwardClass(object):
    @di
    def __init__(self, list_summer_upper):
        self.sum = list_summer_upper

    def sum_this_list(self, list_of_ints):
        return self.sum(list_of_ints)


class GlobalsClass(object):
    @di(globals_lookup=True)
    def return_an_awkward_class(self, AwkwardClass):
        return AwkwardClass


def test_the_sum_of_a_list():
    k = SpecialClass()

    assert k.the_sum_of_a_list([1, 2, 3, 4]) == 10


def test_the_sum_of_a_list__reversed_args():
    k = SpecialClass()

    assert k.the_sum_of_a_list__reversed_args([1, 2, 3, 4]) == 10


def test_class_initialization():
    k = AwkwardClass()
    assert k.sum_this_list([1, 2, 3, 4]) == 10


def test_globals_on_methods():
    k = GlobalsClass()
    assert k.return_an_awkward_class() == AwkwardClass
