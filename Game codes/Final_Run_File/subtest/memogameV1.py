import time
import random
import mido
inputport = mido.get_input_names() #get name of device and input port used
outputport = mido.get_output_names() #get name of device and output port used
launchpad = 'Launchpad Pro MK3 LPProMK3 MIDI' #name of launchpad

outport = mido.open_output(launchpad) #open output port for sending commands
inport = mido.open_input(launchpad) #open input port for receiving feedback
r11 = [81,82,71,72]
r12 = [83,84,73,74]
r13 = [85,86,75,76]
r14 = [87,88,77,78]
r21 = [61,62,51,52]
r22 = [63,64,53,54]
r23 = [65,66,55,56]
r24 = [67,68,57,58]
r31 = [41,42,31,32]
r32 = [43,44,33,34]
r33 = [45,46,35,36]
r34 = [47,48,37,38]
r41 = [21,22,11,12]
r42 = [23,24,13,14]
r43 = [25,26,15,16]
r44 = [27,28,17,18]
pos = [r11,r12,r13,r14,
       r21,r22,r23,r24,
       r31,r32,r33,r34,
       r41,r42,r43,r44]
cards = [4,5,10,14,22,42,3,80]
plist = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7]
cardp = [0,0,0,0,
         0,0,0,0,
         0,0,0,0,
         0,0,0,0]

def pixel(pad,color): #function to light up 1 pixel
    msg = mido.Message('note_on', note=pad, velocity=color)
    outport.send(msg)
def pixeloff(pad): #function to light up 1 pixel
    msg = mido.Message('note_off', note=pad)
    outport.send(msg)
btn_state = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
index = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
def button(sposition,color): 
    btn_i =0
    for btn_i in range(len(pos[sposition])):
        pixel(pos[sposition][btn_i],color)
def buttonoff(sposition): 
    btn_i =0
    for btn_i in range(len(pos[sposition])):
        pixeloff(pos[sposition][btn_i])
def vline(startpixel,color): 
    for y in range(8) :        
        pixel(startpixel+y*10,color)
        y +=1
def fill(color):
    for i in range(9):
        np = 11+i
        vline(np,color)
fill(0)
## checks which button the player has pressed(pressed @ line 120) and give player color(pcolor @line113)
def position(spixel):
    global umi
    u = 0 
    position_i = 0
    while u < 16: ##check 'pos' array ->line 70
        position_i = 0
        if btn_state[u] ==0: ## when button in 'btn_state' array is blank -> line 74
            while position_i < 4:     ##find pixel in a single pixel array ->line 60 - 68
                if pos[u][position_i] == spixel: ##calling a specific pixel from the pixel array ->line 60 - 68, 70
                    button(index[u],cards[cardp[u]])
                    btn_state[u] = 1
                    umi = u
                    print(u)
                    position_i = 4
                    u = 17
                else:
                    position_i += 1
            u+=1
        else:
            u +=1
def randcard():
    random_store = []
    random_int = 0
    for randc in range(len(cardp)):
        random_int = random.choice(plist)
        plist.remove(random_int)
        cardp[randc] = random_int
        button(randc,cards[cardp[randc]])
        time.sleep(0.15)
        
    time.sleep(0.4)
    fill(0)
      
correct_selection = [ 0, 0, 0, 0, 0, 0, 0, 0]
randcard()
correct_count = 0
last_correct = 1000
Finished = "no"
while Finished == "no":
    allowed = "yes"
    count = 0
    press_store = [100,100]
    while count < 2:
        print(allowed)
        nte = inport.receive()
        print(nte)
        msg = nte.type
        print(msg)
        if msg == "note_on":
            pressed = nte.note
            position(pressed)
            print(press_store)
            mido.open_output(launchpad)
            if btn_state.count(1) != count and press_store[0] != umi and btn_state[umi] != 0  and last_correct != umi :
                press_store[count] = umi
                print(press_store)
                count += 1
                if press_store.count(100) == 0 and cardp[press_store[0]] != cardp[press_store[1]]:
                    time.sleep(0.1)
                    btn_state[press_store[0]] = 0
                    btn_state[press_store[1]] = 0
                    buttonoff(press_store[0])
                    buttonoff(press_store[1])
                    print(press_store)
                elif press_store.count(100) == 0 and cardp[press_store[0]] == cardp[press_store[1]]:
                    print(cardp)
                    print(cardp[press_store[0]], cardp[press_store[1]])
                    time.sleep(0.1)
                    correct_selection[correct_count] = 1
                    print("correct : "+ str(correct_selection))
                    correct_count += 1
                    last_correct = press_store[1]
                    if correct_selection.count(0) == 0:
                        fill(80)
                        time.sleep(0.25)
                        fill(0)
                        time.sleep(0.25)
                        fill(80)
                        time.sleep(0.25)
                        fill(0)
                        time.sleep(0.25)
                        fill(80)
                        Finished = "yes"
                        
                
                
            
