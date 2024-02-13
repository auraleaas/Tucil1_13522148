import os
import time
from readCLI import generateMatrix, generateSequences, isValidToken
from recursive import searchSequence, findOptimalSequence, calculateReward
from readFile import parse_file, print_matrix, print_sequences


# MENU
def get_menu_option():
    menu_options = ('1', '2')
    
    while True:
        print()
        print()
        print("                                      Welcome to                                                   ")
        print()
        print("________                         ______       ________             _____                  ______   ")
        print("___  __ )_________________ _________  /_      ___  __ \______________  /_____________________  /   ")
        print("__  __  |_  ___/  _ \  __ `/  ___/_  __ \     __  /_/ /_  ___/  __ \  __/  __ \  ___/  __ \_  /    ")
        print("_  /_/ /_  /   /  __/ /_/ // /__ _  / / /     _  ____/_  /   / /_/ / /_ / /_/ / /__ / /_/ /  /     ")
        print("/_____/ /_/    \___/\__,_/ \___/ /_/ /_/      /_/     /_/    \____/\__/ \____/\___/ \____//_/      ")
        print()
        print()
        print()
        print("╔═════════════════ MENU ═════════════╗")
        print("║                                    ║")
        print("║  1. Read from file                 ║")
        print("║  2. Input from CLI                 ║")
        print("║                                    ║")
        print("╚════════════════════════════════════╝")
        print()
        user_input = input(">> Enter your option (1 / 2): ")
        
        
        
        if user_input in menu_options:
            return user_input
        else:
            print()
            print("OPTION NOT AVAILABLE! Please enter either 1 or 2.")
            time.sleep(1)
            
user_input = get_menu_option()
                                                                                                                                        
                                                                                                                                                                                                                                                        
# READ FILE INPUT
if user_input == '1':
    file_name = input("\n>> Please input your file name with .txt: ")
    file_path = os.path.join("..", "test", file_name)
    buffer_size, matrix, sequences = parse_file(file_path)
    
    print()
    print("\n Reading File...")
    time.sleep(2)
    print()
    print("----------------------------------------")
    print("                FILE INFO               ")
    print("----------------------------------------")
    print("\nBuffer Size:", buffer_size)
    print("Matrix Width:", matrix.width, ", Height:", matrix.height)
    print("\n--- MATRIX ---")
    print_matrix(matrix)

    print("\nNumber of Sequences:", len(sequences))
    print("\n--- SEQUENCES ---")
    print_sequences(sequences)
    print()
    print("\n Generating optimal solution...")
    


# READ CLI INPUT
elif user_input == '2':
    number_of_unique_token = int(input("\nInsert number of unique tokens: "))
    unique_tokens = input("Insert tokens: ").split()

    # Validate tokens
    for token in unique_tokens:
        if not isValidToken(token):
            print(f"\nError: Invalid token '{token}'. Token must be alphanumeric and have at most 2 characters.")
            exit()
    
    if len(unique_tokens) != number_of_unique_token:
        print("\nError: Number of tokens doesn't match.")
        exit()
        
    matrix_size = tuple(map(int, input("Insert matrix size (row)(column): ").split()))


    matrix = generateMatrix(unique_tokens, matrix_size)

    print("\n--- GENERATED MATRIX ---")
    for row in matrix.data:
        print(' '.join(row))
    
    
    buffer_size = int(input("\nInsert buffer size: "))
    num_sequences = int(input("Insert number of sequences: "))
    max_sequence = int(input("Insert maximum sequences: "))
        
    sequences = generateSequences(unique_tokens, buffer_size, num_sequences, max_sequence)

    print("\n--- GENERATED SEQUENCES ---")
    for i, seq in enumerate(sequences, start=1):
        print(f"Sequence {i}: {' '.join(seq.sequence)}")
        print(f"Reward sequence {i}: {seq.reward}")
        

#EXECUTION
print()
print()
print("----------------------------------------")
print("              YOUR RESULT               ")
print("----------------------------------------")
stack = []
taken_tokens = []
start_time = time.time()
searchSequence(matrix, stack, 0, 0, buffer_size+1, taken_tokens, True)
max_reward, optimal_solution = findOptimalSequence(taken_tokens, sequences)
result_string = ""     # ??
end_time = time.time()

if max_reward != 0:
    print(f"\nMaximum reward: {max_reward}")
    result_string += str(max_reward) + "\n"
    check = True
    print("Optimal sequence:", end=" ")
    for token in optimal_solution:
        print(token.token, end=" ")
        if not check:
            result_string += " " + token.token
        else:
            result_string += token.token
            check = False

    print("")

    print("Path coordinates:")
    for token in optimal_solution:
        print(str(token.x+1) + ", " + str(token.y+1))
        result_string += '\n' + str(token.x+1) + ", " + str(token.y+1)
        
    execution_time = float(end_time - start_time)*1000
    print("\nExecution time:", execution_time, "ms")
    result_string += f"\nExecution time: {execution_time} ms\n"
    
else:
    print("\nNO OPTIMAL SOLUTION")
    result_string += "NO OPTIMAL SOLUTION\n"


# SAVING SOLUTION
save_solution = input("\n>> Want to save the solution? (Y/N): ")
save_solution = save_solution.upper()

    
if save_solution == 'Y':
    save_file = input(">> Enter file name to save with .txt: ")
    save_path = os.path.join("..", "solution", save_file)
    save = open(save_path, 'w')
    
    save.write(result_string)
    save.close()
    
    print(f"\nSolution saved to '{save_file}'.")
    print("\nThank you for using the program!")

elif save_solution == 'N':
    print("\nThank you for using the program!")
else:
    print("\nOption is invalid. Please enter either Y or N!")
    
    

    



