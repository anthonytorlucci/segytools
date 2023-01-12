from context import segytools

import struct

from segytools.datatypes import DataSampleFormat_INT8, DataSampleFormat_INT16, DataSampleFormat_INT32, \
    DataSampleFormat_UINT8, DataSampleFormat_UINT16, DataSampleFormat_UINT32, \
    DataSampleFormat_FLOAT32, DataSampleFormat_FLOAT64, DataSampleFormat_IBM
from segytools.segy_header_item import SegyHeaderItem

def test_segy_header_item_value_initialization():
    expected = int(0)
    hdr_item = SegyHeaderItem(name='example', sample_format=DataSampleFormat_INT16, value=expected)
    actual = hdr_item.value
    assert actual == expected, "SegyHeaderItem value incorrectly initialized."

def test_segy_header_item_from_bytes_INT8_ONE_LITTLE():
    expected = int(1)
    buf = struct.pack("<b", expected)
    header_item = SegyHeaderItem.from_bytes(buf=buf, endianess='<', name='example', sample_format=DataSampleFormat_INT8, start_byte=0)
    actual = header_item.value
    assert actual == expected

def test_segy_header_item_from_bytes_INT16_ONE_LITTLE():
    expected = int(1)
    buf = struct.pack("<h", expected)
    header_item = SegyHeaderItem.from_bytes(buf=buf, endianess='<', name='example', sample_format=DataSampleFormat_INT16, start_byte=0)
    actual = header_item.value
    assert actual == expected

def test_segy_header_item_from_bytes_INT32_ONE_LITTLE():
    expected = int(1)
    buf = struct.pack("<i", expected)
    header_item = SegyHeaderItem.from_bytes(buf=buf, endianess='<', name='example', sample_format=DataSampleFormat_INT32, start_byte=0)
    actual = header_item.value
    assert actual == expected


def test_segy_header_item_from_bytes_UINT8_ONE_LITTLE():
    expected = int(1)
    buf = struct.pack("<B", expected)
    header_item = SegyHeaderItem.from_bytes(buf=buf, endianess='<', name='example', sample_format=DataSampleFormat_UINT8, start_byte=0)
    actual = header_item.value
    assert actual == expected

def test_segy_header_item_from_bytes_UINT16_ONE_LITTLE():
    expected = int(1)
    buf = struct.pack("<H", expected)
    header_item = SegyHeaderItem.from_bytes(buf=buf, endianess='<', name='example', sample_format=DataSampleFormat_UINT16, start_byte=0)
    actual = header_item.value
    assert actual == expected

def test_segy_header_item_from_bytes_UINT32_ONE_LITTLE():
    expected = int(1)
    buf = struct.pack("<I", expected)
    header_item = SegyHeaderItem.from_bytes(buf=buf, endianess='<', name='example', sample_format=DataSampleFormat_UINT32, start_byte=0)
    actual = header_item.value
    assert actual == expected

def test_segy_header_item_from_bytes_FLOAT32_ONE_LITTLE():
    expected = float(1.0)
    buf = struct.pack("<f", expected)
    header_item = SegyHeaderItem.from_bytes(buf=buf, endianess='<', name='example', sample_format=DataSampleFormat_FLOAT32, start_byte=0)
    actual = header_item.value
    assert actual == expected

def test_segy_header_item_from_bytes_FLOAT64_ONE_LITTLE():
    expected = float(1.0)
    buf = struct.pack("<d", expected)
    header_item = SegyHeaderItem.from_bytes(buf=buf, endianess='<', name='example', sample_format=DataSampleFormat_FLOAT64, start_byte=0)
    actual = header_item.value
    assert actual == expected

def test_segy_header_item_from_bytes_IBM_POS_ONE_LITTLE():
    expected = float(1.0)
    buf = b'A\x10\x00\x00'
    header_item = SegyHeaderItem.from_bytes(buf=buf, endianess='<', name='example', sample_format=DataSampleFormat_IBM, start_byte=0)
    actual = header_item.value
    assert actual == expected

def test_segy_header_item_from_bytes_IBM_NEG_ONE_LITTLE():
    expected = float(-1.0)
    buf = b'\xc1\x10\x00\x00'
    header_item = SegyHeaderItem.from_bytes(buf=buf, endianess='<', name='example', sample_format=DataSampleFormat_IBM, start_byte=0)
    actual = header_item.value
    assert actual == expected

def test_segy_header_item_from_bytes_INT8_ONE_BIG():
    expected = int(1)
    buf = struct.pack(">b", expected)
    header_item = SegyHeaderItem.from_bytes(buf=buf, endianess='>', name='example', sample_format=DataSampleFormat_INT8, start_byte=0)
    actual = header_item.value
    assert actual == expected

def test_segy_header_item_from_bytes_INT16_ONE_BIG():
    expected = int(1)
    buf = struct.pack(">h", expected)
    header_item = SegyHeaderItem.from_bytes(buf=buf, endianess='>', name='example', sample_format=DataSampleFormat_INT16, start_byte=0)
    actual = header_item.value
    assert actual == expected

