import os
def searchfolder(a):
    c=input("Search in")
    os.chdir(c)
    for path, dirnames, files in os.walk(c):
        for file in dirnames:
            if file==a:
                print("found file")
                print(path)
def searchfile(a):
    c=input("Search in")
    os.chdir(c)
    for path, dirnames, files in os.walk(c):
        for file in files:
            if file==a:
                print("found file")
                print(path)


b=input("1:search folder  OR 2:Search files:-")
a=input("Enter name")
if b=="1":
    searchfolder(a)
elif b=="2":
    searchfile(a)
