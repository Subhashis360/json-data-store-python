import json

# Function to check and update user data
def update_user_data(user_number, new_data):
    # Specify the JSON file path
    json_file_path = "userdata.json"

    # Step 1: Read the existing JSON data (if any)
    try:
        with open(json_file_path, 'r') as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        # If the file doesn't exist, create an empty dictionary
        existing_data = {}

    # Step 2: Check if the user number exists in the data
    if user_number in existing_data:
        # If user data exists, update it
        existing_data[user_number].update(new_data)
    else:
        # If user data doesn't exist, create a new entry
        existing_data[user_number] = new_data

    # Step 3: Write the updated data back to the JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)

# Function to find user data by number
def find_user_data(user_number):
    # Specify the JSON file path
    json_file_path = "userdata.json"

    # Step 1: Read the existing JSON data (if any)
    try:
        with open(json_file_path, 'r') as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        return None

    # Step 2: Check if the user number exists in the data
    if user_number in existing_data:
        return existing_data[user_number]
    else:
        return None

# Example usage:
new_data = {
    "data1": "value1",
    "data2": "value2",
    "data3": "value3"
}

user_number = "7875624257"

# Update user data or add new user data
update_user_data(user_number, new_data)

# Find user data by number
found_data = find_user_data(user_number)

if found_data:
    print(f"User data found: {found_data['data1']}")
else:
    print("User data not found.")
