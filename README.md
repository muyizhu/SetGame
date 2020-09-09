How To Run The Program:

1.  Download the zipped SETGAME file and Unzip the file 
2.  open command line and running command “pip install Pillow”， which install the dependency pakage called Pillow
3.  in command line，running “pip install pygame”. which installed the dependency called pygame
4.  open the unziped SetGame folder with your IDE then run ‘SetGame.py’ file or in command line type “Python ”,then drag the "SetGame.py" after "Python "

Game Rules:

Each of the cardsThere have different characteristics which are Colors (red, green, blue and yellow), Numbers (1, 2, 3), Shapes (circle, square, triangle) and Fills ( clear, shaded, solid ). You need form sets by using card on desk and deck until all the cards are used or there is no more set can be formed. The rule of forming a set is selecting exact three cards from the available cards on the board and the each of characteristics of the cards should be either the same or different. For example, set 1 can be {blue clear circle1, blue clear circle2, blue clear circle3} which have same color, shape and fill but different in number. Or set 2 which is {red solid square1, blue sgaded circle2, yellow clear triangle3} where none of their characteristics are the same.

Game Function:

Restart Game: Start a new game. Reshuffle the deck and deal cards to board. Clear hitorical sets and timer

Replace Card: When you can't form a set by using cards on board, you can right click card to replace it or you can use the button Replace Cards to replace all the cards on board.               The replaced card will go back to beck. IMPORTANT: Replace Card funtion can be used only when there still has cards left in deck. If the number of left cards is 0,                 replace function will not work.  

Fill Desk: When desk has empty positions and there still has cards left in deck, you can click Fill Desk botton to fill the empty postions.

Submit: Check the three cards you chose if they can make a set. If they make a set, they will be removed from board.

Timer: Record how fast you can finish the game

Track Message: Show how many cards you have finished and how many cards still left in deck  
