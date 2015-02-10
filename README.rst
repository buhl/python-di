di - Python Dependency Injection
================================


What?
-----
**di.DependencyInjector** is a python class with which you can register dependencies and later wrap/decorate functions and methods.
python-di's home is on https://github.com/buhl/python-di


Why?
----
Dependency Injection was the new black some months/years ago. So it's time I got around to understand the concepts. At the momment, I am deep into Python and loving it, so I used it to play around with DI.

Personally, I haven't used this module yet. But I can see a couple of places it might be useful. For now I will let it mature a bit - perhabs with help from you?


Features
--------
- Wraps function/method and resolves dependencies when called
- Looks for dependencies in the di object and function/methods globals() if activated


Quick start
-----------
Install:

.. code-block:: console

    $ pip install https://github.com/buhl/python-di/archive/master.zip


Import class and initialize:

.. code-block:: python

    from di import DependencyInjector
    di = DependencyInjector()


Register dependencies:

.. code-block:: python

    di.register_dependency('sum_list_of_ints', sum)


Wrap function and call it:

.. code-block:: python

    @di
    def calc_sum(list_of_ints, sum_list_of_ints):
        return sum_list_of_ints(list_of_ints)

    assert calc_sum([1,2,3,4]) == 10  # True


Search in globals:

.. code-block:: python

    @di(globals_lookup=True)
    def calc_sum2(list_of_ints, sum_list_of_ints):
        return sum_list_of_ints(list_of_ints)

    list_of_ints = [1,2,3,4]

    assert calc_sum2() == 10  # True


Uninstall (why would you??):

.. code-block:: console

    $ pip uninstall python-di



Contributing
------------
Contributions are more than welcome. I would also love to know how you are using this module.
