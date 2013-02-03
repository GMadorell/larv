# encoding: UTF-8
from larv.EntityManager import EntityManager
from larv.GroupManager import GroupManager
from larv.EntityFactory import EntityFactory
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
    def entity_manager(self):
        """Returns the entity manager assigned to the system."""
        return self.__entity_manager

    @property
    def group_manager(self):
        """Returns the group manager assignet to the system."""
        return self.__group_manager

    @property
    def entity_manager(self):
        """Returns the entity manager assigned to the system."""
        return self.__entity_manager

    def bindToEntityManager(self, entity_manager):
        """
        Method used by the engine when the system is added to it.
        Can't be override.
        @entity_manager: instance of larv.EntityManager.EntityManager
        """
        assert isinstance(entity_manager, EntityManager)
        self.__entity_manager = entity_manager

    def bindToGroupManager(self, group_manager):
        """
        Method used by the engine when the system is added to it.
        Can't be override.
        @group_manager: instance of larv.GroupManager.GroupManager
        """
        assert isinstance(group_manager, GroupManager)
        self.__group_manager = group_manager

    def bindToEntityFactory(self, entity_factory):
        """
        Method used by the engine when the system is added to it.
        Can't be override.
        @entity_factory: instance of larv.EntityFactory.EntityFactory
        """
        assert isinstance(entity_factory, EntityFactory)
        self.__entity_factory = entity_factory

    @abc.abstractmethod
    def update(self):
        """
        This abstract method will be called every tick of the game loop and
        will iterate over every component the system is intended to work with,
        implementing game logic.
        Needs to be override.
        """
        raise NotImplementedError()