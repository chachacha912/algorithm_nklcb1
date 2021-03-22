def solution(arr1, arr2):
    answer = []
    for row_index, row_value in enumerate(arr1):
        column_array = []
        for column_index, column_value in enumerate(row_value):
            column_array.append(arr1[row_index][column_index] + arr2[row_index][column_index])
        answer.insert(row_index, column_array)
    return answer