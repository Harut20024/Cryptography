import matplotlib.pyplot as plt
from collections import Counter
import string

def count_letters(sentence):
    sentence = sentence.lower()
    sentence = ''.join(filter(str.isalpha, sentence))  
    
    letter_counts = Counter(sentence)
    
    for letter in string.ascii_lowercase:
        if letter not in letter_counts:
            letter_counts[letter] = 0
    
    return letter_counts

def plot_letter_frequency(letter_counts):
    letters = list(letter_counts.keys())
    frequencies = list(letter_counts.values())
    
    plt.figure(figsize=(10, 6))
    plt.bar(letters, frequencies, color='blue')
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.title('Letter Frequency in Sentence')
    plt.show()

sentence = input("Enter a sentence: ")
letter_counts = count_letters(sentence)
plot_letter_frequency(letter_counts)
