def partition(nums, low, high):
    pivot = nums[low]
    i = low
    j = high
    while i < j:
        while i <= high and nums[i] <= pivot:
            i += 1
        while j >= low and nums[j] > pivot:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[low], nums[j] = nums[j], nums[low]
    return j

def quick_sort(nums, low, high):
    if low < high:
        pivot_index = partition(nums, low, high)
        quick_sort(nums, low, pivot_index - 1)
        quick_sort(nums, pivot_index + 1, high)


arr = [64, 34, 25, 12, 22, 12, 12, 11, 90]
quick_sort(arr, 0, len(arr) - 1)
print(f"Sorted array = {arr}")