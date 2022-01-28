#!/usr/bin/python
#coding=utf-8
from graphillion import GraphSet as gs
import graphillion.tutorial as tl
filename = 'out.csv'
f = open(filename, 'r')
lines = f.readlines()
f.close()

univ = []

for line in lines:
    dat = line.split(',')
    dat[2] = float(dat[2])
    edge = tuple(dat[0:3])
    univ.append(edge)
#univ=tl.grid(8,8)
print univ[0]
gs.set_universe(univ)
#tl.draw(univ)
#paths = 

#print len(paths)
print gs.paths('119','162').max_iter().next()