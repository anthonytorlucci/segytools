"""Export first ffid only"""

# standard
import os
from pathlib import Path
import textwrap

# third party
# import numpy

# local
from poland2d_context import segytools

from segytools.segy_file_header import SegyFileHeaderRev2
from segytools.segy_trace_header import SegyTraceHeaderRev2
from segytools.toolkit import read_binary_values

TEXTHEADERLENGTH = 3200
FILEHEADERLENGTH = 400
TRCHEADERLENGTH = 240
ENDIANESS = 'big'
TEXTENCODE = 'ebcdic'

segyfile = "data/Line_001.sgy"
pathsegyfile = Path(str(segyfile))
assert (pathsegyfile.is_file())

segyfilesize = os.path.getsize(segyfile)

#-- bsgyout = bytes()
bsgyarr = bytearray(segyfilesize)  # same size as input; only use for small segy files.

# 'rb' is "read bytes"
with open(segyfile, 'rb') as fobj:
    # read the first 3200 bytes.
    # This will always be 3200 byte textual file header
    b_text_header = fobj.read(TEXTHEADERLENGTH)
    
    # assign the text header byte data to the output
    #--bsgyout += b_text_header
    bsgyarr[0:TEXTHEADERLENGTH] = b_text_header
    last_byte = TEXTHEADERLENGTH

    # create the file header object
    fileheader = SegyFileHeaderRev2()
    b_file_header = fobj.read(FILEHEADERLENGTH)
    fileheader.set_file_header_values(bsgy=b_file_header, endianess=ENDIANESS)

    # assign the file header byte data to the output
    #--bsgyout += b_file_header
    bsgyarr[last_byte:last_byte+FILEHEADERLENGTH] = b_file_header
    last_byte = last_byte+FILEHEADERLENGTH

    # create a trace header object and read the first trace header
    traceheader = SegyTraceHeaderRev2()
    bsgy = fobj.read(TRCHEADERLENGTH)
    traceheader.set_trace_header_values(bsgy=bsgy, endianess=ENDIANESS)

    # get the first ffid value
    first_ffid = traceheader.ffid.value
    print(f'first ffid: {first_ffid}')

    # assign the trace header byte data to the output; if modifying the headers, replace with traceheader.to_bytes()
    #--bsgyout += bsgy
    bsgyarr[last_byte:last_byte+TRCHEADERLENGTH] = bsgy
    last_byte = last_byte+TRCHEADERLENGTH
    
    # get the length of the next trace based on the number of samples in the trace header and length of each byte from the file header
    trace_data_length = traceheader.numsmp.value * fileheader.bytes_per_sample()
    bsgy = fobj.read(trace_data_length)

    # assign the trace data to the output
    #--bsgyout += bsgy
    bsgyarr[last_byte:last_byte+trace_data_length] = bsgy
    last_byte = last_byte + trace_data_length

    # loop through the file while the header matches the first ffid, i.e. the ffid of the first trace.
    while fobj.tell() < segyfilesize:
        bsgy = fobj.read(TRCHEADERLENGTH)
        traceheader.set_trace_header_values(bsgy=bsgy, endianess=ENDIANESS)
        if traceheader.ffid.value != first_ffid:
            break
        else:
            bsgyarr[last_byte:last_byte+TRCHEADERLENGTH] = bsgy
            last_byte = last_byte + TRCHEADERLENGTH
            # the number of samples per trace may change if there are auxialliary channels in the file, so we must re-calculate the trace data length
            trace_data_length = traceheader.numsmp.value * fileheader.bytes_per_sample()
            bsgy = fobj.read(trace_data_length)
            bsgyarr[last_byte:last_byte+trace_data_length] = bsgy
            last_byte = last_byte+trace_data_length
        
    fobj.close()

# write output segy; use only with small segy files
segy_file_out = os.path.join(os.getcwd(), "data", f"poland2d_example_ffid_{first_ffid}.sgy")
with open(segy_file_out, "wb") as fobj2:
    bsgyout = bytes(bsgyarr[:last_byte])
    fobj2.write(bsgyout)
    print("writing complete")
    fobj2.close()