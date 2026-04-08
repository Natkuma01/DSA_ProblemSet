"""
You are given a string items consisting of lowercase English letters and two integers x and y. You may repeatedly remove literal substrings from items to earn value:

Removing the substring "ab" earns x points.

Removing the substring "ba" earns y points.

You may perform these operations in any order and any number of times (as long as the substrings exist). Return the maximum total value you can obtain.
"""
# plan: if x is larger or y is larger, try to find the larger point
# use count to keep track
#   cdbcbbaaabab
#.       ij
# remove it after the substring is found
def maximum_value(items, x, y):
    ref = {"ab": x, "ba": y}
    higher_pt_pattern = max(ref, key=ref.get)       # get the higher point's pattern/ s1 -> "ba"
    higher_pt = 0
    items_lst = list(items)
    
    i = 0
    while i+1 < len(items_lst):
        if items_lst[i] != higher_pt_pattern[0] and items_lst[i+1] != higher_pt_pattern[1]:
            i += 1
        elif items_lst[i] == higher_pt_pattern[0] and items_lst[i+1] == higher_pt_pattern[1]:
            higher_pt += ref[higher_pt_pattern]
            del items_lst[i]
            del items_lst[i]
            i = 0
    return items_lst
    

s1 = "cdbcbbaaabab"
x1, y1 = 4, 5
print(maximum_value(s1, x1, y1))

s2 = "aabbaaxybbaabb"
x2, y2 = 5, 4
print(maximum_value(s2, x2, y2)) 