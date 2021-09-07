#!/usr/bin/python3

lines = open("data.in", "r").read().splitlines()
lines = list(map(lambda x:int(x), lines))

print("Part1", sum(lines))

frq = 0
FRQ = set()
while 1:
  for val in lines:
    frq += val
    if frq in FRQ:
      print("Part2", frq)
      exit()
    FRQ.add(frq)
