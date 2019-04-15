# Source Code 
For any detailed information please check with the project website
https://www.cse.wustl.edu/~wyeoh/courses/cse511a/2019spring/projects/project3.html

### Value iteration
#### 

    python gridworld.py -a value -i 100 -k 10 
    python gridworld.py -a value -i 5


### Value iteration: parameter tuning #1

    python gridworld.py -a value -i 100 -g BridgeGrid --discount 0.9 --noise 0.2

### Value iteration: parameter tuning #2

    python gridworld.py -a value -i 100 -g DiscountGrid --discount 0.9 --noise 0.2 --livingReward 0.0

### Q-learning  

    python gridworld.py -a q -k 5 -m 

### Q-learning: epsilon-greedy

    python gridworld.py -a q -k 100  

### Q-learning: parameter tuning
 
    python gridworld.py -a q -k 50 -n 0 -g BridgeGrid -e 1

### Crawler
    
    python crawler.py
    
### Q-learning: training 
    
    python pacman.py -p PacmanQAgent -x 2000 -n 2010 -l smallGrid
    python pacman.py -p PacmanQAgent -n 10 -l smallGrid -a numTraining=10
    
### Approximate Q-learning

    python pacman.py -p ApproximateQAgent -x 2000 -n 2010 -l smallGrid
    python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 60 -l mediumGrid
    python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 60 -l mediumClassic
    python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 150 -l mediumGrid -q -f
    
## Copyright:
  - If you are students of Washington University in St. Louis, you should cite properly and do not violate the academic integrity when you using this code.

  - Please contact the author through [email](mailto:Li.z@wustl.edu) if you want to use the code in other ways

