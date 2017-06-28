# T5 worldgen HOWTO

T5_worldgen is a set of Python classes that allows you generate Traveller T5 systems, subsectors and sectors. The set includes some scripts to generate these; this note provides some details on how to write your own scripts using the classes.

## System()

System() generates a single star system. You can provide a name and location when you create it.
Example:

```
from T5_worldgen.system import System
system = System("Arthur's World", '0408')
str(system)
"0406 Arthur's World    A246355-D Lo    {+1} (521+0) [149D] B            001  6 Na F3 V"
```

This generates a system, including:

- stellar details
- trade codes
- nobility
- bases
- PBG (population digit, planetoid belts, gas giants)
- importance extension Ix
- economic extension Ex
- cultural extension Cx
- habitable zone

You can dump a JSON representation of the system

```
system.as_json()
'{"mainworld": "{\\"trade_codes\\": [\\"Lo\\"], \\"travel_code\\": \\"\\",
\\"is_mainworld\\": true, \\"uwp\\": \\"A246355-D\\", \\"orbit\\": 5,
\\"bases\\": \\"\\"}", "worlds": 6, "allegiance": "Na", 
"stellar": "{\\"decimal\\": 3, \\"companion\\": null, \\"habitable_zone\\": 5, 
\\"spectral_type\\": \\"F\\", \\"secondaries\\": {}, 
\\"size\\": \\"V\\"}", "Ix": "{+1}", "name": 
"Arthur\'s World", "zone": "", "Cx": "[149D]", "hex": "0406", 
"pbg": "001", "bases": "", "Ex": "(521+0)", "nobility": "B"}'
```


