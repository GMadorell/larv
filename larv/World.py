import larv



"""
UNTESTED - prototype class.
"""

class World:
    """
    The world defines a way to use multiple engines in the same program.
    That might be useful when you want to have, for example, a title screen
    which is an introduction to the game and then an engine for the game itself.
    On every update call, updates the last pushed mode.

    It's not a bad idea to define a global World instance on your games, as
    using many different worlds will rarely be needed.
    """
    def __init__(self):
        self.engine_stack = []

    def push(self, engine):
        """
        Adds the given engine to the engine stack, giving it instant priority.
        @engine: larv.Engine instance.
        """
        assert isinstance(engine, larv.Engine)
        self.engine_stack.append(engine)

    def pop(self):
        """
        Removes the current engine from the stack and returns it.
        Raises EndProgramException if the stack is empty.
        """
        if len(self.engine_stack) == 0:
            raise EndProgramException()
        return self.engine_stack.pop()

    def update(self):
        """
        Activates (updates) the engine on top of the stack.
        """
        if len(self.engine_stack) == 0:
            raise EndProgramException()

        engine = self.engine_stack[-1]
        engine.update()
