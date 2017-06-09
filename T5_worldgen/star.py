'''star module'''

from T5_worldgen.util import Die, Flux, Table
import logging

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

D2 = Die(2)
D5 = Die(5)
D6 = Die(6)
D10 = Die(10)
FLUX = Flux()


class _Star(object):
    '''Star base class'''
    spectral_type_table = Table()
    spectral_type_table.add_row(-6, 'OB')
    spectral_type_table.add_row((-5, -4), 'A')
    spectral_type_table.add_row((-3, -2), 'F')
    spectral_type_table.add_row((-1, 0), 'G')
    spectral_type_table.add_row((1, 2), 'K')
    spectral_type_table.add_row((3, 5), 'M')
    spectral_type_table.add_row((6, 8), 'BD')

    size_o_table = Table()
    size_o_table.add_row((-6, -5), 'Ia')
    size_o_table.add_row(-4, 'Ib')
    size_o_table.add_row(-3, 'II')
    size_o_table.add_row((-2, 0), 'III')
    size_o_table.add_row((1, 3), 'V')
    size_o_table.add_row(4, 'IV')
    size_o_table.add_row(5, 'D')
    size_o_table.add_row((6, 8), 'IV')

    size_b_table = Table()
    size_b_table.add_row((-6, -5), 'Ia')
    size_b_table.add_row(-4, 'Ib')
    size_b_table.add_row(-3, 'II')
    size_b_table.add_row((-2, 1), 'III')
    size_b_table.add_row((2, 3), 'V')
    size_b_table.add_row(4, 'IV')
    size_b_table.add_row(5, 'D')
    size_b_table.add_row((6, 8), 'IV')

    size_a_table = Table()
    size_a_table.add_row((-6, -5), 'Ia')
    size_a_table.add_row(-4, 'Ib')
    size_a_table.add_row(-3, 'II')
    size_a_table.add_row(-2, 'III')
    size_a_table.add_row(-1, 'IV')
    size_a_table.add_row((0, 4), 'V')
    size_a_table.add_row(5, 'D')
    size_a_table.add_row((6, 8), 'V')

    size_f_table = Table()
    size_f_table.add_row((-6, -5), 'II')
    size_f_table.add_row(-4, 'III')
    size_f_table.add_row(-3, 'IV')
    size_f_table.add_row((-2, 3), 'V')
    size_f_table.add_row(4, 'VI')
    size_f_table.add_row(5, 'D')
    size_f_table.add_row((6, 8), 'VI')

    size_g_table = Table()
    size_g_table.add_row((-6, -5), 'II')
    size_g_table.add_row(-4, 'III')
    size_g_table.add_row(-3, 'IV')
    size_g_table.add_row((-2, 3), 'V')
    size_g_table.add_row(4, 'VI')
    size_g_table.add_row(5, 'D')
    size_g_table.add_row((6, 8), 'VI')

    size_k_table = Table()
    size_k_table.add_row((-6, -5), 'II')
    size_k_table.add_row(-4, 'III')
    size_k_table.add_row(-3, 'IV')
    size_k_table.add_row((-2, 3), 'V')
    size_k_table.add_row(4, 'VI')
    size_k_table.add_row(5, 'D')
    size_k_table.add_row((6, 8), 'VI')

    size_m_table = Table()
    size_m_table.add_row((-6, -3), 'II')
    size_m_table.add_row(-2, 'III')
    size_m_table.add_row((-1, 3), 'V')
    size_m_table.add_row(4, 'VI')
    size_m_table.add_row(5, 'D')
    size_m_table.add_row((6, 8), 'VI')

    def __init__(self):
        self.spectral_type = ''
        self.decimal = 0
        self.size = ''
        self.companion = None
        self.primary_rolls = {}

    def __str__(self):
        return self.code()

    def code(self):
        '''Return spec type, decimal, size for this star only'''
        if self.spectral_type == 'BD':
            return 'BD'
        elif self.size == 'D':
            return 'D'
        else:
            return '{}{} {}'.format(
                self.spectral_type, self.decimal, self.size)

    def display(self):
        '''Combine spectral type, decimal, size'''
        resp = [str(self)]
        if self.companion is not None:
            resp.append(str(self.companion))
        return ' '.join(resp)

    def set_decimal(self):
        '''Set spectral decimal'''
        if self.spectral_type == 'F' and self.size == 'VI':
            self.decimal = D5.roll(1, -1)
        else:
            self.decimal = D10.roll(1, -1)

    def has_companion(self):
        '''Companion star?'''
        if FLUX.flux() >= 3:
            LOGGER.debug('Companion exists')
            self.companion = Secondary(self.primary_rolls)


