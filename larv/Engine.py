# encoding: UTF-8

from larv.EntityManager import EntityManager
from larv.EntityFactory import EntityFactory
from larv.PriorityList import PriorityList
from larv.System import System

class Engine:
    """
    The engine is the glue that puts everything together.
    It holds an instance of a systems list (priority list),
    an instance of an entity_manager and an instance of 
    a entity factory.

    When updating, one should only do a Engine.update() call,
    as the Engine will be responsable for updating every
    single system in the right order (given that we insert
    the systems with the right priority).
    """
    def __init__(self, entity_factory):
        self.systems = PriorityList()
        self.entity_manager = EntityManager()

        # not sure if putting entity factory here is a good idea
        assert isinstance(entity_factory, EntityFactory)
        entity_factory.bindToEntityManager(self.entity_manager)
        self.entity_factory = entity_factory

    def addSystem(self, system, priority):
        """
        Adds the given system to the priority list using the given priority and
        also binds the entity_manager to it.
        Priority works as the lower priority value will update first.
        @system: instance of larv.System.System
        """
        assert isinstance(system, System)
        system.bindToEntityManager(self.entity_manager)
        self.systems.add(system, priority)

    def removeSystem(self, system):
        """Removes the given system of the priority list"""
        self.systems.remove(system)

    def update(self):
        """Iterates over every System and calls their update method."""
        for system in self.systems:
            system.update()

    def delete(self):
        """Empties the Engine, setting every container to None"""
        self.systems = None
        self.entity_manager = None
        self.entity_factory = None
