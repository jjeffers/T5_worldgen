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

The Sector() object contains a dictionary of subsectors A-P, corresponding to the 4x4 grid. Each item in the dictionary is a Subsector() object, so you can display a subsector as shown below: 

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
You can also view a system directly:
```>>> for hex_id in sector.hexes.keys():
...     print str(sector.hexes[hex_id])
... 
1305 Name-1305B           D160421-8 De Ni              {-3} (A30+1) [418B] B       S    703  9 Na F6 V          
2616 Name-2616H           EBC6998-4 Fl Hi In Tz        {+0} (987-1) [C956] BE           901  5 Na K2 VI         
2908 Name-2908D           C420126-9 De He Lo Po        {-1} (901-5) [413B] B            503 10 Na G2 IV         
2414 Name-2414G           C37669B-7 Ni Ag Co Da        {-1} (852-1) [6589] BC         A 101  8 Na F1 V          
0734 Name-0734M           C6B9542-8 Fl Ni Ho           {-2} (743+4) [5326] B            801  3 Na K6 II         
0340 Name-0340M           DBA657B-5 Fl Ni Tz           {-3} (840+5) [1288] B       S    402  5 Na M4 V          
2204 Name-2204C           A234644-E Ni                 {+1} (A55+2) [378C] B            802  7 Na K8 V          
0320 Name-0320E           D54836A-3 Lo O:0421 Co Tz    {-3} (921+1) [2158] B       S    603  7 Na K2 V          
1715 Name-1715G           A300400-E Va Ni              {+1} (D33+0) [152G] B       N    404 11 Na F1 V          
3235 Name-3235P           E47367A-4 Ni                 {-3} (253+0) [A354] B            902  9 Na K6 V          
0501 Name-0501A           B20058A-D Va Ni              {+1} (744-2) [566J] B            401  8 Na K4 V          
1940 Name-1940O           E477647-2 Ni Ag              {-2} (551+5) [6442] BC           603 10 Na G6 V          
2733 Name-2733P           B558EAC-B Hi Tz              {+3} (EDC-2) [EH6D] BE           703  6 Na K0 VI         
0421 Name-0421I           A344534-D Ni Ag              {+2} (B46-4) [774G] BC      N    202  4 Na G9 IV         
0202 Name-0202A           E433500-A Ni Po Tz           {-1} (F42+2) [346B] B            903  7 Na M2 V          
2403 Name-2403C           BAE5440-8 Ni Ho Tz           {-1} (831+2) [731A] B            301  3 Na M1 V          
1014 Name-1014F           E330459-6 De Ni Po           {-3} (930+5) [9165] B            100  4 Na K2 V          
1115 Name-1115F           B333878-8 Ph Na Po Co        {+0} (575+3) [8848] Be           400  3 Na G6 V          
2016 Name-2016G           B0008AB-C As Va Ph Na Pi Da  {+2} (777-4) [9A4A] BDe     N  A 202  9 Na F7 V          
2408 Name-2408C           C331448-6 Ni Px Po           {-2} (732-4) [5277] B            203  7 Na F4 V          
0717 Name-0717E           B6658A8-5 Ga Ph Pa Ri        {+1} (377+1) [A923] BcCe         401  5 Na A6 V          
3010 Name-3010D           B976526-8 Ni Ag              {+0} (946-3) [554B] BC      N    402  9 Na K5 V          
2628 Name-2628L           D5685AC-3 Ni Ag Pr           {-2} (944-4) [7353] BcC     S    501  4 Na G4 V          
2134 Name-2134O           E610566-4 Ni O:2733 Co       {-3} (642+4) [2243] B            901  7 Na K6 IV         
0902 Name-0902B           E65358A-4 Ni Po              {-3} (A40-3) [4281] B            502  5 Na A3 V          
1609 Name-1609B           B574320-A Lo                 {+1} (521+1) [1419] B            102  8 Na G7 V          
0538 Name-0538M           E356536-3 Ni Ag              {-2} (940+0) [1336] BC           100  5 Na G9 III        
2317 Name-2317G           E546422-3 Ni Pa              {-3} (432-3) [2185] Bc           500  3 Na K6 V          
0514 Name-0514E           E557311-7 Lo                 {-3} (621+5) [115B] B            901  6 Na A8 IV         
1105 Name-1105B           B633205-C Lo Po              {+1} (A11-3) [135B] B       N    602  9 Na K7 V          
1532 Name-1532N           B354765-7 Ag O:2134 Co Tz    {+1} (663+1) [8847] BC           200  6 Na K6 V          
1007 Name-1007B           C110788-8 Na Pi Tz           {-1} (A69+1) [7634] BD      S    300  3 Na M3 V          
0806 Name-0806A           E552310-7 Lo Po              {-3} (621+0) [2165] B            901  5 Na F8 V          
1108 Name-1108B           C130347-8 De Lo Po           {-2} (A21+0) [6159] B            701  7 Na M7 II         
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

