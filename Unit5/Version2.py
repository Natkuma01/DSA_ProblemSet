# ================ Problem 1 ================
def count_unique_anagrams(words):
    sorted_lst = []
    for word in words:
        sorted_lst.append("".join(sorted(word)))
    
    unique = set(sorted_lst)

    return len(unique)
print("================ Problem 1 ================")
print(count_unique_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # Output: 3
print(count_unique_anagrams(["a", "b", "c", "a"]))                       # Output: 3
print(count_unique_anagrams([]))                                        # Output: 0


# ================ Problem 2 ================
def wealthiest_customer(accounts):
    total = 0
    max_money = 0
    index = 0

    for i, value in enumerate(accounts):
        total = sum(value)
        if total > max_money:
            max_money = total
            index = i
    return [index, max_money]
        

print("================ Problem 2 ================")
accounts = [
  [1, 2, 3],
  [3, 2, 1]
]
print(wealthiest_customer(accounts))

accounts = [
  [1, 5],
  [7, 3],
  [3, 5]
]
print(wealthiest_customer(accounts))

accounts = [
  [2, 8, 7],
  [7, 1, 3],
  [1, 9, 5]
]
print(wealthiest_customer(accounts))


# ================ Problem 3 ================
def smaller_than_current(nums):
    res = []
    count = 0
    for i, num in enumerate(nums):
        for j in range (len(nums)):
            if i != j and num > nums[j]:
                count += 1

        res.append(count)
        count = 0
    return res
        

print("================ Problem 3 ================")
nums = [8, 1, 2, 2, 3]
print(smaller_than_current(nums))

nums = [6, 5, 4, 8]
print(smaller_than_current(nums))

nums = [7, 7, 7, 7]
print(smaller_than_current(nums))


# ================ Problem 4 ================
def diagonal_sum(grid):
    if len(grid) == 1:
        return grid[0][0]
    nums = []
    temp = 0
    total = 0
    for i in range (len(grid)):                     # get the primary diagonal
        temp += grid[i][i]
    nums.append(temp)

    i = 0                                           # get the second diagonal
    while i < len(grid)-1:
        for j in range(len(grid)-1, -1, -1):
            nums.append(grid[i][j])
            i += 1

    total = sum(nums)

    center = len(grid) // 2

    if len(grid) % 2 != 0:                          # if len(grid) is an odd number, remove the center num
        total -= grid[center][center]

    return total

    

print("================ Problem 4 ================")
grid = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
print(diagonal_sum(grid))
# [0][0], [1][1], [2][2] | [0][2], [1][1], [2][0]

grid = [
  [1, 1, 1, 1],
  [1, 1, 1, 1],
  [1, 1, 1, 1],
  [1, 1, 1, 1]
]
print(diagonal_sum(grid))
# [0][0], [1][1], [2][2], [3][3] | [0][3], [1][2], [2][1], [3][0]

grid = [
  [5]
]
print(diagonal_sum(grid))



# ================ Problem 5 ================


print("================ Problem 5 ================")



# ================ Problem 6 ================
def transpose_matrix(matrix):
  res = []
  for i in range (len(matrix[0])):
      temp = []
      for j in range (len(matrix)):
          temp.append(matrix[j][i])
      res.append(temp)
  return res

print("================ Problem 6 ================")
matrix = [
  [1, 2, 3],
  [4, 5, 6]
]
print(transpose_matrix(matrix))
# [0][0], [1][0] | [0][1], [1][1] | [0][2], [1][2]

matrix = [
  [1, 2],
  [3, 4],
  [5, 6]
]
print(transpose_matrix(matrix))
# [0][0], [1][0], [2][0] | [0][1], [1][1], [2][1]