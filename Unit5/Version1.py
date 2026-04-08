# ================ Problem 1 ================
def longest_palindromic_substring(s):
    if len(s) <= 1:
        return s

    i, j = 0, len(s) - 1

    substring = ""
    res = []

    for i in range (len(s)):
        for j in range (i, len(s)):
            substring = s[i:j+1]
            if substring == substring[::-1]:
                res.append(substring)
            
    return max(res, key=len) 
print("================ Problem 1 ================")
print(longest_palindromic_substring("babad"))  # Output: "bab" or "aba"
print(longest_palindromic_substring("cbbd"))   # Output: "bb"
print(longest_palindromic_substring("a"))      # Output: "a"
print(longest_palindromic_substring(""))      # Output: ""



# ================ Problem 2 ================
def remove_adjacent_duplicates(s):
    unique = set(s)
    return "".join(unique)

print("================ Problem 2 ================")
print(remove_adjacent_duplicates("aabbccdde"))  # Output: "abcde"
print(remove_adjacent_duplicates("bookkeeper"))  # Output: "bokeper"


# ================ Problem 3 ================
# [0][0], [1][0], [2][0]
def rotate_matrix_90(matrix):
    res = []
    for i in range (len(matrix)):
        temp = []
        for j in range (len(matrix[0])):
            temp.append(matrix[j][i])
        temp = temp[::-1]
        res.append(temp)
    return res
        


print("================ Problem 3 ================")
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
print(rotate_matrix_90(matrix))
print(rotate_matrix_90([[1]]))  # Output: [[1]]
print(rotate_matrix_90([]))  # Output: []


# ================ Problem 4 ================
def merge_intervals(intervals):
    res = []
    i = 0
    while i < len(intervals)-1:
        if intervals[i][1] > intervals[i+1][0] and intervals[i][1] < intervals[i+1][1]:
            res.append([intervals[i][0], intervals[i+1][1]])
            i += 2
        else:
            res.append(intervals[i])
            i += 1
    
    if intervals[-1] != res[-1]:
        res.append(intervals[-1])

    return res


print("================ Problem 4 ================")
print(merge_intervals([[1, 3], [2, 4], [5, 7], [6, 8]]))
# Output: [[1, 4], [5, 8]]

print(merge_intervals([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]))
# Output: [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]



# ================ Problem 5 ================
def find_missing_clues(clues, lower, upper):
    res = []

    for i in range (1, len(clues)-1):
        temp = []
        if clues[i+1] - clues[i] > 1:
            temp.append(clues[i]+1)
            temp.append(clues[i+1]-1)
        res.append(temp)
    
    if clues[-1] != upper:
        temp = [clues[-1]+1, upper]
        res.append(temp)
    return res

print("================ Problem 5 ================")
clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(find_missing_clues(clues, lower, upper))
# Output: [[2, 2], [4, 49], [51, 74], [76, 99]]

clues = [-1]
lower = -1
upper = -1
print(find_missing_clues(clues, lower, upper))
# Output: []


# ================ Problem 6 ================
def harvest(vegetable_patch):
    count = 0
    for i in range (len(vegetable_patch)):
        for j in range(len(vegetable_patch[0])):
            if vegetable_patch[i][j] == 'c':
                count += 1
    return count


print("================ Problem 6 ================")
vegetable_patch = [
  ['x', 'c', 'x'],
  ['x', 'x', 'x'],
  ['x', 'c', 'c'],
  ['c', 'c', 'c']
]
print(harvest(vegetable_patch))  # Output: 6