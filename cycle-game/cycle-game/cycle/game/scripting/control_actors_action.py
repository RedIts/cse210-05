import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service1 = keyboard_service
        self._keyboard_service2 = keyboard_service
        self._direction1 = Point(constants.CELL_SIZE, 0)
        self._direction2 = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left 1
        if self._keyboard_service1.is_key_down('a'):
            self._direction1 = Point(-constants.CELL_SIZE, 0)
        
        # right 1
        if self._keyboard_service1.is_key_down('d'):
            self._direction1 = Point(constants.CELL_SIZE, 0)
        
        # up 1
        if self._keyboard_service1.is_key_down('w'):
            self._direction1 = Point(0, -constants.CELL_SIZE)
        
        # down 1
        if self._keyboard_service1.is_key_down('s'):
            self._direction1 = Point(0, constants.CELL_SIZE)
        
        # left 2
        if self._keyboard_service2.is_key_down('j'):
            self._direction2 = Point(-constants.CELL_SIZE, 0)
        
        # right 2
        if self._keyboard_service2.is_key_down('l'):
            self._direction2 = Point(constants.CELL_SIZE, 0)
        
        # up 2
        if self._keyboard_service2.is_key_down('i'):
            self._direction2 = Point(0, -constants.CELL_SIZE)
        
        # down 2
        if self._keyboard_service2.is_key_down('k'):
            self._direction2 = Point(0, constants.CELL_SIZE)

        red = cast.get_first_actor("red")
        red.turn_head(self._direction1)

        green = cast.get_first_actor("green")
        green.turn_head(self._direction2)