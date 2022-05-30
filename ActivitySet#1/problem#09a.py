# Lists

fname = raw_input("Enter file name: ")
fo = open(fname)
l = list()                       
for line in fo:                    
    word = line.rstrip().split()    
    for element in word:               
        if element in l:         
            continue              
        else :                     
            l.append(element)         
l.sort()                         
print(l)                          
