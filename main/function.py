import graphics
from graphics import *



def text(a,b,c,d,e, win):

    write = Text(Point(a,b), c)
    write.draw(win)
    write.setSize(d)
    write.setFill(e)
    return write

def rectangle(a,b,c,d,e,win):
    rect = Rectangle(Point(a,b),Point(c, d))
    rect.draw(win)
    rect.setFill(e)
    return rect

def line(a,b,c,d,e,win):
    li = Line(Point(a,b),Point(c,d))
    li.draw(win)
    li.setOutline(e)
    return li

def circle(a,b,c,d,e,win):
    #global circ
    circ = Circle(Point(a,b),c)
    circ.draw(win)
    circ.setOutline(d)
    circ.setFill(e)
    return circ

def entrys(a,b,c,win):
    #global circ
    entr = Entry(Point(a, b),c)
    entr.draw(win)

    return entr
def image(a,b,c,win):
    img = Image(Point(a,b),c)
    img.draw(win)
    return img

def moves(objects,x,y,z,a,b,win):
    staart = 0
    score1 = 0
    score2 = 0
    q =12.5
    r = q

    while staart==0:
        #Coordinates computer paddle
        paddle1_1 = comp_paddle.getP1()
        paddle1_2 = comp_paddle.getP2()
        paddleY1_1 = paddle1_1.getY()
        paddleY1_2 = paddle1_2.getY()

        #Coordinates User Paddle
        paddle_1 = user_paddle.getP1()
        paddle_2 = user_paddle.getP2()
        paddleY_1 = paddle_1.getY()
        paddleY_2 = paddle_2.getY()

        move = win.checkMouse()
        if move == None: #if there is no right click
            
            time.sleep(0.015)
            objects.move(x,y)
            cent= objects.getCenter()
            centY=cent.getY()
            centX=cent.getX()
        
            if centY == 526:
                y = -1
            elif centX == 800:
                x = -1
                #Change score (Goal for cumputer)
                score1 = score1 + 1
                a.undraw()
                a = text(300,37.5,str(score1),30,"Snow")
                
            elif centY == 74:
                y = 1
            elif centX == 0:
                x = 1
                #Change score (Goal for user)
                score2 = score2 + 1
                b.undraw()
                a = text(500,37.5,str(score2),30,"Snow")
                

        
        
            #Ball bounce USER PADDLE
            if centX >= 690:
                if centX <= 710:
                    if centY >= paddleY_1:
                        if centY <= paddleY_2:
                            x = -1
            
            #Ball bounce COMPUTER PADDLE
            if centX <= 116:
                if centX >= 85:
                    if centY >= paddleY1_1:
                        if centY <= paddleY1_2:
                            x = 1

            #Computer Paddle Move
            comp_paddle.move(0,q)
                   
            if paddleY1_2 > 525:
                q =-12.5     
            if paddleY1_1 < 75:
               q = 12.5

        elif move != None: #if there is a right click

            #USER PADDLE MOVEMENT
            moveY = move.getY()
            moveX = move.getX()

            if moveY<563:
                user_paddle.move(0,-25)
            elif moveY>563:
                user_paddle.move(0,25)
           
        






        
