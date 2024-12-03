left_list = []
right_list = []

# Open and read the file
with open("input.txt", "r") as file:
    for line in file:
        # Split each line into two values
        left, right = map(int, line.split())
        # Append the values to their respective lists
        left_list.append(left)
        right_list.append(right)
    
    # sorting the list
    left_list.sort()
    right_list.sort()

    distance = 0
    for l, r in zip(left_list, right_list):     
        distance += abs(l - r)
    # ONE-LINER: 
    # distance = sum(abs(l - r) for l, r in zip(left_list, right_list))    
        

# print("Right List:", right_list)
print("dist:", distance)

# T.C : O(nlogn)