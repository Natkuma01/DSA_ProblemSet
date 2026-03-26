# --- PROBLEM 1: Hundred Acre Wood ---
def welcome():
    print("Welcome to The Hundred Acre Wood!")

# --- PROBLEM 2: Greeting ---
 
 	
def greeting(name):
  pass
  print("Welcome to The Hundred Acre Wood " + name + "! My name is Christopher Robin.")

greeting("Michael")

# --- PROBLEM 3: Catchphrase ---
 
 	
def print_catchphrase(character):
    if character == "Pooh":
        print("Oh, bother!")    
    elif character == "Tigger":
        print("TTFN! Ta-ta for now!")
    elif character == "Eeyore":
        print("Thanks for noticing me.")    
    elif character == "Christopher Robin":
        print("Silly old bear!")
    else:
        print("Sorry! I don't know " + character + "'s catchphrase!")

# --- PROBLEM 4: Return Item ---
 
 	
def get_item(items, x):
    if 0 <= x < len(items):
        return items[x]
    return None

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
get_item(items, x)

# --- PROBLEM 5: Total Honey ---
def sum_honey(hunny_jars):
    total = 0
    for honey in hunny_jars:
        total += honey
    return total

hunny_jars = [2, 3, 4, 5]
sum_honey(hunny_jars)

# --- PROBLEM 6: Double Trouble ---
 
 	
def doubled(hunny_jars):
    doubled_list = []
    for honey in hunny_jars:
        doubled_list.append(honey * 2)
    return doubled_list

hunny_jars = [1, 2, 3]
doubled(hunny_jars)

# --- PROBLEM 7: Poohsticks ---
 
 	
def count_less_than(race_times, threshold):
    count = 0
    for time in race_times:
        if time < threshold:
            count += 1
    return count


race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
count_less_than(race_times, threshold)
# --- PROBLEM 8: Pooh's To Do's ---
 	
def print_todo_list(tasks):
    print("Pooh's To Dos:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

# --- PROBLEM 9: Pairs ---
 	
def can_pair(item_quantities):
    for quantity in item_quantities:
        if quantity % 2 != 0:
            return False
    return True
  
item_quantities = [2, 4, 6, 8]
can_pair(item_quantities)

# --- PROBLEM 10: Split Haycorns ---
 
 	
 
 	
def split_haycorns(quantity):
    divisors = []
    for i in range(1, quantity + 1):
        if quantity % i == 0:
            divisors.append(i)
    return divisors


quantity = 6
split_haycorns(quantity)

# --- PROBLEM 11: Thistle Hunt ---
  	
def locate_thistles(items):
    indices = []
    for i, item in enumerate(items):
        if item == "thistle":
            indices.append(i)
    return indices

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
locate_thistles(items)

# --- PROBLEM 12: Goldilocks Number ---
 
 	
def goldilocks_approved(nums):
    if len(nums) <= 2:
        return -1
    
    min_val = min(nums)
    max_val = max(nums)
    
    for num in nums:
        if num != min_val and num != max_val:
            return num
    
    return -1

nums = [3, 2, 1, 4]
goldilocks_approved(nums)

# --- PROBLEM 13: Count Vowels ---
 
 	
def count_vowels(sentence):
    vowels = "aeiou"
    count = 0
    for char in sentence.lower():
        if char in vowels:
            count += 1
    return count
  
sentence = "The quick brown fox jumps over the lazy dog"
count_vowels(sentence)

# --- PROBLEM 14: Acronym ---

 	
def is_acronym(words, s):
    acronym = ""
    for word in words:
        acronym += word[0]
    return acronym == s                

words = ["christopher", "robin", "milne"]
s = "crm"
is_acronym(words, s)

# ==========================================
# GRADING TESTER (Terminal Output)
# ==========================================

def run_tests():
    divider = "________________________________________\n"


    print("================ GRADE ==========================")

    print(f"{divider}Problem 1: Hundred Acre Wood")
    welcome()

    print(f"{divider}Problem 2: Greeting")
    greeting("Michael")
    greeting("Winnie the Pooh")

    print(f"{divider}Problem 3: Catchphrase")
    print_catchphrase("Pooh")
    print_catchphrase("Piglet")

    print(f"{divider}Problem 4: Return Item")
    print(get_item(["piglet", "pooh", "roo", "rabbit"], 2))
    print(get_item(["piglet", "pooh", "roo", "rabbit"], 5))

    print(f"{divider}Problem 5: Total Honey")
    print(sum_honey([2, 3, 4, 5]))
    print(sum_honey([]))

    print(f"{divider}Problem 6: Double Trouble")
    print(doubled([1, 2, 3]))

    print(f"{divider}Problem 7: Poohsticks")
    print(count_less_than([1, 2, 3, 4, 5, 6], 4))
    print(count_less_than([], 4))

    print(f"{divider}Problem 8: Pooh's To Do's")
    print_todo_list(["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"])
    print_todo_list([])

    print(f"{divider}Problem 9: Pairs")
    print(can_pair([2, 4, 6, 8]))
    print(can_pair([1, 2, 3, 4]))
    print(can_pair([]))

    print(f"{divider}Problem 10: Split Haycorns")
    print(split_haycorns(6))
    print(split_haycorns(1))

    print(f"{divider}Problem 11: Thistle Hunt")
    print(locate_thistles(["thistle", "stick", "carrot", "thistle", "eeyore's tail"]))
    print(locate_thistles(["book", "bouncy ball", "leaf", "red balloon"]))

    print(f"{divider}Problem 12: Goldilocks Number")
    print(goldilocks_approved([3, 2, 1, 4]))
    print(goldilocks_approved([1, 2]))
    print(goldilocks_approved([2, 1, 3]))

    print(f"{divider}Problem 13: Count Vowels")
    print(count_vowels("The quick brown fox jumps over the lazy dog"))
    print(count_vowels("Python"))

    print(f"{divider}Problem 14: Acronym")
    print(is_acronym(["christopher", "robin", "milne"], "crm"))
    print(f"{divider}")

if __name__ == "__main__":
    run_tests()