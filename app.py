def draw_string_pattern(input_string):
    pattern = {
        'A': [
            '  A  ',
            ' A A ',
            'AAAAA',
            'A   A',
            'A   A'
        ],
        'B': [
            'BBBB ',
            'B   B',
            'BBBB ',
            'B   B',
            'BBBB '
        ],
        'C': [
            ' CCCC',
            'C    ',
            'C    ',
            'C    ',
            ' CCCC'
        ],
        # Define more characters as needed...
    }
    
    for i in range(5):
        line = ''
        for char in input_string:
            if char in pattern:
                line += pattern[char][i] + '  '
            else:
                line += '     '  # Default spacing for characters not defined in the pattern
        print(line)


# Get input from the user
user_input = input("Enter a string: ")

# Draw the string pattern
draw_string_pattern(user_input)
