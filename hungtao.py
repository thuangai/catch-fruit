"""
mô tả game hứng quả
hứng táo, lê được 1 điểm
hứng lựu đạn, sầu riêng bị mất điểm
có 10 điểm để thắng
bị âm 2 điểm là thua
"""

from tkinter import *#tạo màng hình
from time import sleep#thời gian nghỉ
from PIL import ImageTk,Image#thên hảnh
from random import randint

img=[0,0,0,0,0,0]#tạo list hình
y=-20#toạn độ ban đầu
a=randint(10,690)
b=randint(10,690)
c=randint(10,690)
d=randint(10,690)
game=Tk()#tạo màng hình
game.title('hứng quả cho má')
canvas=Canvas(master=game,width=700,height=525,background="white")#chỉnh khung hình
canvas.pack()
img[0]=ImageTk.PhotoImage(Image.open('backgr.png'))#ảnh
img[1]=ImageTk.PhotoImage(Image.open('bowl.png'))
img[2]=ImageTk.PhotoImage(Image.open('tao.png'))
img[3]=ImageTk.PhotoImage(Image.open('le.png'))
img[4]=ImageTk.PhotoImage(Image.open('luu.png'))
img[5]=ImageTk.PhotoImage(Image.open('sau.png'))
backgr=canvas.create_image(0,0,anchor=NW,image=img[0])#gán ảnh
tao=canvas.create_image(a,y,anchor=NW,image=img[2])
le=canvas.create_image(b,y,anchor=NW,image=img[3])
bowl=canvas.create_image(0,420,anchor=NW,image=img[1])  
luu=canvas.create_image(c,y,anchor=NW,image=img[4])
sau=canvas.create_image(d,y,anchor=NW,image=img[5])
canvas.update()    
score=0#điểm
text_score=canvas.create_text(620,30,text="score: "+str(score),fill="white",font=("Times",20))#hiện điểm    
def taoroi():#táo rơi
    global tao,score
    canvas.move(tao,0,10)
    if canvas.coords(tao)[1]>550:#khi không nhặt được
        canvas.delete(tao)
        y=-20
        a=randint(10,690)
        tao=canvas.create_image(a,y,anchor=NW,image=img[2])
    if (canvas.coords(tao)[0]>=canvas.coords(bowl)[0] and canvas.coords(tao)[0]+50<=canvas.coords(bowl)[0]+120) and (canvas.coords(tao)[1]+50>= canvas.coords(bowl)[1] and canvas.coords(tao)[1]+50<=canvas.coords(bowl)[1]+37.5):#khi nhặt được
        canvas.delete(tao)
        y=-20
        a=randint(10,690)
        tao=canvas.create_image(a,y,anchor=NW,image=img[2])
        score=score+1
        canvas.itemconfig(text_score,text="score: "+str(score))
    canvas.update()
def leroi():# lê rơi
    global le,score
    canvas.move(le,0,10)
    if canvas.coords(le)[1]>550:
        canvas.delete(le)
        y=-20
        b=randint(10,690)
        le=canvas.create_image(b,y,anchor=NW,image=img[3])
    if (canvas.coords(le)[0]>=canvas.coords(bowl)[0] and canvas.coords(le)[0]+50<=canvas.coords(bowl)[0]+120) and (canvas.coords(le)[1]+50>= canvas.coords(bowl)[1] and canvas.coords(le)[1]+50<=canvas.coords(bowl)[1]+37.5):
        canvas.delete(le)
        y=-20
        b=randint(10,690)
        le=canvas.create_image(b,y,anchor=NW,image=img[3])
        score=score+1
        canvas.itemconfig(text_score,text="score: "+str(score))
    canvas.update()

def luuroi():#lựu đạn rơi
    global luu,score
    canvas.move(luu,0,10)
    if canvas.coords(luu)[1]>550:
        canvas.delete(luu)
        y=-20
        c=randint(10,690)
        luu=canvas.create_image(c,y,anchor=NW,image=img[4])
    if (canvas.coords(luu)[0]>=canvas.coords(bowl)[0] and canvas.coords(luu)[0]+50<=canvas.coords(bowl)[0]+120) and (canvas.coords(luu)[1]+50>= canvas.coords(bowl)[1] and canvas.coords(luu)[1]+50<=canvas.coords(bowl)[1]+37.5):
        canvas.delete(luu)
        y=-20
        c=randint(10,690)
        luu=canvas.create_image(c,y,anchor=NW,image=img[4])
        score=score-2
        canvas.itemconfig(text_score,text="score: "+str(score))
    canvas.update()

def sauroi():#sầu riêng rơi
    global sau,score
    canvas.move(sau,0,10)
    if canvas.coords(sau)[1]>550:
        canvas.delete(sau)
        y=-20
        d=randint(10,690)
        sau=canvas.create_image(d,y,anchor=NW,image=img[5])
    if (canvas.coords(sau)[0]>=canvas.coords(bowl)[0] and canvas.coords(sau)[0]+50<=canvas.coords(bowl)[0]+120) and (canvas.coords(sau)[1]+50>= canvas.coords(bowl)[1] and canvas.coords(sau)[1]+50<=canvas.coords(bowl)[1]+37.5):
        canvas.delete(sau)
        y=-20
        d=randint(10,690)
        sau=canvas.create_image(d,y,anchor=NW,image=img[5])
        score=score-1
        canvas.itemconfig(text_score,text="score: "+str(score))
    canvas.update()
    
def right():#di chuyển phải
    global bowl
    if canvas.coords(bowl)[0]<650:        
        canvas.move(bowl,20,0)
    canvas.update()
def left():#di chuyển trái
    global bowl
    if canvas.coords(bowl)[0]>-10:        
        canvas.move(bowl,-20,0)
    canvas.update()    
def keypress(event):#bấm nút
    if event.keysym=="Right":
        right()     
    if event.keysym=="Left":
        left()
canvas.bind_all("<KeyPress>",keypress)        
              
gameover=False 
while not gameover:#thực hiện trò chơi       
    taoroi()
            
    leroi()
      
    luuroi()
      
    sauroi() 
    sleep(0.05)  
    if score==10:
        gameover=True
        text_end=canvas.create_text(350,250,text="MẸ TỰ HÀO VỀ BẠN",fill="yellow",font=("Times",20))#hiện chữ thắng
        
    if score<=-2:
        gameover=True
        text_end=canvas.create_text(350,250,text="BẠN TOANG RỒI",fill="red",font=("Times",20))#hiện chữ thua   
                    
game.mainloop()