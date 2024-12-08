def quick_sort(arr, low, high,compare_fn=(lambda x,y: x<=y)):
    if low < high:
        pi = partition(arr, low, high,compare_fn)
        quick_sort(arr, low, pi - 1,compare_fn)
        quick_sort(arr, pi + 1, high,compare_fn)

def partition(arr, low, high,compare_fn):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if compare_fn(arr[j],pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def check_divided_by_5_and_3(x):
    if x%5 ==0 and x%3 == 0:
        return 3
    elif x%5 == 0:
        return 2
    elif x%3 == 0:
        return 1
    else:
        return 0

def compare_divided_by_5_and_3(x,y):
    x_priority = check_divided_by_5_and_3(x)
    y_priority = check_divided_by_5_and_3(y)
    if x_priority < y_priority:
        return True
    elif x_priority > y_priority:
        return False
    return x <= y

def compare_by_num_digits(x,y):
    x_digit_amount = len(str(abs(x)))
    y_digit_amount = len(str(abs(y)))
    if x_digit_amount < y_digit_amount:
        return True
    elif x_digit_amount > y_digit_amount:
        return False
    return x <= y

def compare_by_remainder(n,x,y):
    x_remainder = x%n
    y_remainder = y%n
    if x_remainder < y_remainder:
        return True
    elif x_remainder > y_remainder:
        return False
    return x <= y

# arr = [10, 7, 8, 9, 1, 5]
# arr = [15, 10, 9, 3, 7, 5, 12, 30]
arr = [15, 100, 9, 3, 7, 12345, 555, 10]
n = 4
quick_sort(arr, 0, len(arr) - 1,lambda x, y: compare_by_remainder(n, x, y))
print("Sorted array:", arr)