def merge_sort(arr,low,high,compare_fn=(lambda x, y: x <= y)):
    if not arr:
        return arr
    if low >= high:
        return
    mid = low+(high-low)//2
    merge_sort(arr,low,mid,compare_fn)
    merge_sort(arr,mid+1,high,compare_fn)
    merge(arr,low,mid,high,compare_fn)

def merge(arr,low,mid,high,compare_fn):
    left_index = low
    right_index = mid+1
    
    merged = []
    
    while left_index <= mid and right_index <= high:
        if compare_fn(arr[left_index],arr[right_index]):
            merged.append(arr[left_index])
            left_index+=1
        else:
            merged.append(arr[right_index])
            right_index+=1
    if left_index <= mid:
        merged.extend(arr[left_index:mid+1])
    if right_index <= high:
        merged.extend(arr[right_index:high+1])
    
    for i in merged:
        arr[low] = i
        low+=1
                  
def merge_in_place(arr,low,mid,high):
    left_index = low
    right_index = mid+1
    
    while left_index <= mid and right_index <= high:
        if arr[left_index] <= arr[right_index]:
            left_index += 1
        else:
            value = arr[right_index]
            for k in range(right_index, left_index, -1):
                arr[k] = arr[k - 1]
            arr[left_index] = value

            left_index += 1
            mid += 1
            right_index += 1
            
def compare_absolute_values(n1,n2):
    return abs(n1) <= abs(n2)

def capital_first(x, y):
    # Check if both characters are capital or lowercase
    if x.isupper() and y.islower():
        return True
    elif x.islower() and y.isupper():
        return False
    # If both are the same case, compare normally
    return x <= y

def odd_first(x, y):
    # Check if both characters are capital or lowercase
    if x%2==1 and y%2==0:
        return True
    elif x%2==0 and y%2==1:
        return False
    # If both are the same case, compare normally
    return x <= y

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_before_non_prime(n1, n2):
    if is_prime(n1) and not is_prime(n2):
        return True
    elif not is_prime(n1) and is_prime(n2):
        return False
    else:
        return n1 <= n2 
    
    
    
    
# arr = [38, -27, 43, 3, 9, -82, -10]
# arr = ['z', 'A', 'b', 'C', 'd', 'E']
# arr = [4, 3, 2, 5, 1, 6]
arr = [4, 3, 2, 5, 1, 6, 7, 9]
print("unsorted array:", arr)
merge_sort(arr, 0, len(arr) - 1,prime_before_non_prime)
print("Sorted Array:", arr)
    
        