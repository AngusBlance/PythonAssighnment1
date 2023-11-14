text = "this is a test"

def read_file_lines(file):
    file = open(file, 'r')
    return file.readlines()


def create_dict_from_file(file_path):
    my_dict = {}
    # Open the file and read its content
    with open(file_path, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            # Split the line into key and value (assuming space-separated)
            key, value = line.strip().split()
            
            # Convert the value to an integer
            value = int(value)
            
            # Add the key-value pair to the dictionary
            my_dict[key] = value
    
    return my_dict



def letter_vals(text):
    main_values = []
    for i in text:
        sub_vals = []
        

x = create_dict_from_file("data/values.txt")
print(x)

