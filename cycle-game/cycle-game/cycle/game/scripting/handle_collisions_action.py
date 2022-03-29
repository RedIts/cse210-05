import constants
import random
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self.winner = ""

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_enemy_collision(cast)
            #self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_enemy_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score1 = cast.get_first_actor("player1_scores")
        score2 = cast.get_first_actor("player2_scores")
        blue = cast.get_first_actor("blue")
        green = cast.get_first_actor("green")
        blue_front = blue.get_segments()[0]
        green_front = green.get_segments()[0]
        blue_trails = blue.get_segments()[1:]
        green_trails = green.get_segments()[1:]

        number = random.randrange(0,50)

        if number == 25:
            blue.grow_tail(2)
            green.grow_tail(2)

        for green_trail in green_trails:
            if blue_front.get_position().equals(green_trail.get_position()):
                points = 1
                score2.add_points(points)
                self._is_game_over = True
                self.winner = "Green Wins!"

        for blue_trail in blue_trails:
            if green_front.get_position().equals(blue_trail.get_position()):
                points = 1
                score1.add_points(points)
                self._is_game_over = True
                self.winner = "Blue Wins!"
        
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        blue = cast.get_first_actor("blue")
        blue_front = blue.get_segments()[0]
        blue_trails = blue.get_segments()[1:]
        
        for blue_trail in blue_trails:
            if blue_front.get_position().equals(blue_trail.get_position()):
                self._is_game_over = True
        
        green = cast.get_first_actor("green")
        green_front = green.get_segments()[0]
        green_trails = green.get_segments()[1:]
        
        for green_trail in green_trails:
            if green_front.get_position().equals(green_trail.get_position()):
                self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            blue = cast.get_first_actor("blue")
            blue_trails = blue.get_segments()
            green = cast.get_first_actor("green")
            green_trails = green.get_segments()
            # food = cast.get_first_actor("foods")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text(f"Game Over! {self.winner}")
            message.set_position(position)
            cast.add_actor("messages", message)

            for blue_trail in blue_trails:
                blue_trail.set_color(constants.WHITE)
            for green_trail in green_trails:
                green_trail.set_color(constants.WHITE)
            # food.set_color(constants.WHITE)