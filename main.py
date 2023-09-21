def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

def sort_list(arr):
    return sorted(arr)

input_sequence = input("Введите последовательность чисел через пробел: ")
target_number = input("Введите любое число: ")

try:
    input_list = list(map(int, input_sequence.split()))
    target = int(target_number)

    sorted_list = sort_list(input_list)
    position = binary_search(sorted_list, target)

    if position >= len(sorted_list):
        print("Число не может быть вставлено в указанную позицию")
    else:
        sorted_list.insert(position, target)
        print(sorted_list)
except ValueError:
    print("Ошибка ввода данных. Пожалуйста, введите числа, разделенные пробелом.")
