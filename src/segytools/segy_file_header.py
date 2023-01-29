'''
segy file header aka binary header
'''

# import python standard modules

# import 3rd party libraries

# import local python
from segytools.datatypes import (DATA_SAMPLE_FORMAT_INT16,
                                 DATA_SAMPLE_FORMAT_INT32)
from segytools.segy_abstract_header import SegyAbstractHeader
from segytools.segy_header_item import SegyHeaderItem

# --- Mappings
# bytes 25-26
DATA_SAMPLE_FORMAT_CODE = {
    0: "undefined",
    1: "ibm",
    2: "int32",
    3: "int16",
    5: "float32",
    8: "int8",
}

# bytes 29-30
TRACE_SORTING_CODE = {
    -1: "Other",
    0: "Unknown",
    1: "As Recorded (no sorting)",
    2: "CDP Ensemble",
    3: "Single fold continuous profile",
    4: "Horizontally stacked",
    5: "Common source point",
    6: "Common receiver point",
    7: "Common offset point",
    8: "Common mid-point",
    9: "Common Conversion point",
}

# bytes 39-40
SWEEP_TYPE_CODE = {
    0: "undefined",
    1: "linear",
    2: "parabolic",
    3: "exponential",
    4: "other",
}

# bytes 47-48
TAPER_TYPE = {
    0: "undefined",
    1: "linear",
    2: "cos**2",
    3: "other",
}

# bytes 49-50
CORRELATED_DATA_TRACES = {
    0: "undefined",
    1: "no",
    2: "yes",
}

# bytes 51-52
BINARY_GAIN_RECOVERED = {
    0: "undefined",
    1: "yes",
    2: "no",
}

# bytes 53-54
AMPLITUDE_RECOVERY_METHOD = {
    0: "undefined",
    1: "none",
    2: "spherical divergence",
    3: "agc",
    4: "other",
}

# bytes 55-56
MEASUREMENT_SYSTEM = {
    0: "undefined",
    1: "meters",
    2: "feet",
}

# bytes 57-58
IMPULSE_SIGNAL_POLARITY = {
    0: "undefined",
    1: "incerase in pressure or upward geophone case movement gives negative \
        number on tape",
    2: "incerase in pressure or upward geophone case movement gives positive \
        number on tape",
}

# bytes 59-60
VIBRATORY_POLARITY_CODE = {
    0: "undefined",
    1: "337.5 (deg) to 22.5 (deg)",
    2: "22.5 (deg) to 67.5 (deg)",
    3: "67.5 (deg) to 112.5 (deg)",
    4: "112.5 (deg) to 157.5 (deg)",
    5: "157.5 (deg) to 202.5 (deg)",
    6: "202.5 (deg) to 247.5 (deg)",
    7: "247.5 (deg) to 292.5 (deg)",
    8: "292.5 (deg) to 337.5 (deg)",
}


