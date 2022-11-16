'''
segy abstract header
'''

# import python standard modules
from types import FunctionType, MethodType
from typing import Any

# import 3rd party libraries


# import local python


class SegyAbstractHeader(object):
    """
    Base class for Segy Headers.
    
    SegyAbstractHeader is a container of SegyHeaderItem objects and inherited 
    by SegyFileHeader and SegyTraceHeader. Any custom trace headers classes 
    should inherit this class.

    Methods
    -------
    header_list()
        Returns a list of header item objects.
    key_object_dict()
        Returns a dictionary of header items identifiers and header item objects.
    key_property(name:str, field_id: str)
        Returns a property (field_id) of a segy header item based on the identifier `name`.
    mapped_value(name: str)
        Returns the mapped value of the header item with identifier `name` if the header item value is mapped.
    set_key_property(self, name: str, field_id: str, value: Any)
        Sets the value of the field of a header item based on the identifier `name`.
    """

    def header_list(self) -> list:
        """
        Returns a list of header item objects.
        """
        return [key for key, value in self.__dict__.items() if
                              not isinstance(value, (FunctionType, MethodType))]


    def key_object_dict(self) -> dict:
        """
        Returns a dictionary of header items identifiers and header item objects.
        """
        # stackoverflow : http://stackoverflow.com/questions/21945067/how-list-all-fields-of-an-class-in-python-and-no-methods
        # http://stackoverflow.com/questions/1747817/create-a-dictionary-with-list-comprehension-in-python
        # clever list (of sets) comprehension to get a list of all the fields in the class

        # stack overflow : http://stackoverflow.com/questions/19121722/build-dictionary-in-python-loop-list-and-dictionary-comprehensions
        # clever dict comprehension to get a dictionary of all the field.values in a class
        # {_key: _value(_key) for _key in _container}

        SETLIST_HDR_OBJECT = [(key, obj) for key, obj in self.__dict__.items() if
                              not isinstance(obj, (FunctionType, MethodType))]
        #print(len(SETLIST_HDR_OBJECT))

        # return {name: val for (name, val) in self.header_list()}
        return {name: val for (name, val) in SETLIST_HDR_OBJECT}

    def key_property(self, name: str, field_id: str) -> Any:
        """
        Returns a property (field_id) of a 'SegyHeaderItem' based on the identifier `name`.

        Parameters
        ----------
        name : str
            The header item identifier.
        field_id : str
            The field or property of the `SegyHeaderItem` to be retrived.
        """
        # obj is a SegyHeaderItem object
        obj = self.key_object_dict()[name]
        return obj.field(field_id)

    def mapped_value(self, name: str) -> Any:
        """
        Returns the mapped value of the header item with identifier `name` if the header item value is mapped.

        Parameters
        ----------
        name : str
            The `SegyHeaderItem` identifier.
        """
        # get the value from the map_dict if the value from the object (in this case, the key) exists, else
        # return the original value
        # obj is a SegyHeaderTemplate object
        obj = self.key_object_dict()[name]
        return obj.map_dict[obj.value] if obj.value in obj.map_dict else obj.value

    def set_key_property(self, name: str, field_id: str, value: Any) -> None:
        """
        Sets the value of the field of a header item based on the identifier `name`.

        Parameters
        ----------
        name : str
            The `SegyHeaderItem` identifier.
        field_id : str
            The field or property of the `SegyHeaderItem` to be retrived.
        value : Any
            The value that will be assigned to the `SegyHeaderItem` field.
        """
        # obj is a SegyHeaderTemplate object
        obj = self.key_object_dict()[name]
        obj.set_field(field_id, value)

    def _to_bytes(self, endianess: str, byte_length: int = 240) -> bytes:
        """
        Converts each header item to a byte object and returns the complete 
        bytes object of length `byte_length`.

        Parameters
        ----------
        endianess : str
            Either 'big' or 'little'
        byte_length : int
            the number of bytes in the output bytes object. default is 240.
        """
        bsgy = bytearray(byte_length)
        file_key_obj_dict = self.key_object_dict()
        for _, obj in file_key_obj_dict.items():
            
            if obj.map_bool is True:
                # reverse map back to integer
                # tmp_int = list(obj.map_dict.keys())[list(obj.map_dict.values()).index(obj.value)]
                tmp_int = 0
                for key, val in obj.map_dict.items():
                    if obj.value == val:
                        tmp_int = int(key)
                        break
                obj.value = tmp_int
            tmp = int.to_bytes(int(obj.value), length=obj.nbytes, byteorder=endianess, signed=obj.signed)
            bsgy[obj.startbyte - 1:obj.startbyte + obj.nbytes - 1] = tmp
        return bytes(bsgy)