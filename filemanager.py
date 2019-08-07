import os
def allnew():
    os.mkdirs('e:/a/b/c')
    os.removedirs('e:/a/b/v')
    os.rmdir("e:/a")
    os.path.join('e:',"txt.txt")
def remodir(fn):
    try:
        os.rmdir(fn)
        print("folder has been deleted "+fn)
    except:
        print("invalid")
def remofil(fn):
    try:
        os.remove(fn)
        print("file has been deleted "+fn)
    except:
        print("invalid")

def filrenam(fn):
    try:
        a=input("enter the new file name")
        os.rename(fn,a)
        print("renamed to  "+fn)
    except:
        print("invalid")
def chadir(fn):
    try:
        os.chdir(fn)
        print("path changed to "+fn)
    except:
        print("gm")
def cat(fn):
    ob=open(fn)
    content=ob.read()
    print(content)
while True:
    b=input("1.remdir "+"2.remov"+" 3.rename "+ "4.change dir")
    fn=input("enter the file name or dir or path")
    try:
        if(b=="1"):
            remodir(fn)
        elif(b=="2"):
            remofil(fn)
        elif(b=="3"):
            filrenam(fn)
        elif(b=="4"):
            chadir(fn)
        elif(b=="cat"):
            cat(fn)
        elif(b==0):
            break

    except:
        print("enter the valid input")
