# -*- coding: utf-8 -*-
"""
Created on Tue May 31 11:42:43 2022

@author: User
"""


import pygame as pg
import os
import random
#初始化
pg.init()

#遊戲視窗標題名稱
pg.display.set_caption('接球遊戲')
#設置視窗初始位置
os.environ['SDL_VIDEO_WINDOW_POS']="%d,%d"%(0,32)

#視窗大小設定
width,height=1280,720
screen=pg.display.set_mode((width,height))

#圖片變數
background = pg.image.load("picture\\background1.jpg")
pad = pg.image.load("picture\\pad1.png").convert_alpha()
ball =pg.image.load("picture\\ball1.png").convert_alpha()
bomb =pg.image.load("picture\\bomb.png").convert_alpha()
pausebtn =pg.image.load("picture\\pause.png").convert_alpha()
startbtn =pg.image.load("picture\\start12.png").convert_alpha()

#圖片座標
back_rect=background.get_rect()

pad_rect=pad.get_rect()
ball_rect=ball.get_rect()
pad_rect.center=width/2,600
ball_rect.center=width/2,height/2

bomb_rect=bomb.get_rect()
bomb_rect.bottomleft=random.randint(0, width-bomb_rect.width),0

pause_rect=pausebtn.get_rect()
pause_rect.topright=width,0

start_rect=startbtn.get_rect()
start_rect.center=width/2,height/2+130





