import os
from tkinter import *
root=Tk()
#######################################FILE##########################################################
def ffile(c,i):
    def d_drive(c, i):
        with open('d:FNS/d files/file.txt', 'r') as fns:
            content = fns.readlines()
            for item in content:
                if c.upper() in item.upper():
                    x[i] = item[0:len(item) - 1]
                    i = i + 1
        return i
    ii=d_drive(t2.get(),i)
    def e_drive(c, i):
        with open('d:FNS/e files/file.txt', 'r') as fns:
            content = fns.readlines()
            for item in content:
                if c.upper() in item.upper():
                    x[i] = item[0:len(item) - 1]
                    i = i + 1
        return (i)
    iii=e_drive(t2.get(),ii)
    def c_drive(c, i):
        with open('d:FNS/c files/file.txt', 'r') as fns:
            content = fns.readlines()
            for item in content:
                if c.upper() in item.upper():
                    x[i] = item[0:len(item) - 1]
                    i = i + 1
    #c_drive(c,iii)
########################################FNS FILE################################################################




def fns(real_name,i):
    def dfns(real_name,i):
        with open('d:FNS/d files/FNS.txt', 'r') as fns2:
            content2 = fns2.readlines()
            for item in content2:
                if real_name.upper() in item.upper():
                    pat[i] = item[0:len(item) - 1]
                    i = i + 1
        return i
    ii=dfns(real_name,i)
    def efns(real_name,i):
        with open('d:FNS/e files/FNS.txt', 'r') as fns2:
            content2 = fns2.readlines()
            for item in content2:
                if real_name.upper() in item.upper():
                    pat[i] = item[0:len(item) - 1]
                    i = i + 1
    iii=efns(real_name,ii)
    def cfns(real_name,i):
        with open('d:FNS/c files/FNS.txt', 'r') as fns2:
            content2 = fns2.readlines()
            for item in content2:
                if real_name.upper() in item.upper():
                    pat[i] = item[0:len(item) - 1]
                    i = i + 1
  #  cfns(real_name,iii)



###################################################FOLDER################################################


def fol(c,i):
    def d_drive(c, i):
        with open('d:FNS/d folder/file.txt', 'r') as fns:
            content = fns.readlines()
            for item in content:
                if c.upper() in item.upper():
                    x[i] = item[0:len(item) - 1]
                    i = i + 1
        return i

    ii=d_drive(c,i)
    def e_drive(c, i):
        with open('d:FNS/e folder/file.txt', 'r') as fns:
            content = fns.readlines()
            for item in content:
                if c.upper() in item.upper():
                    x[i] = item[0:len(item) - 1]
                    i = i + 1
        return (i)
    iii=e_drive(c,ii)
    def c_drive(c, i):
        with open('d:FNS/c folder/file.txt', 'r') as fns:
            content = fns.readlines()
            for item in content:
                if c.upper() in item.upper():
                    x[i] = item[0:len(item) - 1]
                    i = i + 1

   # c_drive(c,iii)



###############################################FNS FOLDER#########################################################


def fns_fol(real_name,i):
    def dffns(real_name,i):
        print("enter")
        with open('d:FNS/d folder/FNS.txt', 'r') as fns2:
            content2 = fns2.readlines()
            for item in content2:
                if real_name.upper() in item.upper():
                    #print(item)
                    fol_path[i] = item[0:len(item) - 1]
                    i = i + 1
        return(i)
    ii=dffns(real_name,i)
    def effns(real_name,i):
        with open('d:FNS/e folder/FNS.txt', 'r') as fns2:
            content2 = fns2.readlines()
            for item in content2:
                if real_name.upper() in item.upper():
                    #print(item)
                    fol_path[i] = item[0:len(item) - 1]
                    i = i + 1
        return (i)
    iii=effns(real_name,ii)
    def cffns(real_name,i):
        with open('d:FNS/c folder/FNS.txt', 'r') as fns2:
            content2 = fns2.readlines()
            for item in content2:
                if real_name.upper() in item.upper():
                    #print(item)
                    fol_path[i] = item[0:len(item) - 1]
                    i = i + 1
   # cffns(real_name,iii)

lbl1=Label(root, text="1.file or 2.folder")
lbl1.place(x=10,y=50)
#print("1.file"+"\n"+"2.folder")
lbl2=Label(root, text="Enter Number")
lbl2.place(x=10,y=100)
t1=Entry(root)
t1.place(x=100,y=100)
#cc=int(input())
lbl3=Label(root, text="enter file name")
lbl3.place(x=10,y=150)
t2=Entry(root)
t2.place(x=100,y=150)
#c=input("enter file name")
lbl4=Label(root, text="Show the Path")
lbl4.place(x=10,y=230)
t3=Entry(root)
t3.place(x=100,y=230)
lbl4=Label(root, text="Open the Path")
lbl4.place(x=10,y=310)
t4=Entry(root)
t4.place(x=100,y=310)
x={}
i=0
pat={}
fol_path={}
real_name='None'

def first():
    if t1.get()=='1':      #cc==1:
        k=1
        ffile(t2.get(), i)
        for leng in range(len(x)):
            lbl5=Label(root, text=(str(leng) + "   " + x[leng]),width=100)
            lbl5.place(x=300,y=k*50)
            k+=1
            #print(str(leng) + "   " + x[leng])
        #j = int(input("enter the number"))


    if t1.get()=='2':       #cc==2:
        k=1
        fol(t2.get(),i)
        for leng in range(len(x)):
            lbl5=Label(root, text=(str(leng) + "   " + x[leng]),width=100)
            lbl5.place(x=300,y=k*50)
            k+=1
            #print(str(leng) + "   " + x[leng])
        #j = int(input("enter the number"))


def sec():
    if t1.get()=='1':
        real_name =x[int(t3.get())]             #x[j]
        i=0
        m=1
        fns(real_name,i)
        for leng in range(len(pat)):
            lbl6=Label(root, text=(str(leng) + "   " + pat[leng]),width=100)
            lbl6.place(x=850,y=m*50)
            m+=1
            #print(str(leng) + "   " + pat[leng])

    if t1.get()=='2':
        real_name =x[int(t3.get())]      #x[j]
        i=0
        m=1
        fns_fol(real_name,i)
        for leng in range(len(fol_path)):
            lbl6=Label(root, text=(str(leng) + "   " + fol_path[leng]),width=100)
            lbl6.place(x=850,y=m*50)
            m+=1
            #print(str(leng) + "   " + fol_path[leng])

def third():
    if t1.get()=='1':
        real_name = x[int(t3.get())]
        pathh=pat[int(t4.get())]      #pat[int(input("enter the number"))]
        a = pathh.split("\\")
        i = 0
        for kkk in range(len(a) - 1):
            if i == 0:
                real_path = a[kkk]
                i = 1
            else:
                real_path = real_path + "\\" + a[kkk]

        os.startfile(real_path)
        print(real_path)

    if t1.get()=='2':
        real_name = x[int(t3.get())]
        pathh =fol_path[int(t4.get())]      #fol_path[int(input("enter the number"))]
        a = pathh.split("\\")
        i = 0
        for kkk in range(len(a) - 1):
            if i == 0:
                real_path = a[kkk]
                i = 13
            else:
                real_path = real_path + "\\" + a[kkk]

        os.startfile(real_path)
        print(real_path)


btn1=Button(root, text='Search', command=first)
btn1.place(x=10,y=180)
btn2=Button(root, text='Show', command=sec)
btn2.place(x=10,y=260)
btn3=Button(root, text='Open', command=third)
btn3.place(x=10,y=340)
root.title("PySearch")
root.mainloop()