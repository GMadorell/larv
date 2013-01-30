import larv
import pygame

class RenderComponent(larv.Component):
    def __init__(self, sprite):
        assert isinstance(sprite, pygame.Surface)
        self.sprite = sprite