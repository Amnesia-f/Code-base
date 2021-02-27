from tkinter import *
import tkinter.messagebox
import random
class fivechess:
    def __init__(self):
        window=Tk()
        window.title("Five Chess")

        self.canvas=Canvas(window,bg="white",width=420,height=420)
        self.canvas.pack() 
        for i in range(20,410,20):
            self.canvas.create_line(i,20,i,400,fill="blue")
            self.canvas.create_line(20,i,400,i,fill="blue")
            self.r=str(int(i/20))
            self.canvas.create_text(10,i,text=self.r,fill="blue")
            self.canvas.create_text(i,10,text=self.r,fill="blue")

        self.canvas.create_text(210,412,text="蓝方选手使用左键，红方选手使用右键",fill="red")
            
        tkinter.messagebox.showinfo("提醒","蓝方选手使用左键，红方选手使用右键")
        
        
          

        self.canvas.bind("<Button-1>",self.draw)
        self.canvas.bind("<Button-3>",self.draw2)
        self.listall=[]
        self.listnow=()
        self.listall2=[]
        self.listnow2=()
        self.listall21=[]
        self.county=1
        self.countx=1
        self.counta=1
        self.countb=1
        self.turn=0

    #第2人_______________
    def draw2(self,event):
        if self.turn%2==1:
            self.turn+=1
            p=20*round(event.x/20)
            q=20*round(event.y/20)
            self.listnow2=(p,q,1)
            if self.listnow2 in self.listall21 or p<20 or q<20 or p>400 or q>400 :
                print("wrong placement,try again!")
                tkinter.messagebox.showinfo("提醒","此处不可落子！")
            else:
                self.listall2.append(self.listnow2)
                self.listall21.append(self.listnow2)
                self.canvas.create_oval(p-7,q-7,p+7,q+7,fill="red")
                self.checksuccess2(p,q)
          #第一人___________________________
    def draw(self,event):
        if self.turn%2==0:
            self.turn+=1
            m=20*round(event.x/20)
            n=20*round(event.y/20)
            self.listnow=(m,n,1)
            if self.listnow in self.listall21 or m<20 or n<20 or m>400 or n>400 :
                print("wrong placement,try again!")
                tkinter.messagebox.showinfo("提醒","此处不可落子！")
            else:
                self.listall.append(self.listnow)
                self.listall21.append(self.listnow)
                self.canvas.create_oval(m-7,n-7,m+7,n+7,fill="blue")
                #测试是否胜利
                self.checksuccess(m,n)
    #_____________________________________________________
    def checksuccess(self,m,n):
        #text y
        mm=m
        nn=n
        while True:
            if (m,n-20,1) in self.listall:
                self.county+=1
                n-=20
                print("y",self.county)
            else:
                break
        m=mm
        n=nn
        while True:
            if (m,n+20,1) in self.listall:
                self.county+=1
                n+=20
                print("y",self.county)
            else:
                break
        if self.county>=5:
            print("y",self.county)
            print("you blue side winy!")
            tkinter.messagebox.showinfo("恭喜","蓝方纵向五子胜利！")
        self.county=1

        #text x
        mm=m
        nn=n
        while True:
            if (m-20,n,1) in self.listall:
                self.countx+=1
                m-=20
                print("x",self.countx)
            else:
                break
        m=mm
        n=nn
        while True:
            if (m+20,n,1) in self.listall:
                self.countx+=1
                m+=20
                print("x",self.countx)
            else:
                break
        if self.countx>=5:
            print("x",self.countx)
            print("you blue side winx!")
            tkinter.messagebox.showinfo("恭喜","蓝方横向五子胜利！")
        self.countx=1

        #text a
        mm=m
        nn=n
        while True:
            if (m-20,n-20,1) in self.listall:
                self.counta+=1
                n-=20
                m-=20
                print("a",self.counta)
            else:
                break
        m=mm
        n=nn
        while True:
            if (m+20,n+20,1) in self.listall:
                self.counta+=1
                n+=20
                m+=20
                print("a",self.counta)
            else:
                break
        if self.counta>=5:
            print("a",self.counta)
            print("you blue side win-a!")
            tkinter.messagebox.showinfo("恭喜","蓝方正对角五子胜利！")
        self.counta=1

        #text b
        mm=m
        nn=n
        while True:
            if (m+20,n-20,1) in self.listall:
                self.countb+=1
                n-=20
                m+=20
                print("b",self.countb)
            else:
                break
        m=mm
        n=nn
        while True:
            if (m-20,n+20,1) in self.listall:
                self.countb+=1
                n+=20
                m-=20
                print("b",self.countb)
            else:
                break
        if self.countb>=5:
            print("b",self.countb)
            print("you blue side win-b!")
            tkinter.messagebox.showinfo("恭喜","蓝方逆对角五子胜利！")
        self.countb=1
                    
#_____________________________________________________
    def checksuccess2(self,m,n):
        #text y
        mm=m
        nn=n
        while True:
            if (m,n-20,1) in self.listall2:
                self.county+=1
                n-=20
                print("y",self.county)
            else:
                break
        m=mm
        n=nn
        while True:
            if (m,n+20,1) in self.listall2:
                self.county+=1
                n+=20
                print("y",self.county)
            else:
                break
        if self.county>=5:
            print("y",self.county)
            print("you red side winy!")
            tkinter.messagebox.showinfo("恭喜","红方纵向五子胜利！")
        self.county=1

        #text x
        mm=m
        nn=n
        while True:
            if (m-20,n,1) in self.listall2:
                self.countx+=1
                m-=20
                print("x",self.countx)
            else:
                break
        m=mm
        n=nn
        while True:
            if (m+20,n,1) in self.listall2:
                self.countx+=1
                m+=20
                print("x",self.countx)
            else:
                break
        if self.countx>=5:
            print("x",self.countx)
            print("you red side winx!")
            tkinter.messagebox.showinfo("恭喜","红方横向五子胜利！")
        self.countx=1

        #text a
        mm=m
        nn=n
        while True:
            if (m-20,n-20,1) in self.listall2:
                self.counta+=1
                n-=20
                m-=20
                print("a",self.counta)
            else:
                break
        m=mm
        n=nn
        while True:
            if (m+20,n+20,1) in self.listall2:
                self.counta+=1
                n+=20
                m+=20
                print("a",self.counta)
            else:
                break
        if self.counta>=5:
            print("a",self.counta)
            print("you red side win-a!")
            tkinter.messagebox.showinfo("恭喜","红方逆对角五子胜利！")
        self.counta=1

        #text b
        mm=m
        nn=n
        while True:
            if (m+20,n-20,1) in self.listall2:
                self.countb+=1
                n-=20
                m+=20
                print("b",self.countb)
            else:
                break
        m=mm
        n=nn
        while True:
            if (m-20,n+20,1) in self.listall2:
                self.countb+=1
                n+=20
                m-=20
                print("b",self.countb)
            else:
                break
        if self.countb>=5:
            print("b",self.countb)
            print("you red side win-b!")
            tkinter.messagebox.showinfo("恭喜","红方正对角五子胜利！")
        self.countb=1
                    

fivechess()
