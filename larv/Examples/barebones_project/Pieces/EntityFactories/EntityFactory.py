import pygame

import larv
from Pieces.Components import *

class EntityFactory(larv.EntityFactory):
    """
    Used for creating entities.
    """
    def createHero(self):
        sprite = pygame.image.load('Images/placeholder.png')

        new_entity = self.entityManager.createEntity()
        new_position_component = PositionComponent(50,50)
        new_render_component = RenderComponent(sprite)

        self.entityManager.addComponent(new_entity, new_position_component)
        self.entityManager.addComponent(new_entity, new_render_component)

        return new_entity