def linear_search(list, target):

    """Return target vale in the list"""
    for i in range(0,len(list)):
        if(i == target):
            return i
    return None

def verfy (index):
    if index is not None:
        print("Taget found at:", index)
    else:
        print("Target not found")


list1= [1,2,3,3,4,9,0,5,6,7,9]
result = (linear_search(list1, 3))

verfy(result)

