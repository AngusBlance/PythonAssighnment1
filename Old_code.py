'''
first attempt at creating all abreviations looping through each letter
'''        

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




'''
Tried to do it with enumerate but hard to keep track of the indexs and the letters 
when nesting for loops for 2D arrays
'''
def create_all_abrvs2(values, text):
    all_abrvs = []
    
    for word in text:
        abrv = []
        for letter1_index, letter1 in enumerate(word[1:-1]):
            letter1_index = letter1_index +1
            for letter2_index, letter2 in enumerate(word[letter1_index+2:]):
                #There are a few possible combinations of spaces and letters that we
                #need to differentiate between
                #letter2_index = letter2_index +letter1_index 
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


#IDK what the point in this was lmao
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
        


#previous code for finding duplicates
def delete_duplicates(all_abrvs):
    deleted = []
    #loop through all list of abrreviations of each word
    for i, word in enumerate(all_abrvs):
        #loop through each indavidual abreviation
        for j, abrv in enumerate(word):
            #loop through all list of abrreviations of each word
            for k, word2 in enumerate(all_abrvs[i+1:]):
                #loop through each indavidual abreviation
                for l, abrv2 in enumerate(word2):
                    #check if the first abreveation is in the second abreveation
                    if abrv == abrv2:
                        word.remove(abrv)
                        print(abrv)
                
    
#previous code for finding duplicates



