a = str(input()) #test input
b = str(input()) #test input


def anagram(a, b): #main function
    if sorted(a)==sorted(b):
        return True  #Strings are anagram
    else:
        return False #Strings are not anagram

print(anagram(a, b)) #run function