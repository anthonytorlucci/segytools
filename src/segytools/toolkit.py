"""Collection of tools for working with segy data"""

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
        dt = numpy.int8
        dt = dt.newbyteorder(byteorder)
        trc = numpy.frombuffer(buf, dtype=dt)
    elif fmt.ctype == 'unsigned char':
        dt = numpy.uint8
        dt = dt.newbyteorder(byteorder)
        trc = numpy.frombuffer(buf, dtype=dt)
    elif fmt.ctype == 'short':
        dt = numpy.int16
        dt = dt.newbyteorder(byteorder)
        trc = numpy.frombuffer(buf, dtype=dt)
    elif fmt.ctype == 'unsigned short':
        dt = numpy.uint16
        dt = dt.newbyteorder(byteorder)
        trc = numpy.frombuffer(buf, dtype=dt)
    elif fmt.ctype == 'int':
        dt = numpy.int32
        dt = dt.newbyteorder(byteorder)
        trc = numpy.frombuffer(buf, dtype=dt)
    elif fmt.ctype == 'unsigned int':
        dt = numpy.uint32
        dt = dt.newbyteorder(byteorder)
        trc = numpy.frombuffer(buf, dtype=dt)
    elif fmt.ctype == 'float':
        dt = numpy.float32
        dt = dt.newbyteorder(byteorder)
        trc = numpy.frombuffer(buf, dtype=dt)
    elif fmt.ctype == 'double':
        dt = numpy.float64
        dt = dt.newbyteorder(byteorder)
        trc = numpy.frombuffer(buf, dtype=dt)
    elif fmt.ctype == 'ibm':
        trc = ibm2float64(numpy.frombuffer(buffer=buf, dtype=''.join([byteorder,'u4'])))
    else:
        raise ValueError("fmt is an unsupported DataSampleFormat.")

    return trc

