values = "data/values.txt"
trees = "data/trees.txt"



def read_file_lines(file_path):
    
    #open file
    with open(file_path, 'r') as file:

        
        #iterate through the lines in our file and remove and \n's

        words = [line.replace('\n','').upper() for line in file]

    return words

#testing

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
    all_abrvs = []
    for word in text:
        abrv = []
        prev_index1 = None
        for letter1 in word[1:-1]:
            score = 0
            prev_index2 = None
            for letter2 in word[word.index(letter1)+1:]:
                if letter1 == ' ' or letter2 == ' ':
                    continue
                elif prev_index1 and prev_index2 is not None and prev_index1 == ' ':
                    score += values.get(letter2)
                elif prev_index1 and prev_index2 is not None and prev_index2 == ' ':
                    score += values.get(letter1)
                elif prev_index1 and prev_index2 is not None and prev_index1 == ' ' and prev_index2 == ' ':
                    score = 0
                else:
                    score = values.get(letter1) + values.get(letter2)

                prev_index2 = letter2
                score = str(score)
                print(word[0]+letter1+letter2 + ':' +score)
                abrv.append(word[0]+letter1+letter2 + ':' +score)
            prev_index1 = letter1

                
        all_abrvs.append(abrv)

    print(all_abrvs)





def main(values,trees):

    text = read_file_lines(trees)
    #print(text)
    values =  create_dict_from_file(values)
    #print(values)
    word_values = scores_for_words(values, text)     
    #print(word_values)
    create_all_abrvs(values, text)

main(values, trees)



