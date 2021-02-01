from itertools import chain

key = "bookkeeping".replace("j", "i")
alphabet = "abcdefghiklmnopqrstuvwxyz" # note no J

# dedup the list of characters
slots = []
for x in chain(key, alphabet):
  if not x in slots: slots.append(x)

# get our matrix using list slices
matrix = [ slots[i:i+5] for i in range(0, 25, 5) ]
print(matrix)