'''
segy file header aka binary header
'''

# import python standard modules


# import 3rd party libraries


# import local python
from .segy_header_item import SegyHeaderItem
from .segy_abstract_header import SegyAbstractHeader
from .segpy.datatypes import DATA_SAMPLE_FORMAT_TO_SEG_Y_TYPE, SEG_Y_TYPE_TO_CTYPE, size_in_bytes


# bytes 29-30
TRACE_SORTING_CODE = {
    -1: 'Other',
    0: 'Unknown',
    1: 'As Recorded (no sorting)',
    2: 'CDP Ensemble',
    3: 'Single fold continuous profile',
    4: 'Horizontally stacked',
    5: 'Common source point',
    6: 'Common receiver point',
    7: 'Common offset point',
    8: 'Common mid-point',
    9: 'Common Conversion point'
}

# bytes 39-40
SWEEP_TYPE_CODE = {
    1: 'linear',
    2: 'parabolic',
    3: 'exponential',
    4: 'other'
}

# bytes 47-48
TAPER_TYPE = {
    1: 'linear',
    2: 'cos**2',
    3: 'other'
}

# bytes 49-50
CORRELATED_DATA_TRACES = {
    1: 'no',
    2: 'yes'
}

# bytes 51-52
BINARY_GAIN_RECOVERED = {
    1: 'yes',
    2: 'no'
}

# bytes 53-54
AMPLITUDE_RECOVERY_METHOD = {
    1: 'none',
    2: 'spherical divergence',
    3: 'agc',
    4: 'other'
}

# bytes 55-56
MEASUREMENT_SYSTEM = {
    1: 'meters',
    2: 'feet'
}

# bytes 57-58
IMPULSE_SIGNAL_POLARITY = {
    1: 'incerase in pressure or upward geophone case movement gives negative number on tape',
    2: 'incerase in pressure or upward geophone case movement gives positive number on tape'
}

# bytes 59-60
VIBRATORY_POLARITY_CODE = {
    1: '337.5 (deg) to 22.5 (deg)',
    2: '22.5 (deg) to 67.5 (deg)',
    3: '67.5 (deg) to 112.5 (deg)',
    4: '112.5 (deg) to 157.5 (deg)',
    5: '157.5 (deg) to 202.5 (deg)',
    6: '202.5 (deg) to 247.5 (deg)',
    7: '247.5 (deg) to 292.5 (deg)',
    8: '292.5 (deg) to 337.5 (deg)'
}


