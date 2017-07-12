#! /usr/bin/env python
from __future__ import print_function

from T5_worldgen.mapping_region import Subsector

subsector = Subsector('Test Subsector', 'Sparse')
subsector.trade_code_owning_system()
for system in subsector.t5_tab():
    print(system)
