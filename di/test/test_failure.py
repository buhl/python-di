# -*- coding: utf-8 -*-
from di import DependencyInjector
import pytest


def test_invalid_function_injection():
    di = DependencyInjector()

    @di
    def fail_with_typeerror(somethingService):
        return somethingService.do().encredible.stuff()

    with pytest.raises(TypeError) as excinfo:
        fail_with_typeerror()

    assert "fail_with_typeerror() missing 1 required positional argument: 'somethingService'" == str(excinfo.value)


def test_invalid_class_parent():

    di = DependencyInjector()

    with pytest.raises(NameError) as excinfo:
        class Noooo(di.NoneExisting):
            pass

    assert "dependancy name 'NoneExisting' is not defined" == str(excinfo.value)
