import tkinter
import tkinter.messagebox
import tkinter as tk
import 메인화면
from tkinter import *
from tkinter.ttk import *

class SignUp(): #회원가입.

    def __init__(self,root):
        self.__loginRoot=root
        self.__loginRoot.withdraw()
        self.__check2= [0]
        self.__check =False
        self.__sign = tk.Tk()
        self.__sign.title("회원가입")
        self.__sign.geometry("300x350+790+340")  # 화면폭에 맞춰서 늘려줌.
        
        self.__id_label=tk.Label(self.__sign, text="아이디", width=10, height=5, fg="black", relief="solid")
        self.__id_label.grid(column =0,row=0)
        self.__password_label=tk.Label(self.__sign, text="비밀번호", width=10, height=5, fg="black", relief="solid")
        self.__password_label.grid(column = 0, row=1)
        self.__password_label2=tk.Label(self.__sign, text="비밀번호확인", width=10, height=5, fg="black", relief="solid")
        self.__password_label2.grid(column = 0, row=2)
        self.__name_label=tk.Label(self.__sign, text="이름", width=10, height=5, fg="black", relief="solid")
        self.__name_label.grid(column = 0, row=3)
        
        self.__signUpId = tk.Entry(self.__sign, width=20)  #아이디 입력칸 
        self.__signUpId.grid(column = 2 , row = 0)
        
        self.__signUpPassword = tk.Entry(self.__sign, width=20,show="*")  #비밀번호 텍스트박스 생성 (*로 표시됨)
        self.__signUpPassword.grid(column = 2 , row = 1)

        self.__signUpPassword2 = tk.Entry(self.__sign, width=20,show="*") #비밀번호확인 텍스트박스 생성 (*로 표시됨)
        self.__signUpPassword2.grid(column = 2 , row = 2)


        self.__signUpPassword2.bind("<FocusOut>",self.passwordCheck)    # 이렇게 많은 BIND를 준 이유는 키를 실시간으로 입력받을때 한번씩 지연이 돼서 많은 bind를 주어 해결함
        self.__signUpPassword.bind("<FocusOut>",self.passwordCheck)
        self.__signUpPassword2.bind("<Leave>",self.passwordCheck)
        self.__signUpPassword.bind("<Leave>",self.passwordCheck)
        self.__signUpPassword.bind("<Key>",self.passwordCheck)
        self.__signUpPassword2.bind("<Key>",self.passwordCheck)
        self.__signUpPassword.bind("<FocusIn>",self.passwordCheck)
        self.__signUpPassword2.bind("<FocusIn>",self.passwordCheck)
        self.__signUpPassword.bind("<Enter>",self.passwordCheck)
        self.__signUpPassword2.bind("<Enter>",self.passwordCheck)
        self.__signUpPassword.bind("<Motion>",self.passwordCheck)
        self.__signUpPassword2.bind("<Motion>",self.passwordCheck)
        
        self.__checkPassword = tk.Label(self.__sign,text="",width=10)
        self.__checkPassword.grid(column=3,row=2)

        
        self.__signUpName = tk.Entry(self.__sign, width=20)  #이름 입력칸
        self.__signUpName.grid(column = 2 , row = 3)

        self.__signUpButton = tk.Button(self.__sign, text="회원가입",command =self.write_infor)#파일처리 (회원가입) 버튼
        self.__signUpButton.grid(column=2,row=4)

        self.__overlab = tk.Button(self.__sign, text="중복확인", command  = self.overlapCheck)#중복체크버튼
        self.__overlab.grid(column=3,row=0)

        
        self.__sign.mainloop()        
    def overlapCheck(self):
        infor = open("정보.txt","a+")
        infor.seek(0)
        if(id != "" ):
            while(True):
                line = infor.readline()
                asd =line.split(" ")
                if line == "":
                    tk.messagebox.showinfo("중복확인","사용가능한 아이디입니다.")
                    self.__check2[0] = self.__signUpId.get()
                    infor.close()
                    return True
                else:
                    if(asd[0] == self.__signUpId.get()):
                        tk.messagebox.showinfo("중복확인","이미 있는 아이디입니다.")
                        infor.close()
                        return False
        else:
            tk.messagebox.showinfo("중복확인","아이디을 입력하세요") 
            
    def passwordCheck(self,event):
        if(self.__signUpPassword2.get()==self.__signUpPassword.get()): # 두 비밀번호가 서로 일치하면
            self.__checkPassword["text"]="일치"
        else:
            self.__checkPassword["text"]="불일치"

            
    def write_infor(self):
        if(self.__signUpId.get() == self.__check2[0] and self.__checkPassword["text"] =="일치"):
            if(self.__signUpPassword.get() == "" or self.__signUpPassword2.get() == "" or self.__signUpName.get() ==""): tk.messagebox.showinfo("공백확인","입력하지 않은 정보가 있습니다.")
            else:
                information = open("정보.txt","a+")
                information.write(self.__signUpId.get()) # id 쓰기
                information.write(" "+self.__signUpPassword.get()+" "+self.__signUpName.get())
                information.write(" \n")
                information.close()
                tk.messagebox.showinfo("가입완료","가입이 완료되었습니다!")
                self.__sign.destroy()
                self.__loginRoot.deiconify()
        else:
            if(self.__signUpId.get() == self.__check2[0] and self.__checkPassword["text"] !="일치"):
                tk.messagebox.showinfo("불일치","비밀번호가 불일치합니다")
            else:
                tk.messagebox.showinfo("중복확인","중복확인을 해주세요")
