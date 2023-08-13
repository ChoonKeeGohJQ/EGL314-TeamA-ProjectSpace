import mido

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

def main():
    # Connect to the MIDI pads
    pads_ports = mido.get_input_names()

    pads_1_port = None
    pads_2_port = None

    for port in pads_ports:
        if 'Launchpad Pro MK3' in port:
            if 'MIDI 28:0' in port:
                pads_1_port = port
            elif 'MIDI 32:0' in port:
                pads_2_port = port
    clear(pads_1_port)
    clear(pads_2_port)
if __name__ == "__main__":
    main()