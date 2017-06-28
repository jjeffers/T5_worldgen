# T5 worldgen HOWTO

T5_worldgen is a set of Python classes that allows you generate Traveller T5 systems, subsectors and sectors. The set includes some scripts to generate these; this note provides some details on how to write your own scripts using the classes.

## Sector()

Sector() generates a 32x40 grid of systems (or a 4x4 grid of subsectors). You can provide a name and stellar density when you create it. Example:

```
from T5_worldgen.mapping_region import Sector
sector = Sector("Arthur's Sector","Rift")
sector.display()
Hex	Name	UWP	Remarks	{Ix}	(Ex)	[Cx]	Nobility	Bases	Zone	PBG	W	Allegiance	Stars
0308	Name-0308A	B420266-8	De He Lo Po O:0101 Tz	{-1}	(611-1)	[2197]	B	S		801	5	Na	M1 V
0605	Name-0605A	A766B8A-F	Ga Hi	{+3}	(AAA+2)	[DE1E]	BE	S		901	5	Na	G2 III
0218	Name-0208E	E324AAB-9	Hi In Ho	{+1}	(497+1)	[BB29]	BE			402	7	Na	F9 V K2 VI
0512	Name-0502E	E666576-4	Ga Ni Ag Pr	{-2}	(640+1)	[6353]	BcC			900	6	Na	K8 V K4 V
0520	Name-0510E	X24436B-1	Lo O:0101 Tz	{-3}	(921+0)	[5121]	B			002	9	Na	D M9 VI
0815	Name-0805E	D8B758A-5	Fl Ni	{-3}	(843-3)	[6213]	B	S		201	3	Na	F3 V D
0816	Name-0806E	E67676A-1	Ag Pi O:0101 Ho Tr	{-1}	(B69+0)	[B643]	BCD			001	4	Na	F6 V K2 V
0224	Name-0204I	D57949D-6	Ni	{-3}	(631+0)	[3125]	B	S		700	2	Na	G2 V M3 V M2 V
0622	Name-0602I	E567795-5	Ag Ri	{+0}	(264+3)	[675A]	BC			600	4	Na	K9 V
0235	Name-0205M	C984986-5	Hi Pr Ho Tr	{+0}	(485-3)	[B925]	BcE	S		502	7	Na	G4 V M7 VI
0836	Name-0806M	D665877-6	Ga Ph Pa Ri Co Tu	{-1}	(871-4)	[7739]	BcCe	S		602	4	Na	G5 V G1 V
0902	Name-0102B	C200745-9	Va Na Pi Ho	{+0}	(464+3)	[5758]	BD			400	5	Na	G1 V G2 V D
0910	Name-0110B	C964420-5	Ni Pa Co Tu	{-2}	(733+0)	[6265]	Bc			600	5	Na	G3 V
1509	Name-0709B	C773844-6	Ph Pi	{-1}	(575+4)	[8756]	BDe	S		000	2	Na	K3 V
1605	Name-0805B	A7A1100-B	Fl He Lo	{+1}	(501-2)	[328C]	B	N		001	4	Na	F4 V G2 V F9 V
0912	Name-0102F	C220034-7	De Po	{-2}	(508+0)	[0000]	B			803	9	Na	K0 V K8 VI
1613	Name-0803F	C47A311-8	Wa Lo	{-2}	(C21+3)	[2183]	B			301	4	Na	G8 V M2 V
1027	Name-0207J	E742311-6	He Lo Po Co	{-3}	(521-3)	[1164]	B			800	4	Na	M7 II M1 V BD
1127	Name-0307J	X668103-1	Lo Co	{-3}	(201+0)	[1152]	B			201	6	Na	M6 II
1328	Name-0508J	X447110-3	Lo Ho Tz	{-3}	(701+5)	[3132]	B			200	3	Na	M9 V M4 VI BD
1529	Name-0709J	E7A879A-7	Fl	{-2}	(865+4)	[45A8]	B			102	8	Na	G4 V K4 V
1040	Name-0210N	X8D6221-4	Lo Tz	{-3}	(A11+2)	[5174]	B			901	7	Na	M1 III M1 V BD
1334	Name-0504N	E557568-5	Ni Ag O:0101 Ho Tz	{-2}	(542+1)	[3375]	BC			701	4	Na	M8 V
1538	Name-0708N	A565340-C	Lo Tz	{+1}	(C21-1)	[644C]	B	N		200	2	Na	M4 V M7 V
2101	Name-0501C	E863367-3	Lo O:0101	{-3}	(821+0)	[7193]	B			500	6	Na	G0 V
2210	Name-0610C	C245799-7	Ag Pi	{+0}	(565+0)	[6718]	BCD	S		102	9	Na	G7 V D
2304	Name-0704C	E785555-5	Ga Ni Ag Pr	{-2}	(442-5)	[7333]	BcC			901	6	Na	G6 V
2218	Name-0608G	X46937A-0	Lo	{-3}	(621-2)	[4193]	B			003	10	Na	K5 V M9 V
2316	Name-0706G	B674221-A	Lo Co Tu	{+2}	(811+5)	[746B]	B	NS		502	6	Na	G5 IV K4 V
2412	Name-0802G	C68757C-8	Ga Ni Ag Pr Tz	{-1}	(745-3)	[4489]	BcC			704	8	Na	M5 V M0 V
2129	Name-0509K	B552421-9	Ni Po Tz	{+0}	(934+4)	[2468]	B			302	5	Na	M6 V BD
2428	Name-0808K	E772738-6	He Pi	{-2}	(A65+4)	[3516]	BD			304	11	Na	F6 V
1832	Name-0202O	A365200-F	Lo Co	{+1}	(711+3)	[636F]	B			201	4	Na	F0 V
2501	Name-0101D	E410122-4	Lo Co	{-3}	(401-2)	[1151]	B			201	4	Na	G2 V
2518	Name-0108H	E547133-2	Lo	{-3}	(601+1)	[1181]	B			601	3	Na	F8 V G5 V
```

The Sector() object contains a dictionary of subsectors A-P, corresponding to the 4x4 grid. Each item in the dictionary is a Subsector() object. You can 

```
sector.subsectors['A'].display()
0308	Name-0308A	B420266-8	De He Lo Po O:0101 Tz	{-1}	(611-1)	[2197]	B	S		801	5	Na	M1 V
0605	Name-0605A	A766B8A-F	Ga Hi	{+3}	(AAA+2)	[DE1E]	BE	S		901	5	Na	G2 III
sector.subsectors['A'].hexes['0605'].name = 'High-tech Planet'
sector.subsectors['A'].display()
0308	Name-0308A	B420266-8	De He Lo Po O:0101 Tz	{-1}	(611-1)	[2197]	B	S		801	5	Na	M1 V
0605	High-tech Planet	A766B8A-F	Ga Hi	{+3}	(AAA+2)	[DE1E]	BE	S		901	5	Na	G2 III
sector.display()
Hex	Name	UWP	Remarks	{Ix}	(Ex)	[Cx]	Nobility	Bases	Zone	PBG	W	Allegiance	Stars
0308	Name-0308A	B420266-8	De He Lo Po O:0101 Tz	{-1}	(611-1)	[2197]	B	S		801	5	Na	M1 V
0605	High-tech Planet	A766B8A-F	Ga Hi	{+3}	(AAA+2)	[DE1E]	BE	S		901	5	Na	G2 III
0218	Name-0208E	E324AAB-9	Hi In Ho	{+1}	(497+1)	[BB29]	BE			402	7	Na	F9 V K2 VI
...
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