class SegyFileHeaderRev2(SegyAbstractHeader):
    """File or binary header definition of a segy file.

    Parameters
    ----------
    jobid : SegyHeaderItem
        job identification number
    line_number : SegyHeaderItem
        line number
    reel_number : SegyHeaderItem
        reel number
    num_traces_per_ensemble : SegyHeaderItem
        number of data traces per ensemble
    num_aux_traces_per_ensemble : SegyHeaderItem
        number of auxiliary traces per ensemble
    sample_interval : SegyHeaderItem
        sample interval in microseconds
    original_sample_interval : SegyHeaderItem
        sample interval in microseconds or original recording
    num_samples_per_trace : SegyHeaderItem
        number of samples per data trace
    original_num_samples_per_trace : SegyHeaderItem
        number of samples per data trace or original recording
    data_sample_format_code : SegyHeaderItem
        data sample format code
    fold : SegyHeaderItem
        ensemble fold
    sort_code : SegyHeaderItem
        trace sorting code
    vertical_sum_code : SegyHeaderItem
        vertical sum code
    sweep_freq_start : SegyHeaderItem
        sweep frequency at start
    sweep_freq_end : SegyHeaderItem
        sweep frequency at end
    sweep_length : SegyHeaderItem
        sweep length
    sweep_code : SegyHeaderItem
        sweep type code
    sweep_chan : SegyHeaderItem
        trace_number of sweep channel
    sweep_taper_length_start : SegyHeaderItem
        sweep_trace taper length in ms at start
    sweep_taper_length_end : SegyHeaderItem
        sweep trace taper length in ms at end
    taper_type : SegyHeaderItem
        taper type
    correlated_traces : SegyHeaderItem
        correlated data traces
    binary_gain : SegyHeaderItem
        binary gain recovered
    amp_recovery_method : SegyHeaderItem
        amplitude recovery method
    measurement_system : SegyHeaderItem
        measurement system
    polarity : SegyHeaderItem
        impulse signal polarity
    vibe_polarity : SegyHeaderItem
        vibratory polarity code
    segy_revision : SegyHeaderItem
        seg y format revision number
    fixed_length : SegyHeaderItem
        fixed length trace flag
    num_txt_headers : SegyHeaderItem
        number of 3200 byte ext file header records following
    """

    def __init__(self):
        super().__init__()
        self.byte_length = 400
        self.jobid = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,
            start_byte=1,
            description="job identification number",
        )
        self.line_number = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,
            start_byte=5,
            description="line number",
        )
        self.reel_number = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,
            start_byte=9,
            description="reel number",
        )
        self.num_traces_per_ensemble = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,
            start_byte=13,
            description="number of data traces per ensemble",
        )
        self.num_aux_traces_per_ensemble = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,
            start_byte=15,
            description="number of auxiliary traces per ensemble",
        )
        self.sample_interval = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,
            start_byte=17,
            description="sample interval in microseconds",
        )
        self.original_sample_interval = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,
            start_byte=19,
            description="sample interval in microseconds or original \
                recording",
        )
        self.num_samples_per_trace = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,
            start_byte=21,
            description="number of samples per data trace",
        )
        self.original_num_samples_per_trace = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,
            start_byte=23,
            description="number of samples per data trace or original \
                recording",
        )
        self.data_sample_format_code = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,
            start_byte=25,
            description="data sample format code",
            map_dict=DATA_SAMPLE_FORMAT_CODE,
        )
        self.fold = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,
            start_byte=27,
            description="ensemble fold",
        )
        self.sort_code = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,
            start_byte=29,
            description="trace sorting code",
            map_dict=TRACE_SORTING_CODE,
        )
        self.vertical_sum_code = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,
            start_byte=31,
            description="vertical sum code",
        )
        self.sweep_freq_start = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,
            start_byte=33,
            description="sweep frequency at start",
        )
        self.sweep_freq_end = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,
            start_byte=35,
            description="sweep frequency at end",
        )
        self.sweep_length = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,
            start_byte=37,
            description="sweep length",
        )
        self.sweep_code = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,
            start_byte=39,
            description="sweep type code",
            map_dict=SWEEP_TYPE_CODE,
        )
        self.sweep_chan = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,
            start_byte=41,
            description="trace number of sweep channel",
        )
        self.sweep_taper_length_start = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,
            start_byte=43,
            description="sweep trace taper length in ms at start",
        )
        self.sweep_taper_length_end = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,
            start_byte=45,
            description="sweep trace taper length in ms at end",
        )
        self.taper_type = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,
            start_byte=47,
            description="taper type",
            map_dict=TAPER_TYPE,
        )
        self.correlated_traces = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,
            start_byte=49,
            description="correlated data traces",
            map_dict=CORRELATED_DATA_TRACES,
        )
        self.binary_gain = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,
            start_byte=51,
            description="binary gain recovered",
            map_dict=BINARY_GAIN_RECOVERED,
        )
        self.amp_recovery_method = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,
            start_byte=53,
            description="amplitude recovery method",
            map_dict=AMPLITUDE_RECOVERY_METHOD,
        )
        self.measurement_system = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,
            start_byte=55,
            description="measurement system",
            map_dict=MEASUREMENT_SYSTEM,
        )
        self.polarity = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,
            start_byte=57,
            description="impulse signal polarity",
            map_dict=IMPULSE_SIGNAL_POLARITY,
        )
        self.vibe_polarity = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,
            start_byte=59,
            description="vibratory polarity code",
            map_dict=VIBRATORY_POLARITY_CODE,
        )
        # unassigned
        self.segy_revision = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,
            start_byte=301,
            description="segy format revision number",
            value=2,
        )
        self.fixed_length = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,
            start_byte=303,
            description="fixed length trace flag",
        )
        self.num_txt_headers = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,
            start_byte=305,
            description="number of 3200 byte ext file header \
                records following",
        )
        # unassigned

    # --- METHODS ---
    def segy_type(self) -> str:
        """Return the segy type, e.g. 'ibm', 'int32', 'int16', 'float32', or \
            'int8'.
        """
        return self.data_sample_format_code._mapped_value

    def sample_format_size_in_bytes(self) -> int:
        """Return the number of bytes in each sample based on the \
            `data_sample_format_code`.
        """
        fmt = self.data_sample_format_code._mapped_value
        byte_size = 4  # default
        if fmt == "ibm":
            byte_size = 4
        elif fmt == "float32":
            byte_size = 4
        elif fmt == "int32":
            byte_size = 4
        elif fmt == "int16":
            byte_size = 2
        elif fmt == "int8":
            byte_size = 1
        else:
            raise ValueError(
                "Unable to determine sample format size in bytes \
                as sample format is undefined."
            )
        return byte_size

    # TODO: def is_fixed_length(self):
    #     if self.fixedlen == ??:
    #         return True
    #     else:
    #         return False
