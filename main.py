import hashlib
wlist=input("wordlist: ")
hash2crack=input("hash: ")

wlistlines=open(wlist,"r").readlines()
print(wlistlines)


for i in range(0,len(wlistlines)):
    hash2comp=hashlib.md5(wlistlines[i].replace("\n","").encode()).hexdigest()

    if(hash2crack==hash2comp):
        print("password found: "+wlistlines[i].replace("\n"," "))
        exit()

print("Password Not Found")