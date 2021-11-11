
"""
@Author: Shivam Mathur
@Date: 2021-11-10
@Last Modified by: Shivam Mathur
@Last Modified time: 2021-11-10
@Title : Write a Program to play a Cross Game or Tic-Tac-Toe Game. Player 1
is the Computer and the Player 2 is the user. Player 1 take Random Cell that is
the Column and Row
"""

import random

class TicTacToe:
    userPosition = []
    computerPosition = []

    def createBoard(self):
        """ 
         Description:Creating game board
        """
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
    def printBoard(self):
        """
           Description:Display board
          
        """
        for row in range(len(self.board)):
            print("\n______")
            for column in range(len(self.board)):
                print(str(self.board[row][column]), end='|')

    def userTurn(self):
        """
        Description: search for new emty position
        Return: return new user position
        """
        try:
            userPosition = int(input("\n Enter your placement (1-9): "))
        except Exception as e:
            print(e)
            return self.userTurn()
        while userPosition in self.userPosition or userPosition in self.computerPosition:#search for empty position
            print("Position Allready filled ! Enter another position")
            return self.userTurn()
        if userPosition < 1 or userPosition > 9:
            print("plz enter position should be between 1-9 ")
            return self.userTurn()
        return userPosition
    
    def computerTurn(self):
        """
        Description: search for new emty position
        Return: return new computer position
        """
        try:
            compPosition = random.randint(1, 9)
        except Exception as e:
            print(e)
            return self.computerTurn()
        while compPosition in self.userPosition or compPosition in self.computerPosition:#search for empty position
            print("Position Allready filled ! Enter another position")
            return self.computerTurn()
        if compPosition < 1 or compPosition > 9:
            print("plz Enter position should be between 1-9")
            return self.computerTurn()
        return compPosition

    def placePosition(self, player, pos):
        """
        Description:for position inserting symbols in board array
        """
        symbol = ' '
        if player == 'user':
            symbol = 'X'
            self.userPosition.append(pos)
        elif player == 'comp':
            symbol = 'O'
            self.computerPosition.append(pos)

        self.board[(pos - 1) // 3][(pos - 1) % 3] = symbol

    def findWinner(self):
        """
        Description:checking who is win the game
        Return: returns winning message
        """
        win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for condition in win:
            if set(condition).intersection(set(self.userPosition)) == set(condition):
                return "Congratulation you won!"
            elif set(condition).intersection(set(self.computerPosition)) == set(condition):
                return "Computer won!"
            elif len(self.computerPosition)+len(self.userPosition) == 9:
                return "No empty Space to move"
        return ""

if __name__ == "__main__":

    object1 = TicTacToe()
    object1.createBoard()
    object1.printBoard()
    while True:
        userpos = object1.userTurn()
        object1.placePosition('user', userpos)
        winner = object1.findWinner()
        if len(winner) > 0:
            print(winner)
            object1.printBoard()
            break
        print('\n')
        object1.printBoard()
        comppos = object1.computerTurn()
        object1.placePosition('comp', comppos)
        winner = object1.findWinner()
        if len(winner) > 0:
            print(winner)
            object1.printBoard()
            break
        print('\n')
        object1.printBoard()