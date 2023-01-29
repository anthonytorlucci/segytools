"""Mappings between the coding systems used for sample types.
"""

# A mapping from data sample format codes to SEG Y types.
from collections import namedtuple

DataSampleFormat = namedtuple(
    'DataSampleFormat', ['format', 'ctype', 'size_in_bytes'])

# https://docs.python.org/3/library/struct.html
DATA_SAMPLE_FORMAT_INT8 = DataSampleFormat(
    format='b', ctype='char', size_in_bytes=1)
DATA_SAMPLE_FORMAT_UINT8 = DataSampleFormat(
    format='B', ctype='unsigned char', size_in_bytes=1)
DATA_SAMPLE_FORMAT_INT16 = DataSampleFormat(
    format='h', ctype='short', size_in_bytes=2)
DATA_SAMPLE_FORMAT_UINT16 = DataSampleFormat(
    format='H', ctype='unsigned short', size_in_bytes=2)
DATA_SAMPLE_FORMAT_INT32 = DataSampleFormat(
    format='i', ctype='int', size_in_bytes=4)
DATA_SAMPLE_FORMAT_UINT32 = DataSampleFormat(
    format='I', ctype='unsigned int', size_in_bytes=4)
DATA_SAMPLE_FORMAT_FLOAT32 = DataSampleFormat(
    format='f', ctype='float', size_in_bytes=4)
DATA_SAMPLE_FORMAT_FLOAT64 = DataSampleFormat(
    format='d', ctype='double', size_in_bytes=8)
DATA_SAMPLE_FORMAT_IBM = DataSampleFormat(
    format='ibm', ctype='ibm', size_in_bytes=4)
