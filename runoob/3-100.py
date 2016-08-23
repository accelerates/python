#!/usr/bin/python
#coding=utf-8
import math
for i in range(0,100000):
  sqrt1 = int(math.sqrt(i+100))
  sqrt2 = int(math.sqrt(i+268))
  if(sqrt1*sqrt1 == i+100) and (sqrt2*sqrt2 == i+268):
    print i
