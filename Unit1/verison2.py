# --- PROBLEM 1: Mad Libs ---
def madlib(verb):
    print(f"I have one power. I never {verb}. - Batman")

# --- PROBLEM 2: Trilogy ---
 
 	
def trilogy(year):
    if year == 2005:
        print('"Batman Begins"')
    elif year == 2008:
        print('"The Dark Knight"')
    elif year == 2012:
        print('"The Dark Knight Rises"')
    else:
        print(f'"Christopher Nolan did not release a Batman movie in {year}."')

# --- PROBLEM 3: Last ---
 
 	
def get_last(items):
    if len(items) == 0:
        return None
    return items[-1]

# --- PROBLEM 4: Concatenate ---
def concatenate(words):
    result = ""
    for word in words:
        result += word
    return result

# --- PROBLEM 5: Squared ---
 
 	
def squared(numbers):
    result = [ ]
    for num in numbers:
        result.append(num ** 2)
    return result

# --- PROBLEM 6: NaNaNa Batman! ---
 
 	
def nanana_batman(x):
    na_part = ""
    for i in range(x):
        na_part += "na"
    
    if na_part:
        print(na_part + " batman!")
    else:
        print("batman!")

# --- PROBLEM 7: Find the Villain ---
 
 	
def find_villain(crowd, villain):
    indices = [ ]
    for i in range(len(crowd)):
        if crowd[i] == villain:
            indices.append(i)
    return indices

# --- PROBLEM 8: Up and Down ---
 
 	
def up_and_down(lst):
    odd_count = 0
    even_count = 0
    
    for num in lst:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    return odd_count - even_count

# --- PROBLEM 9: Running Sum ---
 
 	
def running_sum(superhero_stats):
    for i in range(1, len(superhero_stats)):
        superhero_stats[i] += superhero_stats[i - 1]
    return superhero_stats

# --- PROBLEM 10: Reverse Pairs ---
 
 	
def reverse_pairs(pairs):
    result = [ ]
    n = len(pairs) // 2
    
    for i in range(n):
        result.append(pairs[i + n])
        result.append(pairs[i])
    
    return result

# --- PROBLEM 11: String Array Equivalency ---
 
 	
def are_equivalent(word1, word2):
    str1 = ""
    str2 = ""
    
    for w in word1:
        str1 += w
        
    for w in word2:
        str2 += w
        
    return str1 == str2

# --- PROBLEM 12: Count Even Strings ---
 
 	
def count_evens(lst):
    count = 0
    for s in lst:
        if len(s) % 2 == 0:
            count += 1
    return count

# --- PROBLEM 13: Secret Identity ---
 
 	
def remove_name(people, secret_identity):
    i = 0
    while i < len(people):
        if people[i] == secret_identity:
            people.pop(i)
        else:
            i += 1
    return people

# --- PROBLEM 14: Count Digits ---
def count_digits(n):
    if n == 0:
        return 1

    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

# ==========================================
# GRADING TESTER (Terminal Output)
# ==========================================

def run_tests():
    line = "________________________________________"
    
    print(f"{line}\nProblem 1: Mad Libs")
    madlib("give up")
    madlib("nap")

    print(f"{line}\nProblem 2: Trilogy")
    trilogy(2008)
    trilogy(1998)

    print(f"{line}\nProblem 3: Last")
    print(get_last(["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]))
    print(get_last([]))

    print(f"{line}\nProblem 4: Concatenate")
    print(f"'{concatenate(['vengeance', 'darkness', 'batman'])}'")
    print(f"'{concatenate([])}'")

    print(f"{line}\nProblem 5: Squared")
    print(squared([1, 2, 3]))

    print(f"{line}\nProblem 6: NaNaNa Batman!")
    nanana_batman(6)
    nanana_batman(0)

    print(f"{line}\nProblem 7: Find the Villain")
    print(find_villain(['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker'], 'The Joker'))

    print(f"{line}\nProblem 8: Up and Down")
    print(up_and_down([1, 2, 3]))
    print(up_and_down([1, 3, 5]))
    print(up_and_down([2, 4, 10, 2]))

    print(f"{line}\nProblem 9: Running Sum")
    print(running_sum([1, 2, 3, 4]))
    print(running_sum([3, 1, 2, 10, 1]))

    print(f"{line}\nProblem 10: Reverse Pairs")
    print(reverse_pairs([1, 2, 3, 4, 5, 6]))
    print(reverse_pairs(['Batman', 'Robin', 'The Joker', 'Harley Quinn']))

    print(f"{line}\nProblem 11: String Array Equivalency")
    print(are_equivalent(["bat", "man"], ["b", "atman"]))
    print(are_equivalent(["alfred", "pennyworth"], ["alfredpenny", "word"]))

    print(f"{line}\nProblem 12: Count Even Strings")
    print(count_evens(["na", "nana", "nanana", "batman", "!"]))
    print(count_evens(["the", "joker", "robin"]))

    print(f"{line}\nProblem 13: Secret Identity")
    print(remove_name(['Batman', 'Superman', 'Bruce Wayne', 'The Riddler', 'Bruce Wayne'], 'Bruce Wayne'))

    print(f"{line}\nProblem 14: Count Digits")
    print(count_digits(964))
    print(count_digits(0))
    print(line)

if __name__ == "__main__":
    run_tests()