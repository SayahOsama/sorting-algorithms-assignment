
def bubble_sort(arr,compare_fn = lambda x,y: x<=y):
    n = len(arr)
    for i in range(n):
        swapped = False
        
        for j in range(0, n-i-1):
            if not compare_fn(arr[j],arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if not swapped:
            break

    return arr

def compare_by_diff(x,y,target):
    x_diff_from_target = abs(target-x)
    y_diff_from_target = abs(target-y)
    if x_diff_from_target == y_diff_from_target:
        return x <= y
    return x_diff_from_target <= y_diff_from_target

def is_palindromic(num):
    str_num = str(num)
    return str_num == str_num[::-1]
    
def compare_by_palindromic(x,y):
    x_is_palindromic = is_palindromic(x)
    y_is_palindromic = is_palindromic(y)
    if x_is_palindromic and not y_is_palindromic:
        return True
    if not x_is_palindromic and y_is_palindromic:
        return False
    return x <= y
    
# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)

arr = [1, 9, 3, 4, 7]
target = 5
sorted_arr = bubble_sort(arr,lambda x, y: compare_by_diff(x, y, target))
print("Sorted array by difference from target:", sorted_arr)
        
arr = [123, 121, 44, 78, 7]
sorted_arr = bubble_sort(arr,compare_by_palindromic)
print("Sorted by palindromic numbers first:", sorted_arr)