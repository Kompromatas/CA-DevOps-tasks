def index_search(arr, target):
   
    if target in arr:
        return arr.index(target)
    else:
        return -1
    
input_list = input("Enter a list of elements separated by spaces: ").split()
target_element = input("Enter the element to search for: ")

print("Index of the target element:", index_search(input_list, target_element))