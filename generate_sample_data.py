#! /usr/bin/env python

'''
Mega-system generator
'''

from T5_worldgen.system import System

print('name,port,siz,atm,hyd,pop,gov,law,tl,uwp')
for ctr in range(5000):
    syst = System('System-{0:04d}'.format(ctr))
    print(','.join([
        syst.name,
        str(syst.mainworld.starport),
        str(syst.mainworld.size),
        str(syst.mainworld.atmosphere),
        str(syst.mainworld.hydrographics),
        str(syst.mainworld.population),
        str(syst.mainworld.government),
        str(syst.mainworld.law_level),
        str(syst.mainworld.tech_level),
        syst.mainworld.uwp()
    ]))
