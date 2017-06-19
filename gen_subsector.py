#! /usr/bin/env python
from __future__ import print_function

from T5_worldgen.mapping_region import Subsector

subsector = Subsector('Test Subsector', 'Sparse')
print(subsector.t5_tab())
