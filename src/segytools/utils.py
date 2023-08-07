"""
Utility functions for segy data.
"""

# Copyright 2022 Anthony Torlucci

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


# standard
import textwrap

# third party
import numpy
from ibm2ieee import ibm2float32, ibm2float64

# local
from .datatypes import DataSampleFormat

def format_textheader_string(textheader):
    """Format the textheader to have each line be 80 characters long and
    return a single string.

    Parameters
    ----------
    textheader : str
        The textual header string after decoding.

    Returns
    -------
    str
        Textual header with 80 characters per line.
    """
    return "\n".join(textwrap.wrap(textheader, 80))

def read_trace_data(buf:bytes, fmt:DataSampleFormat, byteorder='<') -> numpy.array:
    """convert an input byte array to a numpy array.

    Parameters
    ----------
    buf : bytearray
        input byte array object
    fmt : DataSampleFormat
        Describes the format of the samples in the buffer
    byteorder : str
        Either '<' for little endian or '>' for big endian

    Returns
    -------
    numpy.ndarray
        1D array of trace data of length number of samples.

    Raises
    ------
    ValueError
    """
    # TODO: assert byteorder '<' or '>'
    if fmt.ctype == 'char':
        dt = numpy.dtype(numpy.int8)
        dt = dt.newbyteorder(byteorder)
        trc = numpy.frombuffer(buf, dtype=dt)
    elif fmt.ctype == 'unsigned char':
        dt = numpy.dtype(numpy.uint8)
        dt = dt.newbyteorder(byteorder)
        trc = numpy.frombuffer(buf, dtype=dt)
    elif fmt.ctype == 'short':
        dt = numpy.dtype(numpy.int16)
        dt = dt.newbyteorder(byteorder)
        trc = numpy.frombuffer(buf, dtype=dt)
    elif fmt.ctype == 'unsigned short':
        dt = numpy.dtype(numpy.uint16)
        dt = dt.newbyteorder(byteorder)
        trc = numpy.frombuffer(buf, dtype=dt)
    elif fmt.ctype == 'int':
        dt = numpy.dtype(numpy.int32)
        dt = dt.newbyteorder(byteorder)
        trc = numpy.frombuffer(buf, dtype=dt)
    elif fmt.ctype == 'unsigned int':
        dt = numpy.dtype(numpy.uint32)
        dt = dt.newbyteorder(byteorder)
        trc = numpy.frombuffer(buf, dtype=dt)
    elif fmt.ctype == 'float':
        dt = numpy.dtype(numpy.float32)
        dt = dt.newbyteorder(byteorder)
        trc = numpy.frombuffer(buf, dtype=dt)
    elif fmt.ctype == 'double':
        dt = numpy.dtype(numpy.float64)
        dt = dt.newbyteorder(byteorder)
        trc = numpy.frombuffer(buf, dtype=dt)
    elif fmt.ctype == 'ibm':
        trc = ibm2float64(numpy.frombuffer(buffer=buf, dtype=''.join([byteorder,'u4'])))
    else:
        raise ValueError("fmt is an unsupported DataSampleFormat.")

    return trc
