def find_largest(numbers):
    return max(numbers)

def find_smallest(numbers):
    return min(numbers)
    
numbers_list = [34, 78, 12, 90, 56, 23]

largest = find_largest(numbers_list)
smallest = find_smallest(numbers_list)

print(f"The largest number in the list is {largest}")
print(f"The smallest number in the list is {smallest}")

