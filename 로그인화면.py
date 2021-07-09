import tkinter
import tkinter.messagebox
import tkinter as tk
import 메인화면
import 회원가입화면
from tkinter import *
from tkinter.ttk import *

class Sign():
        
    def __init__(self):
        pass
        
    def createWindow(self):
        self.__root = tk.Tk()
        self.__root.title("미로찾기")
        self.__root.geometry("250x200+790+340")  # 화면폭에 맞춰서 늘려줌.


        self.__frame1 = tkinter.Frame(self.__root,bd=2,width=10,background = "brown")
        self.__frame1.pack(side="top",fill="both",expand=True)

        self.__frame2 = tkinter.Frame(self.__root,bd=2,width=100,background = "brown")
        self.__frame2.pack(side="bottom",fill="both",expand=True)

        self.__id_label=tk.Label(self.__frame1, text="ID", width=10, height=5, fg="white",background = "brown")
        self.__id_label.grid(column =0,row=0)
        self.__password_label=tk.Label(self.__frame1, text="password", width=10, height=5, fg="white",background = "brown")
        self.__password_label.grid(column = 0, row=1)
        
        self.__id = tk.Entry(self.__frame1, width=20)  #아이디 입력칸 
        self.__id.grid(column = 2 , row = 0)
        self.__password = tk.Entry(self.__frame1, width=20,show="*")  #비밀번호 입력칸 
        self.__password.grid(column = 2 , row = 1)

        
        self.__button7 = tk.Button(self.__frame2, text="로그인",padx =10, command = self.findInfor)#로그인 버튼 
        self.__button7.grid(column=1,row=3)
        self.__button8 = tk.Button(self.__frame2, text="회원가입",padx =10, command = lambda:회원가입화면.SignUp(self.__root)) #회원가입 버튼 
        self.__button8.grid(column=3,row=3)
        self.__passwordFind =tk.Button(self.__frame2, text="비밀번호찾기",padx =10,command=lambda:self.findPassword(self.__root)) #비밀번호찾기 버튼
        self.__passwordFind.grid(column=2,row=3)
     
        self.__root.mainloop()
        
    def findInfor(self): #로그인
        information = open("정보.txt","r")
        idText = self.__id.get()
        while(True):
            infor = information.readline()
            register =infor.split(" ")
            if not infor:
                tk.messagebox.showinfo("로그인 실패","없는 계정입니다.")
                break
            if(register[0] == self.__id.get()):
                if(register[1] == self.__password.get()):
                    tk.messagebox.showinfo("로그인 성공 ","로그인 성공") #새로운 로그인
                    self.__root.destroy()
                    메인화면.mainScreen(idText)
                    break
                else:
                    tk.messagebox.showinfo("로그인 실패","비밀번호가 틀렸습니다")
                    break
            
    
        information.close()
    def findPassword(self,root):
        import 비밀번호찾기
        b=비밀번호찾기.passwordFind()
        b.createWindow(root)
        
        
        
def main():
    a=Sign()
    a.createWindow()
    

if __name__ =="__main__":
    main()






