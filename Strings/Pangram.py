# Given a String, check if it contains all the alphabets.

# As simple as it seems, there are many tricky corner cases to be considered. 
# For example, case sensitivity, spaces, non - alphabets etc.

str = input().strip()   # Input String
alpset = set()          # Cache set which contains numeric ASCII values of case - insensitive alphabets.
count = 0               # Count var for number of unique alphabets.

for i in range(len(str)):
    cnum = ord(str[i])              # ASCII value of char
    if(cnum in range(65, 91)):      # If in CAPS, assign to small
        cnum += 32
    if(cnum not in alpset and cnum in range(97, 123)):
        count += 1
        alpset.add(cnum)
    if(count >= 26):
        break

if(count == 26):
    print('pangram')
else:
    print('not pangram')
