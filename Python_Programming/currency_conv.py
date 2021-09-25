#defining a function curconv() which will take currency and amount as input and then convert and return the amount in US dollars 
def curconv(currency, amount):
    infile = open('currencies.txt')

#declaring counter 

  
#reading and splitting the file to separate words
    content  = infile.read()
    wordList = content.split("  ")
    infile.close()
    count=0
    for line in wordList:
        count += 1
        #print("{}: {}".format(count, line.strip()))
    
#checking if currency from the user matches in the file 
    for ch in wordList:
        print (ch[0:3])
        print (ch[4])
#        print (ch)

curconv('Eur', 100 )