class Primary(_Star):
    '''Primary class'''
    def __init__(self):
        super(Primary, self).__init__()
        self.primary_rolls = {'Spectral type': 0, 'Size': 0}
        self.secondaries = {'Close': None, 'Near': None, 'Far': None}
        self.set_spectral_type()
        self.set_decimal()
        self.set_size()
        LOGGER.debug('Primary: primary_rolls = %s', self.primary_rolls)
        self.has_companion()
        for zone in self.secondaries:
            self.has_secondary(zone)

    def display(self):
        '''Combine spectral type, decimal, size'''
        resp = [str(self)]
        if self.companion is not None:
            resp.append(str(self.companion))
        for zone in self.secondaries:
            if self.secondaries[zone] is not None:
                resp.append(str(self.secondaries[zone]))
        return ' '.join(resp)

    def set_spectral_type(self):
        '''Set spectral type'''
        roll = FLUX.flux()
        self.spectral_type = self.spectral_type_table.lookup(roll)
        if self.spectral_type == 'OB':
            # Decide randomly
            self.spectral_type = 'OB'[D2.roll(1, -1)]
        self.primary_rolls['Spectral type'] = roll

    def set_size(self):
        '''Set size'''
        roll = FLUX.flux()
        self.primary_rolls['Size'] = roll
        if self.spectral_type == 'O':
            self.size = self.size_o_table.lookup(roll)
        elif self.spectral_type == 'B':
            self.size = self.size_b_table.lookup(roll)
        elif self.spectral_type == 'A':
            self.size = self.size_a_table.lookup(roll)
        elif self.spectral_type == 'F':
            self.size = self.size_f_table.lookup(roll)
        elif self.spectral_type == 'G':
            self.size = self.size_g_table.lookup(roll)
        elif self.spectral_type == 'K':
            self.size = self.size_k_table.lookup(roll)
        elif self.spectral_type == 'M':
            self.size = self.size_m_table.lookup(roll)

    def has_secondary(self, zone):
        '''Secondary in zone?'''
        if FLUX.flux() >= 3:
            LOGGER.debug('Secondary in zone %s exists', zone)
            self.secondaries[zone] = Secondary(self.primary_rolls)


class Secondary(_Star):
    '''Non-primary star class'''
    def __init__(self, primary_rolls):
        super(Secondary, self).__init__()
        self.primary_rolls = primary_rolls
        LOGGER.debug('Secondary: primary_rolls = %s', self.primary_rolls)
        self.set_spectral_type()
        self.set_decimal()
        self.set_size()
        self.has_companion()

    def set_spectral_type(self):
        '''Set spectral type'''
        roll = D6.roll(1, -1)
        roll += self.primary_rolls['Spectral type']
        roll = min(roll, 8)
        roll = max(roll, -6)
        self.spectral_type = self.spectral_type_table.lookup(roll)
        if self.spectral_type == 'OB':
            # Decide randomly
            self.spectral_type = 'OB'[D2.roll(1, -1)]

    def set_size(self):
        '''Set size'''
        roll = D6.roll(1, -1)
        roll += self.primary_rolls['Size']
        roll = min(roll, 8)
        roll = max(roll, -6)
        if self.spectral_type == 'O':
            self.size = self.size_o_table.lookup(roll)
        elif self.spectral_type == 'B':
            self.size = self.size_b_table.lookup(roll)
        elif self.spectral_type == 'A':
            self.size = self.size_a_table.lookup(roll)
        elif self.spectral_type == 'F':
            self.size = self.size_f_table.lookup(roll)
        elif self.spectral_type == 'G':
            self.size = self.size_g_table.lookup(roll)
        elif self.spectral_type == 'K':
            self.size = self.size_k_table.lookup(roll)
        elif self.spectral_type == 'M':
            self.size = self.size_m_table.lookup(roll)
