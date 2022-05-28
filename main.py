# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from tabnanny import check


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = input("Enter the first word: ")
    anagram = input("Enter the second word: ")

    str1 = word.lower()
    str2 = anagram.lower()

    if(sorted(str1) == sorted(str2)):

        return True
    else:
        return False

str1="elbow"
str2="below"
print(find_anagram(str1,str2))