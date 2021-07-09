import tkinter
import tkinter.messagebox
import tkinter as tk
import 메인화면

check2= [0]
def overlapCheck(id,button,check2):
    infor = open("정보.txt","r")
    if(id != "" ):
        while(True):
            line = infor.readline()
            asd =line.split(" ")
            print(asd)
            if line == "":
                tk.messagebox.showinfo("중복확인","사용가능한 아이디입니다.")
                check2[0] = id
                print(check2)
                infor.close()
                #button.config(state=tk.NORMAL)
                return True
            else:
                if(asd[0] == id):
                    print(asd[3])
                    tk.messagebox.showinfo("중복확인","이미 있는 아이디입니다.")
                    #button.config(state=tk.DISABLED)
                    infor.close()
                    return False
    else:
        tk.messagebox.showinfo("중복확인","아이디을 입력하세요") 
        

def write_infor(id,password,name,mail,check2,sign):
    if(id == check2[0]):
        if(password == "" or name == "" or mail ==""): tk.messagebox.showinfo("공백확인","입력하지 않은 정보가 있습니다.")
        information = open("정보.txt","a+")
        information.write(id) # id 쓰기
        information.write(" "+password+" "+name+" "+mail)
        information.write(" \n")
        information.close()
        tk.messagebox.showinfo("가입완료","가입이 완료되었습니다!")
        sign.destroy()
    else:
        tk.messagebox.showinfo("중복확인","중복확인을 해주세요")
def SignUp(): #회원가입 
    check =False
    sign = tk.Tk()
    sign.title("회원가입")
    sign.geometry("350x500+100+100")  # 화면폭에 맞춰서 늘려줌.
    
    id_label=tk.Label(sign, text="ID", width=10, height=5, fg="black", relief="solid")
    id_label.grid(column =0,row=0)
    password_label=tk.Label(sign, text="password", width=10, height=5, fg="black", relief="solid")
    password_label.grid(column = 0, row=1)
    password_label=tk.Label(sign, text="이름", width=10, height=5, fg="black", relief="solid")
    password_label.grid(column = 0, row=2)
    password_label=tk.Label(sign, text="이메일", width=10, height=5, fg="black", relief="solid")
    password_label.grid(column = 0, row=3)
    
    signUpId = tk.Entry(sign, width=20)  #아이디 입력칸 
    signUpId.grid(column = 2 , row = 0)

    
    signUpPassword = tk.Entry(sign, width=20)  #비밀번호 입력칸 
    signUpPassword.grid(column = 2 , row = 1)

    signUpName = tk.Entry(sign, width=20)  #이름 입력칸
    signUpName.grid(column = 2 , row = 2)

    
    signUpMail = tk.Entry(sign, width=20)  #이메일입력칸
    signUpMail.grid(column = 2 , row = 3)

    signUpButton = tk.Button(sign, text="회원가입",command =lambda : write_infor(signUpId.get(),signUpPassword.get(),signUpName.get(),signUpMail.get(),check2,sign))#파일처리 (회원가입) 버튼
    #signUpButton.config(state=tk.DISABLED)
    signUpButton.grid(column=2,row=4)

    overlab = tk.Button(sign, text="중복확인", command  = lambda : overlapCheck(signUpId.get(),signUpButton,check2))#중복체크버튼
    overlab.grid(column=3,row=0)

    
    sign.mainloop()
def SignIn(id,password,root): #로그인
    i = 0
    information = open("정보.txt","r")
    while(True):
        infor = information.readline()
        register =infor.split(" ")
        if not infor:
            tk.messagebox.showinfo("로그인 실패","없는 계정입니다.")
            break
        if(register[0] == id):
            print(register[1])
            if(register[1] == password):
                tk.messagebox.showinfo("로그인 성공 ","로그인 성공") #새로운 로그인
                root.destroy()
                메인화면.mainScreen(id)
                break
            else:
                tk.messagebox.showinfo("로그인 실패","비밀번호가 틀렸습니다")
                break
        
        
    information.close()
    
def main():
    root = tk.Tk()
    root.title("미로찾기")
    root.geometry("350x200+100+100")  # 화면폭에 맞춰서 늘려줌.

    id_label=tk.Label(root, text="ID", width=10, height=5, fg="black", relief="solid")
    id_label.grid(column =0,row=0)
    password_label=tk.Label(root, text="password", width=10, height=5, fg="black", relief="solid")
    password_label.grid(column = 0, row=1)
    
    id = tk.Entry(root, width=20)  #아이디 입력칸 
    id.grid(column = 2 , row = 0)
    password = tk.Entry(root, width=20)  #비밀번호 입력칸 
    password.grid(column = 2 , row = 1)

    
    button7 = tk.Button(root, text="로그인", command = lambda : SignIn(id.get(),password.get(),root))#로그인 버튼 
    button7.grid(column=1,row=3)
    button8 = tk.Button(root, text="회원가입", command = SignUp) #회원가입 버튼 
    button8.grid(column=2,row=3)
 
    root.mainloop()

if __name__ == "__main__":
    main()
