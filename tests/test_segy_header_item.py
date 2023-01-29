from context import segytools

import struct

from segytools.datatypes import DATA_SAMPLE_FORMAT_INT8, \
    DATA_SAMPLE_FORMAT_INT16, DATA_SAMPLE_FORMAT_INT32, \
    DATA_SAMPLE_FORMAT_UINT8, DATA_SAMPLE_FORMAT_UINT16, \
    DATA_SAMPLE_FORMAT_UINT32, DATA_SAMPLE_FORMAT_FLOAT32, \
    DATA_SAMPLE_FORMAT_FLOAT64, DATA_SAMPLE_FORMAT_IBM
from segytools.segy_header_item import SegyHeaderItem


def test_value_initialization():
    expected = int(0)
    hdr_item = SegyHeaderItem(
        sample_format=DATA_SAMPLE_FORMAT_INT16,
        value=expected)
    actual = hdr_item.value
    assert actual == expected, "SegyHeaderItem value incorrectly initialized."


def test_from_bytes_INT8_ONE_LITTLE():
    expected = int(1)
    buf = struct.pack("<b", expected)
    header_item = SegyHeaderItem.from_bytes(
        buf=buf,
        endianess='<',
        sample_format=DATA_SAMPLE_FORMAT_INT8,
        start_byte=0)
    actual = header_item.value
    assert actual == expected


def test_from_bytes_INT16_ONE_LITTLE():
    expected = int(1)
    buf = struct.pack("<h", expected)
    header_item = SegyHeaderItem.from_bytes(
        buf=buf,
        endianess='<',
        sample_format=DATA_SAMPLE_FORMAT_INT16,
        start_byte=0)
    actual = header_item.value
    assert actual == expected


def test_from_bytes_INT32_ONE_LITTLE():
    expected = int(1)
    buf = struct.pack("<i", expected)
    header_item = SegyHeaderItem.from_bytes(
        buf=buf,
        endianess='<',
        sample_format=DATA_SAMPLE_FORMAT_INT32,
        start_byte=0)
    actual = header_item.value
    assert actual == expected


def test_from_bytes_UINT8_ONE_LITTLE():
    expected = int(1)
    buf = struct.pack("<B", expected)
    header_item = SegyHeaderItem.from_bytes(
        buf=buf,
        endianess='<',
        sample_format=DATA_SAMPLE_FORMAT_UINT8,
        start_byte=0)
    actual = header_item.value
    assert actual == expected


def test_from_bytes_UINT16_ONE_LITTLE():
    expected = int(1)
    buf = struct.pack("<H", expected)
    header_item = SegyHeaderItem.from_bytes(
        buf=buf,
        endianess='<',
        sample_format=DATA_SAMPLE_FORMAT_UINT16,
        start_byte=0)
    actual = header_item.value
    assert actual == expected


def test_from_bytes_UINT32_ONE_LITTLE():
    expected = int(1)
    buf = struct.pack("<I", expected)
    header_item = SegyHeaderItem.from_bytes(
        buf=buf,
        endianess='<',
        sample_format=DATA_SAMPLE_FORMAT_UINT32,
        start_byte=0)
    actual = header_item.value
    assert actual == expected


def test_from_bytes_FLOAT32_ONE_LITTLE():
    expected = float(1.0)
    buf = struct.pack("<f", expected)
    header_item = SegyHeaderItem.from_bytes(
        buf=buf,
        endianess='<',
        sample_format=DATA_SAMPLE_FORMAT_FLOAT32,
        start_byte=0)
    actual = header_item.value
    assert actual == expected


def test_from_bytes_FLOAT64_ONE_LITTLE():
    expected = float(1.0)
    buf = struct.pack("<d", expected)
    header_item = SegyHeaderItem.from_bytes(
        buf=buf,
        endianess='<',
        sample_format=DATA_SAMPLE_FORMAT_FLOAT64,
        start_byte=0)
    actual = header_item.value
    assert actual == expected


def test_from_bytes_IBM_POS_ONE_LITTLE():
    expected = float(1.0)
    buf = b'A\x10\x00\x00'
    header_item = SegyHeaderItem.from_bytes(
        buf=buf,
        endianess='<',
        sample_format=DATA_SAMPLE_FORMAT_IBM,
        start_byte=0)
    actual = header_item.value
    assert actual == expected


