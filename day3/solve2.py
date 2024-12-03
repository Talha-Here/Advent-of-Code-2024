
import re

def process_instructions(text):

    pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
    total = 0
    
    # Find all matches
    matches = re.finditer(pattern, text)
    
    # Process each valid instruction
    do =  True
    # for match in matches:
    #     instruction = match.group(0)
    #     if instruction == "do()":
    #         do = True
    #     elif instruction == "don't()":
    #         do = False
    #     else: 
    #         if do:
    #             x, y = map(int, match.groups())
    #             # for x, y in matches:
    #                 # print(x,y)
    #             total += x * y
    for match in matches:
        if match.group(0) == "do()":
            do = True
        elif match.group(0) == "don't()":
            do = False
        else:
            # Process mul(x, y) when `do` is True
            if do and match.group(1) and match.group(2):
                x, y = int(match.group(1)), int(match.group(2))
                total += x * y
    return total


def extract_and_multiply(data):
    # Regular expression to match valid mul(X,Y)
    pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
    
    # Find all matches in the input string
    matches = re.findall(pattern, data)
    
    # Calculate the sum of the products
    do = True
    total_sum = 0
    for x, y in matches:
        total_sum += int(x) * int(y)
    
    return total_sum
res = 0
with open("input3.txt", 'r') as file:
    s = file.read().strip()
    print(s)
    res1 = process_instructions(s)
    # res = extract_and_multiply(s)

    print(res1)
