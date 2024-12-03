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
    
    similarity_sum = 0
    for l, r in zip(left_list, right_list):
        similarity_sum += l * right_list.count(l)
    print(similarity_sum)


## ========= OPTIMIZED ==============

# from collections import Counter

# # Precompute the count of each element in the right list
# right_counts = Counter(right_list)

# # Initialize the similarity sum
# similarity_sum = 0

# # Iterate through the left list
# for l in left_list:
#     similarity_sum += l * right_counts.get(l, 0)  # Use the precomputed count

# print("Similarity Score:", similarity_sum)