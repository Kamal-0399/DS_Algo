def binary_search(list, target):
    first =0
    last = len(list) -1

    while first <= last:
        midpoint = (first + last)//2 # floor division 

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint -1
    return None

def verfy (index):
    if index is not None:
        print("Target found at:", index)
    else:
        print("Target not found")


list1= [1,2,3,3,4,9,0,5,6,7,9]
result = (binary_search(list1, 3))

verfy(result)