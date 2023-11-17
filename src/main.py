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
                #check if the previous letter is a space and if the letter is not a space
                elif prev_index1 == '$' and prev_index2 != '$' and letter2 != '$':
                    #just use letter 2 for the score as letter1 has a space behind it hence =0
                    score += values.get(letter2)

                    #set the previous letter to the current letter for the next iteration
                    prev_index2 = letter2
                    #add the abreviation and score to the list of abreviations
                    abrv.append(word[0]+letter1+letter2 + ':' +str(score))
                    score = 0
                    continue
                    
                elif prev_index2 == '$' and prev_index1 != '$' and letter1 != '$':
                    #just use letter 1 for the score as letter2 has a space behind it hence =0
                    score += values.get(letter1)

                    #set the previous letter to the current letter for the next iteration
                    prev_index2 = letter2
                    #add the abreviation and score to the list of abreviations
                    abrv.append(word[0]+letter1+letter2 + ':' +str(score))
                    score = 0
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
                    

                
            #reset the score to 0 for the next letter
            

            #set the previous letter to the current letter for the next iteration
            prev_index1 = letter1

                
        all_abrvs.append(abrv)

    return all_abrvs





def main(values,trees):

    text = read_file_lines(trees)
    #print(text)
    values =  create_dict_from_file(values)
    #print(values)
    word_values = scores_for_words(values, text)     
    #print(word_values)
    all_abrvs = create_all_abrvs(values, text)
    print(all_abrvs[29])

main(values, trees)



