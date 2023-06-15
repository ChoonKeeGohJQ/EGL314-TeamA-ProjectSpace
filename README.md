# EGL314-TeamA-ProjectSpace


## How to use midi to control midi devices.

1. Library to use.
-mido
-rtmidi


how to use mido?
1. import mido library(line 1)
2. how to detect devices(line 2-3)
2_1. line 2 and line 3 gives you similar results.
```
import mido                                                                                                                     
inputport = mido.get_input_names() #get name of device and input port used
outputport = mido.get_output_names() #get name of device and output port used
```


# This is the baseline for Tic Tac Toe on launchpad
```
import mido                                                                                                                     
import socket
inputport = mido.get_input_names() #get name of device and input port used
outputport = mido.get_output_names() #get name of device and output port used
launchpad = 'Launchpad MK2 MIDI 1' #name of launchpad

outport = mido.open_output(launchpad) #open output port for sending commands
inport = mido.open_input(launchpad) #open input port for receiving feedback


TCP_IP='192.168.10.10'
TCP_PORT=5005
BUFFER_SIZE=1024

A = [
b"TCPSend(1,'{wdcustomscriptclick(19)}')!",
b"TCPSend(1,'{wdcustomscriptclick(20)}')!",
b"TCPSend(1,'{wdcustomscriptclick(21)}')!",
b"TCPSend(1,'{wdcustomscriptclick(22)}')!",
b"TCPSend(1,'{wdcustomscriptclick(23)}')!",
b"TCPSend(1,'{wdcustomscriptclick(24)}')!",
b"TCPSend(1,'{wdcustomscriptclick(25)}')!",
b"TCPSend(1,'{wdcustomscriptclick(26)}')!",
b"TCPSend(1,'{wdcustomscriptclick(27)}')!"
    ]	#Lines for turning off O

B = [
b"TCPSend(1,'{wdcustomscriptclick(28)}')!",
b"TCPSend(1,'{wdcustomscriptclick(29)}')!",
b"TCPSend(1,'{wdcustomscriptclick(30)}')!",
b"TCPSend(1,'{wdcustomscriptclick(31)}')!",
b"TCPSend(1,'{wdcustomscriptclick(32)}')!",
b"TCPSend(1,'{wdcustomscriptclick(33)}')!",
b"TCPSend(1,'{wdcustomscriptclick(34)}')!",
b"TCPSend(1,'{wdcustomscriptclick(35)}')!",
b"TCPSend(1,'{wdcustomscriptclick(36)}')!"
    ]	#Lines for turning off X

C = [
b"TCPSend(1,'{wdcustomscriptclick(38)}')!",   
b"TCPSend(1,'{wdcustomscriptclick(40)}')!"    
    ]	#Lines to turn off winner signs
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))
def pixel(x,y,color): #function to light up 1 pixel
    grid = y*10 +x
    msg = mido.Message('note_on', note=grid, velocity=color)
    outport.send(msg)
btn_state = [0,0,0,0,0,0,0,0,0]
#function to fill all pixels with stated color
def fill(color):
    fill_i = 0
    for x in range(1,9):
        for fill_i in range(9):
            pixel(x,fill_i,color)
            btn_state[x-1] =1
            fill_i += 1
        x += 1
        
#function to clear all pixels        
def clear(): 
    fill(0)
```

## draw horizontal line
```
def hline(startpixel,color): 
    spixel = str(startpixel/10) ## line 28 - 31 splits the pad no into x,y cordinate
    yx = spixel.split('.')
    y = int(yx[0])
    x = int(yx[1])
    for x in range(1,9) :        
        pixel(x,y,color)
        x +=1
```

## draw vertical line
```
def vline(startpixel,color): 
    spixel = str(startpixel/10)  ## line 37 - 40 splits the pad no into x,y cordinate
    yx = spixel.split('.')
    y = int(yx[0])
    x = int(yx[1])
    for y in range(1,9) :        
        pixel(x,y,color)
        y +=
```
        
## draw TicTacToe Frame
```      
def frame(color): 
    vline(13,color)
    vline(16,color)
    hline(31,color)
    hline(61,color)
    pixel(9,1,10)
```    
    
