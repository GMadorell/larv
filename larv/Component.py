# encoding: UTF-8
import abc

class Component(metaclass = abc.ABCMeta):
    """
    Abstract meta class for every component.
    It's utility is to keep the code more organized.
    Also allows for type checking when debugging.

    A component is just a ton of data, almost always with just a __init__ method
    that sets up some variables.
    Can also have some properties (most of the times it's easier to
    just make the variables public) to modify and/or access the data, 
    but can't have any logic around it.
    Logic is 100% done by the Systems.
    """
    @abc.abstractmethod
    def __init__():
        raise NotImplementedError()


    """
    # EXAMPLE COMPONENT:
    import larv
    class HealthComponent(larv.Component):
        def __init__(self, health):
            self.health = health
    # And that's it!
    """