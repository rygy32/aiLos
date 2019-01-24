import mido
from chain import Chain

# Class for Parsing input to a MK Chain
class MKParser:

    def __init__(self, file):

        # Instantiate parse file on instantion
        self.file = file
        self.tempo = None
        self.tpb = None
        self.chain = Chain()
        self._parse()

    # Parse midi file:
    #    - Group in notes if they occur simultaneously
    #    - Look for tempo messages
    #    - Sequence them into the MK Dictionary
    def _parse(self):
        mid = mido.MidiFile(self.file)
        self.tpb = mid.ticks_per_beat
        old_lst = []
        temp_lst = []
        for track in mid.tracks:
            for message in track:
                #print (message)
                if message.type == "set_tempo":
                    self.tempo = message.tempo
                elif message.type == "note_on":
                    if message.time == 0:
                        temp_lst.append(message.note)
                    else:
                        temp_lst.append(message.note)
                        self._sequence(old_lst,temp_lst,message.time)
                        old_lst = temp_lst
                        temp_lst = []

    # Add note permutations to MK Chain
    def _sequence(self, old_lst,temp_lst, duration):
        for i in old_lst:
            for j in temp_lst:
                self.chain.add(i,j,self._time(duration))

    # Get time using tempo and time from midi file
    def _time(self,ticks):
        time_ms = ((ticks*self.tempo)/self.tpb)/1000
        return int(time_ms - (time_ms % 30) + 30)

    def return_chain(self):
        return self.chain