'''Sector/subsector'''
from __future__ import print_function

from random import randint, seed
import re
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

    def process_hex(self, hex_id, ss_id=''):
        '''Add system on probability check'''
        name = 'Name-{}{}'.format(hex_id, ss_id)
        if self.percentile() <= \
                self.system_presence_table.lookup(self.density):
            self.hexes[hex_id] = System(name, hex_id)

    def t5_tab(self):
        '''Output in T5 tab format'''
        header = '\t'.join([
            'Hex', 'Name', 'UWP', 'Remarks', '{Ix}', '(Ex)', '[Cx]',
            'Nobility', 'Bases', 'Zone', 'PBG', 'W', 'Allegiance',
            'Stars'])
        print(header)
        self.display()


class Subsector(_MappingRegion):
    '''Subsector
    Subsector(name)
    Optional
    - subsector_id (dflt = '')
    - density (dflt='Standard')
    '''
    def __init__(self, name, subsector_id='', density='Standard'):
        super(Subsector, self).__init__(name, density)
        self.size_x = 8
        self.size_y = 10
        self.base_x = 0
        self.base_y = 0
        self.subsector_id = subsector_id
        self.populate_subsector()

    def populate_subsector(self):
        '''Generate systems'''
        for x_coord in range(1, self.size_x + 1):
            for y_coord in range(1, self.size_y + 1):
                self.process_hex(
                    '{:02d}{:02d}'.format(x_coord, y_coord),
                    self.subsector_id)



class Sector(_MappingRegion):
    '''Sector'''
    def __init__(self, name, density='Standard'):
        super(Sector, self).__init__(name, density)
        self._subsector_offsets = {}
        self._determine_offsets()
        self.subsectors = {}
        self.generate_subsectors()
        self.get_system_hex = re.compile(r'^(\d\d\d\d)')

    def display(self):
        '''Display'''
        subsectors = 'AEIMBFJNCHKODHLP'
        for ss_id in subsectors:
            for hex_id in sorted(self.subsectors[ss_id].hexes.keys()):
                data = self.subsectors[ss_id].hexes[hex_id].display()
                # Transform hex to Sector co-ordinates
                print(self.transform_coordinates(data, ss_id))


    def generate_subsectors(self):
        '''Generate subsectors'''
        for ss_id in 'ABCDEFGHIJKLMNOP':
            self.subsectors[ss_id] = Subsector(
                'Subsector-{}'.format(ss_id), ss_id, self.density)

    def _determine_offsets(self):
        '''Determine hex offsets by sector_id'''
        subsector_ids = 'ABCDEFGHIJKLMNOP'
        for subsector_id in subsector_ids:
            subsector_num = subsector_ids.index(subsector_id)
            offset_x = 8 * (subsector_num // 4)
            offset_y = 10 * (subsector_num // 4)
            self._subsector_offsets[subsector_id] = (offset_x, offset_y)

    def transform_coordinates(self, system_data, ss_id):
        '''System data: transform hex to Sector co-ordinates'''
        orig = self.get_system_hex.match(system_data).group(1)
        x_id = int(orig[:2])
        y_id = int(orig[2:])
        x_id += self._subsector_offsets[ss_id][0]
        y_id += self._subsector_offsets[ss_id][1]
        new = '{:02d}{:02d}'.format(x_id, y_id)
        return system_data.replace(orig, new, 1)
