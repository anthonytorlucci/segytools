'''
segy header item
'''

# import python standard modules


# import 3rd party libraries


# import local python
from segytools.datatypes import DataSampleFormat, data_sample_format_size_in_bytes


class SegyHeaderItem(object):
    """Used to describe a single header item or field in a segy file header or trace header.

    Parameters
    ----------
    name : str
        Header item identifier.
    sample_format : DataSampleFormat
        data sample format that tells the system how to interpret the bytes
    startbyte : int
        Zero-indexed starting location.
    description : str
        Description of the header item.
    is_signed : bool
        If the header item is an int, this flag indicates that the bytes object is signed.
    map_dict : `dict`
        Dictionary in which the key is the interpreted value. Required if map_bool is True.
    value : Any
        Header item value.

    Methods
    -------
    has_mapping_dictionary
    """

    def __init__(self, name:str, sample_format:DataSampleFormat, start_byte:int=0, description:str='', is_signed:bool=True,
                 map_dict:dict={}, value=0):
        self._name = name
        self._sample_format = sample_format  # TODO: assert type DataSampleFormat Enum class
        self._n_bytes = data_sample_format_size_in_bytes(self._sample_format)  # length of the header in bytes; default to 4, but may be 2
        self._start_byte = start_byte      # the relative byte location to start reading
        self._description = description  # defualt to empty string
        self._is_signed = is_signed      # a boolean; True is a signed twos complement integer, False is not signed and all values are positive.
        self._value = value              # the value obtained from the segy file
        self._supplementary = ''         # any additional supplementary material
        self._map_dict = map_dict        # name of the dictionary to map to

    def __str__(self):
        s = 'name: ' + self.name + ', '
        s += 'description: ' + self.description + ', '
        s += 'start byte: ' + str(self.startbyte) + ', '
        s += 'byte length: ' + str(self.nbytes) + ', '
        s += 'value: ' + str(self.value)
        return s

    @property
    def name(self) -> str:
        """Return the item's name."""
        return self._name

    @name.setter
    def name(self, name:str):
        """Set the item's name.

        Parameters
        ----------
        name : str
            The name to be set.
        """
        # TODO: name validation: must be a string; raise ValueError
        self._name = name

    @property
    def sample_format(self) -> DataSampleFormat:
        """Get the sample format of the data."""
        return self.sample_format
    
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
        self._n_bytes = data_sample_format_size_in_bytes(self._sample_format)

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
    def is_signed(self) -> bool:
        """Return True if the item is a signed integer. Otherwise, returns false."""
        return self._is_signed

    @is_signed.setter
    def is_signed(self, signed:bool):
        """Set the item's is_signed flag.

        The segy format defines all header to be two's complement or signed integers. However, some contractors
        will put unsigned integers in a header to increase the range of possible values when it is known that the
        header will never be negative.

        Note: floating point values (either ibm or ieee) are not affected by this.

        Parameters
        ----------
        signed : bool
            Whether the item is be interpreted as a signed integer or unsigned integer.
        """
        # TODO: if sample_format is either IBM or FLOAT32, print a warning that this is invalid and does nothing.
        self._is_signed = signed

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
            The desired system endian for output. Either 'little' or 'big'.
        """
        # TODO: endianess validation; must be either 'little' or 'big'
        # TODO: use try/except to convert self.value to int
        if self._sample_format == DataSampleFormat.INT8 or \
            self._sample_format == DataSampleFormat.INT16 or \
                self._sample_format == DataSampleFormat.INT32:
            tmp_value = self._value
            if self._map_dict:
                # this item has a mapping dictionary defined, map in reverse order back to an int so it can be converted to a bytes object
                for key, val in self._map_dict.items():
                    if self._value == val:
                        tmp_value = key
                        break
            try:
                int_val = int(tmp_value)
            except ValueError as err:
                print(f"SegyHeaderItem unable to convert value {tmp_value} to an integer. Please check mapping and sample format.")
                raise err

            bout = int.to_bytes(int_val, length=self._nbytes, byteorder=endianess, signed=self._is_signed)
        else:
            raise NotImplementedError("Converting to a non-integer value is not yet supported.")
        return bout

        

    @classmethod
    def from_bytes(cls, bsgy:bytes, endianess: str, name:str, sample_format:DataSampleFormat, start_byte:int, description:str, is_signed:bool=True, map_dict:dict={}) -> SegyHeaderItem:
        """Create a segy header item from a bytes object.

        Parameters
        ----------
        bsgy : bytes
            The byte data.
        """
        header_item = SegyHeaderItem(name=name, sample_format=sample_format, startbyte=start_byte, description=description, is_signed=is_signed, map_dict=map_dict)
        if header_item.sample_format == DataSampleFormat.INT8 or \
            header_item.sample_format == DataSampleFormat.INT16 or \
                header_item.sample_format == DataSampleFormat.INT32:
            header_item.value = int.from_bytes(bobj, byteorder=endianess, signed=header_item.is_signed)
            if header_item.map_dict:
                header_item.value = header_item.map_dict[header_item.value]
        else:
            raise NotImplementedError("Converting from floating point header items are not yet implemented.")

        return header_item
    
    
    
    # # ACCESSORS
    # def field(self, field_id):
    #     """Likely to be depreciated in favor of property decorators."""
    #     if field_id == 'name':
    #         return self.name
    #     elif field_id == 'nbytes':
    #         return self.nbytes
    #     elif field_id == 'startbyte':
    #         return self.startbyte
    #     elif field_id == 'description':
    #         return self.description
    #     elif field_id == 'signed':
    #         return self.signed
    #     elif field_id == 'value':
    #         return self.value
    #     elif field_id == 'supplementary':
    #         return self.supplementary
    #     elif field_id == 'map_bool':
    #         return self.map_bool
    #     elif field_id == 'map_dict':
    #         return self.map_dict
    #     else:
    #         print('field not found')
    #         return None

    # def header_name(self):
    #     """Likely to be depreciated in favor of property decorators."""
    #     return self.name

    # def number_of_bytes(self):
    #     """Likely to be depreciated in favor of property decorators."""
    #     return self.nbytes

    # def start_byte(self):
    #     """Likely to be depreciated in favor of property decorators."""
    #     return self.startbyte

    # # def description(self):
    # #     return self.description

    # def is_signed(self):
    #     """Likely to be depreciated in favor of property decorators."""
    #     return self.signed

    # # def value(self):
    # #     return self.value

    # # def supplementary(self):
    # #     return self.supplementary

    # # MUTATORS 
    # def set_field(self, field, value):
    #     if field == 'name':
    #         self.name = value
    #     elif field == 'nbytes':
    #         self.nbytes = value
    #     elif field == 'startbyte':
    #         self.startbyte = value
    #     elif field == 'description':
    #         self.description = value
    #     elif field == 'signed':
    #         self.signed = value
    #     elif field == 'value':
    #         self.value = value
    #     elif field == 'supplementary':
    #         self.supplementary = value
    #     elif field == 'map_bool':
    #         self.map_bool = value
    #     elif field == 'map_dict':
    #         self.map_dict = value
    #     else:
    #         print('field not found')


    # def set_name(self, name:str):
    #     self.name = name

    # def set_number_of_bytes(self, nbytes:int):
    #     self.nbytes = nbytes

    # def set_start_byte(self, startbyte:int):
    #     self.startbyte = startbyte

    # def set_description(self, description:str):
    #     self.description = description

    # def set_signed(self, signed:bool):
    #     self.signed = signed

    # def set_value(self, value):
    #     self.value = value

    # def set_supplementary_text(self, supplementary:str):
    #     self.supplementary = supplementary