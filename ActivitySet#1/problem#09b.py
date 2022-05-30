fop = open("mbox-short.txt")
c = 0
for l in fop:
    l = l.rstrip()
    if l == "": continue
        
    words = l.split()
    if words[0] !="From": continue
        
    print(words[1])
    c += 1

print ("There were", c, "lines in the file with From as the first word")