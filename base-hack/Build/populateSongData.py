'Patches vanilla song data to ROM.'
from typing import BinaryIO
song_data=[0,257,256,392,393,256,256,1088,393,2242,2242,2242,2242,2242,256,2612,410,410,2244,265,2749,257,1591,1591,1607,256,256,392,256,256,394,256,1599,1599,468,1599,408,402,2324,256,2253,2142,2205,2132,2132,1092,2245,1589,392,256,256,394,394,256,2202,256,257,152,400,2356,264,392,395,256,256,1093,2341,1095,257,1221,392,410,402,400,256,2304,1597,256,256,256,256,392,392,257,403,258,280,280,256,392,256,257,256,256,256,256,2322,256,256,256,256,458,264,256,426,257,256,410,400,257,265,257,257,256,2194,2194,256,392,256,256,256,256,256,257,408,272,256,1212,1086,256,256,256,256,257,256,256,256,256,256,256,256,257,256,1093,1607,1607,1605,1605,256,256,256,1605,256,256,256,256,256,256,256,256,257,256,256,256,256,256,256,256,256,392,472,394,1605,24,264]
def writeVanillaSongData(fh):
	'Write data to ROM.';fh.seek(33550336)
	for A in song_data:fh.write(A.to_bytes(2,'big'))