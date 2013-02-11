
from larv.Component import Component
from larv.Engine import Engine
from larv.EntityFactory import EntityFactory
from larv.EntityManager import EntityManager
from larv.PriorityList import PriorityList
from larv.System import System
from larv.GroupManager import GroupManager
from larv.Entity import Entity
from larv.World import World

## Define custom exceptions
# General larv exception
class LarvException(Exception): pass

class EndEngineException(LarvException):
    """
    Exception used by the world to know when an engine will need to finish.
    This exception will need to be raised by a system when the appropiate event
    is triggered, such as ending a level.
    Usage:
        try:
            raise EndEngineException('level_success')
        except EndEngineException, (instance):
            value = instance.value 
    """
    def __init__(self, value):
        self.value = value

class EndProgramException(LarvException):
    """To be called by World when there aren't any more Engines in the stack."""
    pass 

