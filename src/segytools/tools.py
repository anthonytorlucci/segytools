"""Segy file toolkit largely based on sixty-north/segpy"""

# import standard

# import third party

# import local
from segytools.segpy.toolkit import unpack_ibm_floats, unpack_values

# modified from segpy toolkit.py
def read_binary_values(buf, num_items, ctype, endian):
    values = (unpack_ibm_floats(buf, num_items)
              if ctype == 'ibm'
              else unpack_values(buf, ctype, endian))
    assert len(values) == num_items
    return values