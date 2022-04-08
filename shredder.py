import os
#from time import sleep  #Use for observation

def shred(file):
    with open(file, 'rb') as f:
        data = f.read()
    
    with open(file, 'wb') as f:
        f.write(os.urandom(len(data)))

def shredder(file):
    for _ in range(30):
        #sleep(1)  #Use for observation
        shred(file)

shredder(input("Please enter what file to delete: "))
