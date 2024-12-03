# def check_safe(num):
#     is_inc = False
#     is_dec = False
#     increasing = None

#     for i in range(len(num)-1):
#         diff =  num[i] - num[i+1]

#         # checking is it in 1-3 
#         if not (1 <= diff <= 3):
#             return False
#         # Check if it's not consistently increasing or decreasing
#         if diff > 0:  # Increasing
#             is_inc = True
#         elif diff < 0:  # Decreasing
#             is_dec = True

#     # Safe if either increasing or decreasing
#     return is_inc or is_dec



# with open("test.txt", "r") as file:
#     for line in file:
#         # Convert the line into a list of integers
#         numbers = list(map(int, line.split()))
        
#         if check_safe(numbers):
#             print("Safe")
#         else:
#             print("UN-safe")

def is_safe_report(levels):
    """
    Check if a report is safe according to Red-Nosed reactor safety rules.
    
    Args:
        levels (list[int]): List of reactor levels
        
    Returns:
        bool: True if the report is safe, False otherwise
    """
    if len(levels) < 2:
        return True
    
    # Check the first two numbers to determine if we should be increasing or decreasing
    direction = 1 if levels[1] > levels[0] else -1
    
    # Check each adjacent pair
    for i in range(len(levels) - 1):
        difference = levels[i + 1] - levels[i]
        
        # Check if direction changes
        if (direction > 0 and difference <= 0) or (direction < 0 and difference >= 0):
            return False
        
        # Check if difference is within bounds (1-3)
        if abs(difference) < 1 or abs(difference) > 3:
            return False
    
    return True

def count_safe_reports(filename):
    """
    Read reports from a file and count how many are safe.
    
    Args:
        filename (str): Path to the input file
        
    Returns:
        int: Number of safe reports
    """
    safe_count = 0
    
    try:
        with open(filename, 'r') as file:
            current_report = []
            
            for line in file:
                # Skip empty lines
                line = line.strip()
                if not line:
                    continue
                
                # Convert line to list of integers
                levels = [int(x) for x in line.split()]
                
                if is_safe_report(levels):
                    safe_count += 1
                    
        return safe_count
    
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
        return None
    except ValueError:
        print("Error: Invalid data format in file")
        return None

# Example usage
if __name__ == "__main__":
    filename = "input.txt"  # Change this to your input file name
    result = count_safe_reports(filename)
    
    if result is not None:
        print(f"Number of safe reports: {result}")