
my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}


def check_key_exists(dictionary, key):
    return key in dictionary

key_to_check = 'name'


if check_key_exists(my_dict, key_to_check):
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")

