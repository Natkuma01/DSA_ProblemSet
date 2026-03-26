from collections import Counter
# ============ Problem 1 ================
def cast_vote(votes, candidate):
    if candidate in votes:
        votes[candidate]
    else:
        votes[candidate] = 1
    return votes

print("============= Problem 1 =================")
votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(cast_vote)
print(votes)


# ============ Problem 2 ================
 
 	
def nested_sum(nums):
    total = 0
    for subset in nums:
        total += sum(subset)
    return total

print("============= Problem 2 =================")
nums = [[1, 2, 3], [4, 5], [6]]
print(nested_sum(nums))

# ============ Problem 3 ================
 
 	
def flatten_list(nested_list):
    flattened = []
    for subset in nested_list:
        for item in subset:
            flattened.append(item)
    return flattened


print("============= Problem 3 =================")
nested_list = [[1, 2], [3, 4], [5, 6]]
print(flatten_list(nested_list))


# ============ Problem 4 ================
 
def find_key(nested_dict, key):
    for inner_dict in nested_dict.values():
        if key in inner_dict:
            print(inner_dict[key])
            return
    print("None")


print("============= Problem 4 =================")
nested_dict = {
    "a": {"name": "Alice", "age": 25},
    "b": {"name": "Bob", "age": 30},
    "c": {"name": "Charlie", "age": 35}
}
key = "name"
print(find_key(nested_dict, key))

# ============ Problem 5 ================
def count_occurrences(nums):
    occurences = {}
    for num in nums:
        if num in occurences:
            occurences[num] += 1
        else:
            occurences[num] = 1 
    print(occurences)

print("============= Problem 5 =================")
nums = [1, 2, 2, 3, 3, 3, 4]
print(count_occurrences(nums)) 


# ============ Problem 6 ================
 
 	
def restock_inventory(current_inventory, restock_list):
    for item, amount in restock_list.items():
        if item in current_inventory:
            current_inventory[item] += amount
        else:
            current_inventory[item] = amount
    return current_inventory

print("============= Problem 6 =================")
current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}  
print(restock_inventory(current_inventory, restock_list))



# ============ Problem 7 ================
def calculate_gpa(report_card):
    total_points = 0
    num_classes = 0
    grade_points = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}

    for subject, grade in report_card.items():
        total_points += grade_points[grade]
        num_classes += 1

    if num_classes == 0:
        return 0
    return (total_points / num_classes)

print("============= Problem 7 =================")
report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))



# ============ Problem 8 ================
def has_duplicates(nums, k):
    if k > len(nums):
        return False

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if j - i >= k:
                break
            if nums[i] == nums[j]:
                return True

    return False
      
print("============= Problem 8 =================")
nums = [5, 6, 8, 2, 6, 4, 9]
check1 = has_duplicates(nums, 3)
print(check1)
check2 = has_duplicates(nums, 5)
print(check2)



# ============ Problem 9 ================
def highest_rated(books):
    highest = 0
    best_book = ""
    for book in books:
        if book["rating"] > highest:
            highest = book["rating"]
            best_book = book
    print(best_book)
# return max(books, key=lambda book: book["rating"])

print("============= Problem 9 =================")
books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]
print(highest_rated(books))