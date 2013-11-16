#!/usr/bin/env python
'''Restriction mapper

Usage:
  res_mapper <cut_piece>...
  res_mapper (-h | --help)

Options:
  -h --help     Show this screen
  cut_piece     One of many lengths for your genome cuts
'''
import lib
from docopt import docopt

if __name__=='__main__':
  starting_pieces = [2,2,3,3,4,5,6,7,8,10]
  args = docopt(__doc__)
  if len (args['<cut_piece>']) < 5:
    print ("Not enough starting pieces... using example default of:")
    print (starting_pieces)
  else:
    starting_pieces = [int (x) for x in args['<cut_piece>']]
  print ("Cut placements in genome are at:")
  lib.find_restriction_map(starting_pieces)
