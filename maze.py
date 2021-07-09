from random import randint
from tkinter import *
import tkinter
import threading
from tkinter.ttk import *
import tkinter.messagebox
import tkinter as tk


class Mazeexe():
    def __init__(self,rcSize,id):
        self.__mapSize = 15#픽셀 
        self.__ms = rcSize # 행 렬 사이즈 
        self.__visited_cells = []
        self.__walls = []
        self.__revisitedCells = []
        self.__map = [["벽" for _ in range(self.__ms)] for _ in range(self.__ms)]   #맵전체를 "벽"로줌 즉 검정색으로 칠함

        self.__startRow = 1 #시작 위치는 1, 1 임
        self.__startColumn = 1 #시작위치
        self.__score = 0 #미로찾기 스코
        self.__id = id # 사용자 아이디 
             
        #시작구간 생성
    def startTimer(self):
        self.__timer = threading.Timer(0.01,self.startTimer) #0.01초마다 타이머 시행 
        self.__timer.start()
        self.__score =self.__score + 0.01  #점수를 0.01씩 더해줌 
    def Start(self):         
        currentRow, currentColumn = self.__startRow, self.__startColumn  #초기 좌표를 줌 
        self.__x1 = currentRow * self.__ms #맵사이즈만큼 더해줌  
        self.__y1 = currentColumn * self.__ms #맵사이즈만큼 서해줌 
        self.__map[currentRow][currentColumn] = "길"
        while True:  #미로 만드는 구간 
            self.__visitable = self.checkNeighbours(currentRow, currentColumn)  #이동가능한 길인지 확인하는 함수 호출후 값을 받아옴 
            if len(self.__visitable) != 0:  #길이 있으면 (리턴값이 공백이 아니면)
                d = randint(1, len(self.__visitable))-1  
                ncr, ncc = self.__visitable[d]  #여기서 상 하 좌 우를 랜덤으로 받아와 그 좌표를 설정해줌 
                self.__map[ncr][ncc] = "길"  #그 좌표에 있는 값을 "길"로 바꾸어줌
                self.__visited_cells.append([ncr, ncc]) #방문된 곳 을 추가함 
                currentRow, currentColumn = ncr, ncc  #그리고 "길"로 바꾼 좌표를 현재좌표로 변경해줌
            if len(self.__visitable) == 0: #값이 없으면 (캔버스의 좌표가 벗어나면)
                try:
                    currentRow, currentColumn = self.__visited_cells.pop() #현재 좌표를 가장 최근에 방문했던 값으로 바꿈 (길을 만들다 막히게 되면 안막히는 길쪽으로 다시 돌아감)
                    self.__revisitedCells.append([currentRow, currentColumn])    #재방문한 좌표를 추가  
                except:
                    break 
        self.__MazeFrame = Tk()
        self.__MazeFrame.title('미로찾기')
        self.__MazeFrame.resizable(False,False)#창변경 불가능하게
        canvas_side = self.__ms*self.__mapSize #캔버스의 크기를 행렬크기와 한 블럭의크기(네모의 크기) 만큼 곱해줘서 캔버스의 사이즈를 정함
        self.__ffs = Canvas(self.__MazeFrame, width = canvas_side, height = canvas_side, bg = 'brown')
        self.__MazeFrame.geometry("%dx%d+%d+%d"%(canvas_side,canvas_side,850,400) )#1920 x1080 사이즈 기준으로 화면설정
        self.__ffs.pack()
         
         
        self.create()
        self.__y1 = self.__startRow * self.__mapSize   #현재위치 만들기 
        self.__x1 = self.__startColumn * self.__mapSize  #현재위치 만들기
        self.draw(self.__startRow, self.__startColumn, 'red') #현재위치 그리기 


        self.draw(self.__ms-2, self.__ms-2, 'blue') #종착지 그리기

        self.__MazeFrame.bind("<Key>", self.move)
        
        self.startTimer() #게임을 만듬과 동시에 타이머 시작 
     
         
        self.__MazeFrame.mainloop()

         
    def checkNeighbours(self,row, column):
        self.__neighbours = [[row,column - 1,row - 1,column - 2,row,column - 2,row + 1,column - 2,row - 1, column - 1, row + 1,column - 1],# 왼쪽방향 
                    [row, column + 1, row - 1, column + 2, row, column + 2, row + 1, column + 2, row - 1, column + 1, row + 1, column + 1], #오른쪽방향
                    [row - 1, column, row - 2, column - 1, row - 2, column, row - 2, column + 1, row - 1, column - 1, row - 1, column + 1], #위쪽방향
                    [row + 1, column, row + 2, column - 1, row + 2, column, row + 2, column + 1, row + 1, column-1, row + 1, column + 1]] #아랫쪽방향
        self.__visitable = []           
        for i in self.__neighbours:   #통과 가능한 길을 탐색함 , 튜플의 한 행씩 읽음 (이터레이터)
            if i[0] > 0 and i[0] < (self.__ms-1) and i[1] > 0 and i[1] < (self.__ms-1):         #좌표가 캔버스 크기 안에 있으면 
                if self.__map[i[2]][i[3]] == "길" or self.__map[i[4]][i[5]] == "길" or self.__map[i[6]][i[7]] == "길" or self.__map[i[8]][i[9]] == "길" or self.__map[i[10]][i[11]] == "길":  #길이 하나도 없으면 
                    self.__walls.append(i[0:2])     #좌표를 walls 에 추가 
                else:
                    self.__visitable.append(i[0:2])   #길이면 visitable에 추가후 리턴
        return self.__visitable

    def create(self): #맵 생성 
        for row in range(self.__ms):
            for col in range(self.__ms):
                if self.__map[row][col] == "길": #맵의 좌표에 있는 값이 길이면 흰색처리 
                    color = 'white'
                elif self.__map[row][col] == "벽": #아니면 검정처리 
                    color = 'brown'
                self.draw(row, col, color)
     
     
    def draw(self, row, col, color):  #그릴 행렬에 픽셀사이즈 네모사이즈를 곱해줌 (canvas좌표에 맞혀줌)
        self.__x1 = col * self.__mapSize
        self.__y1 = row * self.__mapSize
        self.__x2 = self.__x1 + self.__mapSize
        self.__y2 = self.__y1 + self.__mapSize
        self.__ffs.create_rectangle(self.__x1, self.__y1, self.__x2, self.__y2, fill=color) #좌상단 구석좌표 와 우하단 구석좌표를 구해 받아온 color를 그 사각형만큼 칠해줌
     
     


     
    def presentLocation(self): #현재위치 그리기
        self.__ffs.create_rectangle((self.__x1, self.__y1, self.__x1 + self.__mapSize, self.__y1 + self.__mapSize), fill="blue") #현재위치를 파란색으로 표시함. 
     
    def priviousLocationClear(self): #지나간길 초기화 
        self.__ffs.create_rectangle((self.__x1, self.__y1, self.__x1 + self.__mapSize, self.__y1 + self.__mapSize), fill="white") #지나간 길을 다시 흰배경으로 채움 
     
    def move(self,event):  #움직이는 이벤트 

        self.__col = self.__w = self.__x1//self.__mapSize
        self.__row = self.__h = self.__y1//self.__mapSize
       # print("before", self.__map[self.__row][self.__col])
        self.priviousLocationClear() #키보드를 입력받아 현재있는 좌표의 블럭을 흰색으로바꿈 
        if event.char == "4":
            if self.__map[self.__row][self.__col - 1] == "길":
                self.__x1 -= self.__mapSize
        elif event.char == "6":
            if self.__map[self.__row][self.__col + 1] == "길":
                self.__x1 += self.__mapSize
        elif event.char == "8":
            if self.__map[self.__row - 1][self.__col] == "길":
                self.__y1 -= self.__mapSize
        elif event.char == "5":
            if self.__map[self.__row + 1][self.__col] == "길":
                self.__y1 += self.__mapSize
        self.presentLocation()  #위에서 움직인 좌표의 다음좌표의 값이 "길"이면 그 좌표에 파란색을 칠해줘서 현재위치를 표시함 
        self.__col = self.__w = self.__x1//self.__mapSize 
        self.__row = self.__h = self.__y1//self.__mapSize
       # print(self.__w, self.__h)
       # print("after", self.__map[self.__row][self.__col])
        if(self.__w == 1 and self.__h== 1):             #도착을 한다면 
            self.writeRanking()
    def writeRanking(self):
        ranking = "랭킹.txt"
        check=False
        userInfor = [] #유저정보 수정을 위해 만듬
        self.__timer.cancel()
        self.__MazeFrame.destroy()
        self.__score = round(self.__score,2) #점수를 소수점 2째짜리까지 반올림함 ( 타이머기능의 오차가 있어서 반올림 해줌)
        if(self.__ms == 10):
            ranking = "랭킹초급.txt"
        elif(self.__ms == 20):
            ranking = "랭킹중급.txt"
        elif(self.__ms == 30):
            ranking = "랭킹고급.txt"
        information = open(ranking,"a+")
        information.seek(0)
        while(True): #유저정보를 읽음 
            infor = information.readline()
            userinfor = infor.split(" ")
            if(userinfor[0] != ''):
                userinfor[1] = userinfor[1].replace("\n","") # \n 을 ""으로 대체해 파일에 엔터가 두번들어가지 않게 함.
                userInfor.append(userinfor)
                if userinfor[0] == self.__id:
                    check= True
               # print(userInfor)
            if not infor: #읽을 파일이 없으면 
                break #while문 해제
        information.close()
        information2 = open(ranking,"w") #수정된 값들을 다시 파일에 덮어씌움
        for i in userInfor:
            if(i[0] == self.__id): #로그인된 아이디의 정보가 이미 있으
                if float(i[1])> self.__score: #시간단축을 성공했으면
                    i[1] = str(self.__score)
            information2.write(i[0])
            information2.write(" "+i[1])
            information2.write("\n")
        if not userInfor or check ==False:
            information2.write(self.__id)
            information2.write(" "+str(self.__score))
            information2.write("\n")
        tk.messagebox.showinfo("축하합니다.","통과하셨습니다 기록\n %s초 입니다."% str(self.__score))
        information2.close()
            
            
        print(self.__score)    
