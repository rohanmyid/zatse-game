    
    
    #This program is free software: you can redistribute it and/or modify
    #it under the terms of the GNU General Public License as published by
    #the Free Software Foundation, either version 3 of the License, or
    #(at your option) any later version.

    #This program is distributed in the hope that it will be useful,
    #but WITHOUT ANY WARRANTY; without even the implied warranty of
    #MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    #GNU General Public License for more details.

    #You should have received a copy of the GNU General Public License
    #along with this program.  If not, see <http://www.gnu.org/licenses/>.


import pygame,sys,time
from pygame.locals import *
print('Hello Friends: This is 2 player snake game\n ')
print('player 1: \n   \n LINE COLOR: blue \n\n CONTROLS:  A    (contols top left and bottom right) \n            S    (contols top right and bottom left)\n')
print('player 2: \n  \n    LINE COLOR: pink\n\n    CONTROLS:  K    (contols top left and bottom right)\n               L    (contols top right and bottom left)')
print('\nPress "ENTER" to continue to GAME: "BEST OF LUCK"')
choice = input()





pygame.init()
windowSurface=pygame.display.set_mode((500,400),0,32)
pixArray = pygame.PixelArray(windowSurface)
q=0
w=0
#external mazes starts
while( q<500):
    w=0
    while(w<15):
        pixArray[q][w]=(200,200,200)
        w=w+1
    q=q+1        

q=485
while( q<500):
    w=15
    while(w<385):
        pixArray[q][w]=(200,200,200)
        w=w+1
    q=q+1       
q=0 
while( q<15):
    w=15
    while(w<385):
        pixArray[q][w]=(200,200,200)
        w=w+1
    q=q+1     
q=0   
while( q<500):
    w=385
    while(w<400):
        pixArray[q][w]=(200,200,200)
        w=w+1
    q=q+1
#external mazes ends
#internal mazes starts
#maze 1
q=110
while( q<120):
    w=100
    while(w<200):
        pixArray[q][w]=(200,200,200)
        w=w+1
    q=q+1        
#maze 2
q=200   
while( q<210):
    w=200
    while(w<350):
        pixArray[q][w]=(200,200,200)
        w=w+1
    q=q+1       
#maze 3
q=360    
while( q<370):
    w=100
    while(w<200):
        pixArray[q][w]=(200,200,200)
        w=w+1
    q=q+1    
del pixArray
#internal mazes ends here

BLACK=(0,0,0)

o=0
k=1
p=1
z=1
d=1
l=1
f=1
m=1
c=2.1
q=300
w=200

n=1
v=2.1
t=350
y=300
while True:
# check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
#events page 363
        if event.type == KEYDOWN:
# change the keyboard variables
            #player 1
            if event.key == ord('s'):
                if m >= 2.1:
                    m=2.1
                if m<=0:
                    m=0.2
                if r>w:
                    z=2
                    m=m+0.5
                if r<w:
                    z=1
                    m=m-0.5
                if m >= 2.1:
                    m=2.1
                if m<=0:
                    m=0.2
               
                l=1    
                
                
                c=w-(m*q)
            if event.key == ord('a'):
                if m <= -2.1:
                    m=-2.1
                if m>=0:
                    m=-0.2
                if r>w:
                    k=2
                    m=m+0.5
                if r<w:
                    k=1
                    m=m-0.5
                if m <= -2.1:
                    m=-2.1
                if m>=0:
                    m=-0.2
               
                l=0    
                
                
                c=w-(m*q)
            #player 2 keys
            if event.key == event.key == ord('k'):
                if n >= 2.1:
                    n=2.1
                if n<=0:
                    n=0.2
                if i>y:
                    d=2 
                    n=n+0.5
                if i<y:
                    d=1 
                    n=n-0.5
                if n >= 2.1:
                    n=2.1
                if n<=0:
                    n=0.2
               
                f=1    
                
                
                v=y-(n*t)
           
            if event.key == ord('l'):
                if n <= -2.1:
                    n=-2.1
                if n>=0:
                    n=-0.2
                if i>y:
                    p=2# if not works properly either change k same with l in first player or playing keys of player 2
                    n=n+0.5
                if i<y:
                    p=1
                    n=n-0.5
                if n <= -2.1:
                    n=-2.1
                if n>=0:
                    n=-0.2
               
                f=0    #tbc
                
                
                v=y-(n*t)
                

   #player 1 line variables q w and etra variables e r slope m cons c controls a s
    if l==1: 
        e=q
        r=w
        if z==1:    
            q=q-1
        if z==2:
            q=q+1 
        w=(m*q)+c
    if l==0: 
        e=q
        r=w
        if k==1:    
            q=q+1
        if k==2:
            q=q-1 
        w=(m*q)+c
   #player 2 controls t y extra variables u i slope n cons v controls  k l
    if f==1: 
        u=t
        i=y
        if d==1:    
            t=t-1
        if d==2:
            t=t+1 
        y=(n*t)+v
    if f==0: 
        u=t
        i=y
        if p==1:    
            t=t+1
        if p==2:
            t=t-1 
        y=(n*t)+v
    #player 1 maze external condition 
    if q>485 or q<15 or w<15 or w>400:
        spam='player 2 win'
        print(spam)
                
        time.sleep(1)   
        pygame.quit()
        sys.exit()
    #player 2 maze external condition     
    if t>485 or t<15 or y<15 or y>400:
        spam='player 1 win'
        print(spam)
        pygame.quit()
        sys.exit()

     #player 1 internal maze condition    
    if q>110 and q<120 and w>100 and w<200:
        spam='player 2 win'
        print(spam)
                
        time.sleep(1)   
        pygame.quit()
        sys.exit()    
    if q>200 and q<210 and w<350 and w>200:
        spam='player 2 win'
        print(spam)
                
        time.sleep(1)   
        pygame.quit()
        sys.exit()
    if q>360 and q<370 and w<200 and w>100:
        spam='player 2 win'
        print(spam)
                
        time.sleep(1)   
        pygame.quit()
        sys.exit()


    #player 2 maze internal condition    
    if t>110 and t<120 and y>100 and y<200:
        spam='player 1 win'
        print(spam)
                
        time.sleep(1)   
        pygame.quit()
        sys.exit()    
    if t>200 and t<210 and y<350 and y>200:
        spam='player 1 win'
        print(spam)
                
        time.sleep(1)   
        pygame.quit()
        sys.exit()
    if t>360 and t<370 and y<200 and y>100:
        spam='player 1 win'
        print(spam)
                
        time.sleep(1)   
        pygame.quit()
        sys.exit()  
    pygame.draw.line(windowSurface, (0,200,200), (e,r), (q,
w), 3)
    
    pygame.draw.line(windowSurface, (200,0,200), (u,i), (t,
y), 3)
    pygame.display.update()
    o=1
    time.sleep(0.01)

