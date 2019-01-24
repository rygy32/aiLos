from collections import Counter, defaultdict, namedtuple
import random

Note = namedtuple('Note', ['note', 'duration'])

# Markov Chain Class
class Chain:
	# Instantiate the dictionaries
	def __init__(self):
		self.chain = defaultdict(Counter)
		self.counts = defaultdict(int)

	def _maketuple(self, note, duration):
		return Note(note,duration)

	# Sequence the note permutation
	def add(self, from_note, to_note, duration):
		self.chain[from_note][self._maketuple(to_note, duration)] += 1
		self.counts[from_note] += 1

	# Add the next note for writing midi files
	# If the previous note isn't in the chain, add a random note from chain
	# Otherwise, pick a random count and go through notes until one is selected
	def next_note(self, prev_note):
		print self.chain.keys()
		if prev_note is None or prev_note.note not in self.chain.keys():
			random_chain = self.chain[random.choice(list(self.chain.keys()))]
			return random.choice(list(random_chain.keys()))
		count = random.randint(0, self.counts[prev_note.note])
		for note, frequency in self.chain[prev_note.note].items():
			count -= frequency
			if count <= 0:
				return note

	# Print out the ditionay as a matrix, limiting the printed columns
	def matrix(self,limit=10):
		columns = []
		for from_note, to_notes in self.chain.items():
			for note in to_notes:
				if note not in columns:
					columns.append(note)
		_col = lambda string: '{:<8}'.format(string)
		_note = lambda note: '{}:{}'.format(note.note, note.duration)
		out = _col('')
		out +=  ''.join([_col(_note(note)) for note in columns[:limit]]) + '\n'
		for from_note,to_notes in self.chain.items():
			out += _col(from_note)
			for note in columns[:limit]:
				out += _col(to_notes[note])
			out += '\n'
		print(out)

	def get_chain(self):
		return {i: dict(j) for i, j in self.chain.items()}