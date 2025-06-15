def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    steps = 0
    while low <= high:
        mid = (low + high) // 2
        steps += 1
        print(f"Step {steps}: low={low}, high={high}, mid={mid}")
        if arr[mid] == target:
            print(f"Found {target} at index {mid}")
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    print(f"{target} not found in array")
    return -1

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7]
    target = 4
    binary_search(array, target)