def test_from_bytes_IBM_NEG_ONE_LITTLE():
    expected = float(-1.0)
    buf = b'\xc1\x10\x00\x00'
    header_item = SegyHeaderItem.from_bytes(
        buf=buf,
        endianess='<',
        sample_format=DATA_SAMPLE_FORMAT_IBM,
        start_byte=0)
    actual = header_item.value
    assert actual == expected


def test_from_bytes_INT8_ONE_BIG():
    expected = int(1)
    buf = struct.pack(">b", expected)
    header_item = SegyHeaderItem.from_bytes(
        buf=buf,
        endianess='>',
        sample_format=DATA_SAMPLE_FORMAT_INT8,
        start_byte=0)
    actual = header_item.value
    assert actual == expected


def test_from_bytes_INT16_ONE_BIG():
    expected = int(1)
    buf = struct.pack(">h", expected)
    header_item = SegyHeaderItem.from_bytes(
        buf=buf,
        endianess='>',
        sample_format=DATA_SAMPLE_FORMAT_INT16,
        start_byte=0)
    actual = header_item.value
    assert actual == expected


def test_from_bytes_INT32_ONE_BIG():
    expected = int(1)
    buf = struct.pack(">i", expected)
    header_item = SegyHeaderItem.from_bytes(
        buf=buf,
        endianess='>',
        sample_format=DATA_SAMPLE_FORMAT_INT32,
        start_byte=0)
    actual = header_item.value
    assert actual == expected


def test_from_bytes_UINT8_ONE_BIG():
    expected = int(1)
    buf = struct.pack(">B", expected)
    header_item = SegyHeaderItem.from_bytes(
        buf=buf,
        endianess='>',
        sample_format=DATA_SAMPLE_FORMAT_UINT8,
        start_byte=0)
    actual = header_item.value
    assert actual == expected


def test_from_bytes_UINT16_ONE_BIG():
    expected = int(1)
    buf = struct.pack(">H", expected)
    header_item = SegyHeaderItem.from_bytes(
        buf=buf,
        endianess='>',
        sample_format=DATA_SAMPLE_FORMAT_UINT16,
        start_byte=0)
    actual = header_item.value
    assert actual == expected


def test_from_bytes_UINT32_ONE_BIG():
    expected = int(1)
    buf = struct.pack(">I", expected)
    header_item = SegyHeaderItem.from_bytes(
        buf=buf,
        endianess='>',
        sample_format=DATA_SAMPLE_FORMAT_UINT32,
        start_byte=0)
    actual = header_item.value
    assert actual == expected


def test_from_bytes_FLOAT32_ONE_BIG():
    expected = float(1.0)
    buf = struct.pack(">f", expected)
    header_item = SegyHeaderItem.from_bytes(
        buf=buf,
        endianess='>',
        sample_format=DATA_SAMPLE_FORMAT_FLOAT32,
        start_byte=0)
    actual = header_item.value
    assert actual == expected


def test_from_bytes_FLOAT64_ONE_BIG():
    expected = float(1.0)
    buf = struct.pack(">d", expected)
    header_item = SegyHeaderItem.from_bytes(
        buf=buf,
        endianess='>',
        sample_format=DATA_SAMPLE_FORMAT_FLOAT64,
        start_byte=0)
    actual = header_item.value
    assert actual == expected


def test_from_bytes_IBM_POS_ONE_BIG():
    expected = float(1.0)
    buf = b'A\x10\x00\x00'
    header_item = SegyHeaderItem.from_bytes(
        buf=buf,
        endianess='>',
        sample_format=DATA_SAMPLE_FORMAT_IBM,
        start_byte=0)
    actual = header_item.value
    assert actual == expected


def test_from_bytes_IBM_NEG_ONE_BIG():
    expected = float(-1.0)
    buf = b'\xc1\x10\x00\x00'
    header_item = SegyHeaderItem.from_bytes(
        buf=buf,
        endianess='>',
        sample_format=DATA_SAMPLE_FORMAT_IBM,
        start_byte=0)
    actual = header_item.value
    assert actual == expected


def test_to_bytes_INT8_ONE_LITTLE():
    expected = int(1).to_bytes(1, byteorder='little', signed=True)
    header_item = SegyHeaderItem(
        sample_format=DATA_SAMPLE_FORMAT_INT8,
        value=int(1))
    actual = header_item.to_bytes(endianess='<')
    assert actual == expected


def test_to_bytes_INT16_ONE_LITTLE():
    expected = int(1).to_bytes(2, byteorder='little', signed=True)
    header_item = SegyHeaderItem(
        sample_format=DATA_SAMPLE_FORMAT_INT16,
        value=int(1))
    actual = header_item.to_bytes(endianess='<')
    assert actual == expected


