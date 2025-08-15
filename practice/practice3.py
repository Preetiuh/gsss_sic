def draw_triangle(number_of_lines):
    for i in range(1, number_of_lines + 1):
        # Print leading spaces
        print(' ' * (number_of_lines - i), end='')
        # Print asterisks
        print('*' * (2 * i - 1))

# Main execution
number_of_lines = 17
draw_triangle(number_of_lines)