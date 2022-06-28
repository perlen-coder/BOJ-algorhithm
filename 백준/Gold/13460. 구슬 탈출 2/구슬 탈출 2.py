from collections import deque
from sys import stdin
input=stdin.readline

n,m=map(int,input().split())
board=[list(input().rstrip()) for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
q=deque()

visited=[[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]

def init(): # R 구슬 위치와 B 구슬 위치를 넣어 큐에 두개 들어감
    rx,ry, bx, by = [0]*4
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                rx,ry = i,j
            elif board[i][j] == 'B':
                bx,by = i,j
    q.append((rx,ry,bx,by,1))
    visited[rx][ry][bx][by] = True

def move(x,y,dx,dy):
    count=0  #벽을 만나거낙 0을 만나기 전까지 계속 직진
    while board[x+dx][y+dy] != "#" and board[x][y] != 'O':
        x+=dx
        y+=dy
        count+=1
    return x,y,count

def bfs():
    init()
    while q:
        rx,ry,bx,by,depth=q.popleft()
        if depth>10:
            break
        for i in range(4):
            n_rx,n_ry,rcnt=move(rx,ry,dx[i],dy[i])
            n_bx,n_by,bcnt=move(bx,by,dx[i],dy[i])
            if board[n_bx][n_by] !='O':
                if board[n_rx][n_ry]=='O':
                    print(depth)
                    return
                if n_rx == n_bx and n_ry == n_by:
                    if rcnt>bcnt:
                        n_rx -= dx[i]
                        n_ry -= dy[i]
                    else:
                        n_bx -= dx[i]
                        n_by -= dy[i]

                if not visited[n_rx][n_ry][n_bx][n_by]:
                    visited[n_rx][n_ry][n_bx][n_by] = True
                    q.append((n_rx,n_ry,n_bx,n_by,depth+1)) 
    print(-1)
bfs()