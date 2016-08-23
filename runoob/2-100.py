#!/usr/bin/python
#coding=utf-8

bonus = 0

crash = [1000000,600000,400000,200000,100000,0]

rate = [0.01,0.015,0.03,0.05,0.075,0.1]

profit = raw_input("请输入您的利润:");

profit = int(profit)

if profit<0 : 
  print "您输入的利润不正确"
  sys.exit()

crash_len = len(crash)
for i in range(0,crash_len) :
    if profit>crash[i]:
      bonus += (profit - crash[i])*rate[i]
      profit = crash[i]


print bonus
      


      
      
  
