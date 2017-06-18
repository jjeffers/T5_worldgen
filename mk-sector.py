'''mk-sector.py'''

wrkdir='./tmp'

_subsector_offsets={}
for i, row in enumerate(['ABCD', 'EFGH', 'IJKL', 'MNOP']):
    for ss in row:
        offset_x = row.index(ss) * 8
        offset_y = i * 10
_subsector_offsets[ss] = (offset_x, offset_y)


with open('{}/sector.t5tab'.format(wrkdir, 'w') as outfile:
    outfile.write('\t'.join([
        'Hex', 'Name', 'UWP', 'Remarks', '{Ix}', '(Ex)', '[Cx]',
        'Nobility', 'Bases', 'Zone', 'PBG', 'W', 'Allegiance',
        'Stars'])
     outfile.write('\n')
    for ss in 'ABCDEFGHIJKLMNOP':
        with open('{}/subsector-{}.t5tab'.format(wrkdir, ss), 'r') as ssfile:
            ssdata = ssfile.readlines()