## line 60 - 68 are arrays to show which pixels belong to each button 
```   
lb = [11,12,21,22]  
lm = [41,42,51,52]
lt = [71,72,81,82]
mb = [14,15,24,25]
c = [44,45,54,55]
mt = [74,75,84,85]
rb = [17,18,27,28]
rm = [47,48,57,58]
rt = [77,78,87,88]

tcp_btn_p2 = [
b"TCPSend(1,'{wdcustomscriptclick(1)}')!",
b"TCPSend(1,'{wdcustomscriptclick(2)}')!",
b"TCPSend(1,'{wdcustomscriptclick(3)}')!",
b"TCPSend(1,'{wdcustomscriptclick(4)}')!",
b"TCPSend(1,'{wdcustomscriptclick(5)}')!",
b"TCPSend(1,'{wdcustomscriptclick(6)}')!",
b"TCPSend(1,'{wdcustomscriptclick(7)}')!",
b"TCPSend(1,'{wdcustomscriptclick(8)}')!",
b"TCPSend(1,'{wdcustomscriptclick(9)}')!"
    ]
tcp_btn_p1 = [
b"TCPSend(1,'{wdcustomscriptclick(10)}')!",
b"TCPSend(1,'{wdcustomscriptclick(11)}')!",
b"TCPSend(1,'{wdcustomscriptclick(12)}')!",
b"TCPSend(1,'{wdcustomscriptclick(13)}')!",
b"TCPSend(1,'{wdcustomscriptclick(14)}')!",
b"TCPSend(1,'{wdcustomscriptclick(15)}')!",
b"TCPSend(1,'{wdcustomscriptclick(16)}')!",
b"TCPSend(1,'{wdcustomscriptclick(17)}')!",
b"TCPSend(1,'{wdcustomscriptclick(18)}')!"
    ]
tcp_win_statement = [
b"TCPSend(1,'{wdcustomscriptclick(37)}')!",
b"TCPSend(1,'{wdcustomscriptclick(39)}')!" 
    ]

pos = [lb,lm,lt,mb,c,mt,rb,rm,rt] ## array to store the arrays for buttons

index = [0,1,2,3,4,5,6,7,8]  ## array of the index for array 'pos'

btn_state = [0,0,0,0,0,0,0,0,0] ## array for the states of button.
```

## fill pixels in the single player box with the stated pos
def button(sposition,color): 
    btn_i =0
    for btn_i in range(len(pos[sposition])):
        spixel = str(pos[sposition][btn_i]/10)  ## line 79 - 84 splits the pad no into x,y cordinate
        yx = spixel.split('.')
        y = int(yx[0])
        x = int(yx[1])
        grid = y*10 +x
        msg = mido.Message('note_on', note=grid, velocity=color)
        outport.send(msg)

