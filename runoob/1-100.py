#!/usr/bin/python
num = 0
for i in range(1,5):
  for ii in range(1,5):
    for iii in range(1,5):
      if(i != ii) and ( ii != iii ) and ( iii != i):
        num = num + 1;

print num
