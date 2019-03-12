# multiAgents.py
# --------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more infos, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from util import manhattanDistance
from game import Directions
import random, util

from game import Agent


class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()

        "*** YOUR CODE HERE ***"
        foodList=newFood.asList()
        if len(foodList) == 0:
            score = 1
        else:
            distanceList = map(lambda food: manhattanDistance(food, newPos), foodList)
            minDistance = reduce(lambda x, y: x if x < y else y, distanceList)
            score = 1.0/(minDistance*(len(foodList)))
        for ghostPos in successorGameState.getGhostPositions():
            if manhattanDistance(newPos, ghostPos) <= 1:
                score = 0
        return score+successorGameState.getScore()


def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getLegalActionsNoStop(self, gameState, agentIndex=0):
        actions = gameState.getLegalActions(agentIndex)
        if 'Stop' in actions:
            actions.remove('Stop')
        return actions

    def maxFn(self, gameState, index):
        if gameState.isLose() or gameState.isWin() or self.depth*gameState.getNumAgents() == index:
            return self.evaluationFunction(gameState)
        return max(map(lambda action: self.minFn(gameState.generatePacmanSuccessor(action), index + 1),
                       self.getLegalActionsNoStop(gameState)))

    def minFn(self, gameState, index):
        if gameState.isLose() or gameState.isWin() or self.depth*gameState.getNumAgents() == index:
            return self.evaluationFunction(gameState)
        if (index+1) % gameState.getNumAgents() != 0:
            return min(map(
                lambda action: self.minFn(gameState.generateSuccessor(index % gameState.getNumAgents(), action),
                                          index + 1),
                self.getLegalActionsNoStop(gameState, index % gameState.getNumAgents())))
        return min(map(
            lambda action: self.maxFn(gameState.generateSuccessor(index % gameState.getNumAgents(), action), index + 1),
            self.getLegalActionsNoStop(gameState, index % gameState.getNumAgents())))

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          Directions.STOP:
            The stop direction, which is always legal

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        actions = self.getLegalActionsNoStop(gameState)
        scores = {action: self.minFn(gameState.generatePacmanSuccessor(action), 1) for action in actions}
        return max(scores, key=scores.get)


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """
    def getLegalActionsNoStop(self, gameState, agentIndex=0):
        actions = gameState.getLegalActions(agentIndex)
        if 'Stop' in actions:
            actions.remove('Stop')
        return actions

    def maxFn(self, gameState, index, alpha, beta):
        if gameState.isLose() or gameState.isWin() or self.depth*gameState.getNumAgents() == index:
            return self.evaluationFunction(gameState)
        import sys
        value = -sys.maxint
        for action in self.getLegalActionsNoStop(gameState):
            value = max(value, self.minFn(gameState.generatePacmanSuccessor(action), index + 1, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                return value
        return value

    def minFn(self, gameState, index, alpha, beta):
        if gameState.isLose() or gameState.isWin() or self.depth*gameState.getNumAgents() == index:
            return self.evaluationFunction(gameState)
        import sys
        value = sys.maxint
        if (index + 1) % gameState.getNumAgents() != 0:
            for action in self.getLegalActionsNoStop(gameState, index % gameState.getNumAgents()):
                value = min(value,
                            self.minFn(gameState.generateSuccessor(index % gameState.getNumAgents(), action), index + 1,
                                       alpha, beta))
                beta = min(beta, value)
                if alpha >= beta:
                    return value
            return value

        for action in self.getLegalActionsNoStop(gameState, index % gameState.getNumAgents()):
            value = min(value,
                        self.maxFn(gameState.generateSuccessor(index % gameState.getNumAgents(), action), index + 1,
                                   alpha, beta))
            beta = min(beta, value)
            if alpha >= beta:
                return value
        return value

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        import sys
        actions = self.getLegalActionsNoStop(gameState)
        alpha = -sys.maxint
        beta = sys.maxint
        scores = {action: self.minFn(gameState.generatePacmanSuccessor(action), 1, alpha, beta) for action in actions}
        return max(scores, key=scores.get)



class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getLegalActionsNoStop(self, gameState, agentIndex=0):
        actions = gameState.getLegalActions(agentIndex)
        if 'Stop' in actions:
            actions.remove('Stop')
        return actions

    def maxFn(self, gameState, index):
        if gameState.isLose() or gameState.isWin() or self.depth*gameState.getNumAgents() == index:
            return self.evaluationFunction(gameState)
        return max(map(lambda action: self.expFn(gameState.generatePacmanSuccessor(action), index + 1),
                       self.getLegalActionsNoStop(gameState)))

    def expFn(self, gameState, index):
        if gameState.isLose() or gameState.isWin() or self.depth*gameState.getNumAgents() == index:
            return self.evaluationFunction(gameState)
        actions=self.getLegalActionsNoStop(gameState, index % gameState.getNumAgents())
        if (index+1) % gameState.getNumAgents() != 0:
            return reduce(lambda x, y: x+y, map(
                lambda action: self.expFn(gameState.generateSuccessor(index % gameState.getNumAgents(), action),
                                          index + 1), actions))/len(actions)

        return reduce(lambda x, y: x+y, map(
            lambda action: self.maxFn(gameState.generateSuccessor(index % gameState.getNumAgents(), action), index + 1),
            actions))/len(actions)

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        actions = self.getLegalActionsNoStop(gameState)
        scores = {action: self.expFn(gameState.generatePacmanSuccessor(action), 1) for action in actions}
        return max(scores, key=scores.get)

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: a. value of least food distance: value up score down
                   b. value of least pellet distance: value up score down
                   c. value of ghost distance: if scaredTime>ghostDistance value up score up highly
                                               else value up score up
                   d. value of left food number: value up score down
                   e. value of the current state: value up score up
    """
    "*** YOUR CODE HERE ***"
    import sys
    gameState = currentGameState
    pos = gameState.getPacmanPosition()
    food = gameState.getFood()
    foodList = food.asList()
    caps = gameState.getCapsules()
    ghostStates = gameState.getGhostStates()
    # distance to the food

    if len(foodList) == 0:
        foodDistanceScore = sys.maxint
    else:
        distanceList = map(lambda food: manhattanDistance(food, pos), foodList)
        minDistance = reduce(lambda x, y: x if x < y else y, distanceList)
        foodDistanceScore = 1.0 / minDistance

    # distance to the pellets

    if len(caps)==0:
        capDistanceScore=0
    else:
        distanceList = map(lambda cap: manhattanDistance(cap, pos), caps)
        minDistance = reduce(lambda x, y: x if x < y else y, distanceList)
        capDistanceScore = 1.0 / minDistance

    # distance to the ghost
    ghostScore=0
    for ghost in ghostStates:
        if ghost.scaredTimer>0:
            if manhattanDistance(pos,ghost.getPosition())<=ghost.scaredTimer:
                ghostScore+=+20
        else:
            ghostScore+=manhattanDistance(pos,ghost.getPosition())

    # left foods
    if len(foodList) == 0:
        foodNumScore=sys.maxint
    else:
        foodNumScore = 1.0/len(foodList)

    if gameState.isLose():
        return -sys.maxint
    return foodDistanceScore+40*capDistanceScore+2*ghostScore+foodNumScore+gameState.getScore()


