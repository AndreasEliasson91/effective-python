"""Tennis game scoresheet application.

This module contains the new and improved tennis game scoresheet,
as per the customer's request.

Attributes:
    SCORE (dict): const dictionary to bind the player points to its tennis terminology counterpart

"""

from dataclasses import dataclass

SCORE = {
    0: "Love",
    1: "Fifteen",
    2: "Thirty",
    3: "Forty"
}


@dataclass
class Player:
    """Basic dataclass to keep track of the player information and score.

    Only contains getters, setters for attributes and an update_score method.

    Attributes:
        _name (str): Player name
        points (int): Player points, 0 by default
    """
    _name: str = None
    points: int = 0

    @property
    def name(self) -> str:
        """Getter for private property _name.
        
        Returns:
            str: The players name
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """Setter for private property _name.

        Args:
            name (str): The players name
        """
        self._name = name

    def get_points(self) -> int:
        """Getter for points

        Returns:
            int: The players points
        """
        return self.points

    def update_points(self) -> None:
        """Method to update the player's points"""
        self.points += 1


class TennisGame:
    """Main class for the tennis game.

    Attributes:
        player_one (Player):  Player object, representing player one
        player_two (Player):  Player object, representing player two
    """

    def __init__(self, player_one: str, player_two: str) -> None:
        """Initialize the tennis game
        
        Args:
            player_one (str): Name of the first player
            player_two (str): Name of the second player
        """

        self.player_one = Player()
        self.player_two = Player()

        self.player_one.name = player_one
        self.player_two.name = player_two

        #: List of str: Valid name inputs from user
        self._valid_inputs = None
        self.valid_inputs = [
            self.player_one.name.lower(),
            self.player_one.name.split()[0].lower(),  # First players first name
            self.player_one.name.split()[1].lower(),  # First players last name
            self.player_two.name.lower(),
            self.player_two.name.split()[0].lower(),  # Second players first name
            self.player_two.name.split()[1].lower(),  # Second players last name
        ]

    @property
    def valid_inputs(self) -> list[str]:
        """Getter for valid input list

        Returns:
            list of str objects: List of valid name inputs
        """
        return self._valid_inputs

    @valid_inputs.setter
    def valid_inputs(self, names: list[str]) -> None:
        """Setter for valid input list

        If the name already exists in the list, it removes that name.
        This is to prevent the application to give the first player a point
        if, for example, both player share their first or last name.

        Args:
            names (list of str objects): List of the players full, first and last name
        """
        valid = []
        for name in names:
            if name not in valid:
                valid.append(name)
            else:
                valid.remove(name)

        self._valid_inputs = valid

    def player_scored(self, name: str) -> None:
        """Method to set the points for player that scored

        The input name is compared to the players name in a match-case scenario,
        to see if it's a valid input
        
        Args:
            name (str): The name of the scoring player

        Returns:
            None
        """
        match name:
            case self.player_one.name:
                self.player_one.update_points()
            case self.player_two.name:
                self.player_two.update_points()
            case _:
                pass

    def result(self) -> str:
        """Print method to see the current result.
        
        Returns:
            str: String with the current result
        """
        # Early return if 'deuce'
        if self.player_one.get_points() == 3 and self.player_two.get_points() == 3:
            return 'Deuce'

        # Return if it's a tie game
        if self.player_one.get_points() == self.player_two.get_points():
            return f'{SCORE[self.player_one.get_points()]}-All'

        # Return winner
        if self.player_one.get_points() == 4 and self.player_one.get_points() > self.player_two.get_points():
            return f'{self.player_one.name} wins!'
        if self.player_two.get_points() == 4 and self.player_one.get_points() < self.player_two.get_points():
            return f'{self.player_two.name} wins!'

        return f'{SCORE[self.player_one.get_points()]}-{SCORE[self.player_two.get_points()]}'

    def deuce(self) -> None:
        """Method to set the winner after a deuce scenario

        It contains two temporary variables to store the players scores,
        and they either store 0 ('forty'), 1 ('advantage') or 2 ('win').
        The while loop runs until a player gets 2.

        Returns:
            None
        """
        temp_points_p1, temp_points_p2 = 0, 0

        while temp_points_p1 < 2 and temp_points_p2 < 2:
            scorer = self.get_who_scored()

            if isinstance(scorer, int):
                # If the index is on the lower half of the list, player one scores
                if scorer < (len(self.valid_inputs) / 2):
                    temp_points_p1 += 1
                else:
                    temp_points_p2 += 1

                # Check and print if a player is in advantage or if it's a tie
                if temp_points_p1 == 1 and temp_points_p2 == 1:  # Reset temp points if the deuce goes back to a tie
                    temp_points_p1, temp_points_p2 = 0, 0
                    print('Deuce')
                elif temp_points_p2 < temp_points_p1 != 2:
                    print(f'Advantage {self.player_one.name}')
                elif temp_points_p1 < temp_points_p2 != 2:
                    print(f'Advantage {self.player_two.name}')

            else:
                print(scorer)

        if temp_points_p1 == 2:
            self.player_scored(self.player_one.name)
        else:
            self.player_scored(self.player_two.name)

        del temp_points_p1, temp_points_p2

    def run(self) -> None:
        """Method to start and run the application.

        Runs while self.result() not return a winning result

        Returns:
            None
        """
        while ' wins!' not in self.result():
            if self.result() == 'Deuce':
                self.deuce()
            else:
                scorer = self.get_who_scored()

                if isinstance(scorer, int):
                    # If the index is on the lower half of the valid inputs list, player one scores
                    if scorer < (len(self.valid_inputs) / 2):
                        self.player_scored(self.player_one.name)
                    else:
                        self.player_scored(self.player_two.name)
                else:
                    print(scorer)
                    continue

            print(self.result())

    def get_who_scored(self) -> int or str:
        """Method to see if the input is valid or not

        Returns:
            int or str: The index of the scoring player or invalid input message
        """
        who_scored = input('Enter the name on the player that scored:\n>> ')

        # Get the input from valid_inputs list
        if who_scored.lower() in self.valid_inputs:
            return self.valid_inputs.index(who_scored.lower())

        return 'Invalid name input.\n'


if __name__ == '__main__':
    game = TennisGame('Serena Williams', 'Venus Williams')
    game.run()
