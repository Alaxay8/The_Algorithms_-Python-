def smallest(arr):
    small = arr[0]
    index = 0
    for i in range(1,len(arr)):
        if arr[i]<small:
            small = arr[i]
            index = i
    return index


list = [3,2,1,4,6,9,8,10,5]

print(smallest(list))

def selectionSort(arr):
    newList = []
    for i in range(1,len(arr)):
        smallester = smallest(arr)
        newList.append(arr.pop(smallester))
    return newList

print(selectionSort(list))