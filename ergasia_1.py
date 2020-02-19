file=raw_input("File Path: ")
words=[]
N=len(words)
vowels=["a","e","i","o","u","y"]
reve=[]
rev=""
with open(file,'r') as f:
    for line in f:
        for word in line.split():
           words.append(word)
for i in range(N):
    words[i]=words[i].strip()
words.sort(key=len)
for i in range(-1,-6,-1):
    for chr in words[i]:
        if chr not in vowels:
            rev=rev+chr
    reve.insert(i,rev)
    rev=""
for item in reve:
    print item


        

               



