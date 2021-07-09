import tkinter
import tkinter.messagebox
import tkinter as tk
import maze
from tkinter import *
import tkinter.scrolledtext as tkst
from tkinter.ttk import *

def help():
    helpImage=tkinter.Toplevel() 
    helpImage.title("도움말")
    helpImage.geometry("500x430+850+400") #1920 x1080 사이즈
    w = tkinter.PhotoImage(file="help.gif") 
    img = tkinter.PhotoImage(file=r"help.gif") 
    w = tkinter.Label(helpImage, image=img) 
    w.pack() 
    knapp=tkinter.Button(helpImage, text="Ok", command=lambda:quit(helpImage),width = 500)
    knapp.pack() 
    knapp.mainloop() 

def quit(root): #종료 함수 
    root.destroy()
def start(root,difi,id):
    a = maze.Mazeexe(difi,id)
    root.destroy()
    a.Start()
def diffculty(id):
    diff = tkinter.Tk()
    diff.title("난이도 설정")
    diff.geometry("190x140+850+400") #1920 x1080 사이즈
    diff.resizable(False,False)#창변경 불가능하게

    easy =tkinter.Button(diff, text = "쉬움",command = lambda : start(diff,10,id),width=26,height=2)
    easy.grid(column=0,row=0)
    normal =tkinter.Button(diff, text = "보통",command = lambda : start(diff,20,id),width=26,height=2)
    normal.grid(column=0,row=1)
    hard =tkinter.Button(diff, text = "어려움",command = lambda : start(diff,40,id),width=26,height=2)
    hard.grid(column=0,row=2)
def rank(rankTextBox,txt):
    count =0;
    rankScore=[]
    order=[]
    try:
        rankInformation = open(txt,"r")
        rankTextBox.delete("1.0",END)
        while True:
            infor = rankInformation.readline()
            if not infor:
                break;
            rankScore2 = infor.split(" ")
            count = count +1
            rankScore2[1] = rankScore2[1].replace("\n","") # \n 을 ""으로 대체해 파일에 엔터가 두번들어가지 않게 함.
            rankScore2.append(str(count))
            rankScore.append(rankScore2)
        for i in range(0,len(rankScore)):    #랭킹 파일을 읽어와 버블정렬을 하여 순위정렬을함. 
            for j in range(0,len(rankScore)-1):
                if float(rankScore[j][1]) > float(rankScore[j+1][1]):
                    temp = rankScore[j]
                    rankScore[j] =rankScore[j+1]
                    rankScore[j+1] =temp
        count=0
        for i in rankScore:
            count= count+1  
            c=str(count)+" "+i[0]+" "+i[1]
            rankTextBox.insert(END,c+"\n\n") 
    except:
        tk.messagebox.showinfo("정보","현재 랭킹이 없습니다.")
        
def rankWindow():
    rankRoot = tkinter.Tk()
    rankRoot.title("순위 보기")
    rankRoot.geometry("300x300+745+398") #1920 x1080 사이즈
    rankRoot.resizable(False,False)#창변경 불가능하게
    f1 = tkinter.Menu(rankRoot)
    
    rankMenubar = tkinter.Menu(f1,tearoff=0)
    rankMenubar2 = tkinter.Menu(f1,tearoff=0)
    rankMenubar3 = tkinter.Menu(f1,tearoff=0)


    f1.add_cascade(label ="랭킹초급",command = lambda : rank(rankTextBox,"랭킹초급.txt"))
    f1.add_cascade(label ="랭킹중급",command = lambda : rank(rankTextBox,"랭킹중급.txt"))
    f1.add_cascade(label ="랭킹고급",command = lambda : rank(rankTextBox,"랭킹.txt"))

    rankRoot.config(menu=f1)

    rankTextBox = tkst.ScrolledText(rankRoot, width=75, height=20, wrap=tk.WORD) # Create a scrolledtext
    rankTextBox.grid(column=0, row=0)
    rankTextBox.focus_set()
    
    rankRoot.mainloop()
    
def mainScreen(id):
    root = tkinter.Tk()
    root.title("지뢰찾기")
    root.geometry("190x140+850+400")
    root.resizable(False,False)#창변경 불가능하게

    frame1 = tkinter.Frame(root,bd=2,width=10,background="brown")
    frame1.pack(side="top",fill="both",expand=True)

    frame2 = tkinter.Frame(root,bd=2,width=100,background="brown")
    frame2.pack(side="bottom",fill="both",expand=True)
    
    id_label=tkinter.Label(frame1, text= str(id)+"님 환영합니다! ", width=25, height=1,background="brown",fg="white")
    id_label.grid(column =0,row=0)

    
    button7 = tkinter.Button(frame2, text="실행", command = lambda : diffculty(id),width = 25)
    button7.grid(column=1,row=3)
    button8 = tkinter.Button(frame2, text="도움말", command =help,width = 25) 
    button8.grid(column=1,row=4)
    button8 = tkinter.Button(frame2, text="랭킹", command =rankWindow,width = 25)
    button8.grid(column=1,row=5)
    button8 = tkinter.Button(frame2, text="나가기", command = lambda : quit(root),width = 25) 
    button8.grid(column=1,row=6)
    root.mainloop()

