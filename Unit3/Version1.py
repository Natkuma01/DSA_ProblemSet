# ================ Problem 1 ================
def vowel_count(s):
    count = 0
    vowel = "aeiouAEIOU"
    for char in s:
        if char in vowel:
            count += 1
    return count



my_str = "hello world"
my_str2 = "aAaAaAaAAA"
my_str3 = "ths strng s mssng vwls"
print("=========== Problem 1 ==============")
count1 = vowel_count(my_str)
print(count1)
count2 = vowel_count(my_str2)
print(count2)
count3 = vowel_count(my_str3)
print(count3)   


# ================ Problem 2 ================
def find_missing_positive(nums):
    for i in range (len(nums)):
        if i+1 != nums[i]:
            return i+1
    return i+2

print("=========== Problem 2 ==============")
nums1 = [1,2,3,5,6,10]
print(find_missing_positive(nums1))

nums2 = [1,2,3,4,5]
print(find_missing_positive(nums2))


# ================ Problem 3 ================
def word_pattern(pattern, s):
    words = s.split()

    char_to_word = {}             # a: dog
    word_to_char = {}            # dog: a
    for char, word in zip(pattern, words):
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            char_to_word[char] = word

        if word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            word_to_char[word] = char
    return True


print("=========== Problem 3 ==============")
pattern = "abba"
s = "dog cat cat dog"
print(word_pattern(pattern, s))
s2 = "dog cat cat fish"
print(word_pattern(pattern, s2))

pattern2 = "aaaa"
s3 = "dog cat dog cat"
print(word_pattern(pattern2, s3))
s4 = "dog dog dog dog"
print(word_pattern(pattern2, s4))


# ================ Problem 4 ================
def compress_string(my_str):
    res = ""
    i, j = 0, 1
    while j < len(my_str):
        if my_str[i] == my_str[j]:
            j += 1
        else: 
            my_str[i] != my_str[j]
            count = j - i
            res += my_str[i] + str(count)
            count = 0
            i = j
            j += 1
    if len(res) > len(my_str):
        return my_str
    else:
        return res
        



print("=========== Problem 4 ==============")
my_str = "aaaaabbcccd"
compressed_Str = compress_string(my_str)
print(compressed_Str)

my_str2 = "abcde"
compressed_Str2 = compress_string(my_str2)
print(compressed_Str2)

# ================ Problem 5 ================






# ================ Problem 6 ================


print("=========== Problem 6 ==============")



# ================ Problem 7 ================
def longest_uniform_substring(s):
    i, j = 0, 1
    count = []
    while j < len(s):
        if s[i] == s[j]:
            j += 1
        else:
            count.append(j-i)
            i = j
            j += 1
    return max(count)

print("=========== Problem 7 ==============")
s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2)


# ================ Problem 8 ================
def exclusive_elements(lst1, lst2):
    return list(set(lst1) ^ set(lst2))

print("=========== Problem 8 ==============")
lst1 = [3, 1, 8, 10]
lst2 = [4, 5, 3, 7, 8]
excl_lst = exclusive_elements(lst1, lst2)
print(excl_lst)


# ================ Problem 9 ================
def merge_alternately(word1, word2):
    res = ""
    for char1, char2 in zip(word1, word2):
        res += char1 + char2
    
    min_length = min(len(word1), len(word2))
    res += word1[min_length:]
    res += word2[min_length:]

    return res

print("=========== Problem 9 ==============")
word1 = "wol"
word2 = "oze"
print(merge_alternately(word1, word2))

word1 = "hfa"
word2 = "eflump"
print(merge_alternately(word1, word2))

word1 = "eyre"
word2 = "eo"
print(merge_alternately(word1, word2))
