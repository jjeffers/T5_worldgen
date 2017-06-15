#! /usr/bin/env python

from T5_worldgen.mapping_region import Sector
import os

sector_name = 'Test_Sector'

sector = Sector(sector_name, 'Scattered')
# sector.display()
for _ in sector.t5_tab():
    print _

# Save JSON data in ./tmp/sector_name/subsector_name.json
try:
    os.makedirs('./tmp/{}/'.format(sector_name))
except OSError:
    if not os.path.isdir('./tmp/{}/'.format(sector_name)):
        raise
for ss_id in sector.subsectors.keys():
    with open(
            './tmp/{}/Subsector-{}.json'.format(sector_name, ss_id),
            'w') as jout:
        for hex_id in sector.subsectors[ss_id].hexes.keys():
            jout.write(
                sector.subsectors[ss_id].hexes[hex_id].as_json() + "\n"
            )
