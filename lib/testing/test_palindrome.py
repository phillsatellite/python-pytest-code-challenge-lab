from palindrome import longest_palindromic_substring

#Constraints / Assumptions 
# 1 <= s.length <= 1000
# s consists of only digits and english letters

'''
Test 1 - Testing multi valid palindromes
Innput: babad
Output: bab or aba 
'''

def test_multi_valid_palindrome():
    assert longest_palindromic_substring('babad') in ['bab', 'aba']

'''
Test 2 - Longest palindrome in cbbd 
Input: cbbd 
Output: bb
'''

def test_palindrome_in_cbbd():
    assert longest_palindromic_substring('cbbd') == "bb"

'''
Test 3 - Testing single characters 
Input: a 
Output: a
'''

def test_single_character_palindrome():
    assert longest_palindromic_substring('a') == 'a'

'''
Test 4 - Either single characters are valid
Input: ac 
Output: a or c
'''

def test_either_single_chars():
    assert longest_palindromic_substring('ac') in ['a', 'c']

'''
Test 5 - Testing an entire string
Input: racecar
Output: racecar
'''

def test_entire_string():
    assert longest_palindromic_substring('racecar') == 'racecar'

'''
Test 6 - Testing with all the same chars 
Input: aaaaa
Output: aaaaa
'''

def test_all_same_letters():
    assert longest_palindromic_substring('aaaaa') == 'aaaaa'

'''
Test 7 - Palindrome in a numeric string
Input: 123321456
Output: 123321
'''

def test_numeric_strings():
    assert longest_palindromic_substring('123321456') == '123321'

'''
Test 8 - Palindrome with numbers and letters 
Input: a1b2b1a
Output: a1b2b1a
'''

def test_mixed_numbers_letters():
    assert longest_palindromic_substring('a1b2b1a') == 'a1b2b1a'