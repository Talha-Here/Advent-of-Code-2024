def is_safe_sequence(levels):
    """
    Check if a sequence of levels is safe according to basic rules.
    
    Args:
        levels (list[int]): List of reactor levels
        
    Returns:
        bool: True if the sequence is safe, False otherwise
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

def is_safe_report_with_dampener(levels):
    """
    Check if a report is safe either as-is or by removing one level.
    
    Args:
        levels (list[int]): List of reactor levels
        
    Returns:
        bool: True if the report is safe or can be made safe by removing one level
    """
    # First check if it's safe without any modifications
    if is_safe_sequence(levels):
        return True
    
    # Try removing each level one at a time
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i+1:]
        if is_safe_sequence(modified_levels):
            return True
    
    return False

def count_safe_reports(filename):
    """
    Read reports from a file and count how many are safe with the Problem Dampener.
    
    Args:
        filename (str): Path to the input file
        
    Returns:
        int: Number of safe reports
    """
    safe_count = 0
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Skip empty lines
                line = line.strip()
                if not line:
                    continue
                
                # Convert line to list of integers
                levels = [int(x) for x in line.split()]
                
                if is_safe_report_with_dampener(levels):
                    safe_count += 1
                    
        return safe_count
    
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
        return None
    except ValueError:
        print("Error: Invalid data format in file")
        return None

def analyze_report_details(levels):
    """
    Analyze a report and provide details about its safety status.
    
    Args:
        levels (list[int]): List of reactor levels
        
    Returns:
        str: Detailed analysis of the report
    """
    if is_safe_sequence(levels):
        return "Safe without any modifications"
    
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i+1:]
        if is_safe_sequence(modified_levels):
            return f"Safe by removing level {levels[i]} at position {i+1}"
    
    return "Unsafe regardless of which level is removed"

# Example usage with detailed analysis
if __name__ == "__main__":
    filename = "input.txt"  # Change this to your input file name
    
    try:
        with open(filename, 'r') as file:
            print("Detailed Analysis:")
            for line in file:
                line = line.strip()
                if not line:
                    continue
                    
                levels = [int(x) for x in line.split()]
                result = analyze_report_details(levels)
                print(f"{levels}: {result}")
            
        result = count_safe_reports(filename)
        if result is not None:
            print(f"\nTotal number of safe reports: {result}")
            
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
    except ValueError:
        print("Error: Invalid data format in file")