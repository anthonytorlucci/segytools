'''
segy file header aka binary header
'''

# import python standard modules


# import 3rd party libraries


# import local python
from segytools.datatypes import DataSampleFormat, \
    DATA_SAMPLE_FORMAT_INT16, DATA_SAMPLE_FORMAT_INT32
from segytools.segy_header_item import SegyHeaderItem
from segytools.segy_abstract_header import SegyAbstractHeader


# --- Mappings
# bytes 25-26
DATA_SAMPLE_FORMAT_CODE = {
    0: 'undefined',
    1: 'ibm',
    2: 'int32',
    3: 'int16',
    5: 'float32',
    8: 'int8'
}

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
    0: 'undefined',
    1: 'linear',
    2: 'parabolic',
    3: 'exponential',
    4: 'other'
}

# bytes 47-48
TAPER_TYPE = {
    0: 'undefined',
    1: 'linear',
    2: 'cos**2',
    3: 'other'
}

# bytes 49-50
CORRELATED_DATA_TRACES = {
    0: 'undefined',
    1: 'no',
    2: 'yes'
}

# bytes 51-52
BINARY_GAIN_RECOVERED = {
    0: 'undefined',
    1: 'yes',
    2: 'no'
}

# bytes 53-54
AMPLITUDE_RECOVERY_METHOD = {
    0: 'undefined',
    1: 'none',
    2: 'spherical divergence',
    3: 'agc',
    4: 'other'
}

# bytes 55-56
MEASUREMENT_SYSTEM = {
    0: 'undefined',
    1: 'meters',
    2: 'feet'
}

# bytes 57-58
IMPULSE_SIGNAL_POLARITY = {
    0: 'undefined',
    1: 'incerase in pressure or upward geophone case movement gives negative number on tape',
    2: 'incerase in pressure or upward geophone case movement gives positive number on tape'
}

# bytes 59-60
VIBRATORY_POLARITY_CODE = {
    0: 'undefined',
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

    Parameters
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
    """

    def __init__(self):
        super().__init__()
        self.byte_length = 400
        self.jobid = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32, 
            start_byte=1,
            description='job identification number')
        self.lineno = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32, 
            start_byte=5,
            description='line number')
        self.reelno = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32, 
            start_byte=9,
            description='reel number')
        self.ntrcens = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16, 
            start_byte=13,
            description='number of data traces per ensemble')
        self.ntrcaux = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16, 
            start_byte=15,
            description='number of auxiliary traces per ensemble')
        self.smpint = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16, 
            start_byte=17,
            description='sample interval in microseconds')
        self.smpinto = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16, 
            start_byte=19,
            description='sample interval in microseconds or original recording')
        self.numsmp = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16, 
            start_byte=21,
            description='number of samples per data trace')
        self.numsmpo = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16, 
            start_byte=23,
            description='number of samples per data trace or original recording')
        self.dsfmt = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16, 
            start_byte=25,
            description='data sample format code',
            map_dict=DATA_SAMPLE_FORMAT_CODE)
        self.fold = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16, 
            start_byte=27,
            description='ensemble fold')
        self.sortcode = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16, 
            start_byte=29,
            description='trace sorting code',
            map_dict=TRACE_SORTING_CODE)
        self.vsumcode = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16, 
            start_byte=31,
            description='vertical sum code')
        self.sweepfs = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16, 
            start_byte=33,
            description='sweep_frequency_at_start')
        self.sweepfe = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16, 
            start_byte=35,
            description='sweep_frequency_at_end')
        self.sweeplen = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16, 
            start_byte=37,
            description='sweep_length')
        self.sweepcode = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16, 
            start_byte=39,
            description='sweep_type_code',
            map_dict=SWEEP_TYPE_CODE)
        self.sweepchan = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16, 
            start_byte=41,
            description='trace_number_of_sweep_channel')
        self.sweeptprs = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16, 
            start_byte=43,
            description='sweep_trace_taper_length_in_ms_at_start')
        self.sweeptpre = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16, 
            start_byte=45,
            description='sweep_trace_taper_length_in_ms_at_end')
        self.tprtype = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16, 
            start_byte=47,
            description='taper_type',
            map_dict=TAPER_TYPE)
        self.corrtrc = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16, 
            start_byte=49,
            description='correlated_data_traces',
            map_dict=CORRELATED_DATA_TRACES)
        self.bingain = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16, 
            start_byte=51,
            description='binary_gain_recovered',
            map_dict=BINARY_GAIN_RECOVERED)
        self.amprec = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16, 
            start_byte=53,
            description='amplitude_recovery_method',
            map_dict=AMPLITUDE_RECOVERY_METHOD)
        self.meassys = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16, 
            start_byte=55,
            description='measurement_system',
            map_dict=MEASUREMENT_SYSTEM)
        self.polarity = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16, 
            start_byte=57,
            description='impulse_signal_polarity',
            map_dict=IMPULSE_SIGNAL_POLARITY)
        self.vpolarity = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,
            start_byte=59,
            description='vibratory_polarity_code',
            map_dict=VIBRATORY_POLARITY_CODE)
        # unassigned
        self.segyrev = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16, 
            start_byte=301,
            description='seg_y_format_revision_number',
            value=2)
        self.fixedlen = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16, 
            start_byte=303,
            description='fixed_length_trace_flag')
        self.ntxthead = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16, 
            start_byte=305,
            description='number_of_3200_byte_ext_file_header_records_following')
        # unassigned

    # --- METHODS ---
    def segy_type(self):
        """Return the segy type, e.g. 'ibm', 'int32', 'int16'.
        """
        return self.dsfmt.mapped_value

    # TODO: def is_fixed_length(self):
    #     if self.fixedlen == ??:
    #         return True
    #     else:
    #         return False
