import tkinter
import tkinter.messagebox
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import 로그인화면
class passwordFind(로그인화면.Sign): #비밀번호찾기.

    def __init__(self):
        super().__init__()
    def createWindow(self,root):  #오버라이딩
        self.__mainRoot = root
        self.__mainRoot.withdraw()
        self.__check2= [0]
        self.__check =False
        self.__sign = tk.Tk()
        self.__sign.title("비밀번호 찾기")
        self.__sign.geometry("250x200+800+400")  # 화면폭에 맞춰서 늘려줌.
        self.__sign.configure(background='brown')
        
        self.__id_label=tk.Label(self.__sign, text="아이디", width=10, height=5, fg="white",background = "brown")
        self.__id_label.grid(column =0,row=0)
        self.__password_label=tk.Label(self.__sign, text="이름", width=10, height=5, fg="white",background = "brown")
        self.__password_label.grid(column = 0, row=1)
        
        self.__signId = tk.Entry(self.__sign, width=20)  #아이디 입력칸 
        self.__signId.grid(column = 2 , row = 0)
        
        self.__signName = tk.Entry(self.__sign, width=20)  #이름 입력칸
        self.__signName.grid(column = 2 , row = 1)

        self.__signUpButton = tk.Button(self.__sign, text="비밀번호 찾기",command =self.findInfor )#비밀번호 찾기버튼
        self.__signUpButton.grid(column=2,row=4)
        
        self.__sign.mainloop()
    def findInfor(self):  #메소드 오버라이딩
        information = open("정보.txt","r")
        if(self.__signId.get() != "" and self.__signName.get()!= ""):
            while(True):
                infor = information.readline()
                userInformation =infor.split(" ")
                if(userInformation[0] == ""):
                    tk.messagebox.showinfo("찾기 실패","없는 아이디입니다.")
                    break
                if not infor:
                    break
                if(userInformation[0] == self.__signId.get()):
                    if(userInformation[2] == self.__signName.get()):
                        tk.messagebox.showinfo("비밀번호",userInformation[1]+"입니다")
                        self.__sign.destroy()
                        self.__mainRoot.deiconify()
                        break
                    else:
                        tk.messagebox.showinfo("찾기 실패","없는 정보입니다.")
                        break
        else:
                
            tk.messagebox.showinfo("찾기 실패","정보를 모두 입력해주세요.")
            
        information.close()        

