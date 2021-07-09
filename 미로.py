from random import randint
from tkinter import * 
 
mapSize = 50#pixels
ms = 20# rows and columns
visited_cells = [] #방문한것을 확인함 
walls = []
revisited_cells = [] #재방문한것 
 
# 받아온 사
map = [['w' for _ in range(ms)] for _ in range(ms)]
 
 
 
def create(): #색깔을 정한후 색을칠해줌 
    for row in range(ms):
        for col in range(ms):
            if map[row][col] == 'P':  #map의 위치가 P이면(길이면)
                color = 'White' #색을 하얀색으로 칠해줌 
            elif map[row][col] == 'w': #map의 위치가  'w' 이면 
                color = 'black' #색을 검은색으로 칠함 
            draw(row, col, color) #그리고 그 좌표에 색을 칠해줌  
 
 
def draw(row, col, color): #그리는 함수 
    x1 = col * mapSize    #
    y1 = row * mapSize
    x2 = x1 + mapSize
    y2 = y1 + mapSize
    ffs.create_rectangle(x1, y1, x2, y2, fill=color)
 
 
def check_neighbours(ccr, ccc):
    neighbours = [[ccr,ccc - 1,ccr - 1,ccc - 2,ccr,ccc - 2,ccr + 1,ccc - 2,ccr - 1, ccc - 1, ccr + 1,ccc - 1],# 왼쪽
                [ccr, ccc + 1, ccr - 1, ccc + 2, ccr, ccc + 2, ccr + 1, ccc + 2, ccr - 1, ccc + 1, ccr + 1, ccc + 1], #오른쪽방향
                [ccr - 1, ccc, ccr - 2, ccc - 1, ccr - 2, ccc, ccr - 2, ccc + 1, ccr - 1, ccc - 1, ccr - 1, ccc + 1], #위방향
                [ccr + 1, ccc, ccr + 2, ccc - 1, ccr + 2, ccc, ccr + 2, ccc + 1, ccr + 1, ccc-1, ccr + 1, ccc + 1]] #아랫방향
    visitable_neighbours = []           
    for i in neighbours:                                                                        #find neighbours to visit
        if i[0] > 0 and i[0] < (ms-1) and i[1] > 0 and i[1] < (ms-1): #미로크기 안이면 
            if map[i[2]][i[3]] == 'P' or map[i[4]][i[5]] == 'P' or map[i[6]][i[7]] == 'P' or map[i[8]][i[9]] == 'P' or map[i[10]][i[11]] == 'P': #목표 방향 주변에 길이 있으면 벽을 생성함 
                walls.append(i[0:2])
            else:
                visitable_neighbours.append(i[0:2]) #길이 없으면 좌표값을 추가해줌 
    return visitable_neighbours 
 
#시작구간 생성 
 
startRow = 1 #시작 위치는 1, 1 임
startColumn = 1 #시작위치 
start_color = 'Blue'
ccr, ccc = startRow, startColumn
x1 = ccr * mapSize
y1 = ccc * mapSize
 
map[ccr][ccc] = 'P'
loop = 1
while loop:  #미로 만드는 구간 
    visitable_neighbours = check_neighbours(ccr, ccc)
    if len(visitable_neighbours) != 0:  #
        d = randint(1, len(visitable_neighbours))-1
        ncr, ncc = visitable_neighbours[d]
        map[ncr][ncc] = 'P'
        visited_cells.append([ncr, ncc])
        ccr, ccc = ncr, ncc
    if len(visitable_neighbours) == 0: #길이 없다면 
        try:
            ccr, ccc = visited_cells.pop() #방문했던 좌표를 뺴옴 
            revisited_cells.append([ccr, ccc]) #그리고 재방문
 
        except:
            loop = 0
 
 
MazeFrame = Tk()
MazeFrame.title('미로찾기')
canvas_side = ms*mapSize
ffs = Canvas(MazeFrame, width = 200, height = 200, bg = 'grey')
ffs.pack()

 
 
create()
y1 = mapSize   #현재위치 만들기 
x1 = mapSize  #현재위치 만들기
draw(startRow, startColumn, start_color) #현재위치 그리기 




e = randint(1, len(revisited_cells))-1 
ecr = revisited_cells[e][0]
ecc = revisited_cells[e][1]
end_color = 'red' #종착지 색설정 
draw(ecr, ecc, end_color) #종착지 그리기 
 
 





 
def presentLocation(): #현재위치 그리기 
    ffs.create_rectangle((x1, y1, x1 +mapSize, y1 + mapSize), fill="blue") #현재위치를 파란색으로 표시함.
 
def priviousLocationClear(): #지나간길 초기화 
    ffs.create_rectangle((x1, y1, x1 + mapSize, y1 + mapSize), fill="white") #지나간 길을 다시 흰배경으로 채움 
 
def move(event):  #움직이는 이벤트 
    global x1, y1
    col = w = x1//mapSize
    row = h = y1//mapSize
    print("before", map[row][col])
    priviousLocationClear()
    if event.char == "a":
        if map[row][col - 1] == "P":
            x1 -= mapSize
    elif event.char == "d":
        if map[row][col + 1] == "P":
            x1 += mapSize
    elif event.char == "w":
        if map[row - 1][col] == "P":
            y1 -= mapSize
    elif event.char == "s":
        if map[row + 1][col] == "P":
            y1 += mapSize
    presentLocation()
    col = w = x1//mapSize
    row = h = y1//mapSize
    print(w, h)
    print("after", map[row][col])
 
 
MazeFrame.bind("<Key>", move)
 
 
MazeFrame.mainloop()
