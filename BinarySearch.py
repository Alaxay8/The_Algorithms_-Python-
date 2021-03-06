def binarySearch(list,item):
    start = 0
    end = len(list)-1
    while start<=end:
        mid = start+end
        guess = list[mid]
        if guess==item:
            return mid
        if item<=guess:
            end = mid+1
        else:
            start = mid-1
    return None