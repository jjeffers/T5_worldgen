'''
Trade codes module
'''


class TradeCodes(object):
    '''
    Trade codes for planet (type Planet)
    '''
    def __init__(self, planet):
        self.planet = planet

    def generate(self):
        '''
        Generate trade codes
        '''
        trade_codes = []
        trade_codes.extend(self._planetary())
        trade_codes.extend(self._population())
        trade_codes.extend(self._economic())
        return trade_codes

    def _planetary(self):
        '''Set planetary trade codes'''
        trade_codes = []
        # As - asteroid belt
        if (
                str(self.planet.size) == '0' and
                str(self.planet.atmosphere) == '0' and
                str(self.planet.hydrographics) == '0'):
            trade_codes.append('As')
        # De - desert
        if (str(self.planet.atmosphere) in '234566789' and
                str(self.planet.hydrographics) == '0'):
            trade_codes.append('De')
        # Fl - fluid oceans
        if (
                str(self.planet.atmosphere) in 'ABC' and
                str(self.planet.hydrographics) in '123456789A'):
            trade_codes.append('Fl')
        # Ga - garden world
        if (
                str(self.planet.size) in '678' and
                str(self.planet.atmosphere) in '568' and
                str(self.planet.hydrographics) in '567'):
            trade_codes.append('Ga')
        # He - hellworld
        if (
                str(self.planet.size) in '3456789ABC' and
                str(self.planet.atmosphere) in '2479ABC' and
                str(self.planet.hydrographics) in '012'):
            trade_codes.append('He')
        # Ic - ice-capped
        if (
                str(self.planet.atmosphere) in '01' and
                str(self.planet.hydrographics) in '123456789A'):
            trade_codes.append('Ic')
        # Oc - ocean world
        if (
                str(self.planet.size) in 'ABCDEF' and
                str(self.planet.atmosphere) in '3456789ABC' and
                str(self.planet.hydrographics == 'A')):
            trade_codes.append('Oc')
        # Va - vacuum
        if str(self.planet.atmosphere) == '0':
            trade_codes.append('Va')
        # Wa - water world
        if (
                str(self.planet.size) in '3456789A' and
                str(self.planet.atmosphere) in '3456789ABC' and
                str(self.planet.hydrographics) == 'A'):
            trade_codes.append('Wa')
        return trade_codes

    def _population(self):
        '''Set population-related trade codes'''
        trade_codes = []
        # Di - Dieback
        # Also
        # Ba - Barren
        if (
                str(self.planet.population) == '0' and
                str(self.planet.government) == '0' and
                str(self.planet.law_level) == '0'):
            trade_codes.append('Di')
            trade_codes.append('Ba')
        # Lo - low population
        if str(self.planet.population) in '123':
            trade_codes.append('Lo')
        # Ni - non-industrial
        if str(self.planet.population) in '456':
            trade_codes.append('Ni')
        # Ph - pre-high population
        if str(self.planet.population) == '8':
            trade_codes.append('Ph')
        # Hi - high population
        if str(self.planet.population) >= '9':
            trade_codes.append('Hi')
        return trade_codes

    def _economic(self):
        '''Set economic trade codes'''
        trade_codes = []
        # Pa - pre-agricultural
        if (
                str(self.planet.atmosphere) in '456789' and
                str(self.planet.hydrographics) in '45678' and
                str(self.planet.population) in '48'):
            trade_codes.append('Pa')
        # Ag - agricultural
        if (
                str(self.planet.atmosphere) in '456789' and
                str(self.planet.hydrographics) in '45678' and
                str(self.planet.population) in '567'):
            trade_codes.append('Ag')
        # Na - non-agricultural
        if (
                str(self.planet.atmosphere) in '0123' and
                str(self.planet.hydrographics) in '0123' and
                str(self.planet.population) >= '6'):
            trade_codes.append('Na')
        # Px - prison or exile camp
        if (
                str(self.planet.atmosphere) in '23AB' and
                str(self.planet.hydrographics) in '12345' and
                str(self.planet.population) in '3456' and
                str(self.planet.law_level) in '6789'):
            trade_codes.append('Px')
        # Pi - pre-industrial
        if (
                str(self.planet.atmosphere) in '012479' and
                str(self.planet.population) in '78'):
            trade_codes.append('Pi')
        # In - industrial
        if (
                str(self.planet.atmosphere) in '012479ABC' and
                str(self.planet.population) >= '9'):
            trade_codes.append('In')
        # Po - poor
        if (
                str(self.planet.atmosphere) in '2345' and
                str(self.planet.hydrographics) in '0123'):
            trade_codes.append('Po')
        # Pr - pre-rich
        if (
                str(self.planet.atmosphere) in '68' and
                str(self.planet.population) in '59'):
            trade_codes.append('Pr')
        # Ri - rich
        if (
                str(self.planet.atmosphere) in '68' and
                str(self.planet.population) in '678'):
            trade_codes.append('Ri')
        return trade_codes
