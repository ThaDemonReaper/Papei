file=raw_input("File Path: ")
words=[]
N=len(words)
chars=["f","c","k","r"]
with open(file,'r') as f:
    for line in f:
        for word in line.split():
           words.append(word)
for i in range(N):
    words[i]=words[i].strip()
counter=0
cntr=0
for i in range(len(words)):
    for j in words[i]:
        if j in chars:
            counter=counter+1
        else:
            cntr=cntr+1
    if counter>cntr:
        print "the word is bad"
    else:
        print "the word is good"
    cntr=0
    counter=0
        
