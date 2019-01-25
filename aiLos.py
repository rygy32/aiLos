import mido
import sys
from midi_parser import MKParser
from output import MKOutput
from chain import Chain

# List of files to play around with
f_lst = []
for i in sys.argv[1:]:
	f_lst.append(i)
o_lst = ['out.mid']

# Parse a chain from the file, then display matrix output
# Write the new midi file afterwards
chain = MKParser(f_lst).return_chain()
chain.matrix()

MKOutput.load(chain).write_midi(o_lst[0])
print("Success!")
