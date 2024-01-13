
def bubble_sort(arr):
    print("Bubble Sort")
    print("O(n^2)")
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

            print(f'{(i * len(arr)) + j}: {arr}')
            
def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i-1, -1, -1):
            if arr[j] > arr[j+1]: # swap greater element to the right
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp

            print(f'{(i * len(arr)) + j}: {arr}')
            

            
    
                    