#t = input("Enter:")
#words = t.lower().split() 
#wordcount = {}
#for word in words:
    #if word in wordcount:
        #wordcount[word] += 1
    #else:
        #wordcount[word] = 1

#m = max(wordcount, key=wordcount.get)
#print(m)


t = input("Enter:")
words = t.lower().split() 
unique = set(words)
print(len(unique))