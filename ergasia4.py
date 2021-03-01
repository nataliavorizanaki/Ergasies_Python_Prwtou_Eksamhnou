import random
import string
import os
file_name = input("Please insert file name  ")
file_name.strip()
if os.path.exists(file_name):
   infile = open(file_name, 'r')
else:
   print("The file does not exist")
   flag = True
   while flag == True:
       file_name = input("Please insert file name again   ")
       if os.path.exists(file_name):
           infile = open(file_name, 'r')
           flag = False
       else:
           continue

firstlist=[]
line=infile.readline()
result = ""



for c in line:
    c.replace("\n","")
    c.replace("\t","")
    c.replace("\r","")
    c.replace("\x0b","")
    c.replace("\x0c","")
    #If char is not punctuation, add it to the result.
    if c not in string.punctuation:
            result += c
            line = result

listV = line.splitlines()

while (line !="") :
 listV = line.splitlines()
 #print(listV)
 line = infile.readline()
 for c in line:
    c.replace("\t","")
    c.replace("\r","")
    c.replace("\x0b","")
    c.replace("\x0c","")
    # If char is not punctuation, add it to the result.
    if c not in string.punctuation:
            result += c
            line = result



 # remove space
for substring in listV:
     substring_split = substring.split(" ")
     #print(substring_split)
     firstlist.extend(substring_split)
#print(listV)

#print(firstlist)
infile.close()

mhkos = len(firstlist)
i = 0
finallist = []
u = mhkos
flag = True
while flag == True:
 if u - 2  >= 3:
     finallist.append(firstlist[i] + " " + firstlist[i+1] + " " + firstlist[i+2])
     i = i + 1
     u = mhkos - i
 else:
     flag = False
#print(finallist)

randomtriad = random.choice(finallist)
position = randomtriad.find(" ")
#print(position)
twolastwords = randomtriad[position+1:]
#print(twolastwords)
#print(len(finallist))
fname = input("Insert file name to show the results:  ")
filename = fname.strip()
outfile = open("{}".format(filename), 'w')
words = 0
while ((words <= 200) and (finallist != [])):
  randomtriad=random.choice(finallist)
  position=randomtriad.find(" ")
  #print(position)
  twolastwords=randomtriad[position+1:]
  #print(twolastwords)
  for fl in finallist:
    if (fl.startswith(twolastwords) == True):
       outfile.writelines(fl.replace(twolastwords,"").strip() + " ")
       words = words + 3
       if (randomtriad == fl):
             finallist.remove(fl)
       else:
             continue
    else:
        continue

outfile.close()
