# game_tic-tac-toe
Tic-Tac-Toe game constructed in python by Mitch Miller. Can be played by two human players, but also features a **single-player game mode in which the computer plays against you**. The computer player is programmed to derive the best possible position to play on each turn, simultaneously considering each position for offensive and defensive – then selects the position which provides the ideal compromise between disrupting your strategy while advancing its own.


### Computer Decision Logic
The computer player's decision tree deduces the best move by the following logic: 

1. Each possible winning combination is compared with the current state of the board;
2. potential moves are separated into defensive and offensive opportunities; 
3. offensive and defensive opportunities are cross-examined for mutual tactical overlap; and 
4. a scoring system is applied to deduce the most preferable move based on the above factors.

- The _scoring system_ allows the computer to decide between the most strategically efficacious moves _versus_ the most urgent. 

### Difficulty

**To reduce difficulty for the human** player,
- there are two are 2:1 odds of the human player receiving the first turn; and
- the computer has 1:2 odds of selecting the _second-best_ move rather than best.

