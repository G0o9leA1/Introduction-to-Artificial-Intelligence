# Source Code 
For any detailed information please check with the project website
https://www.cse.wustl.edu/~wyeoh/courses/cse511a/2019spring/projects/project2.html

### Reflex Agent
#### 

    python pacman.py -p ReflexAgent -l testClassic 
    python pacman.py --frameTime 0 -p ReflexAgent -k 1
    python pacman.py --frameTime 0 -p ReflexAgent -k 2
    python pacman.py -p ReflexAgent -l openClassic -n 10 -q


### Minimax Agent

    python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4 
    python pacman.py -p MinimaxAgent -l trappedClassic -a depth=3

### Alpha-Beta Agent

    python pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic

### Expectimax Agent  

    python pacman.py -p AlphaBetaAgent -l trappedClassic -a depth=3 -q -n 10
    python pacman.py -p ExpectimaxAgent -l trappedClassic -a depth=3 -q -n 10 

### CornersProblem search problem in searchAgents.py.

    python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem  
    python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

### Better Evaluation Function 
 
    python pacman.py -l smallClassic -p ExpectimaxAgent -a evalFn=better -q -n 10

    
## Copyright:
  - If you are students of Washington University in St. Louis, you should cite properly and do not violate the academic integrity when you using this code.

  - Please contact the author through [email](mailto:Li.z@wustl.edu) if you want to use the code in other ways

