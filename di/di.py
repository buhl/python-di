# -*- coding: utf-8 -*-
from functools import wraps
import inspect


class DependencyInjector(object):
    def __init__(self, dependencies=None, globals_lookup=False):
        self.globals_lookup = globals_lookup
        self.dependencies = {}
        if isinstance(dependencies, dict):
            self.dependencies = dependencies

    def register_dependency(self, dep_name, dep_object=None):
        if dep_object is None:
            dep_object = dep_name
            dep_name = dep_object.__name__

        self.dependencies[dep_name] = dep_object

    def __call__(self, *args, **kwargs):
        if not kwargs and len(args) == 1 and callable(args[0]):
            return self._wrap(args[0])

        if kwargs.pop("keep", False):
            di = self
        else:
            di = DependencyInjector(self.dependencies, self.globals_lookup)

        for arg in args:
            di.register_dependency(arg)

        for key in kwargs:
            if key in ["globals_lookup"]:
                setattr(di, key, kwargs[key])
            else:
                di.register_dependency(key, kwargs[key])

        return di

    def __getattr__(self, attr):
        if attr in self.dependencies:
            return self.dependencies[attr]
        raise NameError("dependancy name '{}' is not defined".format(attr))

    def _get_globals(self, f):
        if not self.globals_lookup:
            return {}

        if inspect.isfunction(f):
            return f.__globals__

    def _wrap(self, f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            args, kwargs = self._inject(f, args, kwargs)
            return f(*args, **kwargs)

        return wrapper

    def _inject(self, f, args, kwargs):
        largs = list(args)
        signature = inspect.signature(f)
        namespace = self._get_globals(f)

        for key in signature.parameters:
            if key in self.dependencies:
                kwargs[key] = self.dependencies[key]
            elif key in namespace:
                kwargs[key] = namespace[key]
            elif largs:
                kwargs[key] = largs.pop(0)

        return tuple(largs), kwargs
