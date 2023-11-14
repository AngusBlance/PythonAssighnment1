values = "data/values.txt"
trees = "data/trees.txt"



def read_file_lines(file_path):
    
    #open file
    with open(file_path, 'r') as file:

        
        #iterate through the lines in our file and remove and \n's

        words = [line.replace('\n','').upper() for line in file]

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

def scores_for_words(values, text):
    scores = []
    for words in text:
        sub_score = []
        prev_index = None
        for letter in words:
            if letter == ' ':
                sub_score.append('$')
            elif prev_index is not None and prev_index == ' ':
                sub_score.append(0)
            else:
                sub_score.append(values.get(letter))
            prev_index = letter
            
        scores.append(sub_score)
    
    return(scores)
        
   

def main(values,trees):

    text = read_file_lines(trees)
    #print(text)
    values =  create_dict_from_file(values)
    #print(values)
    word_values = scores_for_words(values, text)     
    print(word_values)


main(values, trees)



