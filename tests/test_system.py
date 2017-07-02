'''test_system.py'''
from __future__ import print_function

import unittest
import json

from T5_worldgen.system import System
import T5_worldgen.upp as uwp


class TestJson(unittest.TestCase):
    '''Test JSON importer, exporter'''
    def test_as_json(self):
        '''Test system as_json() exporter'''
        system = System()
        jdata = system.as_json()
        s_data = json.loads(jdata)
        self.assertTrue(s_data['name'] == system.name)
        self.assertTrue(s_data['hex'] == system.hex)
        self.assertTrue(s_data['bases'] == system.bases)
        self.assertTrue(s_data['allegiance'] == system.allegiance)
        self.assertTrue(s_data['worlds'] == system.num_worlds)
        self.assertTrue(s_data['Ix'] == str(system.importance_x))
        self.assertTrue(s_data['Ex'] == str(system.economic_x))
        self.assertTrue(s_data['Cx'] == str(system.cultural_x))
        self.assertTrue(s_data['pbg'] == str(system.pbg))

    def test_json_importer(self):
        '''Test system.json_import() importer'''
        jdata = '{"mainworld": "{\\"trade_codes\\": [\\"Ni\\"], \\"travel_code\\": \\"\\", \\"is_mainworld\\": true, \\"uwp\\": \\"E510423-8\\", \\"orbit\\": 7, \\"bases\\": \\"\\"}", "worlds": 5, "allegiance": "Na", "stellar": "{\\"decimal\\": 2, \\"companion\\": \\"{\\\\\\"habitable_zone\\\\\\": 7, \\\\\\"spectral_type\\\\\\": \\\\\\"A\\\\\\", \\\\\\"companion\\\\\\": null, \\\\\\"decimal\\\\\\": 7, \\\\\\"size\\\\\\": \\\\\\"V\\\\\\"}\\", \\"habitable_zone\\": 7, \\"spectral_type\\": \\"A\\", \\"secondaries\\": {}, \\"size\\": \\"V\\"}", "Ix": "{-3}", "name": "", "zone": "", "Cx": "[511C]", "hex": "0000", "pbg": "001", "bases": "", "Ex": "(A31+2)", "nobility": "B"}'
        s_data = json.loads(jdata)
        system = System()
        system.json_import(jdata)
        self.assertTrue(s_data['name'] == system.name)
        self.assertTrue(s_data['hex'] == system.hex)
        self.assertTrue(s_data['bases'] == system.bases)
        self.assertTrue(s_data['allegiance'] == system.allegiance)
        self.assertTrue(s_data['worlds'] == system.num_worlds)
        self.assertTrue(s_data['Ix'] == str(system.importance_x))
        self.assertTrue(s_data['Ex'] == str(system.economic_x))
        self.assertTrue(s_data['Cx'] == str(system.cultural_x))
        self.assertTrue(s_data['pbg'] == str(system.pbg))


class TestTravelZones(unittest.TestCase):
    '''Test travel zone'''
    def test_green_zone_gov_law(self):
        '''Test gov+law < 20 => green TZ'''
        system = System()
        system.mainworld.government = uwp.Government('2')
        system.mainworld.law_level = uwp.LawLevel('5')
        system.determine_travel_zone()
        self.assertTrue(system.zone == '')

    def test_amber_zone_gov_law(self):
        '''Test gov+law in [20,21] => amber TZ'''
        system = System()
        system.mainworld.government = uwp.Government('A')
        system.mainworld.law_level = uwp.LawLevel('B')
        system.determine_travel_zone()
        self.assertTrue(system.zone == 'A')

    def test_red_zone_gov_law(self):
        '''Test gov+law >= 22 => red TZ'''
        system = System()
        system.mainworld.government = uwp.Government('C')
        system.mainworld.law_level = uwp.LawLevel('D')
        system.determine_travel_zone()
        self.assertTrue(system.zone == 'R')
