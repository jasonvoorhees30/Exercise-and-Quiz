#Open the mbox-short.txt file
fhand = open("mbox-short.txt")

#Create a list to store email addresses from lines starting with 'From '
list = []
for line in fhand:
    if not line.startswith("From "): 
        continue
    line = line.split()
    list.append(line[1])

#Create a dictionary containing keys and values for each email address
counts = {}
for word in list:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] = counts.get(word,0) + 1

#Create a tuple by considering the parameters (value, key) in the counts dictionary and then inserting it into tmp
tmp = []
for key, value in counts.items():
    newtup = (value, key)
    tmp.append(newtup)

#Sort tmp to get the order of values from highest
tmp = sorted(tmp, reverse = True)

print("The top three email addresses with the most message senders are:" )
#Take the 3 highest values ​​from tmp
for value, key in tmp[:3]:
    print(key, "with a total of", value, "messages")
