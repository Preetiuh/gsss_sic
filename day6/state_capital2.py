import sys
import os

filename = input('Enter file name: ')

# Read file content safely
try:
    with open(filename, 'r') as file:
        data = file.read()
except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
    sys.exit(1)

print('User given input is:\n', data)

states = []
capitals = []

# Parse command-line arguments for state-capital pairs
for string in sys.argv[1:]:
    temp_list = string.split(' ')
    if len(temp_list) >= 2:
        states.append(temp_list[0])
        capitals.append(temp_list[1])
    else:
        print(f"Invalid input format: '{string}' — expected 'State Capital'")

print('-' * 24)
print('%-15s %s' % ('STATE', 'CAPITAL'))
print('-' * 24)
for i in range(len(states)):
    print('%-15s %s' % (states[i], capitals[i]))