def test_to_bytes_INT32_ONE_LITTLE():
    expected = int(1).to_bytes(4, byteorder='little', signed=True)
    header_item = SegyHeaderItem(
        sample_format=DATA_SAMPLE_FORMAT_INT32,
        value=int(1))
    actual = header_item.to_bytes(endianess='<')
    assert actual == expected


def test_to_bytes_UINT8_ONE_LITTLE():
    expected = int(1).to_bytes(1, byteorder='little', signed=False)
    header_item = SegyHeaderItem(
        sample_format=DATA_SAMPLE_FORMAT_UINT8,
        value=int(1))
    actual = header_item.to_bytes(endianess='<')
    assert actual == expected


def test_to_bytes_UINT16_ONE_LITTLE():
    expected = int(1).to_bytes(2, byteorder='little', signed=False)
    header_item = SegyHeaderItem(
        sample_format=DATA_SAMPLE_FORMAT_UINT16,
        value=int(1))
    actual = header_item.to_bytes(endianess='<')
    assert actual == expected


def test_to_bytes_UINT32_ONE_LITTLE():
    expected = int(1).to_bytes(4, byteorder='little', signed=False)
    header_item = SegyHeaderItem(
        sample_format=DATA_SAMPLE_FORMAT_UINT32,
        value=int(1))
    actual = header_item.to_bytes(endianess='<')
    assert actual == expected


def test_to_bytes_FLOAT32_ONE_LITTLE():
    expected = struct.pack("<f", float(1.0))
    header_item = SegyHeaderItem(
        sample_format=DATA_SAMPLE_FORMAT_FLOAT32,
        value=float(1.0))
    actual = header_item.to_bytes(endianess='<')
    assert actual == expected


def test_has_mapping_dictionary_False():
    expected = False
    header_item = SegyHeaderItem(
        sample_format=DATA_SAMPLE_FORMAT_INT16,
        value=int(1))
    actual = header_item.has_mapping_dictionary()
    assert actual == expected


def test_has_mapping_dictionary_True():
    expected = True
    d = {1: 'has a mapping'}
    header_item = SegyHeaderItem(
        sample_format=DATA_SAMPLE_FORMAT_INT16,
        value=int(1),
        map_dict=d)
    actual = header_item.has_mapping_dictionary()
    assert actual == expected


def test_mapping_dictionary_value():
    expected = 0.01
    d = {1: 0.01}
    header_item = SegyHeaderItem(
        sample_format=DATA_SAMPLE_FORMAT_INT16,
        value=int(1),
        map_dict=d)
    actual = header_item.mapped_value
    assert actual == expected


def test_mapping_dictionary_getter():
    d = {1: 0.01}
    expected = d
    header_item = SegyHeaderItem(
        sample_format=DATA_SAMPLE_FORMAT_INT16,
        value=int(1),
        map_dict=d)
    actual = header_item.map_dict
    assert actual == expected


def test_mapping_dictionary_setter():
    d = {1: 0.01}
    expected = 0.01
    header_item = SegyHeaderItem(
        sample_format=DATA_SAMPLE_FORMAT_INT16,
        value=int(1))
    header_item.map_dict = d
    actual = header_item.mapped_value
    assert actual == expected


def test_value_setter():
    expected = 1
    header_item = SegyHeaderItem(
        sample_format=DATA_SAMPLE_FORMAT_INT16)
    header_item.value = expected
    actual = header_item.value
    assert actual == expected


def test_n_bytes_getter_INT8():
    expected = 1
    header_item = SegyHeaderItem(
        sample_format=DATA_SAMPLE_FORMAT_INT8)
    actual = header_item.n_bytes
    assert actual == expected


def test_n_bytes_getter_INT16():
    expected = 2
    header_item = SegyHeaderItem(
        sample_format=DATA_SAMPLE_FORMAT_INT16)
    actual = header_item.n_bytes
    assert actual == expected


def test_n_bytes_getter_INT32():
    expected = 4
    header_item = SegyHeaderItem(
        sample_format=DATA_SAMPLE_FORMAT_INT32)
    actual = header_item.n_bytes
    assert actual == expected


def test_sample_format_setter_nbytes_INT8():
    expected = 1
    header_item = SegyHeaderItem(
        sample_format=DATA_SAMPLE_FORMAT_INT16)
    header_item.sample_format = DATA_SAMPLE_FORMAT_INT8
    actual = header_item.n_bytes
    assert actual == expected
