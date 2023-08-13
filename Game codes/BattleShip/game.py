import mido
import subprocess
import socket

def pixel(p,color,port):
    msg = mido.Message('note_on', note=p, velocity=color)
    outport = mido.open_output(port)
    outport.send(msg)

def fill(color,port):
    for x in range (9):
        for y in range(9):
            a = y*10 + x
            pixel(a,color,port)
    
def clear(port):
    fill(0, port)

def saveMsg1(message,port):
    looped1 = 0
    printS1 = 0
    while printS1 == 0:
        msg = str(message).split(" ")[0]
        note = str(message).split(" ")[2]
        printN1 = str(note).split("=")[1]
        if msg == "note_on" and looped1 == 0:
            looped1 = 1
        for i in range(5):
            if pad1Sav[i] == 0:
                placeTile(pad1Sav, 37, port, printN1)
            else:
                continue
        looped1 = 1
        printS1 = 1
        
def saveMsg2(message, port):
    looped2 = 0
    printS2 = 0
    while printS2 == 0:
        msg = str(message).split(" ")[0]
        note = str(message).split(" ")[2]
        printN2 = str(note).split("=")[1]
        if msg == "note_on" and looped2 == 0:
            looped2 = 1
        for i in range(5):
            if pad2Sav[i] == 0:
                placeTile(pad2Sav, 120, port, printN2)
            else:
                continue
        looped2 = 1
        printS2 = 1
        
def placeTile(array,colors,port,message):
    for i in range(5):
        if array[i] == message:
            return False
        if array[i] == 0:
            array[i] = message
            pixel(int(message), colors, port)
            if colors == 37:
                name = "pad1Sav"
            elif colors == 120:
                name = "pad2Sav"      
            print("the array is " + name + f": {array}")
            return True
        else:
            continue
    return False

def checkTiles(array, message, port, player, guess):
    msg = str(message).split(" ")[2]
    note = str(msg).split("=")[1]
    count = 0
    while count != 1:
        if port == "Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0":
            mido.open_input("Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 32:0").close()
        elif port == "Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 32:0":
            mido.open_input("Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0").close()
        else:
            continue

        for i in range(5):
            if note != array[i]:
                pixel(int(note), 12, port)
                continue
            if note == array[i]:
                if player == "p1":
                    guess += 1
                    print("guess" + str(guess))
                elif player == "p2":
                    print("hi")
                    guess += 1
                pixel(int(note), 67, port)
                return guess
            else:
                continue
        count += 1
        return guess

def tcpSend(layerfunc):
    
    TCP_IP='192.168.10.10'
    TCP_PORT=5005
    BUFFER_SIZE=1024
    
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((TCP_IP,TCP_PORT))
    
    if layerfunc == "allOff":
        s.send(b"TCPSend(1,'{wdcustomscriptclick(124)}')!")
        s.send(b"TCPSend(1,'{wdcustomscriptclick(125)}')!")
        s.send(b"TCPSend(1,'{wdcustomscriptclick(126)}')!")
        s.send(b"TCPSend(1,'{wdcustomscriptclick(128)}')!")
        s.send(b"TCPSend(1,'{wdcustomscriptclick(130)}')!")
    elif layerfunc == "p1Choose":
        s.send(b"TCPSend(1,'{wdcustomscriptclick(121)}')!")
    elif layerfunc == "p2Choose":
        s.send(b"TCPSend(1,'{wdcustomscriptclick(122)}')!")
        s.send(b"TCPSend(1,'{wdcustomscriptclick(124)}')!")
    elif layerfunc == "guessGrid":
        print("bish")
        s.send(b"TCPSend(1,'{wdcustomscriptclick(123)}')!")
        s.send(b"TCPSend(1,'{wdcustomscriptclick(125)}')!")
    elif layerfunc == "p1Win":
        s.send(b"TCPSend(1,'{wdcustomscriptclick(127)}')!")
        s.send(b"TCPSend(1,'{wdcustomscriptclick(126)}')!")
    elif layerfunc == "p2Win":
        s.send(b"TCPSend(1,'{wdcustomscriptclick(129)}')!")
        s.send(b"TCPSend(1,'{wdcustomscriptclick(126)}')!")
        
    data=s.recv(BUFFER_SIZE)

def padDir():   
    pads_ports = mido.get_input_names()
    pads_1_port = None
    pads_2_port = None
    
    tileP1 = 0
    tileP2 = 0
    poiuy = 0
    abcde = 0

    for port in pads_ports:
        if 'Launchpad Pro MK3' in port:
            if 'MIDI 28:0' in port:
                pads_1_port = port
            elif 'MIDI 32:0' in port:
                pads_2_port = port
                
    for i in range(5):
        if pad1Sav[i] == 0:
            inport = mido.open_input(pads_1_port)
            mido.open_input(pads_2_port).close()
            while pad1Sav[4] == 0:
                tcpSend("p1Choose")
                saveMsg1(inport.receive(), pads_1_port)
        if pad2Sav[i] == 0 and pad1Sav[4] != 0:
            inport = mido.open_input(pads_2_port)
            mido.open_input(pads_1_port).close()
            while pad2Sav[4] == 0:
                tcpSend("p2Choose")
                saveMsg2(inport.receive(), pads_2_port)
                
    subprocess.run(["python", "clear.py"])
    tcpSend("guessGrid")
    print("guessing time")
    
    for i in range(25):
        if pad1Sav[4] != 0 and pad2Sav[4] != 0:
            if tileP1 < 25 and tileP1 == tileP2:
                inport = mido.open_input(pads_1_port)
                mido.open_input(pads_2_port).close()
                poiuy = checkTiles(pad2Sav,inport.receive(), pads_1_port, "p1", poiuy)
                print("player 1 correct count = " + str(poiuy))
                tileP1 += 1
                print("tileP1 is: " + str(tileP1))
            if tileP1 > tileP2:
                inport = mido.open_input(pads_2_port)
                mido.open_input(pads_2_port).close()
                abcde = checkTiles(pad1Sav,inport.receive(), pads_2_port, "p2", abcde)
                print("player 2 correct count = " + str(abcde))
                tileP2 += 1
                print("tileP2 is: " + str(tileP2))
                
            if poiuy == 5 and abcde < 5:
                print("player 1 wins yippee !!!")
                tcpSend("p1Win")
                break
            elif abcde == 5 and poiuy < 5:
                print("player 2 wins yahoo !!!")
                tcpSend("p2Win")
                break
            else:
                continue

def main():
    tcpSend("allOff")
    subprocess.run(["python", "clear.py"])
    padDir()

pad1Sav = [0,0,0,0,0]
pad2Sav = [0,0,0,0,0]

if __name__ == "__main__":
    main()

