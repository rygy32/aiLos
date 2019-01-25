from collections import namedtuple
import matplotlib.pyplot as plt
import mido
import sys

Note = namedtuple('Note', ['note', 'duration'])

def maketuple(note, duration):
	return Note(note,duration)

def time(ticks,tempo,tpb):
	time_ms = ((ticks*tempo)/tpb)/1000
	#return int(time_ms - (time_ms % 50) + 50)
	return int(time_ms)

note_lst = []
duration_lst = []

plot = {}
chan={}

file = sys.argv[1]

for i in range(0,16):
	plot[i]=[]
	chan[i]=[]

mid = mido.MidiFile(file)
tpb = mid.ticks_per_beat
for track in mid.tracks:
	for message in track:
		if message.type == "set_tempo":
			tempo = message.tempo
		#print (message)
		elif message.type == "note_on":
			#print message.channel
			note = maketuple(message.note,time(message.time,tempo,tpb))
			chan[message.channel].append(note)
		elif message.type == "note_off":
		#	print 'test'
			chan[message.channel].append(maketuple(None,time(message.time,tempo,tpb)))


for i in range(0,16):
	for j in range(0,len(chan[i])):
		for k in range((chan[i][j].duration)+1):
			plot[i].append(chan[i][j].note)
		#plot[i].append(chan[i][j].note)
		#print chan[i][j].note
	plt.plot(plot[i],'.',markersize=3)

#plt.plot(note_lst,'s',markersize=3)
plt.show()