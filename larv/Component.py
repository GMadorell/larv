# encoding: UTF-8
import abc

"""
A camponent is just a ton of data, almost always with just a __init__ method
that set's up some variables values.
Can maybe also have some properties, but generally every logic thing will be
done in systems.
"""

class Component(metaclass = abc.ABCMeta):
    """
    Abstract meta class for every component.
    It's utility is to keep the code more organized.
    Also allows for checking if something is a component when debugging.
    """
    @abc.abstractmethod
    def __init__():
        raise NotImplementedError()


    """
    # EXAMPLE COMPONENT:
    import Component
    class HealthComponent(Component.Component):
        def __init__(self, health):
            self.health = health
    # And that's it!
    """