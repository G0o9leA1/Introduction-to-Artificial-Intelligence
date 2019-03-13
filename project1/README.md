# Source Code 
For any detailed information please check with the project website
https://www.cse.wustl.edu/~wyeoh/courses/cse511a/2019spring/projects/project1.html

### Depth-first search (DFS) algorithm 
#### 

    python pacman.py -l tinyMaze -p SearchAgent  
    python pacman.py -l mediumMaze -p SearchAgent  
    python pacman.py -l bigMaze -z .5 -p SearchAgent


### Breadth-first search (BFS) algorithm 

    python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs  
    python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5

### Uniform-cost graph search algorithm 

    python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs  
    python pacman.py -l mediumDottedMaze -p StayEastSearchAgent  
    python pacman.py -l mediumScaryMaze -p StayWestSearchAgent

### A* graph search  

    python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic 

### CornersProblem search problem in searchAgents.py.

    python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem  
    python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

### Non-trivial, consistent heuristic for the CornersProblem 
 
    python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5

### FoodHeuristic with a consistent heuristic 
    python pacman.py -l trickySearch -p AStarFoodSearchAgent

### Implement  findPathToClosestDot

    python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5 
    
## Copyright:
  - If you are students of Washington University in St. Louis, you should cite properly and do not violate the academic integrity when you using this code.

  - Please contact the author through [email](mailto:Li.z@wustl.edu) if you want to use this code in other ways
