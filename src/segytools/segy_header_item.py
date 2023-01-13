'''
segy header item
'''

# import python standard modules
import struct

# import 3rd party libraries
import numpy
from ibm2ieee import ibm2float32, ibm2float64

# import local python
from segytools.datatypes import DataSampleFormat


class SegyHeaderItem(object):
    """Used to describe a single header item or field in a segy file header or trace header.

    Parameters
    ----------
    name : str
        Header item identifier.
    sample_format : DataSampleFormat
        data sample format that tells the system how to interpret the bytes
    start_byte : int
        Index of the first byte to read. Uses SEGY standard notation which starts a header container at one, not zero. 
        For example, reading a 4-byte integer header from a bytes or bytearray object, b[0:4] would have a start_byte = 1.
    description : str
        Description of the header item.
    map_dict : `dict`
        Dictionary in which the key is the interpreted value. Required if map_bool is True.
    value : Any
        Header item value.

    Methods
    -------
    has_mapping_dictionary
    """

    def __init__(self, sample_format:DataSampleFormat, start_byte:int=0, description:str='', map_dict:dict={}, value=0):
        self._sample_format = sample_format  # TODO: assert derived from DataSampleFormat name tuple
        self._n_bytes = sample_format.size_in_bytes  # length of the header in bytes; default to 4, but may be 2
        self._start_byte = start_byte      # the relative byte location to start reading
        self._description = description  # defualt to empty string
        self._value = value              # the value obtained from the segy file
        self._supplementary = ''         # any additional supplementary material
        self._map_dict = map_dict        # name of the dictionary to map to
        self._mapped_value = None
        if map_dict:
            self._mapped_value = map_dict[value]

    def __str__(self):
        s += 'description: ' + self._description + ', '
        s += 'start byte: ' + str(self._start_byte) + ', '
        s += 'byte length: ' + str(self._n_bytes) + ', '
        s += 'value: ' + str(self._value)
        return s

    @property
    def sample_format(self) -> DataSampleFormat:
        """Get the sample format of the data."""
        return self._sample_format
    
    @sample_format.setter
    def sample_format(self, sample_format:DataSampleFormat):
        """Set the item's data sample format.

        Parameters
        ----------
        sample_format : DataSampleFormat
            The format to be set.
        """
        # TODO: sample format validation; must be a valid DataSampleFormat Enum Type
        # TODO: convert the value to this format
        self._sample_format = sample_format
        self._n_bytes = sample_format.size_in_bytes

    @property
    def n_bytes(self) -> int:
        """Get the item's number of bytes."""
        return self._n_bytes

    # NOTE: no _nbytes setter; must be set with data_sample_format()
    
    @property
    def start_byte(self) -> int:
        """Get the item's start byte."""
        return self._start_byte

    @start_byte.setter
    def start_byte(self, start_byte:int):
        """Set the item's start byte.

        Parameters
        ----------
        start_byte : int
            start byte value to be set.
        """
        # TODO: start_byte validation; must be non-negative integer
        self._start_byte = start_byte   

    @property
    def description(self) -> str:
        """Get the item's description."""
        return self._description

    @description.setter
    def description(self, description:str):
        """Set the item's description.

        Parameters
        ----------
        description : str
            Description of item to be set.
        """
        # TODO: description validation; assert is string.
        # should be short, but doesn't have to be. A very long string may indicate something is being improperly set.
        self._description = description

    @property
    def value(self):
        """Get the item's value."""
        return self._value

    @value.setter
    def value(self, value):
        """Set the item's value.

        Parameter
        ---------
        value : Any
            The value to be set.
        """
        # TODO: if this item is mapped to another value, assert this value assigned matches the type in the mapping.
        self._value = value
        if self._map_dict:
            self._mapped_value = self._map_dict[value]

    @property
    def supplementary(self) -> str:
        """Get the item's supplementary content."""
        return self._supplementary

    @supplementary.setter
    def supplementary(self, supplementary:str):
        """Set the item's supplementary content.

        Parameters
        ----------
        supplementary : str
            The supplementary content to be set.
        """
        self._supplementary = supplementary
    
    @property
    def map_dict(self) -> dict:
        """Get the item's mapping dictionary. If not mapping dictionary provided, returns an empty dict."""
        return self._map_dict

    @map_dict.setter
    def map_dict(self, mapping_dictionary:dict):
        """Set the item's mapping dictionary."""
        self._map_dict = mapping_dictionary
        self._mapped_value = self._map_dict[self._value]
    
    @property
    def mapped_value(self):
        """Get the item's mapped_value."""
        return self._mapped_value
    
    def has_mapping_dictionary(self) -> bool:
        """Returns True if there is a mapping dictionary provided to map the interpreted value to another value. Otherwise, returns False."""
        tmp_out = False
        if self._map_dict:
            tmp_out = True
        return tmp_out


    def to_bytes(self, endianess: str) -> bytes:
        """Convert the segy header item to a bytes object for writing back out to segy format.
        
        Parameters
        ----------
        endianess : str
            '>' for big endian, '<' for little.
        """
        if self._sample_format == 'ibm':
            raise NotImplementedError("IBM floats are not supported for writing to bytes. Use DataSampleFormat_FLOAT32.")
        else:
            fmt = ''.join([endianess, self._sample_format.format])
            #val = self._value
            bout = struct.pack(fmt, self._value)
        return bout

    @staticmethod
    def value_from_buffer(buf:bytes, endianess:str, sample_format:DataSampleFormat):
        """Unpack value from buffer.

        Parameters
        ----------
        buf : bytes
            buffer
        endianess : str
            either '<' for little or '>' for big endian
        sample_format : DataSampleFormat
            data sample format used for interpreting bytes object.
        """
        if sample_format.format == 'ibm':
            # NOTE: only 32-bit ibm floats currently tested and supported
            fmt = ''.join([endianess,'u4'])
            val = ibm2float32(numpy.frombuffer(buffer=buf, dtype='>u4'))
        else:
            fmt = ''.join([endianess, sample_format.format])
            val = struct.unpack(fmt, buf)
            val = val[0]  # unpack always returns a tuple
        return val
    
    
    @classmethod
    def from_bytes(cls, buf:bytes, endianess: str, sample_format:DataSampleFormat, start_byte:int=0, description:str='', map_dict:dict={}):
        """Create a segy header item from a bytes object.

        Parameters
        ----------
        buf : bytes
            The byte data.
        endianess : str
            '>' for big endian, '<' for little
        """
        header_item = SegyHeaderItem(sample_format=sample_format, start_byte=start_byte, description=description, map_dict=map_dict)
        header_item.value = cls.value_from_buffer(buf=buf, endianess=endianess, sample_format=sample_format)

        return header_item
