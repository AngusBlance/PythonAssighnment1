#import the os library so we can get the name of the input file without the extension
import os
#set the file paths for the values and trees files
values = "data/values.txt"
trees = "data/trees.txt"



def read_file_lines(file_path):
    
    #open file
    with open(file_path, 'r') as file:
        #iterate through the lines in our file and remove and \n's, spaces, -'s and 's aswell changing spaces to $'s and making everything uppercase
        words = [line.replace('\n','').replace(' ', '$').replace('-','').replace("'",'').upper() for line in file]
    #return the list of words
    return words

#make array of words without any changes for writing to file
def read_file_normal(file_path):
    # Create an empty list to store the words
    words = []
    # Open the file and read its content
    with open(file_path, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            # Split each line into words and add them to the list.
            words.append(line.strip())

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





def create_all_abrvs(values, text):
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
    
    
    
    

    

            
            

def find_best_score(all_abrvs):
    # I regret using high score as a variable the lowest score is the best :( 
    #create a list for the best abreviations
    best_abrvs = []

    # iterate through all combinations of abbreviations
    for abrvs_index, abrvs in enumerate(all_abrvs):
        # create a High score it is high so that the first score is always lower
        High_score = 1000
        # save the index of the highest score. i dont think this is needed 
        High_score_index = 0

        # loop through each individual score and keep track of its index
        for abrve_single_index, abrv_single in enumerate(abrvs):
            # create the score of the current abbreviation we are on
            current_score = int(abrv_single[-2:].replace(':', ''))
            # check if the current score is less than the Highest score so far
            if current_score < High_score:
                # if it is, we create a new high-score (lowest score) and save its index
                High_score = current_score
                High_score_index = abrve_single_index

        # check if High_score_index is within bounds before accessing the list (I had problems with empty lists from the 
        # delete_duplicates function)
        if 0 <= High_score_index < len(abrvs):
            # once we have found this, we append this to our abrv high scores for our current word
            best_abrvs.append(abrvs[High_score_index])
        else:
            # if the index is out of bounds we append an empty string 
            best_abrvs.append('') 

    return best_abrvs


# just some user interface stuff as requested in the assighnment
def grab_file_name():
    #print welcome message. Very cool!
    print('Welcome to the abbreviation generator!')
    print('to use the trees file as for the assighnment use data/trees.txt')
    #get the file name and the users name
    file =  input('Please enter the directory of the file you would like to abbreviate: ')
    name = input('Please enter your surname: ')
    #return the file name and the users name
    return file, name





def write_to_file(best_abrvs,norm_text, name, input_file):
    # Using the os library, get the name of the input file without the extension
    # I used this website to help me with this https://docs.python.org/3/library/os.path.html
    # use os.path for pathname manipulations
    # use basename to get the base name of the file
    file_name = os.path.basename(input_file)
    #use splitext to split the file name and the extension to get the file name without the extension (gets rit of .txt)
    file_name_without_extension = os.path.splitext(file_name)[0]
    
    # doing this made it work?
    base_file_name = os.path.basename(file_name_without_extension)
    
    # Construct the output filename
    filename = name + '_' +  base_file_name + '_abbrevs.txt'
    
    # Open the output file
    with open(filename, 'w') as output_file:
        # itterate through the list of normal words and the list of best abreviations
        for n, abrv in zip(norm_text, best_abrvs):
            # write the word and the abreviation to the file as asked in assignment
            output_file.write(n + '\n')
            output_file.write(abrv + '\n') 
        

# delete duplicates as asked in the assighnment
def delete_duplicates(all_abrvs):
    # turn our matrix of abbreviations into a one dimensional list of abbreviations
    #same as 2 for loops and appending to a list
    flat_abrvs = [item for sublist in all_abrvs for item in sublist]

    # create dictionary (hashmap) where the key is the abbreviation and the value 
    # is the count of the abbreviation
    abbreviation_counts = {}
    # iterate through each abbreviation 
    for item in flat_abrvs:
        # split the abbreviation into the word and the score at the ':'
        # but keep only the word [0]
        abbreviation = item.split(':')[0]
        # add the abbreviation to the dictionary and increment its count by 1
        abbreviation_counts[abbreviation] = abbreviation_counts.get(abbreviation, 0) + 1

    
    # create a new list for the filtered abbreviations
    filtered_abrvs = []

    # iterate through each sublist in the list of all abbreviations
    for sublist in all_abrvs:
        # create a new list for the filtered abbreviations for the current word
        filtered_sublist = []
        # iterate through each abbreviation in the current sublist
        for item in sublist:
            # split the abbreviation into the word and the score at the ':' as seen previously
            abbreviation = item.split(':')[0]
            # check if the abbreviation only occurs once in the list of abbreviations
            if abbreviation_counts[abbreviation] == 1:
                # if it does, we append it to the filtered list
                filtered_sublist.append(item)
        # append the filtered list to the list of filtered abbreviations
        filtered_abrvs.append(filtered_sublist)

    
    # return the filtered list of abbreviations
    return filtered_abrvs
            




def main(values):
    #get the file name and the users name
    [file, name] = grab_file_name()
    
    #read the text file and save it to a variable
    text = read_file_lines(file)
    
    #create a dictionary from the values file
    values =  create_dict_from_file(values)
    
    #create a list of all abreviations
    all_abrvs = create_all_abrvs(values, text)
   
    
    #delete all duplicates
    all_abrvs = delete_duplicates(all_abrvs)
    
    #find the best score for each word
    best_abrvs = find_best_score(all_abrvs)
    
    #read the text file again but this time without any changes
    norm_text = read_file_normal(file)
    
    #write the best abreviations to a file
    write_to_file(best_abrvs,norm_text, name, file)
    
    
    

main(values)



