"""Tennis game scoresheet application.

This module contains two different examples for a tennis game scoresheet,
and a main function to demonstrate them.

Todo:
    * Check pylint-score
    * Add a main function
    * Add a third option for the tennis game scoresheet (according to the customer's request)
    * Increase pylint-score (currently 2.77)
"""

class TennisGame1:
    """First option for the tennis game scoresheet

    Attributes:
        player1Name (str): Name for the first player
        player2Name (str): Name for the second player
        p1points (int): The first player's points
        p2points (int): The second player's points
    """

    def __init__(self, player1Name: str, player2Name: str) -> None:
        """Initialize the tennis game

        Args:
        player1Name (str): Name for the first player
        player2Name (str): Name for the second player
        """

        self.player1Name = player1Name
        self.player2Name = player2Name

        #: int: The first player's points, initial score is 0
        self.p1points = 0
        #: int: The second player's points, initial score is 0
        self.p2points = 0 

    def won_point(self, playerName: str) -> None:
        """Method to set the points for the player that scored

        Args:
            playerName (str): Name for the scoring player

        Returns:
            None
        """

        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1
    
    def score(self) -> str:
        """Method to check and return the current result for the game

        Returns:
            str: The current result and/or who won the game
        """
        result = ""
        tempScore=0
        if (self.p1points==self.p2points):
            result = {
                0 : "Love-All",
                1 : "Fifteen-All",
                2 : "Thirty-All",
            }.get(self.p1points, "Deuce")
        elif (self.p1points>=4 or self.p2points>=4):
            minusResult = self.p1points-self.p2points
            if (minusResult==1):
                result ="Advantage " + self.player1Name
            elif (minusResult ==-1):
                result ="Advantage " + self.player2Name
            elif (minusResult>=2):
                result = "Win for " + self.player1Name
            else:
                result ="Win for " + self.player2Name
        else:
            for i in range(1,3):
                if (i==1):
                    tempScore = self.p1points
                else:
                    result+="-"
                    tempScore = self.p2points
                result += {
                    0 : "Love",
                    1 : "Fifteen",
                    2 : "Thirty",
                    3 : "Forty",
                }[tempScore]
        return result


