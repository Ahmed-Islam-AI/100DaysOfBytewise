# QuickSort is a divide and conquer algorithm. 
# It picks an element as a pivot and partitions the given array around the picked pivot.

# define a function and giving a parameter of array which is list
# low pointing the starting index of array and the High pointing the last index of array.
def quick_Sort(arr, low, high):
    
    if low < high:
        pi = partition(arr, low, high) #partition function call for choosing pivot element
        quick_Sort(arr, low, pi-1) #recursive function call
        quick_Sort(arr, pi+1, high)
        
        
def partition(arr, low, high):
    p = arr[low]
    i = low + 1
    j = high
    while True:
        while i <= j and arr[i] <= p:  #left to right move for picking the value that is greater than pivot
            i = i + 1
        while i <= j and arr[j] >=p:  # right to left move 
            j = j - 1
        
        # checking the value of i is less than j if yes than swap it's values
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i] #swapping values
        else:
            break
    
    arr[low], arr[j] = arr[j], arr[low] #swapping pivot
    return j


# dummy array or list of numbers
arr = [3, 6, 8, 10, 1, 2, 1]
quick_Sort(arr, 0, len(arr) - 1)
print(arr)  # Output: [1, 1, 2, 3, 6, 8, 10]