from collections import Counter
# Problem 1
def add_student_grade(grades, student_name, grade):
    for key, value in grades.items():
        if key == student_name:
            value.append(grade)
    if student_name not in grades:
        grades[student_name] = [grade]
    return grades


print("============ Problem 1 =================")

grades = {"Alice": [90, 85], "Bob": [70, 80]}
add_student_grade(grades, "Alice", 95)
add_student_grade(grades, "Charlie", 88)
print(grades)



# Problem 2
def find_pairs(nums, target):
    lst = []
    for item in nums:
        if isinstance(item, list):
            lst.extend(item)
        else:
            lst.append(item)

    res = []
    seen = set()
    for num in lst:
        complement = target - num
        if complement in seen:
            res.append((complement, num))
        seen.add(num)
    return res


print("============ Problem 2 =================")
nums = [1, 2, [3, 4], [5], 6]
target = 7
print(find_pairs(nums, target))



# Problem 3
# def dict_intersection(d1, d2):
#     return dict(d1.items() & d2.items())

def dict_intersection(d1, d2):
    result = {}
    for key in d1:
        if key in d2 and d1[key] == d2[key]:
            result[key] = d1[key]
    return result

print("============ Problem 3 =================")
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 4}
print(dict_intersection(d1, d2))



# Problem 4
# def sum_even_values(dictionary):
#     return sum(value for value in dictionary.values() if value % 2 == 0)

 	
def sum_even_values(dictionary):
    total = 0
    for value in dictionary.values():
        if value % 2 == 0:
            total += value
    return total


print("============ Problem 4 =================")
dictionary = {"a": 4, "b": 1, "c": 2, "d": 8, }
print(sum_even_values(dictionary))


# Problem 5
 	
def merge_catalogs(catalog1, catalog2):
    for product, price in catalog2.items():
        catalog1[product] = price
    return catalog1


print("============ Problem 5 =================")
catalog1 = {"apple": 1.0, "banana": 0.5}
catalog2 = {"banana": 0.75, "cherry": 1.25}
print(merge_catalogs(catalog1, catalog2))


# Problem 6
 
 	
def find_mode(lst):
    counts = {}
    for num in lst:
        counts[num] = counts.get(num, 0) + 1
    
    max_count = 0
    mode = lst[0]
    
    for num in lst:
        if counts[num] > max_count:
            max_count = counts[num]
            mode = num
    
    return mode

print("============ Problem 6 =================")
lst = [1,2,3,2,3,3,4,4,4,4,4]
mode = find_mode(lst)
print(mode)



# Problem 7
 
 	
def transpose_matrix(matrix):
    transposed = [ ]
    for c in range(len(matrix[0])):
        new_row = [ ]
        for r in range(len(matrix)):
            new_row.append(matrix[r][c])
        transposed.append(new_row)
    return transposed

print("============ Problem 7 =================")
matrix1 = [
    [1, 2],
    [3, 4]
]
print(transpose_matrix(matrix1))
matrix2 = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose_matrix(matrix2))


# Problem 8
 
 	
def smaller_numbers_than_current(nums):
    result = [ ]
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if j != i and nums[j] < nums[i]:
                count += 1
        result.append(count)
    return result


print("============ Problem 8 =================")
nums = [6,1,2,2,3]
print(smaller_numbers_than_current(nums))



# Problem 9
# def most_popular_genre(movies):
#     most = max(movies, key=lambda movie: movie["rating"])
#     return most["genre"]

 
 	
def most_popular_genre(movies):
    genre_totals = {}
    genre_counts = {}
    
    for movie in movies:
        genre = movie["genre"]
        rating = movie["rating"]
        genre_totals[genre] = genre_totals.get(genre, 0) + rating
        genre_counts[genre] = genre_counts.get(genre, 0) + 1
    
    highest_avg = 0
    best_genre = None
    
    for genre in genre_totals:
        avg = genre_totals[genre] / genre_counts[genre]
        if avg > highest_avg:
            highest_avg = avg
            best_genre = genre
    
    return best_genre

print("============ Problem 9 =================")
movies = [
    {"title": "Inception",
     "genre": "Science Fiction",
     "rating": 8.8
    },
    {"title": "The Matrix", 
     "genre": "Science Fiction",
     "rating": 8.7
    },
    {"title": "Pride and Prejudice", 
     "genre": "Romance",
     "rating": 7.8
    },
    {"title": "Sense and Sensibility", 
     "genre": "Romance",
     "rating": 7.7
    }
]
print(most_popular_genre(movies))