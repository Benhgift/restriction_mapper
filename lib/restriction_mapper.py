# this will take a bunch of cuts in a genome and give us the map of where the genome was cut
# only "find_restriction_map" is usable, all others are helpers

def pop_max (pieces): 
  return pop_do (pieces, max (pieces))

def pop_do (pieces, piece):
  if piece in pieces:
    pieces.remove(piece)
    return piece
  else:
    return []


def get_middles (cut_map, target_cut_site):
  # to remove from pieces
  site_list = []
  for cut_site in cut_map:
    if (cut_site > 0) and (cut_site < max (cut_map)):
      site_list.append (abs (cut_site - target_cut_site))
  return site_list

def do_direction (pieces, piece, cut_map, get_middles):
  # find extra lens cut map/piece differences
  middle_pieces = get_middles (cut_map, piece)
  if set (middle_pieces).issubset (pieces) or not middle_pieces:
    # the piece works for now.
    cut_map.append (piece)
    cut_map.sort()
    # remove the lens from pieces
    for mid_piece in middle_pieces: 
      pieces.remove (mid_piece)
    #continue recursion
    return find_res (pieces[:], cut_map[:])
  else:
    return []


def find_res (pieces, cut_map):
  # if there are no more pieces, we win!
  if not pieces:
    return cut_map
  # get the next big piece and its mirror
  max_piece = pop_max (pieces)
  mirror_piece = pop_do (pieces, max (cut_map) - max_piece)
  if not max_piece or not mirror_piece:
    return []

  # pretend it's the left or right piece, whichever works out, and if neither it'll return []
  mapped = do_direction (pieces[:], max_piece, cut_map[:], get_middles)
  if not mapped:
    mapped = do_direction (pieces[:], mirror_piece, cut_map[:], get_middles)
  return mapped

def find_restriction_map (pieces):
  # set up starting restriction_map
  cut_map = [0, pop_max (pieces)]
  # start recursively matching pieces to cut map
  cut_map = find_res (pieces, cut_map)
  print cut_map

if __name__ == "__main__":
  find_restriction_map (starting_pieces)

