
sentence = input("Enter a sentence: ") # user input
words = sentence.split() # splits sentence into words
print(f'Words in sentence are: {words}') # displays words in sentence
print(f'Number of words in sentence is: {len(words)}') # counts number of words in sentence
print(f'The last word is: {words[-1]}') # displays last word in the sentence
reversed_sentence = " ".join(reversed(words)) # joins reversed words into a string
print(f'The sentence in reverse is: {reversed_sentence}') # displays the reversed sentence
words.sort() # sorts the list alphabetically
sorted_sentence = " ".join(words) # joins sorted words into a string
print(f'The sentence words in alphabetical order are: {sorted_sentence}') # displays sentence words sorted alphabetically
