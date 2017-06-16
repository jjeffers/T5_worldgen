'''star unit tests'''
from __future__ import print_function

import unittest
import json
from T5_worldgen.star import _Star, Primary

SAMPLE_SIZE = 1000


class TestStarTables(unittest.TestCase):
    '''Confirm contents of star generation tables'''
    def check_table_contents(self, table_data, table):
        '''Generic table contents checker'''
        for (ctr, size) in enumerate(table_data):
            table_contents = table.lookup(ctr - 6)
            print(ctr, ctr - 6, size, table_contents)
            self.assertTrue(
                size == table_contents)

    def test_spectral_type_table(self):
        '''Confirm contents of spectral type table'''
        star = _Star()
        table_data = [
            'OB', 'A', 'A', 'F', 'F',
            'G', 'G', 'K', 'K', 'M',
            'M', 'M', 'BD', 'BD', 'BD']
        self.check_table_contents(table_data, star.spectral_type_table)

    def test_size_o(self):
        '''Confirm contents of size table type O'''
        star = _Star()
        table_data = [
            'Ia', 'Ia', 'Ib', 'II', 'III',
            'III', 'III', 'V', 'V', 'V',
            'IV', 'D', 'IV', 'IV', 'IV']
        self.check_table_contents(table_data, star.size_o_table)

    def test_size_b(self):
        ''' Confirm contents of size table type B'''
        star = _Star()
        table_data = [
            'Ia', 'Ia', 'Ib', 'II', 'III',
            'III', 'III', 'III', 'V', 'V',
            'IV', 'D', 'IV', 'IV', 'IV']
        self.check_table_contents(table_data, star.size_b_table)

    def test_size_a(self):
        ''' Confirm contents of size table type A'''
        star = _Star()
        table_data = [
            'Ia', 'Ia', 'Ib', 'II', 'III',
            'IV', 'V', 'V', 'V', 'V',
            'V', 'D', 'V', 'V', 'V']
        self.check_table_contents(table_data, star.size_a_table)

    def test_size_f(self):
        ''' Confirm contents of size table type F'''
        star = _Star()
        table_data = [
            'II', 'II', 'III', 'IV', 'V',
            'V', 'V', 'V', 'V', 'V',
            'VI', 'D', 'VI', 'VI', 'VI']
        self.check_table_contents(table_data, star.size_f_table)

    def test_size_g(self):
        ''' Confirm contents of size table type G'''
        star = _Star()
        table_data = [
            'II', 'II', 'III', 'IV', 'V',
            'V', 'V', 'V', 'V', 'V',
            'VI', 'D', 'VI', 'VI', 'VI']
        self.check_table_contents(table_data, star.size_g_table)

    def test_size_k(self):
        ''' Confirm contents of size table type K'''
        star = _Star()
        table_data = [
            'II', 'II', 'III', 'IV', 'V',
            'V', 'V', 'V', 'V', 'V',
            'VI', 'D', 'VI', 'VI', 'VI']
        self.check_table_contents(table_data, star.size_k_table)

    def test_size_m(self):
        ''' Confirm contents of size table type M'''
        star = _Star()
        table_data = [
            'II', 'II', 'II', 'II', 'III',
            'V', 'V', 'V', 'V', 'V',
            'VI', 'D', 'VI', 'VI', 'VI']
        self.check_table_contents(table_data, star.size_m_table)


class TestFVIDecimals(unittest.TestCase):
    '''FVi edge case'''
    def test_f_vi_decimal(self):
        '''Confirm F VI has decimals in range 0-4'''
        for _ in range(0, SAMPLE_SIZE):
            star = _Star()
            star.spectral_type = 'F'
            star.size = 'VI'
            star.set_decimal()
            print(star.decimal)
            self.assertTrue(star.decimal <= 4)

