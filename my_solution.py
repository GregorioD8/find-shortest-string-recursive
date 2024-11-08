def find_shortest_string_recursive(arr, index=0):
    # Base case: if we've reached the end of the list, return that element
    if index == len(arr) - 1:
        return arr[index]
    
    # Recursive case: get the shortest string from the rest of the array
    shortest_in_rest = find_shortest_string_recursive(arr, index + 1)
    
    # Compare current element with the shortest found in the rest
    return arr[index] if len(arr[index]) <= len(shortest_in_rest) else shortest_in_rest

# Testing
if __name__ == '__main__':
    print("Expecting: 'a'")
    print(find_shortest_string_recursive(['aaa', 'a', 'bb', 'ccc']))

    print("Expecting: 'hi'")
    print(find_shortest_string_recursive(['cat', 'hi', 'dog', 'an']))

    print("Expecting: 'lily'")
    print(find_shortest_string_recursive(['flower', 'juniper', 'lily', 'dandelion']))
