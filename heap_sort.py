def heapify(arr, n, i, compare_fn):
    largest = i  
    left = 2 * i + 1  
    right = 2 * i + 2  

    if left < n and not compare_fn(arr[left], arr[largest]):
        largest = left

    if right < n and not compare_fn(arr[right], arr[largest]):
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, compare_fn)

def heap_sort(arr, compare_fn=lambda x, y: x <= y):

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, compare_fn)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0, compare_fn)

def digits_sum(x):
    return sum(int(digit) for digit in str(x))

def compare_digits_sum(x, y):
    x_digits_sum = digits_sum(x)
    y_digits_sum = digits_sum(y)
    if x_digits_sum < y_digits_sum:
        return True
    elif x_digits_sum > y_digits_sum:
        return False
    return x <= y

def is_perfect_number(x):
    if x < 2:
        return False
    divisor_sum = sum(i for i in range(1, x // 2 + 1) if x % i == 0)
    return divisor_sum == x

def compare_by_perfect_number(x,y):
    x_is_perfect_number = is_perfect_number(x)
    y_is_perfect_number = is_perfect_number(y)
    if not x_is_perfect_number and y_is_perfect_number:
        return False
    elif x_is_perfect_number and not y_is_perfect_number:
        return True
    return x <= y

# Example usage
arr1 = [12, 11, 13, 5, 6, 7]
heap_sort(arr1)
print("Sorted array (default):", arr1)

arr2 = [24, 31, 12, 40, 111]
heap_sort(arr2, compare_digits_sum)
print("Sorted array by digit sum:", arr2)

arr3 = [28, 6, 496, 12, 20, 8, 1, 7]
heap_sort(arr3,compare_by_perfect_number)
print("Sorted by perfect numbers first:", arr3)
