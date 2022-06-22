'''
segy header item
'''

__author__ = 'Anthony Torlucci'
__version__ = '0.0.1'

# import python standard modules


# import 3rd party libraries


# import local python


class SegyHeaderItem(object):

    def __init__(self, name:str, nbytes=4, startbyte=0, description='', signed=False,
                 map_bool=False, map_dict={}, value=0):
        self.name = name
        self.nbytes = nbytes            # length of the header in bytes; default to 4, but may be 2
        self.startbyte = startbyte      # the relative byte location to start reading
        self.description = description  # defualt to empty string
        self.signed = signed            # a boolean; True is a signed twos complement integer, False is not signed
        self.value = value              # the value obtained from the segy file
        self.supplementary = ''         # any additional supplementary material
        self.map_bool = map_bool        # True if value is mapped to a dict; False otherwise
        self.map_dict = map_dict        # name of the dictionary to map to

    def __str__(self):
        s = 'name: ' + self.name + ', '
        s += 'description: ' + self.description + ', '
        s += 'start byte: ' + str(self.startbyte) + ', '
        s += 'byte length: ' + str(self.nbytes) + ', '
        s += 'value: ' + str(self.value)
        return s

    # ACCESSORS
    def field(self, field_id):
        if field_id == 'name':
            return self.name
        elif field_id == 'nbytes':
            return self.nbytes
        elif field_id == 'startbyte':
            return self.startbyte
        elif field_id == 'description':
            return self.description
        elif field_id == 'signed':
            return self.signed
        elif field_id == 'value':
            return self.value
        elif field_id == 'supplementary':
            return self.supplementary
        elif field_id == 'map_bool':
            return self.map_bool
        elif field_id == 'map_dict':
            return self.map_dict
        else:
            print('field not found')
            return None

    def header_name(self):
        return self.name

    def number_of_bytes(self):
        return self.nbytes

    def start_byte(self):
        return self.startbyte

    # def description(self):
    #     return self.description

    def is_signed(self):
        return self.signed

    # def value(self):
    #     return self.value

    # def supplementary(self):
    #     return self.supplementary

    # MUTATORS 
    def set_field(self, field, value):
        if field == 'name':
            self.name = value
        elif field == 'nbytes':
            self.nbytes = value
        elif field == 'startbyte':
            self.startbyte = value
        elif field == 'description':
            self.description = value
        elif field == 'signed':
            self.signed = value
        elif field == 'value':
            self.value = value
        elif field == 'supplementary':
            self.supplementary = value
        elif field == 'map_bool':
            self.map_bool = value
        elif field == 'map_dict':
            self.map_dict = value
        else:
            print('field not found')


    def set_name(self, name:str):
        self.name = name

    def set_number_of_bytes(self, nbytes:int):
        self.nbytes = nbytes

    def set_start_byte(self, startbyte:int):
        self.startbyte = startbyte

    def set_description(self, description:str):
        self.description = description

    def set_signed(self, signed:bool):
        self.signed = signed

    def set_value(self, value):
        self.value = value

    def set_supplementary_text(self, supplementary:str):
        self.supplementary = supplementary