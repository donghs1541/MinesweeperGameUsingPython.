import tkinter
import tkinter.messagebox
import tkinter as tk
import maze

def help():
    root = tkinter.Tk()
    root.title("도움말")

    id_label=tkinter.Label(root, text= str(id)+"님 환영합니다! ", width=25, height=1)
    id_label.grid(column =0,row=0)

    root.mainloop()

def quit(root): #종료 함수 
    root.destroy()
def start(difi):
    a = maze.Mazeexe(difi)
    a.Start()
def diffculty():
    diff = tkinter.Tk()
    diff.title("난이도 설정")

    easy =tkinter.Button(diff, text = "쉬움",command = lambda : start(10))
    easy.grid(column=0,row=0)
    normal =tkinter.Button(diff, text = "보통",command = lambda : start(20))
    normal.grid(column=0,row=1)
    hard =tkinter.Button(diff, text = "어려움",command = lambda : start(40))
    hard.grid(column=0,row=2)
def mainScreen(id):
    root = tkinter.Tk()
    root.title("지뢰찾기")

    id_label=tkinter.Label(root, text= str(id)+"님 환영합니다! ", width=25, height=1)
    id_label.grid(column =0,row=0)

    
   # id = tkinter.Entry(root, width=20)  #아이디 입력칸 
   # id.grid(column = 2 , row = 0)

    
    button7 = tkinter.Button(root, text="실행", command = diffculty)
    button7.grid(column=1,row=3)
    button8 = tkinter.Button(root, text="도움말", command =2) 
    button8.grid(column=1,row=4)
    button8 = tkinter.Button(root, text="랭킹", command =2)
    button8.grid(column=1,row=5)
    button8 = tkinter.Button(root, text="나가기", command = lambda : quit(root)) 
    button8.grid(column=1,row=6)
    root.mainloop()


