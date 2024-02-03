
# test sentence
# the quick brown fox jumped over the lazy dog

sentence = input("\nEnter a sentence: ") # user input

# splits sentence into words and displays them as a list
words = sentence.split() 
print(f'\nList of words in sentence: {words}') 

# counts number of words in the sentence
print(f'Number of words in sentence is: {len(words)}') 

# displays last word in the sentence
print(f'The last word is: {words[-1]}') 

# joins reversed words into a string and displays them
reversed_sentence = " ".join(reversed(words)) 
print(f'The sentence in reverse is: {reversed_sentence}') 

# sorts the list alphabetically, joins them, displays them
words.sort() 
sorted_sentence = " ".join(words) 
print(f'The sentence words in alphabetical order are: {sorted_sentence}') 


