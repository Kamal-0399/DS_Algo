def RBS(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2
    
    if list[midpoint] == target:
        return True
    else:
        if list[midpoint] <target:
            return RBS(list[midpoint+1:], target)
        else:
            return RBS(list[:midpoint], target)

def verfy (index):
    if index is not None:
        print("Target found:", index)
    else:
        print("Target not found")


list1= [1,2,3,3,4,9,0,5,6,7,9]
result = (RBS(list1, 3))

verfy(result)