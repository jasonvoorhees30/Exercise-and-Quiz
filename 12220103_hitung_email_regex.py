#Calling the regular expression library
import re

#Open the mbox-short.txt file
fhand = open("mbox-short.txt")

#Create a list to store email addresses from lines starting with 'From ' with the help of regex
list = []
for line in fhand:
    x = re.findall('^From ([a-zA-Z0-9]\S*@\S*[a-zA-Z0-9])', line)
    if len(x) > 0:
        list.append(x[0])     
        
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

#Sort tmp to get the order of values ​​from highest
tmp = sorted(tmp, reverse = True)

print("The order of unique email addresses in mbox-short.txt with the highest number is as follows:")
for v, k in tmp:
    print("Email address", k, "with an amount of", v)
