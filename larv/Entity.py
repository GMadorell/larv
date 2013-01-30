# encoding: UTF-8

class Entity:
    """
    An entity is just an ID, which will be assigned some components.
    Components hold the data and systems are the responsables of the logic
    behind it.
    """
    def __init__(self, id):
        """
        Constructor.
        We should pass a unique id everytime we create a new entity.
        """
        self.__id = id

    @property
    def id(self):
        """Read only property for the id private variable."""
        return self.__id
