import string
punct = string.punctuation

#Unique word file romeo-short.txt
fhand = open("romeo-short.txt") #Open file
fread = fhand.read().lower() #Reads files and lowercases every capital letter in the file
fread = fread.translate(fread.maketrans('','',punct)) #Delete the punctuation on the file
fread = fread.split() #Split word by word on file
unique_word = {} #Initiate unique words dictionary
for word in fread: 
    if word not in unique_word: #Conditional to find unique words
        unique_word[word] = 1
    else :
        unique_word[word] = unique_word.get(word,0) + 1
print("Unique word dictionary in romeo-short.txt file: ")
print(unique_word) #Displays unique words and their number in dictionary form 
print(end="\n")
print ("The number of elements in the romeo-short.txt file is", len(unique_word), "elements") #Displays multiple dictionary elements

