def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    print(f"Pivot: {pivot}")
    less = [x for x in arr[1:] if x <= pivot]
    print(f"Less than pivot: {less}")
    greater = [x for x in arr[1:] if x > pivot]
    print(f"Greater than pivot: {greater}")
    return quick_sort(less) + [pivot] + quick_sort(greater)

if __name__ == "__main__":
    array = [3, 6, 8, 10, 1, 2, 1]
    print("Original array:", array)
    sorted_array = quick_sort(array)
    print("Sorted array:", sorted_array)