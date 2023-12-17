list = [1,2,3,4,5,6,7,8,9,10]

for i, num in enumerate(list[1:4]):
    print(i)
    
    

    
    
def remove_duplicates_pairwise(all_abrvs):
    # Create a copy of the input array to avoid modifying the original array
    result_list = [subarray.copy() for subarray in all_abrvs]

    # Iterate through each subarray in the input array
    for i in range(len(result_list)):
        # Iterate through each element in the current subarray
        for j in range(i + 1, len(result_list[i])):
            # Get the current element for comparison
            current_element = result_list[i][j]

            # Remove the current element from the current subarray
            result_list[i] = [element for element in result_list[i] if element != current_element]

            # Remove the same element from subsequent subarrays
            for k in range(i + 1, len(result_list)):
                result_list[k] = [element for element in result_list[k] if element != current_element]

    return result_list

all_abrvs = [['a', 'b', 'c'], ['d', 'e'], ['a', 'c', 'f']]
output_array = remove_duplicates_pairwise(all_abrvs)
print(output_array)

