import os
values = "data/values.txt"
trees = "data/trees.txt"



def read_file_lines(file_path):
    
    #open file
    with open(file_path, 'r') as file:
        #iterate through the lines in our file and remove and \n's

        words = [line.replace('\n','').replace(' ', '$').replace('-','').replace("'",'').upper() for line in file]

    return words



def create_dict_from_file(file_path):
    #create dictionary from the values file. It looks like a dictionary (hashmap)
    # in the txt file so this makes sense
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





def create_all_abrvs3(values, text):
    #make list for all abreviations
    all_abrvs = []
    #itterate through each word
    for word in text:
        #make list for each word
        abrv = []
        #itterate through each letter in the word starting from the second letter to the second to last letter
        for letter1_index in range(1, len(word) - 1):
            #save the letter we are on
            letter1 = word[letter1_index]
            #itterate through each letter after the current letter to the last letter
            for letter2_index in range(letter1_index +1, len(word)):
                #save the letter we are on 
                letter2 = word[letter2_index]
                #check if any current letter is a space
                if letter1 == '$' or letter2 == '$':
                    continue
                #check if both previous letters are spaces
                elif word[letter1_index - 1] == '$' and word[letter2_index - 1] == '$':
                    score = 0
                    abrv.append(word[0] + letter1 + letter2 + ':' + str(score))
                    continue
                #check if the previous letter of letter 1 is a space
                elif word[letter1_index - 1] == '$':
                    score = values.get(letter2)
                    abrv.append(word[0] + letter1 + letter2 + ':' + str(score))
                    continue
                #check if the previous letter of letter 2 is a space
                elif word[letter2_index - 1] == '$':
                    score = values.get(letter1)
                    abrv.append(word[0] + letter1 + letter2 + ':' + str(score))
                    continue
                #if none of the previous letters are spaces then we add the values together
                else:
                    score = values.get(letter1) + values.get(letter2)
                    score = int(score)
                    abrv.append(word[0] + letter1 + letter2 + ':' + str(score))
        #add the list of abreviations for the current word to the list of all abreviations 
        all_abrvs.append(abrv)
    #return the list of all abreviations
    return all_abrvs
    
    
    
    

    
def Delete_Multiples(all_abrvs):

    #loop through all abrreviations of each word
    for word_index, word in enumerate(all_abrvs):
        #loop through each indavidual abreviation
        
        for abrv1_index, abrv1 in enumerate(word):
            #we are now itterating through each abreviation
            #now we need to itterate from the current abreviation to the end of the list to check for duplicates
            for abrv2_index, abrv2 in enumerate(all_abrvs[word_index:][abrv1_index+1:]):
                #if the current abreviation is in the word then we delete it
                if abrv1 in abrv2:
                    all_abrvs[word_index].remove(abrv1)
                    #all_abrvs[abrv2_i].remove(abrv)
                    print( str(abrv1) + ' at position ' + str(abrv1_index) + str(abrv2_index) )
                    continue
                
    return all_abrvs
            
            

def find_best_score(all_abrvs):
    #I regret using high score as a variable name but I am too far in to change it now
    best_abrvs = []
    
    #ittarate through all combinations of abreviations
    for abrvs_index, abrvs in enumerate(all_abrvs):
        #create an array for the high scores for each word incase of multiple options
        abrv_high_scores = ''
        #create a High score
        High_score = 1000
        #save the index of the highest score
        High_score_index = 0
        
        #loop through each indavidual score and keep track of its index
        for abrve_single_index, abrv_single in enumerate(abrvs):
            #create the score of the current abreviation we are on
            current_score = abrv_single[-2:].replace(':','')
            current_score = int(current_score)
            #check if the current score is less than the Highest score so far
            if current_score < High_score:
                #if it is > then we create a new high-score and save its index
                High_score = current_score
                High_score_index = abrve_single_index
                
        #once we have found this we append this to our abrv high scores for our current word  
        abrv_high_scores= all_abrvs[abrvs_index][High_score_index]
        #we then append these to all of our abrvs
        High_score_index = 0
        High_score = 1000   
        best_abrvs.append(abrv_high_scores)
        
    return best_abrvs
        
            


def delete_duplicates2(all_abrvs):
    unique_abrvs_set = set()
    
    # Iterate over each word in the 2D array
    for word in all_abrvs:
        # Use a set to keep track of unique abbreviations within the current word
        unique_in_word = set()
        unique_word = []
        for abrv in word:
            if abrv not in unique_in_word:
                # If the abbreviation is not in the set, add it to both sets
                unique_in_word.add(abrv)
                unique_abrvs_set.add(abrv)
                unique_word.append(abrv)
        
        # Replace the original word with the list of unique abbreviations
        word[:] = unique_word
        
        
def grab_file_name():
    print('Welcome to the abbreviation generator!')
    print('to use the trees file as for the assighnment use data/trees.txt')
    file =  input('Please enter the directory of the file you would like to abbreviate: ')
    name = input('Please enter your surname: ')
    return file, name

def write_to_file(best_abrvs, name, file):
    #using the os library we can get the name of the file without the extension
    #I found details for the os library on https://docs.python.org/3/library/os.html
    #get the name of the file without the extension
    file_name = os.path.basename(file)
    #get the name of the file without the extension
    file_name_without_extension = os.path.splitext(file_name)[0]
    #Extract only the base name without the directory
    file = os.path.basename(file_name_without_extension)
    
    filename = name + '_' +  file + '_abbrevs.txt'
    
    with open(filename, 'w') as file:
        for abrv in best_abrvs:
            file.write(abrv + '\n')
        file.write(name)


def main(values):
    
    #C:\Users\angus\Programmes\PythonAssighnment1-1\data\trees.txt
    [file, name] = grab_file_name()
    
    #read the text file and save it to a variable
    text = read_file_lines(file)
    
    #create a dictionary from the values file
    values =  create_dict_from_file(values)
    
    #create a list of all abreviations
    all_abrvs = create_all_abrvs3(values, text)
    #delete all duplicates
    all_abrvs = Delete_Multiples(all_abrvs)
    best_abrvs = find_best_score(all_abrvs)
    
    write_to_file(best_abrvs, name, file)
    
    print(best_abrvs)
    
    
    
    

main(values)



