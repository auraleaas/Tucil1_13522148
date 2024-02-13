
import random
import string
from matrix import Matrix
from sequence import Sequence


def generateMatrix(tokens, matrix_size):
    matrix = [['_' for _ in range(matrix_size[1])] for _ in range(matrix_size[0])]
    random_tokens = random.choices(tokens, k=matrix_size[0]*matrix_size[1])
    for i in range(len(random_tokens)):
        row = i // matrix_size[1]
        col = i % matrix_size[1]
        matrix[row][col] = random_tokens[i]
    return Matrix(matrix_size[1], matrix_size[0], matrix)

def generateSequences(tokens, buffer_size, num_sequences, max_sequence):
    sequences = []
    for _ in range(num_sequences):
        sequence = random.choices(tokens, k=random.randint(2, max_sequence))
        sequences.append(Sequence(sequence, random.randint(-50, 100)))
        # Remove buffer elements
        for _ in range(buffer_size):
            if len(sequence) > buffer_size:
                sequence.pop(0)
    return sequences

def isValidToken(token):
    # Check if token is alphanumeric and has at most 2 characters
    return token.isalnum() and len(token) <= 2