class TestHZTables(unittest.TestCase):
    '''Check HZ orbit tables'''
    def check_hz_orbits(self):
        '''Test HZ orbits'''

        hz_table = {
            'O': {'Ia': 15, 'Ib': 15, 'II': 14, 'III': 13, 'IV': 12, 'V': 11, 'VI': None, 'D': 1},
            'B': {'Ia': 13, 'Ib': 13, 'II': 12, 'III': 11, 'IV': 10, 'V': 9, 'VI': None, 'D': 0},
            'A': {'Ia': 12, 'Ib': 11, 'II': 9, 'III': 7, 'IV': 7, 'V': 7, 'VI': None, 'D': 0},
            'F': {'Ia': 11, 'Ib': 10, 'II': 9, 'III': 6, 'IV': 6, 'V': 5, 'VI': 3, 'D': 0},
            'G': {'Ia': 12, 'Ib': 10, 'II': 9, 'III': 7, 'IV': 5, 'V': 3, 'VI': 2, 'D': 0},
            'K': {'Ia': 12, 'Ib': 10, 'II': 9, 'III': 8, 'IV': 5, 'V': 2, 'VI': 1, 'D': 0},
            'M': {'Ia': 12, 'Ib': 11, 'II': 10, 'III': 9, 'IV': None, 'V': 0, 'VI': 0, 'D': 0}
        }

        for sta in 'OBAFGKM':
            for siz in ['Ia', 'Ia', 'II', 'III', 'IV', 'V', 'VI', 'D']:
                star = _Star()
                star.spectral_type = sta
                star.size = siz
                star.set_hz()
                print('st = {} sz = {} hz_table = {} star.habitable_zone = {}'.format(
                    sta, siz, hz_table[sta][siz], star.habitable_zone))
                self.assertTrue(star.habitable_zone == hz_table[sta][siz])


class TestJson(unittest.TestCase):
    '''Test JSON importer, exporter'''
    def test_as_json(self):
        '''Test star as_json() exporter'''
        star = Primary()
        jdata = star.as_json()
        s_data = json.loads(jdata)
        print('s_data', s_data)
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

    def test_json_import(self):
        '''Test star.json_import() importer'''
        jdata = '{"decimal": 4, "companion": null, ' +\
            '"habitable_zone": 7, "spectral_type": "A", "secondaries": ' +\
            '{"Far": "{\\"habitable_zone\\": 3, \\"spectral_type\\": \\"G\\", ' +\
            '\\"companion\\": null, \\"decimal\\": 1, \\"size\\": ' +\
            '\\"V\\"}"}, "size": "V"}'

        s_data = json.loads(jdata)
        star = Primary()
        print(s_data)
        star.json_import(jdata)
        print(
            's_data spectral_type = {} star spectral_type {}'.format(
                s_data['spectral_type'], star.spectral_type))
        self.assertTrue(s_data['spectral_type'] == star.spectral_type)
        self.assertTrue(s_data['size'] == star.size)
        self.assertTrue(s_data['decimal'] == star.decimal)
        self.assertTrue(s_data['habitable_zone'] == star.habitable_zone)
        # Companion
        if s_data['companion'] is not None:
            c_data = json.loads(s_data['companion'])
            self.assertTrue(
                c_data['spectral_type'] == star.companion.spectral_type)
            self.assertTrue(
                c_data['size'] == star.companion.size)
            self.assertTrue(
                c_data['decimal'] == star.companion.decimal)
            self.assertTrue(
                c_data['habitable_zone'] == star.companion.habitable_zone)
        # self.assertTrue(s_data['companion'] == star.companion)
        print('secondaries: {}'.format(s_data['secondaries']))
        for sec in s_data['secondaries'].keys():
            sec_data = json.loads(s_data['secondaries'][sec])
            obj_data = star.secondaries[sec]
            print('s_data: sec = {} data = {}; star = {}'.format(
                sec,
                s_data['secondaries'][sec],
                obj_data.display()))
            self.assertTrue(
                sec_data['spectral_type'] == obj_data.spectral_type)
            self.assertTrue(
                sec_data['size'] == obj_data.size)
            self.assertTrue(
                sec_data['decimal'] == obj_data.decimal)
            self.assertTrue(
                sec_data['habitable_zone'] == obj_data.habitable_zone)
            if sec_data['companion'] is not None:
                self.assertTrue(sec_data['companion']['spectral_type'] ==\
                    obj_data.companion.spectral_type)
                self.assertTrue(sec_data['companion']['size'] ==\
                    obj_data.companion.size)
                self.assertTrue(sec_data['companion']['habitable_zone'] ==\
                    obj_data.companion.habitable_zone)
                self.assertTrue(sec_data['companion']['decimal'] ==\
                    obj_data.companion.decimal)
            else:
                self.assertTrue(obj_data.companion == None)
