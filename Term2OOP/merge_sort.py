# Merge sorting algorithm implemented in Python. The function recursively splits a list into individual elements and puts the 
# list back together in order. The algorithm works by pointing to the mid point of a list and splitting the list at that point. The 
# function is then called recursively to continue that process on each of the split halves until the list is split to individual 
# elements. The list is then pieced back together in order according to size. 

def merge_sort(list):

    if len(list)>1:
        # determing the middle, left split and right split
        mid = len(list)//2
        lefthalf = list[:mid]
        righthalf = list[mid:]
        # calling the function recursively to split the list
        merge_sort(lefthalf)
        merge_sort(righthalf)
        # initializing incrementing variables
        i=0
        j=0
        k=0
        # loop to check for element size and piecing the list back together
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                list[k]=lefthalf[i]
                i=i+1
            else:
                list[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            list[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            list[k]=righthalf[j]
            j=j+1
            k=k+1
    # returning the arranged list
    return list

# testing
list = [54,26,93,17,77,31,44,55,20]
print(merge_sort(list))

