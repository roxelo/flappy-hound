import graphics
from graphics import *
import function
from function import *
import random
from random import *

win = GraphWin("Game", 800, 600)
sc = 0
setback = 380
setbock = -200
background = Image(Point(400,300),r"flapback.gif")
background.draw(win)
obstacle = Image(Point(800,setback),r"obstacle.gif")
obstacle.draw(win)
obstacle1 = Image(Point(800,setbock),r"obstacle.gif")
obstacle1.draw(win)

wid = obstacle.getWidth()
wid = wid/2
leng = obstacle.getHeight()
leng = leng/2


kat = Image(Point(400,300),r"Flappy.gif")
kat.draw(win)
score = text(400,50,str(sc),35,"white",win)
lek = kat.getHeight()
lek = lek/2
s = 0
b = 0
a = 0
g =0


while s== 0:
    if g == 0:
        if a < sc:
            a = sc
            print(a)
        menuback = Image(Point(400,300),r"menu.gif")
        menuback.draw(win)
        mtext1 = text(400,200,"Best Score",35,"white",win)
        mtext2 = text(400,250,str(a),35,"Red",win)
        mtext3 = text(400,350,"Your Score",35,"white",win)
        mtext4 = text(400,400,str(sc),35,"Red",win)
        menuback1 = Image(Point(310,475),r"menup1.gif")
        menuback1.draw(win)
        mtext5 = text(310,462,"Press Q",25,"Orange",win)
        mtext5b = text(310,489,"to Start",25,"Orange",win)
        menuback2 = Image(Point(490,475),r"menup1.gif")
        menuback2.draw(win)
        mtext6 = text(490,462,"Press A",25,"Orange",win)
        mtext6b = text(490,489,"to Quit",25,"Orange",win)
        
        g = 1
        
    
    if win.isClosed() == False:
        cool = win.checkKey()
        
        if cool == "q":
           cool = 1
        if cool == "a":
            win.close()
            s=1
            b=1
                        
        
        if cool == 1:
            menuback.undraw()
            mtext1.undraw()
            mtext2.undraw()
            mtext3.undraw()
            mtext4.undraw()
            menuback1.undraw()
            menuback2.undraw()
            mtext5.undraw()
            mtext5b.undraw()
            mtext6.undraw()
            mtext6b.undraw()
            g = 0
        
            b = 0
            kat.undraw()
            kat = Image(Point(400,300),r"Flappy.gif")
            kat.draw(win)
            obstacle.undraw()
            obstacle = Image(Point(800,setback),r"obstacle.gif")
            obstacle.draw(win)
            obstacle1.undraw()
            obstacle1 = Image(Point(800,setbock),r"obstacle.gif")
            obstacle1.draw(win)
            
            sc = 0
            score.undraw()
            score = text(400,50,str(sc),35,"white",win)
            while b ==0:
                time.sleep(0.015)
                kat.move(0,2.5)
                obstacle.move(-2,0)
                obstacle1.move(-2,0)
                obstacle_cor = obstacle.getAnchor()
                obstacle_corX = obstacle_cor.getX()
                obstacle_corY = obstacle_cor.getY()
                obstacle1_cor = obstacle1.getAnchor()
                obstacle1_corX = obstacle1_cor.getX()
                obstacle1_corY = obstacle1_cor.getY()
                obstacle_out = obstacle_corY - leng
                obstacle1_out = obstacle1_corY + leng
                kat_cor = kat.getAnchor()
                kat_corY = kat_cor.getY()
                kat_out1 = kat_corY+lek
                kat_out2 = kat_corY-lek
                obstacle_corXf = obstacle_corX+wid
                obstacle_corXg = obstacle_corX-wid
                if obstacle_corXg <= 400:
                    if obstacle_corXf >=400:
                    
                        if kat_out2<=obstacle1_out:
                            b = 1
                    
                    
                        if kat_out1>= obstacle_out:
                            b =1
                    
        
                if obstacle_corX == 0-wid:       
            
                    l = random()
            
                    setback = 380*l
            
                    setback = 800 - setback
                    setbock = setback - 580
            
                    obstacle1.undraw()
                    obstacle.undraw()
                    obstacle1 = Image(Point(800,setbock),r"obstacle.gif")
                    obstacle1.draw(win)
                    obstacle = Image(Point(800,setback),r"obstacle.gif")
                    obstacle.draw(win)
                    sc += 1
                    score.undraw()
                    score = text(400,50,str(sc),35,"white",win)
            
        
        

                move = win.checkKey()
                if move == "Up":
                    kat.move(0,-50.5)

    
