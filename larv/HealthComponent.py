
"""
Component which holds data about health.
"""

class HealthComponent:
    """docstring for HealthComponent"""
    def __init__(self, current_hp, max_hp):
        """
        Constructor.
        """
        self.current_hp = current_hp
        self.max_hp = max_hp
        self.alive = True
