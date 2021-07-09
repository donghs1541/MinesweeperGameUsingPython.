from random import randint
from tkinter import *
import tkinter


class Mazeexe():
    def __init__(self,rcSize):
        self.__mapSize = 15#픽셀 
        self.__ms = rcSize # 행 렬 사이즈 
        self.__visited_cells = []
        self.__walls = []
        self.__revisitedCells = []
        self.__map = [['Wall' for _ in range(self.__ms)] for _ in range(self.__ms)]   #맵전체를 'Wall'로줌 즉 검정색으로 칠함

        self.__startRow = 1 #시작 위치는 1, 1 임
        self.__startColumn = 1 #시작위치 
             
        #시작구간 생성 
    def Start(self):         
        ccr, ccc = self.__startRow, self.__startColumn
        self.__x1 = ccr * self.__ms
        self.__y1 = ccc * self.__ms
        print(self.__startRow, self.__startColumn)
        print(ccr, ccc)
            
        self.__map[ccr][ccc] = 'PassAway'
        loop = 1
        while loop:  #미로 만드는 구간 
            self.__visitable_neighbours = self.checkNeighbours(ccr, ccc)
            if len(self.__visitable_neighbours) != 0:
                d = randint(1, len(self.__visitable_neighbours))-1
                ncr, ncc = self.__visitable_neighbours[d]
                self.__map[ncr][ncc] = 'PassAway'
                self.__visited_cells.append([ncr, ncc])
                ccr, ccc = ncr, ncc
            if len(self.__visitable_neighbours) == 0:
                try:
                    ccr, ccc = self.__visited_cells.pop()
                    self.__revisitedCells.append([ccr, ccc])
         
                except:
                    loop = 0
        self.__MazeFrame = Tk()
        self.__MazeFrame.title('미로찾기')
        canvas_side = self.__ms*self.__mapSize
        self.__ffs = Canvas(self.__MazeFrame, width = canvas_side, height = canvas_side, bg = 'grey')
        self.__ffs.pack()
         
         
        self.create()
        self.__y1 = self.__startRow * self.__mapSize   #현재위치 만들기 
        self.__x1 = self.__startColumn * self.__mapSize  #현재위치 만들기
        self.draw(self.__startRow, self.__startColumn, 'red') #현재위치 그리기 


        self.draw(self.__ms-2, self.__ms-2, 'blue') #종착지 그리기 
          

        self.__MazeFrame.bind("<Key>", self.move)
     
     
        self.__MazeFrame.mainloop()

         


    def create(self): #맵 생성 
        for row in range(self.__ms):
            for col in range(self.__ms):
                if self.__map[row][col] == 'PassAway':
                    color = 'White'
                elif self.__map[row][col] == 'Wall':
                    color = 'black'
                self.draw(row, col, color)
     
     
    def draw(self, row, col, color):
        self.__x1 = col * self.__mapSize
        self.__y1 = row * self.__mapSize
        self.__x2 = self.__x1 + self.__mapSize
        self.__y2 = self.__y1 + self.__mapSize
        self.__ffs.create_rectangle(self.__x1, self.__y1, self.__x2, self.__y2, fill=color)
     
     
    def checkNeighbours(self,ccr, ccc):
        self.__neighbours = [[ccr,ccc - 1,ccr - 1,ccc - 2,ccr,ccc - 2,ccr + 1,ccc - 2,ccr - 1, ccc - 1, ccr + 1,ccc - 1],# left
                    [ccr, ccc + 1, ccr - 1, ccc + 2, ccr, ccc + 2, ccr + 1, ccc + 2, ccr - 1, ccc + 1, ccr + 1, ccc + 1], #right
                    [ccr - 1, ccc, ccr - 2, ccc - 1, ccr - 2, ccc, ccr - 2, ccc + 1, ccr - 1, ccc - 1, ccr - 1, ccc + 1], #top
                    [ccr + 1, ccc, ccr + 2, ccc - 1, ccr + 2, ccc, ccr + 2, ccc + 1, ccr + 1, ccc-1, ccr + 1, ccc + 1]] #bottom
        self.__visitable_neighbours = []           
        for i in self.__neighbours:                                                                        #find neighbours to visit
            if i[0] > 0 and i[0] < (self.__ms-1) and i[1] > 0 and i[1] < (self.__ms-1):
                if self.__map[i[2]][i[3]] == 'PassAway' or self.__map[i[4]][i[5]] == 'PassAway' or self.__map[i[6]][i[7]] == 'PassAway' or self.__map[i[8]][i[9]] == 'PassAway' or self.__map[i[10]][i[11]] == 'PassAway':
                    self.__walls.append(i[0:2])                                                                                               
                else:
                    self.__visitable_neighbours.append(i[0:2])
        return self.__visitable_neighbours


     
    def presentLocation(self): #현재위치 그리기
        self.__ffs.create_rectangle((self.__x1, self.__y1, self.__x1 + self.__mapSize, self.__y1 + self.__mapSize), fill="blue") #현재위치를 파란색으로 표시함. 
     
    def priviousLocationClear(self): #지나간길 초기화 
        self.__ffs.create_rectangle((self.__x1, self.__y1, self.__x1 + self.__mapSize, self.__y1 + self.__mapSize), fill="white") #지나간 길을 다시 흰배경으로 채움 
     
    def move(self,event):  #움직이는 이벤트 

        self.__col = self.__w = self.__x1//self.__mapSize
        self.__row = self.__h = self.__y1//self.__mapSize
        print("before", self.__map[self.__row][self.__col])
        self.priviousLocationClear()
        if event.char == "a":
            if self.__map[self.__row][self.__col - 1] == "PassAway":
                self.__x1 -= self.__mapSize
        elif event.char == "d":
            if self.__map[self.__row][self.__col + 1] == "PassAway":
                self.__x1 += self.__mapSize
        elif event.char == "w":
            if self.__map[self.__row - 1][self.__col] == "PassAway":
                self.__y1 -= self.__mapSize
        elif event.char == "s":
            if self.__map[self.__row + 1][self.__col] == "PassAway":
                self.__y1 += self.__mapSize
        self.presentLocation()
        self.__col = self.__w = self.__x1//self.__mapSize #
        self.__row = self.__h = self.__y1//self.__mapSize
        print(self.__w, self.__h)
        print("after", self.__map[self.__row][self.__col])
        if(self.__w == 1 and self.__h== 1):
            
            print("통과")
            self.__MazeFrame.destroy()
            
     
