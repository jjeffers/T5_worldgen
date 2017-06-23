'''JsonIntegrationTests'''
from __future__ import print_function

import unittest
import json
import logging

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

from T5_worldgen.system import System
from T5_worldgen.star import _Star, Primary
from T5_worldgen.planet import Planet
from T5_worldgen import upp

SAMPLE_SIZE = 1000

class JsonIntegrationTests(unittest.TestCase):
    '''Integration tests for jsoon export/import'''
    def compare_dict_to_system(self, s_data, system):
        '''Compare s_data dict to system'''
        self.assertTrue(s_data['name'] == system.name)
        self.assertTrue(s_data['hex'] == system.hex)
        self.assertTrue(s_data['bases'] == system.bases)
        self.assertTrue(s_data['allegiance'] == system.allegiance)
        self.assertTrue(s_data['worlds'] == system.num_worlds)
        self.assertTrue(s_data['Ix'] == str(system.importance_x))
        self.assertTrue(s_data['Ex'] == str(system.economic_x))
        self.assertTrue(s_data['Cx'] == str(system.cultural_x))
        self.assertTrue(s_data['pbg'] == str(system.pbg))

    def compare_dict_to_planet(self, p_data, planet):
        '''Compare p_data dict to planet'''
        self.assertTrue(p_data['uwp'] == planet.uwp())
        self.assertTrue(p_data['trade_codes'] == planet.trade_codes)
        self.assertTrue(p_data['travel_code'] == planet.travel_code)
        self.assertTrue(p_data['bases'] == planet.bases)
        self.assertTrue(p_data['orbit'] == planet.orbit)
        self.assertTrue(p_data['is_mainworld'] == planet.is_mainworld)

    def compare_dict_to_star(self, s_data, star):
        '''Compare s_data to star'''
        self.assertTrue(s_data['spectral_type'] == star.spectral_type)
        self.assertTrue(s_data['size'] == star.size)
        self.assertTrue(s_data['decimal'] == star.decimal)
        self.assertTrue(s_data['habitable_zone'] == star.habitable_zone)
        if s_data['companion'] is None:
            self.assertTrue(star.companion == None)
        else:
            c_data = json.loads(s_data['companion'])
            self.assertTrue(
                c_data['spectral_type'] == star.companion.spectral_type)
            self.assertTrue(
                c_data['size'] == star.companion.size)
            self.assertTrue(
                c_data['habitable_zone'] == star.companion.habitable_zone)
            self.assertTrue(
                c_data['decimal'] == star.companion.decimal)
        for sec in s_data['secondaries'].keys():
            sec_data = json.loads(s_data['secondaries'][sec])
            obj_data = star.secondaries[sec]
            self.assertTrue(
                sec_data['spectral_type'] == obj_data.spectral_type)
            self.assertTrue(
                sec_data['size'] == obj_data.size)
            self.assertTrue(
                sec_data['decimal'] == obj_data.decimal)
            self.assertTrue(
                sec_data['habitable_zone'] == obj_data.habitable_zone)
            if sec_data['companion'] is not None:
                c_data = json.loads(sec_data['companion'])
                self.assertTrue(
                    c_data['spectral_type'] == \
                        obj_data.companion.spectral_type)
                self.assertTrue(
                    c_data['size'] == \
                        obj_data.companion.size)
                self.assertTrue(
                    c_data['decimal'] == \
                        obj_data.companion.decimal)
                self.assertTrue(
                    c_data['habitable_zone'] == \
                        obj_data.companion.habitable_zone)
            else:
                self.assertTrue(obj_data.companion == None)

    def test_export_import(self):
        '''Test re-import of exported data'''
        for _ in range(SAMPLE_SIZE):
            syst = System()
            # System
            s_data = json.loads(syst.as_json())
            LOGGER.debug('s_data type: %s', type(s_data))
            LOGGER.debug('s_data: %s', s_data)
            self.compare_dict_to_system(s_data, syst)
            # Planet
            p_data = json.loads(syst.mainworld.as_json())
            LOGGER.debug('p_data type: %s', type(p_data))
            LOGGER.debug('p_data: %s', p_data)
            self.compare_dict_to_planet(p_data, syst.mainworld)
            # Star(s)
            st_data = json.loads(syst.stellar.as_json())
            LOGGER.debug('st_data type: %s', type(st_data))
            LOGGER.debug('st_data: %s', st_data)
            self.compare_dict_to_star(st_data, syst.stellar)
