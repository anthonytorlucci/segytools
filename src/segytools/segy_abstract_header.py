"""
segy abstract header

Copyright 2022 Anthony Torlucci

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

# import python standard modules
# from typing import Any
import logging

# import 3rd party libraries

# import local python
from segytools.segy_header_item import SegyHeaderItem


class SegyAbstractHeader(object):
    """
    Base class for Segy Headers.

    SegyAbstractHeader is a container of SegyHeaderItem objects and inherited
    by SegyFileHeader and SegyTraceHeader. Any custom trace headers classes
    should inherit this class.

    Attributes
    ----------
    byte_length : int
        The number of bytes of the header. This must be overwritten is
        converting back to bytes object.

    Methods
    -------
    header_list()
        Returns a list of header item objects.
    key_object_dict()
        Returns a dictionary of header items identifiers and header item
        objects.
    key_property(name:str, field_id: str)
        Returns a property (field_id) of a segy header item based on the
        identifier `name`.
    mapped_value(name: str)
        Returns the mapped value of the header item with identifier `name` if
        the header item value is mapped.
    set_key_property(self, name: str, field_id: str, value: Any)
        Sets the value of the field of a header item based on the identifier
        `name`.
    """
    # default byte length; child objects must override this.
    # segy standard file headers are 400 bytes in length
    # segy standard trace headers are 240 bytes in length
    byte_length = 0

    def __str__(self) -> str:
        s = ''
        for _, hdr_item in self.key_object_dict().items():
            s = ''.join([s, str(hdr_item), '\n'])
        return s

    def header_list(self) -> list:
        """
        Returns a list of header item objects.
        """
        return [
            key for key, obj in self.__dict__.items()
            if isinstance(obj, SegyHeaderItem)]

    def key_object_dict(self) -> dict:
        """
        Returns a dictionary of header items identifiers and header item
        objects.
        """
        SETLIST_HDR_OBJECT = [
            (key, obj) for key, obj in self.__dict__.items()
            if isinstance(obj, SegyHeaderItem)]

        return {name: val for (name, val) in SETLIST_HDR_OBJECT}

    def set_header_values(self, buf: bytes, byteorder: str):
        """Set the value for each header item in the container.

        Parameters
        ----------
        buf : bytes
            The byte data used to set the values. len(bsgy) must be equal to
            the `byte_length` attribute.
        byteorder : str
            Used to decode the byte data. Must be either 'little' or 'big'.

        Raises
        ------
        ValueError
            len(bsgy) != byte_length
        ValueError
            byteorder != 'little' or byteorder != 'big'
        """
        if len(buf) != self.byte_length:
            raise ValueError(f"Number of bytes given {len(buf)} not equal to \
                header container byte length {self.byte_length}")
        if byteorder != '<' and byteorder != '>':
            raise ValueError("Provided endian parameter must be either \
                '<' or '>'.")

        for name, obj in self.key_object_dict().items():
            buf_slice = \
                buf[obj.start_byte - 1:obj.start_byte + obj.n_bytes - 1]
            obj.value = \
                SegyHeaderItem.value_from_buffer(
                    buf=buf_slice,
                    byteorder=byteorder,
                    sample_format=obj.sample_format)

    def to_bytes(self, byteorder: str) -> bytes:
        """
        Converts each header item to a byte object and returns the complete
        bytes object of length `byte_length`.

        Parameters
        ----------
        byteorder : str
            Either 'big' or 'little'

        Returns
        -------
        bytes
        """
        barr = bytearray(self.byte_length)  # TODO: initialize to zero
        file_key_obj_dict = self.key_object_dict()
        for _, obj in file_key_obj_dict.items():
            barr[obj.start_byte - 1:obj.start_byte + obj.n_bytes - 1] = \
                obj.to_bytes(byteorder=byteorder)
        return bytes(barr)
