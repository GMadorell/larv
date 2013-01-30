# encoding: UTF-8
import pygame
### IMPORT ALL THE COMPONENTS HERE

"""
Entity factory is just a helper, it doesn't have any methods.
When implementing a game, every entity will be created from here, so it's
really only a class to put together all the building of entities for easier
reading and usage of the rest of the code.
"""

class EntityFactory:
    """
    Class used for creating entities.
    It has a createX for every entity in the game.
    Handles the creation of the entities and also assigning components to them.

    USAGE:
      When creating the entity factory for your own game, just subclass it and add
      a createX for every X entity you want in your game (remember to import
      all the components you are gonna use beforehand).
      The entity factory will be needed when you create an larv.Engine.Engine
      instance, so programmatically you will need to create it before the engine.
    """

    def __init__(self):
        """
        """
        self.__entity_manager = None

    @property
    def entityManager(self):
        return self.__entity_manager

    def bindToEntityManager(self, entity_manager):
        """
        Binds the EntityFactory to the EntityManager.
        This method is called from the Engine on creation and can't be modified.        
        @entity_manager: instance of larv.EntityManager.EntityManager
        """
        self.__entity_manager = entity_manager

    #### EXAMPLE METHOD
    """
    def createHumanPlayer(self):
        # First we load a new sprite (needed for a component)
        sprite = pygame.image.load('path_to_image.png')

        # Then we create a new entity
        new_entity = self.entityManager.createEntity()

        # Create the components for the entity (better use constants, this is hardcoded)
        new_health_comp = HealthComponent.HealthComponent(current_hp = 200,
                                                          max_hp = 200)
        new_render_comp = RenderComponent.RenderComponent(sprite)

        # Then add the components to the entity
        self.entityManager.addComponent(new_entity, new_health_comp)
        self.entityManager.addComponent(new_entity, new_render_comp)

        # Finally, return the entity
        return new_entity 
    """