#黑洞建置
blackhole=[]
blackhole_rect=[]
for i in range(6):
    blackhole.append(pg.image.load("picture\\hole1.png").convert_alpha())
    blackhole_rect.append(blackhole[i].get_rect())
    blackhole_rect[i].center=200+(i%3)*400,50+(i//3)*150
r=blackhole_rect[0].width/2

    
def rebound1(bx,by,ix,iy,w,h=0):

    X=(speed[0]*(iy-by)/speed[1])+bx        #X為假定的碰撞範圍
    if by+speed[1]>=iy and (ix-w/2<=X and X<=ix+w/2):
        playspeed=0.1
        speed[1]+=playspeed
        speed[1]*=-1
        speed[0]=random.randint(-5,5)
        return  True,speed
    else:	 
        return False,speed
#黑洞碰撞
def hits(bx,by,ix,iy,r):
    if (bx-ix)**2+(by-iy)**2<=r**2:
        return True
    else:
        return False
#吃道具判定
def rebound2(bx,by,ix,iy,w,h=0):
    X=(speed[0]*(iy-by)/speed[1])+bx        #X為假定的碰撞範圍
    if by+speed[1]>=iy and (ix-w/2<=X and X<=ix+w/2): 
        return  True
    else:
        return False
#遊戲暫停
def pause(a):
    while a:
        clock.tick(30)
        #事件處理
        for event in pg.event.get():
            #正常關閉
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                x,y=pg.mouse.get_pos()
                if y>=start_rect.top and y<=start_rect.bottom and x>=start_rect.left and x<=start_rect.right:
                    a=False
                    break 
                   
        #圖片更新    (後寫得在最上)   
        screen.blit(background,back_rect)
        for i in range(6):
            screen.blit(blackhole[i],blackhole_rect[i])
        screen.blit(bomb,bomb_rect) 
        screen.blit(lifetext,life_rect)
        screen.blit(pad,pad_rect)
        screen.blit(ball,ball_rect)
        screen.blit(startbtn,start_rect)
        pg.display.update()
        
def restart(a):
    while a:
          clock.tick(30)   
          scoretext=font2.render(f"your score:{score}",True,(250,200,250))
          score_rect=scoretext.get_rect()
          score_rect.center=width/2,height/2
          gameovertext=font3.render("Game over",True,(250,100,100))
          gameover_rect=gameovertext.get_rect()
          gameover_rect.center=width/2,height/2-50
          #事件處理
          for event in pg.event.get():
              #正常關閉
              if event.type == pg.QUIT:
                  pg.quit()
              if event.type == pg.MOUSEBUTTONDOWN:
                  x,y=pg.mouse.get_pos()
                  if y>=start_rect.top and y<=start_rect.bottom and x>=start_rect.left and x<=start_rect.right:
                      a=False
                      break 
          
          #圖片更新    (後寫得在最上)   
          screen.blit(background,back_rect)
          screen.blit(startbtn,start_rect)
          screen.blit(scoretext,score_rect)
          screen.blit(gameovertext,gameover_rect)
          pg.display.update()
    
    
    
    
            
#全域變數
clock=pg.time.Clock()
speed=[random.randint(-5,5),5]
deadline=710
id=None
life=10
score=0

#文字設定
font = pg.font.SysFont("微軟正黑體",36)
font2 = pg.font.SysFont("微軟正黑體",50)
font3 = pg.font.SysFont("微軟正黑體",70)

bnbnoin=True #炸彈變數
bnbspeed=[0,0]

operation=True
while operation:
    clock.tick(60)
    
    lifetext=font.render(f"life:{life}", True, (250,200,250))
    life_rect=lifetext.get_rect()
    life_rect.top=pad_rect.bottom
    life_rect.centerx=pad_rect.centerx
    
    #事件處理
    for event in pg.event.get():
        #正常關閉
        if event.type == pg.QUIT:
            operation=False
            pg.quit()
        #滑鼠事件
        if event.type ==pg.MOUSEMOTION:
            x,y = pg.mouse.get_pos()
            pad_rect.centerx=x
        if event.type == pg.MOUSEBUTTONDOWN:
            x,y=pg.mouse.get_pos()
            if y>=pause_rect.top and y<=pause_rect.bottom and x>=pause_rect.left and x<=pause_rect.right:
                a=True
                pause(a)
            
            
    if pad_rect.right>=width:
        pad_rect.right=width
    if pad_rect.left<=0:
        pad_rect.left=0
    
    ball_rect=ball_rect.move(speed[0],speed[1])
    #ball_rect=ball_rect.move(speed)
    if ball_rect.left<=0:
        speed[0]=speed[0]*(-1)
        ball_rect.left=0
    if ball_rect.right>=width:
        speed[0]=speed[0]*(-1)
        ball_rect.right=width
    if ball_rect.top<=0:
        speed[1]=speed[1]*(-1)
        ball_rect.top=0
    if ball_rect.bottom>=deadline:
        ball_rect.center=width/2,height/2
        life-=1
    
    hit,speed=rebound1(ball_rect.centerx, ball_rect.centery, pad_rect.centerx, pad_rect.centery,pad_rect.width)
    
    if hit:
        ball_rect.bottom=pad_rect.top
        score+=100
    #黑洞碰撞
    for i in range(6):
        holehit = hits(ball_rect.centerx, ball_rect.centery, blackhole_rect[i].centerx, blackhole_rect[i].centery, r)
     
        if holehit:
            id=i
            a=random.randint(1, 3)
            if a==1:
                speed[0]*=-1
            if a==2:
                speed[1]*=-1
            if a==3:
                speed[0]*=-1
                speed[1]*=-1
            b=random.randint(0, 5)
            while b==id:
                b=random.randint(0, 5)
            if speed[0]>=0 and speed[1]>0:
                ball_rect.topleft=blackhole_rect[b].bottomright
            if speed[0]>=0 and speed[1]<0:
                ball_rect.bottomleft=blackhole_rect[b].topright
            if speed[0]<=0 and speed[1]>0:
                ball_rect.topright=blackhole_rect[b].bottomleft
            if speed[0]<=0 and speed[1]<0:
                ball_rect.bottomright=blackhole_rect[b].topleft
    #炸彈掉落
    probi=random.uniform(0, 1000)
    if probi<=5 and bnbnoin:
        bnbspeed[1]=random.randint(2,5)
        bnbnoin=False
    bomb_rect=bomb_rect.move(bnbspeed)
    bnbhit=rebound2(bomb_rect.centerx, bomb_rect.centery, pad_rect.centerx,pad_rect.centery,pad_rect.width)
    if bnbhit:
        bnbnoin=True
        bomb_rect.bottomleft=random.randint(0, width-bomb_rect.width),0
        life-=2
    if bomb_rect.bottom>=deadline:
        bnbnoin=True
        bomb_rect.bottomleft=random.randint(0, width-bomb_rect.width),0
        
        
            
    if life<=0:
        restart(True)
        life=10
        score=0
     #圖片更新    (後寫得在最上)   
    screen.blit(background,back_rect)
    for i in range(6):
        screen.blit(blackhole[i],blackhole_rect[i])
    screen.blit(bomb,bomb_rect) 
    screen.blit(lifetext,life_rect)
    screen.blit(pad,pad_rect)
    screen.blit(ball,ball_rect)
    screen.blit(pausebtn,pause_rect)

    pg.display.update()
    
    
    
