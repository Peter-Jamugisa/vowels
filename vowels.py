def vowel(letter):
    
    if 'a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word:
        print ("yes all vowels are there")
    # elif 'A' in word and 'E' in word and 'I' in word and 'O' in word and 'U' in word:
        # print ("yes all vowels are there")
    else:
        print("it doesn't have all vowels")
word=input("enter a word")
word=word.casefold()
vowel(word)