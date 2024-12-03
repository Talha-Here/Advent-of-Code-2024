# def process_instructions(text):
#     total = 0
#     i = 0
    
#     while i < len(text) - 6:
#         if text[i:i+4] == 'mul(' and text[i+4].isdigit():
#             # Find numbers between parentheses
#             start = i + 4
#             end = text.find(')', start)
            
#             if end == -1:
#                 i += 1
#                 continue
                
#             # Split numbers by comma
#             nums = text[start:end].split(',')
#             if len(nums) != 2:
#                 i += 1
#                 continue
                
#             x, y = nums
            
#             # Validate numbers
#             if (x.isdigit() and y.isdigit() and 
#                 len(x) <= 3 and len(y) <= 3):
#                 total += int(x) * int(y)
            
#             i = end
#         i += 1
    
#     return total
import re
def process_instructions(text):

    # pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    pattern = r"mul\((\d+),(\d+)\)"
    total = 0
    
    # Find all matches
    matches = re.finditer(pattern, text)
    
    # Process each valid instruction
    for match in matches:
        x, y = map(int, match.groups())
        total += x * y
        
    return total


def extract_and_multiply(data):
    # Regular expression to match valid mul(X,Y)
    pattern = r"mul\((\d+),(\d+)\)"
    
    # Find all matches in the input string
    matches = re.findall(pattern, data)
    
    # Calculate the sum of the products
    total_sum = 0
    for x, y in matches:
        total_sum += int(x) * int(y)
    
    return total_sum
res = 0
with open("test.txt", 'r') as file:
    s = file.read().strip()
    # print(line)
    res1 = process_instructions(s)
    res = extract_and_multiply(s)
    # print(res)
    print(res)
    print(res1)
