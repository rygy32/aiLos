from chain import Chain
import mido

# Markov Chain Generation
class MKOutput:

	# Instantiate the chain
	def __init__(self,chain):
		self.chain = chain

	# Load the chain, asserting its a Chain
	@staticmethod
	def load(chain):
		assert isinstance(chain, Chain)
		return MKOutput(chain)

	# Write out the note on/off message for extend
	def _write_note(self,note):
		return [mido.Message('note_on', note=note.note, velocity=80, time=0),mido.Message('note_off', note=note.note, velocity=0, time=note.duration)]

	# Write the midi file for a given length
	def write_midi(self,file,length=200):
		with mido.midifiles.MidiFile() as mid:
			track = mido.MidiTrack()
			prev_note = None
			for i in range(length):
				new_note = self.chain.next_note(prev_note)
				track.extend(self._write_note(new_note))
				prev_note=new_note
			mid.tracks.append(track)
			mid.save(file)
