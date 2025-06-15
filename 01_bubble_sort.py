def bubble_sort(arr):
    n = len(arr)
    print("Initial array:", arr)
    for i in range(n):
        swapped = False
        print(f"Pass {i + 1}:")
        for j in range(0, n-i-1):
            print(f"  Comparing {arr[j]} and {arr[j+1]}")
            if arr[j] > arr[j+1]:
                print(f"  Swapping {arr[j]} and {arr[j+1]}")
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            print("  Current state:", arr)
        if not swapped:
            break
    print("Sorted array:", arr)
    return arr

if __name__ == "__main__":
    bubble_sort([64, 34, 25, 12, 22, 11, 90])