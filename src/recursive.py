from matrix import Matrix
from sequence import Sequence
from tokenin import TokenInput


def isSequenceEqual(tokens, sequence):
    # Check if a sequence is equal to a list of tokens
    if len(sequence) > len(tokens):
        return False
    else:
        for i in range(len(tokens) - len(sequence) + 1):
            if tokens[i:i+len(sequence)] == sequence:
                return True
        return False


def makeListToken(tokens): 
    # Create a list of tokens from a list of TokenInput
    list_token = []
    for token in tokens:
        list_token.append(token.token)
    return list_token



def calculateReward(sequences, tokens):
    # Calculate the reward of a sequence
    reward = 0
    
    for seq in sequences:
        if isSequenceEqual(makeListToken(tokens), seq.sequence):  
            reward += seq.reward
    return reward


def findOptimalSequence(solutions, sequences): 
    # Find the optimal sequence
    max_reward = 0
    optimal_sequence = []
    for solution in solutions:
        reward = calculateReward(sequences, solution)
        if reward > max_reward:
            max_reward = reward
            optimal_sequence = solution
    return max_reward, optimal_sequence
        
        
        
def passedToken(row, col, stack):  
    # Detect whether a token has been passed or not
    if stack == []:
        return False
    else:
        for token in stack:
            if (token.x == col) and (token.y == row):
                return True

        
        
def searchSequence(matrix : Matrix, stack, row, col, buffer, solution, check_horizontal):
    # Recursive function to search for a sequence
    if buffer == 1:
        solution.append(list(stack))
    else:
        if check_horizontal:
            # Search for horizontal sequence
            for i in range (matrix.width):
                if not passedToken(row, i, stack):
                    stack.append(TokenInput(matrix.data[row][i], i, row))
                    searchSequence(matrix, stack, row, i, buffer-1, solution, False)
                    stack.pop()
        else:
            # Search for vertical sequence
            for i in range (matrix.height):
                if not passedToken(i, col, stack):
                    stack.append(TokenInput(matrix.data[i][col], col, i))
                    searchSequence(matrix, stack, i, col, buffer-1, solution, True)
                    stack.pop()


















                
    