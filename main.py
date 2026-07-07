from names import get_realistic_names_pool

def get_average_target(str1, str2):
    """Calculates the mathematical average of the ASCII sums of two strings."""
    sum1 = sum(ord(c) for c in str1)
    sum2 = sum(ord(c) for c in str2)
    # Using integer division to get a clean whole number for ASCII targeting
    return (sum1 + sum2) // 2

def main():
    print("=== Step 1: Input Strings ===")
    str1 = input("Enter the first string: ").strip()
    str2 = input("Enter the second string: ").strip()
    
    if not str1 or not str2:
        print("Error: Both inputs must contain text.")
        return

    # Calculate individual sums
    sum1 = sum(ord(c) for c in str1)
    sum2 = sum(ord(c) for c in str2)
    
    # Calculate target average sum
    target_sum = get_average_target(str1, str2)
    
    print(f"\nFirst String Value: {sum1}")
    print(f"Second String Value: {sum2}")
    print(f"Target Average Value: {target_sum}")
    
    print("\n=== Step 2: Finding Real Name Matches ===")
    print("Searching database for 3-to-7 letter names...")
    
    name_pool = get_realistic_names_pool()
    forbidden_set = {str1.lower(), str2.lower()}
    
    exact_matches = []
    all_valid_names = []  # To store tuples of (name, sum) for closest value calculations
    
    # Filter the name database
    for name in name_pool:
        # Exclude if it directly matches an original input
        if name.lower() in forbidden_set:
            continue
            
        # Calculate this real name's ASCII score
        current_name_sum = sum(ord(c) for c in name)
        all_valid_names.append((name, current_name_sum))
        
        if current_name_sum == target_sum:
            exact_matches.append(name)
            
    # Remove duplicates if any exist in the database list
    exact_matches = sorted(list(set(exact_matches)))
    
    # Print the final results
    if exact_matches:
        print(f"\nSuccess! Found {len(exact_matches)} name(s) matching the score of {target_sum}:")
        print("-" * 40)
        for i, matched_name in enumerate(exact_matches, 1):
            breakdown = " + ".join(f"'{c}'({ord(c)})" for c in matched_name)
            print(f"{i}. {matched_name}  ->  ({breakdown} = {target_sum})")
        print("-" * 40)
    else:
        print(f"\nNo real names equal exactly {target_sum}.")
        
        if all_valid_names:
            # Find the minimum absolute difference from the target sum
            min_diff = min(abs(item[1] - target_sum) for item in all_valid_names)
            
            # Extract all names that share this minimal difference
            closest_matches = [item for item in all_valid_names if abs(item[1] - target_sum) == min_diff]
            # De-duplicate and sort by name
            closest_matches = sorted(list(set(closest_matches)), key=lambda x: x[0])
            
            # The actual sum of the closest name(s)
            closest_sum = closest_matches[0][1]
            
            print(f"Found the closest name match(es) with a score of {closest_sum} (Difference of {min_diff}):")
            print("-" * 40)
            for i, (matched_name, current_sum) in enumerate(closest_matches, 1):
                breakdown = " + ".join(f"'{c}'({ord(c)})" for c in matched_name)
                print(f"{i}. {matched_name}  ->  ({breakdown} = {current_sum})")
            print("-" * 40)
        else:
            print("The name database is empty or all options were filtered out.")
