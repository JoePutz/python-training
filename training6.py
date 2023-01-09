from datetime import datetime
datetime(2030, 4, 1) - datetime(2030, 1, 1)
#this will show datetime.timedelta(days=90)

datetime.datetime(2030, 1, 1) - datetime.now()
#will give the time between the current time and the other one

#This shows that these objects have properties that aren't normal methods. We didn't make anything to be able to see now() or anything

diff = datetime(2030, 1, 1) - datetime.now()
diff.days
#should be some huge number

now = datetime.now()
now.year 
#this should be the current year

bday = datetime(now.year, 6, 9)
if bday < now:
    bday = datetime(now.year + 1, 6, 9)
diff = bday - now
print(diff.days)
#should show the amount until the next bday


#what is a caesar cypher: all letters are mapped to another letter.

MAPPING = {
  'A': 'N', 
  'B': 'O', 
  'C': 'P', 
  'D': 'Q', 
  'E': 'R', 
  'F': 'S', 
  'G': 'T', 
  'H': 'U', 
  'I': 'V', 
  'J': 'W', 
  'K': 'X', 
  'L': 'Y', 
  'M': 'Z', 
  'N': 'A', 
  'O': 'B', 
  'P': 'C', 
  'Q': 'D', 
  'R': 'E', 
  'S': 'F', 
  'T': 'G', 
  'U': 'H', 
  'V': 'I', 
  'W': 'J', 
  'X': 'K', 
  'Y': 'L', 
  'Z': 'M'
}

#Mapping is a dictionary

def cipher(original):
    text = ""
    for letter in original:
        letter = letter.upper()
        new_letter = MAPPING(letter)
        text = text + new_letter
    return text

text = input("Text or secret: ")
result = cipher(text)
print(result)

#So this will show the input "TExt or secret:" you can input a secret message hit enter and then it will send out the changed text