def get_shape_score(shape):
    if shape == 'A':
        return 1  # Rock
    elif shape == 'B':
        return 2  # Paper
    else:
        return 3  # Scissors

def get_outcome_score(opponent_shape, desired_outcome):
    if desired_outcome == 'X':  # Need to lose
        if opponent_shape == 'A':  # Rock
            return 0 + 3  # Scissors + lose
        elif opponent_shape == 'B':  # Paper
            return 0 + 1  # Rock + lose
        else:  # Scissors
            return 0 + 2  # Paper + lose
    elif desired_outcome == 'Y':  # Need to draw
        return 3 + get_shape_score(opponent_shape)
    else:  # Need to win
        if opponent_shape == 'A':  # Rock
            return 6 + 2  # Paper + win
        elif opponent_shape == 'B':  # Paper
            return 6 + 3  # Scissors + win
        else:  # Scissors
            return 6 + 1  # Rock + win

def calculate_total_score(input_file):
    total_score = 0
    with open(input_file, 'r') as file:
        for line in file:
            opponent_shape, desired_outcome = line.strip().split()
            round_score = get_outcome_score(opponent_shape, desired_outcome)
            total_score += round_score
    return total_score

# Replace 'input_file_name' with the appropriate name of your input file
input_file_name = "input_9_cap1.txt"
total_score = calculate_total_score(input_file_name)
print(f"Total score: {total_score}")