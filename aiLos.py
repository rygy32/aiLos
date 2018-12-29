#Import packages
import mido
import numpy as np


###################
#
# Setup music files
#
###################


f_lst = ['BWV_846.mid']
#for i in range(1,16):
#    f_lst.append('sinfon'+str(i)+'.mid')

#Channel dictionary - Getting number of notes per channel
chan={}

def import_file(k):
    ch0_len=0
    mid = mido.MidiFile(f_lst[k])
    for j in range(16):
        chan[str(j)]=0
    for i, track in enumerate(mid.tracks):
        for msg in track:
            msg_lst=str(msg).split('channel=')
            print(msg)
            for j in range(16):
                if "channel="+str(j) in str(msg):
                    chan[str(j)]=chan[str(j)] + 1
    print(chan)

import_file(0)

