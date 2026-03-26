print ("========= Problem 5 ============")
## Problem 5
def sum_honey(hunny_jars):
  pass                         
  total = 0
  for jars in hunny_jars:
    total += jars
  print(total)                          # <--- usually use return here 

hunny_jars = [2, 3, 4, 5]
hunny_jars = []
sum_honey(hunny_jars)                  # change this to print(sum_honey(hunny_jars))


# remove the pass : pass is only used when a function has no code yet. 
# Since your function already calculates and prints the total, pass should be removed.

# explain on PRINT and RETURN
# print → shows something on the screen (for humans)
# return → sends a value back to the program (for code to use)

print ("========= Problem 6 ============")

# Problem 6
def doubled(hunny_jars):
  for jars in hunny_jars:
        jars *= 2
  print(jars)               # <---use return here, indextation is correct. return jars

hunny_jars = [1, 2, 3]
doubled(hunny_jars)        # <----- print(doubled(hunny_jars))
                           # when you do dobuled(hunny_jars), you are calling the function, so you need
                           #  to add print to print it out. Then the output will be a list
                           # expected output: [2, 4, 6]


print ("========= Problem 12 ============")

# Problem 12
def goldilocks_approved(nums):
    nums.sort()
    middle_index = len(nums) // 2
    print(nums[middle_index])

nums = [3, 2, 1, 4]
goldilocks_approved(nums)

nums = [1, 2]
goldilocks_approved(nums)

nums = [2, 1, 3]
goldilocks_approved(nums)

# in the question, you need to return -1 if the list do not have the middle number,
# so for test case number 2 - nums = [1, 2], should return -1
# you can add en edge case like if len(nums) <= 2: return -1 then keep going with the nums.sort()...


