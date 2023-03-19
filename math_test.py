import numpy as np


def seven_game(n):
    """Outputs the 7game for n players."""
    # Initialize variables
    count = 1
    output_list = [list(np.arange(1, n+1))]
    output_list_temp = []
    player = n*[False]

    # Loop until game is over
    while True:
        # Check if count is divisible by 7
        if count % 5 == 0:
            output_list_temp.append('A')
            player[count % n] = True
            if all(player):
                print(f"All standing at {count}")
                output_list.append(output_list_temp)
                break
        elif count % 7 == 0:
            output_list_temp.append('x')
        else:
            output_list_temp.append('-')

        if len(output_list_temp) == n:
            output_list.append(output_list_temp)
            output_list_temp = []

        # Increment count
        count += 1

        # Check if game is over
        if count > 100:
            break

    for ol in output_list:
        print(ol)


# Example usage
seven_game(12)
