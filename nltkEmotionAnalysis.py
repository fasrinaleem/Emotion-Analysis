import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

# Reading the data
text = open('read.txt', encoding='utf-8').read()
#print("Read Data: " + text)

# Converting the letter into lowercase
lower_case = text.lower()
#print("Convert Lowercase: " + lower_case)

# Removing Punctuations --> 1
# Importing String Library
# All Punctuations available in Python
# print("All Punctuations :" + string.punctuation)

# Removing Punctuations --> 2
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
#print("Remove Punctuation : " + cleaned_text)

# Tokenizing
# Break the sentence into words and save it an array
tokenized_words = word_tokenize(cleaned_text, "english")
print(tokenized_words)

# We need to remove from tokenized word (stop words)
final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

print(final_words)

# NLP Emotion Algorithm
# Remove extra space in line
emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        #print(clear_line)
        # Separate words and emotions
        # Anything before : save to words and anything after : save to emotion
        word, emotion = clear_line.split(':')
        #Check our final word is inside this or not
        # print("Word: " + word + " " + "Emotion: " + emotion)
        # If word is present -> Add the emotion to list
        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)
#Printing how manytimes they are present
w = Counter(emotion_list)
print(w)

#Create the bar graph
# Key -> What emotions are present
# Values -> No of times
fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
# Automatically update the x axis and y axis to make sure all values are presented properly
fig.autofmt_xdate()
#Save graph as an image in project
plt.savefig('nltkGraph.png')
plt.show()