## checks which button the player has pressed(pressed @ line 120) and give player color(pcolor @line113)
```
def position(spixel,color): 
    u = 0 
    position_i = 0
    while u < 9: ##check 'pos' array ->line 70
        position_i = 0
        if btn_state[u] ==0: ## when button in 'btn_state' array is blank -> line 74
            while position_i < 4:     ##find pixel in a single pixel array ->line 60 - 68
                if pos[u][position_i] == spixel: ##calling a specific pixel from the pixel array ->line 60 - 68, 70
                    button(index[u],color)
                    btn_state[u] = 1
                    index_color[u] = color
                    if color == 60:
                        s.send(tcp_btn_p1[u])
                    else:
                        s.send(tcp_btn_p2[u])
                    position_i = 3
                    u = 7
                else:
                    position_i += 1
            u+=1
            
        else:
            u +=1
            
wVpixel = [0,3,6]
wHpixel = [0,1,2]
wDpixel = [0,2]
clear()
frame(50)
pcolor = [60,40]
index_color = [0,0,0,0,0,0,0,0,0]
def VwinCheck(splayer):
        if btn_state[3] == 1 and index_color[3] == splayer:
            if (btn_state[4] == 1 and index_color[4] == splayer)and (btn_state[5] == 1 and index_color[5] == splayer):
                if splayer == 60:
                    s.send(tcp_win_statement[0])
                else:
                    s.send(tcp_win_statement[1])
                
                fill(splayer)
        elif btn_state[0] == 1 and index_color[0] == splayer:
            if (btn_state[1] == 1 and index_color[1] == splayer)and (btn_state[2] == 1 and index_color[2] == splayer):
                if splayer == 60:
                    s.send(tcp_win_statement[0])
                else:
                    s.send(tcp_win_statement[1])
                
                fill(splayer)
        elif btn_state[6] == 1 and index_color[6] == splayer:
            if (btn_state[7] == 1 and index_color[7] == splayer)and (btn_state[8] == 1 and index_color[8] == splayer):
                if splayer == 60:
                    s.send(tcp_win_statement[0])
                else:
                    s.send(tcp_win_statement[1])
            
                fill(splayer)

def HwinCheck(splayer):
    for i in range(3):
        if btn_state[wHpixel[i]] == 1 and index_color[i] == splayer:
            if (btn_state[wHpixel[i]+3] == 1 and index_color[i+3] == splayer)and (btn_state[wHpixel[i]+6] == 1 and index_color[i+6] == splayer):
                if splayer == 60:
                    s.send(tcp_win_statement[0])
                else:
                    s.send(tcp_win_statement[1])
                fill(splayer)
def DwinCheck(splayer):
    if btn_state[0] == 1 and index_color[0] == splayer:
        if (btn_state[4] == 1 and index_color[4] == splayer)and (btn_state[8] == 1 and index_color[8] == splayer):
            if splayer == 60:
                s.send(tcp_win_statement[0])
            else:
                s.send(tcp_win_statement[1])
            fill(splayer)
    elif btn_state[2] == 1 and index_color[2] == splayer:
        if (btn_state[4] == 1 and index_color[4] == splayer)and (btn_state[6] == 1 and index_color[6] == splayer):
            if splayer == 60:
                s.send(tcp_win_statement[0])
            else:
                s.send(tcp_win_statement[1])
            fill(splayer)
while True:
    count = 0
    print('GAME STARTO!')
    for x in A:
        s.send(x)	#Turns all O off
        
    for x in B:
        s.send(x)	#Turns all X off   
        
    for x in C:
        s.send(x)	#Turns all winner signs off
    while count <10:
        inport = mido.open_input(launchpad)
        print(inport)
        nte = inport.receive()
        pressed = nte.note
        inport.close()
        if pressed == 19:
            clear()
            frame(50)
            count = 0
            btn_state = [0,0,0,0,0,0,0,0,0]
            index_color = [0,0,0,0,0,0,0,0,0]
            for x in A:
                s.send(x)	#Turns all O off
                
            for x in B:
                s.send(x)	#Turns all X off   
                
            for x in C:
                s.send(x)	#Turns all winner signs off
            print('note pressed is : ' + str(pressed))
        elif pressed != 19 and nte.velocity == 127:
            if count%2 == 0:
                player = pcolor[0]
                position(pressed,player)
                data=s.recv(BUFFER_SIZE)
                VwinCheck(player)
                HwinCheck(player)
                DwinCheck(player)
                if btn_state.count(1) != count :
                    count +=1
            elif count%2 == 1:
                player = pcolor[1]
                position(pressed,pcolor[1])
                data=s.recv(BUFFER_SIZE)
                VwinCheck(player)
                HwinCheck(player)
                DwinCheck(player)
                if btn_state.count(1) != count :
                    count +=1
```
                   
 # Bill Of Material (BOM)

 1. 1x Novation Launchpad Mk2
 2. 2x Raspberry Pi Raspi 4 Model B
 3. 1x Short Throw Projector Sony VPL-SW630
 4. 1x Media Server Lenovo ThinkStation P920
 5. 2x Ceiling Speakers Extron FF 220T
 6. 1x OEM Screen
 7. 1x Audio Amplifier Extron XPA 1002
 8. 1x Laptop HP Zbook 15 G5
 9. 1x HDMI Extender TX Kramer PT-571
 10. 1x HDMI Extender RX Kramer PT-572+
 11. x1 Wireless Router Netgear

 # Required Software

 1. Christie Pandora Box
 2. Thonny Python IDE
 3. Dongle for pandora license 

 # Network Settings

 # How To Start

