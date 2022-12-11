"""read and dump segy headers"""

import os
from pathlib import Path

import numpy
import pandas

from segytools.segy_file_header import SegyFileHeaderRev2
from segytools.segy_trace_header import SegyTraceHeaderRev2
from segytools.segpy.toolkit import unpack_ibm_floats, unpack_values

# modified from segpy toolkit.py
def read_binary_values(buf, num_items, ctype, endian):
    values = (unpack_ibm_floats(buf, num_items)
              if ctype == 'ibm'
              else unpack_values(buf, ctype, endian))
    assert len(values) == num_items
    return values


TEXTHEADERLENGTH = 3200
FILEHEADERLENGTH = 400
TRCHEADERLENGTH = 240
ENDIANESS = 'big'
textencode = 'ebcidic'

segyfile = "example.sgy"
pathsegyfile = Path(str(segyfile))
assert (pathsegyfile.is_file())

segyfilesize = os.path.getsize(segyfile)

bsgyout = bytes()
hdr4df = {}

# 'rb' is "read bytes"
with open(segyfile, 'rb') as fobj:
    # read the first 3200 bytes.
    # This will always be 3200 byte textual file header
    b_text_header = fobj.read(TEXTHEADERLENGTH)
    # print(type(b_text_header))

    textheader = str()
    if textencode == 'ebcidic':
        textheader = b_text_header.decode(encoding='cp500')
    elif textencode == 'ascii':
        textheader = b_text_header.decode(encoding='utf-8')

    # print(textheader)
    print('\nloading file header ...')
    fileheader = SegyFileHeaderRev2()
    b_file_header = fobj.read(FILEHEADERLENGTH)
    fileheader.set_file_header_values(bsgy=b_file_header, endianess=ENDIANESS)
    # print(fileheader)

    print('\ntrace data')
    #---TRCDATALENGTH = (fileheader.getKeyProperty('numsmp', 'value') * fileheader.getBytesPerSecond())
    TRCDATALENGTH = fileheader.number_of_samples() * fileheader.bytes_per_sample()
    print(f'trace data length in bytes: {TRCDATALENGTH}')

    TRCDATASTART = TEXTHEADERLENGTH + FILEHEADERLENGTH

    # assuming the trace length is the same for all traces. That is, number of samples and sample interval is consistent
    ntraces = (segyfilesize - (TEXTHEADERLENGTH + FILEHEADERLENGTH)) / (TRCDATALENGTH + TRCHEADERLENGTH)
    ntraces = int(ntraces)
    print('number of traces: ', ntraces)

    # loop through each trace (could be optimized later)
    for trccntr in range(ntraces):
        fobj.seek(TRCDATASTART + (trccntr * (TRCDATALENGTH + TRCHEADERLENGTH)))
        bsgy = fobj.read(TRCHEADERLENGTH)
        hdr = SegyTraceHeaderRev2()
        hdr.set_trace_header_values(bsgy=bsgy, endianess=ENDIANESS)
        # if trccntr == 0:
        #     print(hdr)
        hdr4df[str(trccntr)] = hdr.value_dict()

        # bsgy = fobj.read(TRCDATALENGTH)
        # trace_values = read_binary_values(bsgy, fileheader.numsmp.getValue(), fileheader.getCType(), endianess)
        # tracenp = numpy.asarray(trace_values, dtype=numpy.float32, order='C')
        # bsgyout += bsgy

    fobj.close()

# print('\ndataframe')
# print(hdr4df)

df = pandas.DataFrame(data=hdr4df)
df = df.transpose()
print(df.head())
print(df.tail())