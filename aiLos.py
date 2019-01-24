import mido
import sys
from midi_parser import MKParser
from output import MKOutput
from chain import Chain

# List of files to play around with, probably better
# using sys.argv but I wasn't changing files when I tested
#f_lst = ['sinfon2.mid','BWV_846.mid']
f_lst = []
for i in sys.argv[1:]:
	f_lst.append(i)
#f_lst = [sys.argv[1],sys.argv[2]]
print len(sys.argv)
o_lst = ['out.mid']

# Parse a chain from te file, then display matrix output
# Write the new midi file afterwards
chain = MKParser(f_lst).return_chain()
chain.matrix()

MKOutput.load(chain).write_midi(o_lst[0])
print("Success!")
