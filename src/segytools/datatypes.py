"""
Mappings between the coding systems used for sample types.

Copyright 2022 Anthony Torlucci

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
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
