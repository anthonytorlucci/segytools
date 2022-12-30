"""Collection of tools for working with segy data"""

# standard
from array import array

# third party

# local
from segytools.ibm_float import IBMFloat

def unpack_ibm_floats(data, num_items):
    """Unpack a series of binary-encoded big-endian single-precision IBM floats.

    Args:
        data: A sequence of bytes.

        num_items: The number of floats to be read.

    Returns:
        A sequence of floats.
    """
    return [IBMFloat.from_bytes(data[i: i+4]) for i in range(0, num_items * 4, 4)]


def unpack_values(buf, ctype, endian='big'):
    """Unpack a series items from a byte string.

    Args:
        data: A sequence of bytes.

        ctype: A format code (one of the values in the datatype.CTYPES
            dictionary)

        endian: '>' for big-endian data (the standard and default), '<'
            for little-endian (non-standard)

    Returns:
        A sequence of objects with type corresponding to the format code.
    """
    a = array(ctype, buf)
    if endian != sys.byteorder:
        a.byteswap()
    return a

def read_binary_values(buf, num_items, ctype, endian):
    """Read trace data from bytes object and convert to list of floats

    Parameters
    ----------
    buf : bytes
        buffer of byte data
    num_items : int
        number of samples expected in output
    ctype : str
        character type; see segpy.datatypes.SEG_Y_TYPE_TO_CTYPE for acceptable values
    endian : str
        either 'little' or 'big'
    """
    values = (unpack_ibm_floats(buf, num_items)
              if ctype == 'ibm'
              else unpack_values(buf, ctype, endian))
    assert len(values) == num_items
    return values