class SegyFileHeaderRev2(SegyAbstractHeader):
    """
    File or binary header definition of a segy file.

    Attributes
    ----------
    jobid : SegyHeaderItem
        job identification number
    lineno : SegyHeaderItem
        line number
    reelno : SegyHeaderItem
        reel number
    ntrcens : SegyHeaderItem
        number of data traces per ensemble
    ntrcaux : SegyHeaderItem
        number of auxiliary traces per ensemble
    smpint : SegyHeaderItem
        sample interval in microseconds
    smpinto : SegyHeaderItem
        sample interval in microseconds or original recording
    numsmp : SegyHeaderItem
        number of samples per data trace
    numsmpo : SegyHeaderItem
        number of samples per data trace or original recording
    dsfmt : SegyHeaderItem
        data sample format code
    fold : SegyHeaderItem
        ensemble fold
    sortcode : SegyHeaderItem
        trace sorting code
    vsumcode : SegyHeaderItem
        vertical sum code
    sweepfs : SegyHeaderItem
        sweep frequency at start
    sweepfe : SegyHeaderItem
        sweep frequency at end
    sweeplen : SegyHeaderItem
        sweep length
    sweepcode : SegyHeaderItem
        sweep type code
    sweepchan : SegyHeaderItem
        trace_number of sweep channel
    sweeptprs : SegyHeaderItem
        sweep_trace taper length in ms at start
    sweeptpre : SegyHeaderItem
        sweep trace taper length in ms at end
    tprtype : SegyHeaderItem
        taper type
    corrtrc : SegyHeaderItem
        correlated data traces
    bingain : SegyHeaderItem
        binary gain recovered
    amprec : SegyHeaderItem
        amplitude recovery method
    meassys : SegyHeaderItem
        measurement system
    polarity : SegyHeaderItem
        impulse signal polarity
    vpolarity : SegyHeaderItem
        vibratory polarity code
    segyrev : SegyHeaderItem
        seg y format revision number
    fixedlen : SegyHeaderItem
        fixed length trace flag
    ntxthead : SegyHeaderItem
        number of 3200 byte ext file header records following
            

    Methods
    -------
    segy_type
        Returns the value of the data sample format. Result is one of `ibm`, `int32`, `int16`, `float32`, or `int8`. (see segpy datatypes)
    ctype
        Returns the format character used by the python standard library. (see segpy datatypes).
    bytes_per_sample
        Returns the number of bytes for a given datatype.
    number_of_samples
        Returns the number of samples from the `numsmp` header item.
    to_bytes
        Converts the container class to a bytes object usually for exporting a new segy file.
    """

    def __init__(self):
        super().__init__()
        self.jobid = SegyHeaderItem(
            name='jobid', 
            nbytes=4, 
            startbyte=1,
            description='job identification number',
            signed=True)
        self.lineno = SegyHeaderItem(
            name='lineno', 
            nbytes=4, 
            startbyte=5,
            description='line number',
            signed=True)
        self.reelno = SegyHeaderItem(
            name='reelno', 
            nbytes=4, 
            startbyte=9,
            description='reel number',
            signed=True)
        self.ntrcens = SegyHeaderItem(
            name='ntrcens', 
            nbytes=2, 
            startbyte=13,
            description='number of data traces per ensemble',
            signed=True)
        self.ntrcaux = SegyHeaderItem(
            name='ntrcaux', 
            nbytes=2, 
            startbyte=15,
            description='number of auxiliary traces per ensemble',
            signed=True)
        self.smpint = SegyHeaderItem(
            name='smpint', 
            nbytes=2, 
            startbyte=17,
            description='sample interval in microseconds',
            signed=True)
        self.smpinto = SegyHeaderItem(
            name='smpinto', 
            nbytes=2, 
            startbyte=19,
            description='sample interval in microseconds or original recording',
            signed=True)
        self.numsmp = SegyHeaderItem(
            name='numsmp', 
            nbytes=2, 
            startbyte=21,
            description='number of samples per data trace',
            signed=True)
        self.numsmpo = SegyHeaderItem(
            name='numsmpo', 
            nbytes=2, 
            startbyte=23,
            description='number of samples per data trace or original recording',
            signed=True)
        self.dsfmt = SegyHeaderItem(
            name='dsfmt', 
            nbytes=2, 
            startbyte=25,
            description='data sample format code',
            signed=True,
            map_bool=True, 
            map_dict=DATA_SAMPLE_FORMAT_TO_SEG_Y_TYPE)
        self.fold = SegyHeaderItem(
            name='fold', 
            nbytes=2, 
            startbyte=27,
            description='ensemble fold',
            signed=True)
        self.sortcode = SegyHeaderItem(
            name='sortcode', 
            nbytes=2, 
            startbyte=29,
            description='trace sorting code',
            signed=True,
            map_bool=True, 
            map_dict=TRACE_SORTING_CODE)
        self.vsumcode = SegyHeaderItem(
            name='vsumcode', 
            nbytes=2, 
            startbyte=31,
            description='vertical sum code',
            signed=True)
        self.sweepfs = SegyHeaderItem(
            name='sweepfs', 
            nbytes=2, 
            startbyte=33,
            description='sweep_frequency_at_start',
            signed=True)
        self.sweepfe = SegyHeaderItem(
            name='sweepfe', 
            nbytes=2, 
            startbyte=35,
            description='sweep_frequency_at_end',
            signed=True)
        self.sweeplen = SegyHeaderItem(
            name='sweeplen', 
            nbytes=2, 
            startbyte=37,
            description='sweep_length',
            signed=True)
        self.sweepcode = SegyHeaderItem(
            name='sweepcode', 
            nbytes=2, 
            startbyte=39,
            description='sweep_type_code',
            signed=True,
            map_bool=True, 
            map_dict=SWEEP_TYPE_CODE)
        self.sweepchan = SegyHeaderItem(
            name='sweepchan', 
            nbytes=2, 
            startbyte=41,
            description='trace_number_of_sweep_channel',
            signed=True)
        self.sweeptprs = SegyHeaderItem(
            name='sweeptprs', 
            nbytes=2, 
            startbyte=43,
            description='sweep_trace_taper_length_in_ms_at_start',
            signed=True)
        self.sweeptpre = SegyHeaderItem(
            name='sweeptpre', 
            nbytes=2, 
            startbyte=45,
            description='sweep_trace_taper_length_in_ms_at_end',
            signed=True)
        self.tprtype = SegyHeaderItem(
            name='tprtype', 
            nbytes=2, 
            startbyte=47,
            description='taper_type',
            signed=True,
            map_bool=True, 
            map_dict=TAPER_TYPE)
        self.corrtrc = SegyHeaderItem(
            name='corrtrc', 
            nbytes=2, 
            startbyte=49,
            description='correlated_data_traces',
            signed=True,
            map_bool=True, 
            map_dict=CORRELATED_DATA_TRACES)
        self.bingain = SegyHeaderItem(
            name='bingain', 
            nbytes=2, 
            startbyte=51,
            description='binary_gain_recovered',
            signed=True,
            map_bool=True, 
            map_dict=BINARY_GAIN_RECOVERED)
        self.amprec = SegyHeaderItem(
            name='amprec', 
            nbytes=2, 
            startbyte=53,
            description='amplitude_recovery_method',
            signed=True,
            map_bool=True, 
            map_dict=AMPLITUDE_RECOVERY_METHOD)
        self.meassys = SegyHeaderItem(
            name='meassys', 
            nbytes=2, 
            startbyte=55,
            description='measurement_system',
            signed=True,
            map_bool=True, 
            map_dict=MEASUREMENT_SYSTEM)
        self.polarity = SegyHeaderItem(
            name='polarity', 
            nbytes=2, 
            startbyte=57,
            description='impulse_signal_polarity',
            signed=True,
            map_bool=True, 
            map_dict=IMPULSE_SIGNAL_POLARITY)
        self.vpolarity = SegyHeaderItem(
            name='vpolarity', 
            nbytes=2, 
            startbyte=59,
            description='vibratory_polarity_code',
            signed=True,
            map_bool=True, 
            map_dict=VIBRATORY_POLARITY_CODE)
        #self.unassigned1 = SegyAbstractHeader(240, 'unassigned_1', False, 3261)
        self.segyrev = SegyHeaderItem(
            name='segyrev', 
            nbytes=2, 
            startbyte=301,
            description='seg_y_format_revision_number',
            signed=True)
        self.fixedlen = SegyHeaderItem(
            name='fixedlen', 
            nbytes=2, 
            startbyte=303,
            description='fixed_length_trace_flag',
            signed=True)
        self.ntxthead = SegyHeaderItem(
            name='ntxthead', 
            nbytes=2, 
            startbyte=305,
            description='number_of_3200_byte_ext_file_header_records_following',
            signed=True)
        #self.unassigned2 = SegyAbstractHeader(94, 'unassigned_2', False, 3507)


    def __str__(self):
        s = 'segy file headers\n'
        s += str(self.jobid) + '\n'
        s += str(self.lineno) + '\n'
        s += str(self.reelno) + '\n'
        s += str(self.ntrcens) + '\n'
        s += str(self.ntrcaux) + '\n'
        s += str(self.smpint) + '\n'
        s += str(self.smpinto) + '\n'
        s += str(self.numsmp) + '\n'
        s += str(self.numsmpo) + '\n'
        s += str(self.dsfmt) + '\n'
        s += str(self.fold) + '\n'
        s += str(self.sortcode) + '\n'
        s += str(self.vsumcode) + '\n'
        s += str(self.sweepfs) + '\n'
        s += str(self.sweepfe) + '\n'
        s += str(self.sweeplen) + '\n'
        s += str(self.sweepcode) + '\n'
        s += str(self.sweepchan) + '\n'
        s += str(self.sweeptprs) + '\n'
        s += str(self.sweeptpre) + '\n'
        s += str(self.tprtype) + '\n'
        s += str(self.corrtrc) + '\n'
        s += str(self.bingain) + '\n'
        s += str(self.amprec) + '\n'
        s += str(self.meassys) + '\n'
        s += str(self.polarity) + '\n'
        s += str(self.vpolarity) + '\n'
        s += str(self.segyrev) + '\n'
        s += str(self.fixedlen) + '\n'
        s += str(self.ntxthead)
        return s

    # --- METHODS ---
    def segy_type(self):
        return self.dsfmt.value

    def ctype(self):
        return SEG_Y_TYPE_TO_CTYPE[self.segy_type()]

    def bytes_per_sample(self):
        return size_in_bytes(self.ctype())

    def number_of_samples(self):
        return self.numsmp.value


    # MUTATORS
    def set_file_header_values(self, bsgy, endianess):
        file_key_obj_dict = self.key_object_dict()
        for _, obj in file_key_obj_dict.items():
            bobj = bsgy[obj.startbyte - 1:obj.startbyte + obj.nbytes - 1]
            obj.value = int.from_bytes(bobj, byteorder=endianess, signed=obj.signed)

            # TODO: do not map by default. this will cause an error when converting back to bytes.
            if obj.map_bool is True:
                self.set_key_property(obj.name, 'value', self.mapped_value(obj.name))

    # def to_bytes(self, endianess, byte_length=400):
    #     bsgy = bytearray(byte_length)
    #     file_key_obj_dict = self.key_object_dict()
    #     for _, obj in file_key_obj_dict.items():
            
    #         if obj.map_bool is True:
    #             # reverse map back to integer
    #             # tmp_int = list(obj.map_dict.keys())[list(obj.map_dict.values()).index(obj.value)]
    #             tmp_int = 0
    #             for key, val in obj.map_dict.items():
    #                 if obj.value == val:
    #                     tmp_int = int(key)
    #                     break
    #             obj.value = tmp_int
    #         tmp = int.to_bytes(int(obj.value), length=obj.nbytes, byteorder=endianess, signed=obj.signed)
    #         bsgy[obj.startbyte - 1:obj.startbyte + obj.nbytes - 1] = tmp
    #     return bytes(bsgy)

    def to_bytes(self, endianess, byte_length=400):
        return self._to_bytes(endianess=endianess, byte_length=byte_length)

    # TODO: def is_fixed_length(self):
    #     if self.fixedlen == ??:
    #         return True
    #     else:
    #         return False
