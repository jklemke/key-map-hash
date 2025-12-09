#!/usr/bin/python

# trying to figure out the right base58 string for Flickr
# rev-canonical shortening from ID
# *nearly* there....

# yes, this should be written as a test really

import baseconv
# http://www.djangosnippets.org/snippets/1431/ - baseconv.py

base58 = baseconv.BaseConverter('123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ')
# thank you kellan! http://www.flickr.com/groups/api/discuss/72157616713786392/

hashes = {3429289555: '6e3w38',
          3368: '215',
          74: '2h',
          75: '2i',
          94: '2C',
          88: '2w',
          195102: 'ZZQ',
          1253576: '7qDo',
          177: '44',
          193: '4k',
          195: '4n',
       }

for dec in hashes.keys():
  print dec,
  print base58.from_decimal(dec),
  print hashes[dec]

# results:
# 3429289555 6e31iZ 6e3w38 # <--- not right: overflow issue with integer?
# 1253576 7qDo 7qDo
# 195102 ZZQ ZZQ
# 3368 215 215
# 195 4n 4n
# 193 4k 4k
# 177 44 44
# 94 2C 2C
# 88 2w 2w
# 75 2i 2i
# 74 2h 2h
