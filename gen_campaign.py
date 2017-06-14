#! /usr/bin/env python

from T5_worldgen.mapping_region import Subsector

subsector_densities = {
    'A': 'Scattered', 'B': 'Standard', 'C': 'Standard', 'D': 'Scattered',
    'E': 'Scattered', 'F': 'Standard', 'F1': 'Dense',
    'G': 'Dense', 'G1': 'Scattered', 'H': 'Scattered',
    'I': 'Sparse', 'J': 'Standard', 'K': 'Scattered', 'L': 'Scattered',
    'M': 'Scattered', 'N': 'Scattered', 'O': 'Standard',
    'P': 'Standard', 'P1': 'Rift'}

for sd in subsector_densities.keys():
    ofile = 'tmp/subsector-{}.t5tab'.format(sd)
    with open(ofile, 'w') as fil:
        subsector = Subsector(
            'subsector-{}'.format(sd),
            sd,
            subsector_densities[sd])
        fil.write('\n'.join(subsector.t5_tab()))
        o2file = 'tmp/{}.json'.format(subsector.name)
        with open(o2file, 'w') as jfil:
            for hex_id in subsector.hexes.keys():
                jfil.write(subsector.hexes[hex_id].as_json())



# subsector = Subsector('Test Subsector', 'Sparse')
# subsector.t5_tab()
