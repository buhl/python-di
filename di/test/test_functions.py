# -*- coding: utf-8 -*-
from di import DependencyInjector

int_list = [1, 2, 3, 4]


def test_altered_named_function_injection():
    di = DependencyInjector()
    di.register_dependency('sum_list', sum)

    @di
    def calc_sum(list_to_sum, sum_list):
        return sum_list(list_to_sum)

    assert calc_sum(int_list) == 10


def test_function_injection():
    di = DependencyInjector()

    def sumit(list_of_ints):
        return sum(list_of_ints)
    di.register_dependency(sumit)

    @di
    def calc_sum(list_to_sum, sumit):
        return sumit(list_to_sum)

    assert calc_sum(int_list) == 10


def test_globals():
    di = DependencyInjector()

    @di(globals_lookup=True)
    def do_someting(int_list):
        return sum(int_list)

    assert do_someting() == 10


def test_not_decorating():
    def do_someting(int_list):
        return sum(int_list)

    di = DependencyInjector()
    not_decorated = di(globals_lookup=True)(do_someting)

    assert not_decorated() == 10
