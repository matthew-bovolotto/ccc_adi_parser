#!/bin/python3.10

from unidecode import unidecode
import adif_io
import sys

from awards.canadaward    import Canadaward
from awards.ccca          import CCCA
#from awards.wana          import WANA
from awards.warac         import WARAC

from termcolor import colored

#print(sys.argv[1:])

convertfile = []
with open(sys.argv[1], 'r') as file:
    for line in file:
        convertfile.append(unidecode(line))

qsos, header = adif_io.read_from_string(''.join(convertfile))

#canadaward = Canadaward(qsos)
ccca = CCCA(qsos)
#warac = WARAC(qsos)
#wana = WANA(qsos)



