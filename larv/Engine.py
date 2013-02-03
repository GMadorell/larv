# encoding: UTF-8

from larv.EntityManager import EntityManager
from larv.EntityFactory import EntityFactory
from larv.PriorityList import PriorityList
from larv.System import System
from larv.GroupManager import GroupManager

class Engine:
    """
    The engine is the glue that puts everything together.
    It holds:
        - an instance of a systems list (PriorityList): self.systems
        - an instance of an entity manager:  self.entity_manager
        - an instance of a group manager:    self.group_manager
        - an instance of an entity_factory:  self.entity_factory

    When updating the game, one should only do a Engine.update()
    call, as the Engine will be responsable for updating every
    single system in the right order (given that we insert
    the systems in the right priority).
    """
    def __init__(self, entity_factory):
        self.systems = PriorityList()
        self.entity_manager = EntityManager()
        self.group_manager = GroupManager(self)

        # bind Managers to factory
        assert isinstance(entity_factory, EntityFactory)
        entity_factory.bindToEntityManager(self.entity_manager)
        entity_factory.bindToGroupManager(self.group_manager)
        self.entity_factory = entity_factory

    def addSystem(self, system, priority):
        """
        Adds the given system to the priority list using the given priority and
        also binds the managers and the factory to it.
        Priority works as the lower priority value will update first.
        @system: instance of larv.System.System
        @priority: value used for deciding systems updating order.
        """
        assert isinstance(system, System)
        system.bindToEntityManager(self.entity_manager)
        system.bindToGroupManager(self.group_manager)
        system.bindToEntityFactory(self.entity_factory)
        self.systems.add(system, priority)

    def changeSystemPriority(self, system, priority):
        """
        Changes the given system's priority when updating.
        @system: larv.System.System instance.
        @priority: value used for deciding systems updating order.
        """
        assert system in self.systems.list        
        assert isinstance(system, System)
        self.systems.change(system, priority)

    def removeSystem(self, system):
        """Removes the given system of the priority list."""        
        assert isinstance(system, System)
        return self.systems.remove(system)

    def update(self):
        """Iterates over every System and calls their update method."""
        for system in self.systems:
            system.update()

    def delete(self):
        """Empties the Engine, setting every container to None."""
        self.systems = None
        self.entity_manager = None
        self.entity_factory = None
