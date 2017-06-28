# T5 worldgen HOWTO

T5_worldgen is a set of Python classes that allows you generate Traveller T5 systems, subsectors and sectors. The set includes some scripts to generate these; this note provides some details on how to write your own scripts using the classes.

## Subsector()

Subsector() generates an 8x10 subsector of systems. You can provide a name, location within sector and stellar density when you create it. Example:

```
from T5_worldgen.mapping_region import Subsector
subs = Subsector("Arthur's Subsector", "A", "Sparse")
subs.display()
0105	Name-0105A	E648610-6	Ni Ag	{-2}	(854+4)	[3473]	BC			900	5	Na	G8 V G8 V
0107	Name-0107A	X5449BE-0	Hi In	{+0}	(887+2)	[7991]	BE			801	8	Na	K0 V M2 VI BD M2 V
0109	Name-0109A	C7C4540-9	Fl Ni	{-1}	(644-1)	[9416]	B			200	3	Na	K4 V BD BD
0110	Name-0110A	X400124-1	Va Lo	{-3}	(701-2)	[2163]	B			500	6	Na	F9 III K4 V G9 III
0210	Name-0210A	A578378-C	Lo Co Tz	{+1}	(721+0)	[5459]	B			703	8	Na	K4 V
0303	Name-0303A	B0008BB-C	As Va Ph Na Pi Ho	{+2}	(87C+2)	[8A5C]	BDe	N		200	3	Na	F6 V
0305	Name-0305A	X685599-1	Ga Ni Ag Pr	{-2}	(442-2)	[6321]	BcC			601	6	Na	G3 V
0309	Name-0309A	B000247-E	As Va Lo Co	{+1}	(711+2)	[234G]	B			702	6	Na	G0 V
0402	Name-0402A	C462863-4	Ph Ri O:0101	{+0}	(279+0)	[A848]	BCe	S		801	4	Na	F0 V
0408	Name-0408A	E553544-6	Ni Po Ho Tz	{-3}	(441+2)	[5243]	B			000	3	Na	M5 VI M7 VI
0509	Name-0509A	C410512-7	Ni	{-2}	(741+5)	[13A8]	B			400	6	Na	F4 V G7 V
0703	Name-0703A	E6209EH-7	De He Hi Na In Po	{+0}	(787+1)	[9955]	BE			901	8	Na	F9 V
0709	Name-0709A	B0006A9-D	As Va Ni Na	{+1}	(655-4)	[576B]	B			603	5	Na	G0 V G6 VI
0803	Name-0803A	B511587-7	Ic Ni	{-1}	(841+2)	[8445]	B			802	9	Na	G6 IV
0806	Name-0806A	B568986-B	Hi Pr Ho	{+3}	(A8B+3)	[AC4C]	BcE	S		201	4	Na	G2 V K5 VI M9 V
```

The Subsector() object contains a dictionary of hexes containing a system; each dictionary entry is a System() object in its own right. 
This means you can manipulate each system. Example:

```
str(subs.hexes['0305'])
'0305 Name-0305A   X685599-1 Ga Ni Ag Pr  {-2} (442-2) [6321] BcC  601  6 Na G3 V'
subs.hexes['0305'].name = 'Primitive World'
str(subs.hexes['0305'])
'0305 Primitive World   X685599-1 Ga Ni Ag Pr  {-2} (442-2) [6321] BcC  601  6 Na G3 V'
```

Valid densities are:

- Extra-galactic (1%)
- Rift (3%)
- Sparse (17%)
- Scattered (33%)
- Standard (50%)
- Dense (66%)
- Cluster (83%)
- Core (91%)


