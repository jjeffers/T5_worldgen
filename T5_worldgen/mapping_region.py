'''Sector/subsector'''
from __future__ import print_function

from random import randint, seed
from T5_worldgen.system import System
from T5_worldgen.util import Table


class _MappingRegion(object):
    '''Sector/subsector base class'''

    system_presence_table = Table()
    system_presence_table.add_row('Extra galactic', 1)
    system_presence_table.add_row('Rift', 3)
    system_presence_table.add_row('Sparse', 17)
    system_presence_table.add_row('Scattered', 33)
    system_presence_table.add_row('Standard', 50)
    system_presence_table.add_row('Dense', 66)
    system_presence_table.add_row('Cluster', 83)
    system_presence_table.add_row('Core', 91)

    def __init__(self, name, density='Standard'):
        seed()
        self.name = name
        self.size_x = 0
        self.size_y = 0
        self.hexes = {}
        self.density = density

    def display(self):
        '''Display'''
        hexlist = sorted(self.hexes.keys())
        for hex_id in hexlist:
            print(self.hexes[hex_id].display())

    @staticmethod
    def percentile():
        '''1-100%'''
        return randint(1, 100)

    def process_hex(self, hex_id):
        '''Add system on probability check'''
        name = 'Name-{}'.format(hex_id)
        if self.percentile() <= \
                self.system_presence_table.lookup(self.density):
            self.hexes[hex_id] = System(name, hex_id)


class Subsector(_MappingRegion):
    '''Subsector'''
    def __init__(self, name, subsector_id='', density='Standard'):
        super(Subsector, self).__init__(name, density)
        self.size_x = 8
        self.size_y = 10
        self.base_x = 0
        self.base_y = 0
        self.subsector_id = subsector_id

    def populate_subsector(self):
        '''Generate systems'''
        for x_coord in range(1, self.size_x + 1):
            for y_coord in range(1, self.size_y + 1):
                self.process_hex('{:02d}{:02d}'.format(x_coord, y_coord))

    def determine_offsets(self):
        '''Determine hex offsets by sector_id'''
        subsector_ids = 'ABCDEFGHIJKLMNOP'
        try:
            subsector_num = subsector_ids.index(self.subsector_id)
            self.base_x = 8 * (subsector_num // 4) + 1
            self.base_y = 10 * (subsector_num // 4) + 1
        except ValueError:
            self.base_x = 0
            self.base_y = 0
