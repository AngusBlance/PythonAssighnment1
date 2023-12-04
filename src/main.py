values = "data/values.txt"
trees = "data/trees.txt"



def read_file_lines(file_path):
    
    #open file
    with open(file_path, 'r') as file:

        
        #iterate through the lines in our file and remove and \n's

        words = [line.replace('\n','').replace(' ', '$').replace('-','').replace("'",'').upper() for line in file]

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



        
   
def create_all_abrvs(values, text):
    #create a list of all the abreviations for every word
    all_abrvs = []
    #iterate through each word in the text
    for word in text:
        #create a list of abreviations for each indavidual word
        abrv = []
        #keep track of the previous letter for the second letter for scoring
        prev_index1 = word[0]
        #iterate from the second letter to the second to last letter for the second letter in our abreviation
        for letter1 in word[1:-1]:
            #create a score for each abreviation
            score = 0
            #keep track of the previous letter for the third letter for scoring
            prev_index2 = letter1
            #iterate from the third letter to the last letter for the third letter in our abreviation

            for letter2 in word[word.index(letter1)+1:]:
                #if the letter is a space skip it
                if letter1 == '$' or letter2 == '$' or prev_index1 is None or prev_index2 is None:
                    prev_index2 = letter2
                    continue
                
                #if both previous letters are spaces then the score is 0
                elif prev_index1 == '$' and prev_index2 == '$':
                    score = 0

                    #set the previous letter to the current letter for the next iteration
                    prev_index2 = letter2
                    #add the abreviation and score to the list of abreviations
                    abrv.append(word[0]+letter1+letter2 + ':' +str(score))
                    score = 0
                    continue
                    
                #if both letters are not spaces then add the values together
                elif letter1 != '$' and letter2 != '$':
                    score = values.get(letter1) + values.get(letter2)

                    #set the previous letter to the current letter for the next iteration
                    prev_index2 = letter2
                    #add the abreviation and score to the list of abreviations
                    abrv.append(word[0]+letter1+letter2 + ':' +str(score))
                    score = 0
                    continue
                #check if the previous letter is a space and if the letter is not a space
                elif prev_index1 == '$'  and letter2 != '$':
                    #just use letter 2 for the score as letter1 has a space behind it hence =0
                    score += values.get(letter2)

                    #set the previous letter to the current letter for the next iteration
                    prev_index2 = letter2
                    #add the abreviation and score to the list of abreviations
                    abrv.append(word[0]+letter1+letter2 + ':' +str(score))
                    score = 0
                    continue
                    
                elif prev_index2 == '$'  and letter1 != '$':
                    #just use letter 1 for the score as letter2 has a space behind it hence =0
                    score += values.get(letter1)

                    #set the previous letter to the current letter for the next iteration
                    prev_index2 = letter2
                    #add the abreviation and score to the list of abreviations
                    abrv.append(word[0]+letter1+letter2 + ':' +str(score))
                    score = 0
                    continue
                    
                    
                
                    
            #reset the score to 0 for the next letter

            #set the previous letter to the current letter for the next iteration
            prev_index1 = letter1

                
        all_abrvs.append(abrv)

    return all_abrvs





def create_all_abrvs2(values, text):
    all_abrvs = []
    
    for word in text:
        abrv = []
        for letter1_index, letter1 in enumerate(word[1:-1]):
            letter1_index = letter1_index 
            for letter2_index, letter2 in enumerate(word[letter1_index+2:]):
                #There are a few possible combinations of spaces and letters that we
                #need to differentiate between
                letter2_index = letter2_index + letter1_index + 2  
                #there is a space as a letter
                if letter1 == '$' or letter2 == '$':
                    
                    continue
                
                #both previous letters are spaces
                elif word[letter1_index-1] == '$' and word[letter2_index-1] == '$':
                    score = 0
                    abrv.append(word[0]+letter1+letter2 + ':' +str(score))
                    
                    continue
                
                #previous letter of letter 1`` is a space
                elif word[letter1_index-1] == '$':
                    score = values.get(letter2)
                    abrv.append(word[0]+letter1+letter2 + ':' +str(score))
                    
                    continue
                
                #previous letter of letter 2 is a space 
                elif word[letter2_index-1] == '$':
                    score = values.get(letter1)
                    abrv.append(word[0]+letter1+letter2 + ':' +str(score))
                    
                    continue
                
                else:
                    score = values.get(letter1) + values.get(letter2)
                    score = int(score)
                    abrv.append(word[0]+letter1+letter2 + ':' +str(score))
                      

        
        all_abrvs.append(abrv)
        

    return all_abrvs


def Delete_Multiples(all_abrvs):

    #loop through all abrreviations of each word
    for word_index, word in enumerate(all_abrvs):
        #loop through each indavidual abreviation
        
        for abrv1_index, abrv1 in enumerate(word):
            #we are now itterating through each abreviation
            #now we need to itterate from the current abreviation to the end of the list to check for duplicates
            for abrv2_index, abrv2 in enumerate(all_abrvs[word_index][abrv1_index+1:]):
                #if the current abreviation is in the word then we delete it
                if abrv1 in abrv2:
                    all_abrvs[word_index].remove(abrv1)
                    #all_abrvs[abrv2_i].remove(abrv)
                    print(abrv1+ abrv2+' '+ str(abrv1_index) + str(abrv2_index))
                    continue
                
    return all_abrvs
            
            
            
            

def find_best_score(all_abrvs):
    #create an array for the best abreviations
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
        
            
def check_multiple_high_scores(best_abrvs,all_abrvs):
    all_high_scores = []
    
    for i, word in enumerate(all_abrvs):
        multiple_abrv = []
        for j, abrv in enumerate(word):
            
            best_score = str(best_abrvs[i][-2:]).replace(':','')
            best_score = int(best_score)
            current_score = abrv[-2:].replace(':','')
            if best_abrvs[i] == abrv:
                continue
            elif best_score ==current_score:
                multiple_abrv.append(all_abrvs[i][j])
                print(all_abrvs[i][j])
        
        if len(multiple_abrv) != 0:
            all_high_scores.append(multiple_abrv)
            
    if len(all_high_scores) != 0:   
        return all_high_scores
    
    else:
        print('no multiple high scores')
        
            




def main(values,trees):

    text = read_file_lines(trees)
    print(text)
    values =  create_dict_from_file(values)
    #print(values)
    word_values = scores_for_words(values, text)     
    #print(word_values)
    
    # all_abrvs = create_all_abrvs(values, text)
    # print(all_abrvs[0:5]) 
    
    all_abrvs = create_all_abrvs2(values, text)
    print(all_abrvs[0:5])
    #all_abrvs = Delete_Multiples(all_abrvs)
    best_abrvs = find_best_score(all_abrvs)
    
    print(best_abrvs)
    #print(create_all_abrvs2(values, text))
       #print(check_multiple_high_scores(best_abrvs,all_abrvs))
    
    
    

main(values, trees)



