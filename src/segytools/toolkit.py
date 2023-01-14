"""Collection of tools for working with segy data"""

# standard
from array import array
import sys
import textwrap

# third party

# local
#--from segytools.ibm_float import IBMFloat, ibm2ieee, ieee2ibm

# def unpack_ibm_floats(data, num_items):
#     """Unpack a series of binary-encoded big-endian single-precision IBM floats.

#     Args:
#         data: A sequence of bytes.

#         num_items: The number of floats to be read.

#     Returns:
#         A sequence of floats.
#     """
#     return [IBMFloat.from_bytes(data[i: i+4]) for i in range(0, num_items * 4, 4)]


# def unpack_values(buf, ctype, endian='big'):
#     """Unpack a series items from a byte string.

#     Args:
#         data: A sequence of bytes.

#         ctype: A format code (one of the values in the datatype.CTYPES
#             dictionary)

#         endian: '>' for big-endian data (the standard and default), '<'
#             for little-endian (non-standard)

#     Returns:
#         A sequence of objects with type corresponding to the format code.
#     """
#     a = array(ctype, buf)
#     if endian != sys.byteorder:
#         a.byteswap()
#     return a

# def read_binary_values(buf, num_items, ctype, endian):
#     """Read trace data from bytes object and convert to list of floats

#     Parameters
#     ----------
#     buf : bytes
#         buffer of byte data
#     num_items : int
#         number of samples expected in output
#     ctype : str
#         character type; see segpy.datatypes.SEG_Y_TYPE_TO_CTYPE for acceptable values
#     endian : str
#         either 'little' or 'big'
#     """
#     values = (unpack_ibm_floats(buf, num_items)
#               if ctype == 'ibm'
#               else unpack_values(buf, ctype, endian))
#     assert len(values) == num_items
#     return values

# def convert_binary_value(buf: bytes, ctype: str, endian: str):
#     """Read a bytes object and convert to an integer or float depending on the ctype."""
#     # match ctype:
#     #     case 'ibm':
#     #         if sys.byteorder != 'big':
#     #             raise ValueError("ibm float conversion only supported for big endian byteorder.")
#     #         return float(ibm2ieee(big_endian_bytes=buf))
#     #     case 'f':
#     #         return float(buf)
#     #     case 'i':
#     #         return int.from_bytes(bytes=buf, byteorder=endian)
#     #     case _:
#     #         raise ValueError("ctype unsupported.")
#     raise NotImplementedError()

    

def format_textheader_string(textheader):
    """Format the textheader to have each line be 80 characters long and return a single string.

    Parameters
    ----------
    textheader : str
        The textual header string after decoding.

    Returns
    -------
    str
        Textual header with 80 characters per line.
    """
    return '\n'.join(textwrap.wrap(textheader, 80))