def test_segy_header_item_from_bytes_INT32_ONE_BIG():
    expected = int(1)
    buf = struct.pack(">i", expected)
    header_item = SegyHeaderItem.from_bytes(buf=buf, endianess='>', name='example', sample_format=DataSampleFormat_INT32, start_byte=0)
    actual = header_item.value
    assert actual == expected

def test_segy_header_item_from_bytes_UINT8_ONE_BIG():
    expected = int(1)
    buf = struct.pack(">B", expected)
    header_item = SegyHeaderItem.from_bytes(buf=buf, endianess='>', name='example', sample_format=DataSampleFormat_UINT8, start_byte=0)
    actual = header_item.value
    assert actual == expected

def test_segy_header_item_from_bytes_UINT16_ONE_BIG():
    expected = int(1)
    buf = struct.pack(">H", expected)
    header_item = SegyHeaderItem.from_bytes(buf=buf, endianess='>', name='example', sample_format=DataSampleFormat_UINT16, start_byte=0)
    actual = header_item.value
    assert actual == expected

def test_segy_header_item_from_bytes_UINT32_ONE_BIG():
    expected = int(1)
    buf = struct.pack(">I", expected)
    header_item = SegyHeaderItem.from_bytes(buf=buf, endianess='>', name='example', sample_format=DataSampleFormat_UINT32, start_byte=0)
    actual = header_item.value
    assert actual == expected

def test_segy_header_item_from_bytes_FLOAT32_ONE_BIG():
    expected = float(1.0)
    buf = struct.pack(">f", expected)
    header_item = SegyHeaderItem.from_bytes(buf=buf, endianess='>', name='example', sample_format=DataSampleFormat_FLOAT32, start_byte=0)
    actual = header_item.value
    assert actual == expected

def test_segy_header_item_from_bytes_FLOAT64_ONE_BIG():
    expected = float(1.0)
    buf = struct.pack(">d", expected)
    header_item = SegyHeaderItem.from_bytes(buf=buf, endianess='>', name='example', sample_format=DataSampleFormat_FLOAT64, start_byte=0)
    actual = header_item.value
    assert actual == expected

def test_segy_header_item_from_bytes_IBM_POS_ONE_BIG():
    expected = float(1.0)
    buf = b'A\x10\x00\x00'
    header_item = SegyHeaderItem.from_bytes(buf=buf, endianess='>', name='example', sample_format=DataSampleFormat_IBM, start_byte=0)
    actual = header_item.value
    assert actual == expected

def test_segy_header_item_from_bytes_IBM_NEG_ONE_BIG():
    expected = float(-1.0)
    buf = b'\xc1\x10\x00\x00'
    header_item = SegyHeaderItem.from_bytes(buf=buf, endianess='>', name='example', sample_format=DataSampleFormat_IBM, start_byte=0)
    actual = header_item.value
    assert actual == expected







def test_segy_header_item_to_bytes_INT8_ONE_LITTLE():
    expected = int(1).to_bytes(1, byteorder='little', signed=True)
    header_item = SegyHeaderItem(name='example', sample_format=DataSampleFormat_INT8, value=int(1))
    actual = header_item.to_bytes(endianess='<')
    assert actual == expected

def test_segy_header_item_to_bytes_INT16_ONE_LITTLE():
    expected = int(1).to_bytes(2, byteorder='little', signed=True)
    header_item = SegyHeaderItem(name='example', sample_format=DataSampleFormat_INT16, value=int(1))
    actual = header_item.to_bytes(endianess='<')
    assert actual == expected

def test_segy_header_item_to_bytes_INT32_ONE_LITTLE():
    expected = int(1).to_bytes(4, byteorder='little', signed=True)
    header_item = SegyHeaderItem(name='example', sample_format=DataSampleFormat_INT32, value=int(1))
    actual = header_item.to_bytes(endianess='<')
    assert actual == expected

def test_segy_header_item_to_bytes_UINT8_ONE_LITTLE():
    expected = int(1).to_bytes(1, byteorder='little', signed=False)
    header_item = SegyHeaderItem(name='example', sample_format=DataSampleFormat_UINT8, value=int(1))
    actual = header_item.to_bytes(endianess='<')
    assert actual == expected

def test_segy_header_item_to_bytes_UINT16_ONE_LITTLE():
    expected = int(1).to_bytes(2, byteorder='little', signed=False)
    header_item = SegyHeaderItem(name='example', sample_format=DataSampleFormat_UINT16, value=int(1))
    actual = header_item.to_bytes(endianess='<')
    assert actual == expected

def test_segy_header_item_to_bytes_UINT32_ONE_LITTLE():
    expected = int(1).to_bytes(4, byteorder='little', signed=False)
    header_item = SegyHeaderItem(name='example', sample_format=DataSampleFormat_UINT32, value=int(1))
    actual = header_item.to_bytes(endianess='<')
    assert actual == expected

def test_segy_header_item_to_bytes_FLOAT32_ONE_LITTLE():
    expected = struct.pack("<f", float(1.0))
    header_item = SegyHeaderItem(name='example', sample_format=DataSampleFormat_FLOAT32, value=float(1.0))
    actual = header_item.to_bytes(endianess='<')
    assert actual == expected
