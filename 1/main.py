import os
import re

def task1():
    # load input data
    with open(os.path.join(os.path.dirname(__file__), 'input'), 'r') as file:
        list_of_first_last = [int("".join([str(number[0]), str(number[-1])])) for number in
                              [[int(digit) for digit in re.findall(r'\d', line.strip())] for line in file.readlines()]]
    # sum of all first and last digits
    return sum(list_of_first_last)


def task2():
    words_digit_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }



    # load input data
    with open(os.path.join(os.path.dirname(__file__), 'input'), 'r') as file:
        cleaned_lines = [line.strip() for line in file.readlines()]
        converted_lines = []

        for line in cleaned_lines:
            for word, digit in words_digit_dict.items():
                line = line.replace(word, f"{word[0]}{digit}{word[-1]}")

            converted_lines.append(line)
        print(converted_lines)

        list_of_first_last = [int("".join([str(number[0]), str(number[-1])])) for number in
                              [[int(digit) for digit in re.findall(r'\d', line.strip())] for line in converted_lines]]
    # sum of all first and last digits
    return sum(list_of_first_last)


print(task1())
print(task2())