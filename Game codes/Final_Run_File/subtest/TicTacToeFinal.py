#this is a game of tictactoe on a launchpad
import mido
import time
inputport = mido.get_input_names() #get name of device and input port used
outputport = mido.get_output_names() #get name of device and output port used
launchpad = 'Launchpad Pro MK3 LPProMK3 MIDI' #name of launchpad

outport = mido.open_output(launchpad) #open output port for sending commands
inport = mido.open_input(launchpad) #open input port for receiving feedback

def pixel(pad,color): #function to light up 1 pixel
    msg = mido.Message('note_on', note=pad, velocity=color)
    outport.send(msg)
btn_state = [0,0,0,0,0,0,0,0,0]
index = [0,1,2,3,4,5,6,7,8]
#function to fill all pixels with stated color
def fill(color):
    for i in range(9):
        np = 11+i
        vline(np,color)
        btn_state[i] =1
def halfFill(color1,color2):
    for i in range(4):
        np = 11+i
        vline(np,color1)
        btn_state[i] =1
    for i in range(4):
        np = 15+i
        vline(np,color2)
#function to clear all pixels        
def clear(): 
    fill(0)

##draw horizontal line
def hline(startpixel,color): 
    for x in range(8) :        
        pixel(startpixel+x,color)
        x +=1

##draw vertical line
def vline(startpixel,color): 
    for y in range(8) :        
        pixel(startpixel+y*10,color)
        y +=1
        
##draw TicTacToe Frame        
def frame(color): 
    vline(13,color)
    vline(16,color)
    hline(31,color)
    hline(61,color)
    
##line 60 - 68 are arrays to show which pixels belong to each button    
lb = [11,12,21,22]  
lm = [41,42,51,52]
lt = [71,72,81,82]
mb = [14,15,24,25]
c = [44,45,54,55]
mt = [74,75,84,85]
rb = [17,18,27,28]
rm = [47,48,57,58]
rt = [77,78,87,88]

pos = [lb,lm,lt,mb,c,mt,rb,rm,rt] ## array to store the arrays for buttons



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
                    position_i = 4
                    u = 9
                else:
                    position_i += 1
            u+=1
            
        else:
            u +=1

clear()
frame(50)
pcolor = [60,40]
index_color = [0,0,0,0,0,0,0,0,0]
def returngrid():
    for memo in range (len(index_color)):
        print(memo)
        if index_color[memo] != 0:
            button(memo,index_color[memo])
def winCheck(splayer):
    global count
    if (btn_state[3] == 1 and index_color[3] == splayer) and (btn_state[4] == 1 and index_color[4] == splayer)and (btn_state[5] == 1 and index_color[5] == splayer):
        fill(splayer)
        time.sleep(2)
        count = 10
    elif (btn_state[0] == 1 and index_color[0] == splayer) and (btn_state[1] == 1 and index_color[1] == splayer)and (btn_state[2] == 1 and index_color[2] == splayer):
        fill(splayer)
        time.sleep(2)
        count = 10
    elif (btn_state[6] == 1 and index_color[6] == splayer) and (btn_state[7] == 1 and index_color[7] == splayer)and (btn_state[8] == 1 and index_color[8] == splayer):
        fill(splayer)
        time.sleep(2)
        count = 10
    elif (btn_state[0] == 1 and index_color[0] == splayer) and (btn_state[3] == 1 and index_color[3] == splayer)and (btn_state[6] == 1 and index_color[6] == splayer):
        fill(splayer)
        time.sleep(2)
        count = 10
    elif (btn_state[1] == 1 and index_color[1] == splayer) and (btn_state[4] == 1 and index_color[4] == splayer)and (btn_state[7] == 1 and index_color[7] == splayer):
        fill(splayer)
        time.sleep(2)
        count = 10
    elif (btn_state[2] == 1 and index_color[2] == splayer) and (btn_state[5] == 1 and index_color[5] == splayer)and (btn_state[8] == 1 and index_color[8] == splayer):
        fill(splayer)
        time.sleep(2)
        count = 10
    elif (btn_state[0] == 1 and index_color[0] == splayer) and (btn_state[4] == 1 and index_color[4] == splayer)and (btn_state[8] == 1 and index_color[8] == splayer):
        fill(splayer)
        time.sleep(2)
        count = 10
    elif (btn_state[2] == 1 and index_color[2] == splayer) and (btn_state[4] == 1 and index_color[4] == splayer)and (btn_state[6] == 1 and index_color[6] == splayer):
        fill(splayer)
        time.sleep(2)
        count = 10
    elif count == 9:
        halfFill(pcolor[0],pcolor[1])
        time.sleep(1)
        count = 10


count = 0
#     mido.open_input(launchpad)
if inport.closed:
    print("port is closed")
count = 0
print('GAME STARTO!')
clear()
frame(50)
btn_state = [0,0,0,0,0,0,0,0,0]
index_color = [0,0,0,0,0,0,0,0,0]
while count <10:
    print(count)
    nte = inport.receive()
    print(nte)
    pressed = nte.note
    mido.open_output(launchpad)
    print('note pressed is : ' + str(pressed))
    if pressed == 16:
        frame(50)
        returngrid()
    if pressed != 16 and nte.velocity > 0:
        if count%2 == 0:
            print('note pressed is : ' + str(pressed))
            player = pcolor[0]
            position(pressed,player)
            if btn_state.count(1) != count :
                count +=1
                winCheck(player)
        elif count%2 == 1:
            print('note pressed is : ' + str(pressed))
            player = pcolor[1]
            position(pressed,pcolor[1])
            if btn_state.count(1) != count :
                count +=1
                winCheck(player)
