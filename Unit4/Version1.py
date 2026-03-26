# ================ Problem 1 ================
def hunt(lst, target):
    if target not in lst:
        return -1
    count = 0
    for letter in lst:
        if letter == target:
            count += 1
    return count

print("================ Problem 1 ================")
items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
print(hunt(items, target))

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
print(hunt(items, target))

# ================ Problem 2 ================



# ================ Problem 3 ================
def bouncy_flouncy_trouncy_pouncy(operations):
    tigger = 1
    for word in operations:
        if word == "bouncy" or word == "flouncy":
            tigger += 1
        else:
            tigger -= 1
    return tigger


print("================ Problem 3 ================")
operations = ["trouncy", "flouncy", "flouncy"]
print(bouncy_flouncy_trouncy_pouncy(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(bouncy_flouncy_trouncy_pouncy(operations))



# ================ Problem 4 ================






# ================ Problem 5 ================







# ================ Problem 6 ================






# ================ Problem 7 ================







# ================ Problem 8 ================








