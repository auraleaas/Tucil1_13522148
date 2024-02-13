import time
from matrix import Matrix
from sequence import Sequence


def parse_file(file_name):
    with open(file_name, 'r') as file:
        buffer_size = int(file.readline().strip())
        matrix_width, matrix_height = map(int, file.readline().strip().split())

        matrix_data = []
        for _ in range(matrix_height):
            row = file.readline().strip().split()
            matrix_data.append(row)

        matrix = Matrix(matrix_width, matrix_height, matrix_data)

        num_sequences = int(file.readline().strip())

        sequences = []
        for _ in range(num_sequences):
            sequence = file.readline().strip().split()
            reward = int(file.readline().strip())
            sequences.append(Sequence(sequence, reward))

    return buffer_size, matrix, sequences

def print_matrix(matrix):
    for row in matrix.data:
        print(" ".join(row))

def print_sequences(sequences):
    for i, seq in enumerate(sequences, 1):
        print(f"Sequence {i}: {seq.sequence}, Reward: {seq.reward}")


