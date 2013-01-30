# encoding: UTF-8
from larv.EntityManager import EntityManager
import abc

class System(metaclass = abc.ABCMeta):
    """
    Abstract base class from which every system will inherit from.
    Systems are responsables for the logic around the game.
    Every system will need to reimplement the update method.

    Update method will be called every game loop and must implement the logic 
    of the system (aka, where the magic happens).

    When wanting to get components from entity manager, remember to call for those
    using component_class.__name__, else they will not be recognized.
    """
    def __init__(self):
        """
        Systems may not have to implement a __init__ because they may not need
        any extra info to work.
        """
        super().__init__

    @property
    def entityManager(self):
        return self.__entity_manager

    def bindToEntityManager(self, entity_manager):
        """
        Method used by the engine when the system is added to it.
        Can't be override.
        @entity_manager: instance of larv.EntityManager.EntityManager
        """
        assert isinstance(entity_manager, EntityManager)
        self.__entity_manager = entity_manager

    @abc.abstractmethod
    def update(self):
        """
        This abstract method will be called every tick of the game loop and
        will iterate over every component the system is intended to work with
        implementing game logic.
        Needs to be override.
        """
        raise NotImplementedError()