# Abbreviation
better = betterEvaluationFunction

class ContestAgent(MultiAgentSearchAgent):
    """d
      Your agent for the mini-contests
    """
    def __init__(self, evalFn = 'better', depth = '4'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

    def getLegalActionsNoStop(self, gameState, agentIndex=0):
        actions = gameState.getLegalActions(agentIndex)
        if 'Stop' in actions:
            actions.remove('Stop')
        return actions

    def maxFn(self, gameState, index, alpha, beta):
        if gameState.isLose() or gameState.isWin() or self.depth*gameState.getNumAgents() == index:
            return self.evaluationFunction(gameState)
        import sys
        value = -sys.maxint
        for action in self.getLegalActionsNoStop(gameState):
            value = max(value, self.minFn(gameState.generatePacmanSuccessor(action), index + 1, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                return value
        return value

    def minFn(self, gameState, index, alpha, beta):
        if gameState.isLose() or gameState.isWin() or self.depth*gameState.getNumAgents() == index:
            return self.evaluationFunction(gameState)
        import sys
        value = sys.maxint
        if (index + 1) % gameState.getNumAgents() != 0:
            for action in self.getLegalActionsNoStop(gameState, index % gameState.getNumAgents()):
                value = min(value,
                            self.minFn(gameState.generateSuccessor(index % gameState.getNumAgents(), action), index + 1,
                                       alpha, beta))
                beta = min(beta, value)
                if alpha >= beta:
                    return value
            return value

        for action in self.getLegalActionsNoStop(gameState, index % gameState.getNumAgents()):
            value = min(value,
                        self.maxFn(gameState.generateSuccessor(index % gameState.getNumAgents(), action), index + 1,
                                   alpha, beta))
            beta = min(beta, value)
            if alpha >= beta:
                return value
        return value

    def getAction(self, gameState):
        """
          Returns an action.  You can use any method you want and search to any depth you want.
          Just remember that the mini-contest is timed, so you have to trade off speed and computation.

          Ghosts don't behave randomly anymore, but they aren't perfect either -- they'll usually
          just make a beeline straight towards Pacman (or away from him if they're scared!)
        """
        import sys
        actions = self.getLegalActionsNoStop(gameState)
        alpha = -sys.maxint
        beta = sys.maxint
        scores = {action: self.minFn(gameState.generatePacmanSuccessor(action), 1, alpha, beta) for action in actions}
        return max(scores, key=scores.get)
