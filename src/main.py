text = "this is a test"

def read_file_lines(file_path):
    
    #open file
    with open(file_path, 'r') as file:
        #iterate through the lines in our file and remove and \n's
    
        words = [line.rstrip('\n') for line in file]

    return words



def create_dict_from_file(file_path):
    #create dictionary from the values file. It looks like a dictionary in the txt file so this makes sense
    my_dict = {}
    # Open the file and read its content
    with open(file_path, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            # Split the line into key and value
            key, value = line.strip().split()
            
            # Convert the value to an integer
            value = int(value)
            
            # Add the key-value pair to the dictionary
            my_dict[key] = value
    
    return my_dict

def scores_for_words(scores, text):
    for words in text:
        for letter in words:
            print(letter)
        
   





        

# x = create_dict_from_file("data/values.txt")
# print(x)
# y = read_file_lines("data/trees.txt")
# print(y)