class TennisGame2:
    """Second option for the tennis game scoresheet

    Attributes:
        player1Name (str): Name for the first player
        player2Name (str): Name for the second player
        p1points (int): The first player's points
        p2points (int): The second player's points
    """

    def __init__(self, player1Name: str, player2Name: str) -> None:
        """Initialize the tennis game

        Args:
        player1Name (str): Name for the first player
        player2Name (str): Name for the second player
        """

        self.player1Name = player1Name
        self.player2Name = player2Name

        #: int: The first player's points, initial score is 0
        self.p1points = 0
        #: int: The second player's points, initial score is 0
        self.p2points = 0 
        
    def won_point(self, playerName: str) -> None:
        """Method to set the points for the player that scored

        It takes the scoring player name and calls self.P1Score() or self.P2Score()
        based on who scored the points.

        Args:
            playerName (str): Name for the scoring player

        Returns:
            None
        """
        if playerName == self.player1Name:
            self.P1Score()
        else:
            self.P2Score()
    
    def score(self) -> str:
        """Method to check and return the current result for the game

        Returns:
            str: The current result and/or who won the game
        """

        result = ""
        if (self.p1points == self.p2points and self.p1points < 3):
            if (self.p1points==0):
                result = "Love"
            if (self.p1points==1):
                result = "Fifteen"
            if (self.p1points==2):
                result = "Thirty"
            result += "-All"
        if (self.p1points==self.p2points and self.p1points>2):
            result = "Deuce"
        
        P1res = ""
        P2res = ""
        if (self.p1points > 0 and self.p2points==0):
            if (self.p1points==1):
                P1res = "Fifteen"
            if (self.p1points==2):
                P1res = "Thirty"
            if (self.p1points==3):
                P1res = "Forty"
            
            P2res = "Love"
            result = P1res + "-" + P2res
        if (self.p2points > 0 and self.p1points==0):
            if (self.p2points==1):
                P2res = "Fifteen"
            if (self.p2points==2):
                P2res = "Thirty"
            if (self.p2points==3):
                P2res = "Forty"
            
            P1res = "Love"
            result = P1res + "-" + P2res
        
        
        if (self.p1points>self.p2points and self.p1points < 4):
            if (self.p1points==2):
                P1res="Thirty"
            if (self.p1points==3):
                P1res="Forty"
            if (self.p2points==1):
                P2res="Fifteen"
            if (self.p2points==2):
                P2res="Thirty"
            result = P1res + "-" + P2res
        if (self.p2points>self.p1points and self.p2points < 4):
            if (self.p2points==2):
                P2res="Thirty"
            if (self.p2points==3):
                P2res="Forty"
            if (self.p1points==1):
                P1res="Fifteen"
            if (self.p1points==2):
                P1res="Thirty"
            result = P1res + "-" + P2res
        
        if (self.p1points > self.p2points and self.p2points >= 3):
            result = "Advantage " + self.player1Name
        
        if (self.p2points > self.p1points and self.p1points >= 3):
            result = "Advantage " + self.player2Name
        
        if (self.p1points>=4 and self.p2points>=0 and (self.p1points-self.p2points)>=2):
            result = "Win for " + self.player1Name
        if (self.p2points>=4 and self.p1points>=0 and (self.p2points-self.p1points)>=2):
            result = "Win for " + self.player2Name
        return result
    
    def SetP1Score(self, number: int) -> None:
        """Sets the score for the first player

        Args:
            number (int): The number to iterate to set the score
        """
        for i in range(number):
            self.P1Score()
    
    def SetP2Score(self, number: int) -> None:
        """Sets the score for the second player

        Args:
            number (int): The number to iterate to set the score
        """
        for i in range(number):
            self.P2Score()
    
    def P1Score(self) -> None:
        """Increments the first players score with 1"""
        self.p1points +=1
    
    
    def P2Score(self) -> None:
        """Increments the second players score with 1"""
        self.p2points +=1
        

def main() -> None:
    """Main function. 

    Only used to demonstrate the application for now.
    Creates two tennis games and runs their methods in while-loop until a player wins

    Returns:
        None
    """
    game1 = TennisGame1('Roger Federer', 'Rafael Nadal')
    game2 = TennisGame2('Serena Williams', 'Venus Williams')

    print(f'Game 1 between: {game1.player1Name} and {game1.player2Name}')
    while True:
        valid_input = False  # To check if it was an invalid input
        who_scored = input('Enter the name on the player that scored:\n>> ')

        match who_scored.lower():
            case 'roger federer' | 'roger' | 'federer':
                game1.won_point('Roger Federer')
                valid_input = True
            case 'rafael nadal' | 'rafael' | 'nadal':
                game1.won_point('Rafael Nadal')
                valid_input = True
            case _:
                print(f'Invalid player name!\n')

        if valid_input:
            print(game1.score() + '\n')
            if game1.score().startswith('Win for'):
                break
    
    print(f'Game 2 between: {game2.player1Name} and {game2.player2Name}')
    while True:
        valid_input = False  # To check if it was an invalid input
        who_scored = input('Enter the name on the player that scored:\n>> ')

        match who_scored.lower():
            case 'serena williams' | 'serena':
                game2.won_point('Serena Williams')
                valid_input = True
            case 'venus williams' | 'venus':
                game2.won_point('Venus Williams')
                valid_input = True
            case 'williams':
                print('Their both name are williams!\n')
            case _:
                print(f'Invalid player name!\n')

        if valid_input:
            print(game2.score() + '\n')
            if game2.score().startswith('Win for'):
                break


if __name__ == '__main__':
    main()
