"""segy trace header"""

# import python standard modules

# import 3rd party libraries

# import local python
from segytools.datatypes import (DATA_SAMPLE_FORMAT_INT16,
                                 DATA_SAMPLE_FORMAT_INT32)
from segytools.segy_abstract_header import SegyAbstractHeader
from segytools.segy_header_item import SegyHeaderItem

# --- Mappings
# bytes 29-30
TRACE_IDENTIFICATION_CODE = {
    -1: "Other",
    0: "Unknown",
    1: "Seismic Data",
    2: "Dead",
    3: "Dummy",
    4: "Time break",
    5: "Uphole",
    6: "Sweep",
    7: "Timing",
    8: "Waterbreak",
    9: "Near-field gun signature",
    10: "Far-field gun signature",
    11: "Seismic pressure sensor",
    12: "Multi-component seismic sensor - Vertical component",
    13: "Multi-component seismic sensor - Cross-line component",
    14: "Multi-component seismic sensor - In-line component",
    15: "Rotated multi-component seismic sensor - Vertical component",
    16: "Rotated multi-component seismic sensor - Transverse component",
    17: "Rotated multi-component seismic sensor - Radial component",
    18: "Vibrator reaction mass",
    19: "Vibrator baseplate",
    20: "Vibrator estimated ground force",
    21: "Vibrator reference",
    22: "Time-Velocity Pairs",
}

# bytes 35-36
DATA_USE = {
    1: "Production",
    2: "Test",
}

# bytes 69-70 and 71-72
COORDINATE_SCALAR_MULTIPLIER = {
    -10000: 0.0001,
    -1000: 0.001,
    -100: 0.01,
    -10: 0.1,
    -1: 1,
    1: 1,
    10: 10,
    100: 100,
    1000: 1000,
    10000: 10000,
}

# bytes 89-90
COORDINATE_UNITS = {
    1: "Length (meters or feet)",
    2: "Seconds or arc",
    3: "Decimal degrees",
    4: "Degrees, minutes, seconds (DMS)",
}
# TODO: properly handle anything other than length; most routines are based on
# Cartesian system

# bytes 119-120
GAIN_TYPE_OF_FIELD_INSTRUMENTS = {
    1: "fixed",
    2: "binary",
    3: "floating point",
    4: "optional use",
}

# bytes 125-126
CORRELATED = {
    1: "yes",
    2: "no",
}

# bytes 133-134
SWEEP_TYPE = {
    1: "linear",
    2: "parabolic",
    3: "exponential",
    4: "other",
}

# bytes 139-140
TAPER_TYPE = {
    1: "linear",
    2: "cos**2",
    3: "other",
}

# bytes 167-168
TIME_BASIS_CODE = {
    1: "Local",
    2: "GMT (Greenwich Mean Time)",
    3: "Other",
    4: "UTC (Coordinated Universal Time)",
}

# bytes 179-180
OVER_TRAVEL_ASSOCIATED_TAPER_AT_BEGINNING_OR_END_OF_LINE = {
    1: "down (or behind)",
    2: "up (or ahead)",
}

# bytes 203-204
TRACE_VALUE_MEASUREMENT_UNIT = {
    -1: "Other",
    0: "Unknown",
    1: "Pascal (Pa)",
    2: "Volts (v)",
    3: "Millivolts (mV)",
    4: "Amperes (A)",
    5: "Meters (m)",
    6: "Meters per second (m/s)",
    7: "Meters per second squared (m/(s**2))",
    8: "Newton (N)",
    9: "Watt (W)",
}

# bytes 211-212
TRANSDUCTION_UNITS = {
    -1: "Other",
    0: "Unknown",
    1: "Pascal (Pa)",
    2: "Volts (v)",
    3: "Millivolts (mV)",
    4: "Amperes (A)",
    5: "Meters (m)",
    6: "Meters per second (m/s)",
    7: "Meters per second squared (m/(s**2))",
    8: "Newton (N)",
    9: "Watt (W)",
}

# bytes 217-218
SOURCE_TYPE_ORIENTATION = {
    -1: "Other",
    0: "Unknown",
    1: "Vibratory - Vertical orientation",
    2: "Vibratory - Cross-line orientation",
    3: "Vibratory - In-line-orientation",
    4: "Impulsive - Vertical orientation",
    5: "Impulsive - Cross-line orientation",
    6: "Impulsive - In-line-orientation",
    7: "Distributed Impulsive - Vertical orientation",
    8: "Distributed Impulsive - Cross-line orientation",
    9: "Distributed Impulsive - In-line-orientation",
}

# bytes 231-232
SOURCE_MEASUREMENT_UNIT = {
    -1: "Other",
    0: "Unknown",
    1: "Joule (J)",
    2: "Kilowatt (kW)",
    3: "Pascal (P)",
    4: "Bar (Bar)",
    5: "Newton (N)",
    6: "Kilograms (kg)",
}


class SegyTraceHeaderRev2(SegyAbstractHeader):
    """Segy Trace Header container based on segy format revision 2.

    Parameters
    ----------
    trc_seq_num_within_line : SegyHeaderItem
        Trace sequence number within line.
    trc_seq_num_within_file : SegyHeaderItem
        Trace sequence number within segy file.
    field_record_number : SegyHeaderItem
        Original field record number.
    trc_num_within_field_record : SegyHeaderItem
        Trace number within the original field record.
    energy_src_num : SegyHeaderItem
        Energy source point number.
    ensemble_number : SegyHeaderItem
        Ensemble number.
    trc_num_within_ensemble : SegyHeaderItem
        Trace number within ensemble.
    trc_identification_code : SegyHeaderItem
        Trace identification code. See TRACE_IDENTIFICATION_CODE for mapping.
    num_vert_summed_traces : SegyHeaderItem
        Number of vertically stacked traces yielding this trace.
    num_horz_summed_traces : SegyHeaderItem
        Number of horizontally stacked traces yielding this trace.
    data_use : SegyHeaderItem
        Data use. See DATA_USE for mapping.
    offset : SegyHeaderItem
        Distance from center of the source point to the center of the receiver
        group.
    rcv_elevation : SegyHeaderItem
        Receiver group elevation.
    src_elevation : SegyHeaderItem
        Surface elevation at source.
    src_depth : SegyHeaderItem
        Source depth below surface.
    rcv_datum_elevation : SegyHeaderItem
        Datum elevation at receiver group.
    src_datum_elevation : SegyHeaderItem
        Datum elevation at source.
    src_water_depth : SegyHeaderItem
        Water depth at source.
    rcv_water_depth : SegyHeaderItem
        Water depth at group.
    z_scalar : SegyHeaderItem
        Scalar to be applied to all elevations and depths.
    xy_scalar : SegyHeaderItem
        Scalar to be applied to all coordinates.
    src_x_coord : SegyHeaderItem
        Source coordinate x.
    src_y_coord : SegyHeaderItem
        Source coordinate y.
    rcv_x_coord : SegyHeaderItem
        Group coordinate x.
    rcv_y_coord : SegyHeaderItem
        Group coordinate y.
    coord_units : SegyHeaderItem
        Coordinate units. See COORDINATE_UNITS for mapping.
    weathering_velocity : SegyHeaderItem
        Weathering velocity.
    subweathering_velocity : SegyHeaderItem
        Subweathering velocity.
    src_uphole_time : SegyHeaderItem
        Uphole time at source in ms.
    rcv_uphole_time : SegyHeaderItem
        Uphole time at group in ms.
    src_static_correction : SegyHeaderItem
        Source static correction in ms.
    rcv_static_correction : SegyHeaderItem
        Group static correction in ms.
    total_static_applied : SegyHeaderItem
        Total static applied in ms.
    lag_time_A : SegyHeaderItem
        Lag time B.
    lag_time_B : SegyHeaderItem
        Lag time A.
    delay_recording_time : SegyHeaderItem
        Delay recording time.
    mute_start_time : SegyHeaderItem
        Mute time start time in ms.
    mute_end_time : SegyHeaderItem
        Mute time end time in ms.
    num_samples : SegyHeaderItem
        Number of samples in this trace.
    sample_interval : SegyHeaderItem
        Sample interval in ms for this trace.
    gain_type : SegyHeaderItem
        Gain type of field instruments.
    gain_const : SegyHeaderItem
        Instrument gain constant.
    initial_gain : SegyHeaderItem
        Instrument early or initial gain.
    correlated : SegyHeaderItem
        Whether the trace is correlated or not. See CORRELATED for mapping.
    sweep_freq_start : SegyHeaderItem
        Sweep frequency at start.
    sweep_freq_end : SegyHeaderItem
        Sweep frequency at end.
    sweep_length : SegyHeaderItem
        Sweep length.
    sweep_type : SegyHeaderItem
        Sweep type. See SWEEP_TYPE for mapping.
    sweep_taper_length_start : SegyHeaderItem
        Sweep taper length at start.
    sweep_taper_length_end : SegyHeaderItem
        Sweep taper length at end.
    taper_type : SegyHeaderItem
        Taper type. See TAPER_TYPE for mapping.
    alias_filter_freq : SegyHeaderItem
        Alias filter frequency.
    alias_filter_slope : SegyHeaderItem
        Alias filter slope.
    notch_filter_freq : SegyHeaderItem
        Notch filter frequency.
    notch_filter_slope : SegyHeaderItem
        Notch filter slope.
    low_cut_freq : SegyHeaderItem
        Low cut frequency.
    high_cut_freq : SegyHeaderItem
        High cut frequency.
    low_cut_slope : SegyHeaderItem
        Loow cut slope.
    high_cut_slope : SegyHeaderItem
        High cut slope.
    year : SegyHeaderItem
        Year data recorded.
    day : SegyHeaderItem
        Day of year.
    hour : SegyHeaderItem
        Hour of day.
    minute : SegyHeaderItem
        Minute of hour.
    second : SegyHeaderItem
        Second of minute.
    time_basis : SegyHeaderItem
        Time basis code. See TIME_BASIS_CODE for mapping.
    trc_weight : SegyHeaderItem
        Trace weighting factor.
    group_num : SegyHeaderItem
        Geophone group number of roll switch position one.
    first_group_num : SegyHeaderItem
        Geophone group number of trace number one.
    last_group_num : SegyHeaderItem
        Geophone group number of last trace.
    gap_size : SegyHeaderItem
        Gap size.
    over_travel : SegyHeaderItem
        Over travel associated with taper. See
        OVER_TRAVEL_ASSOCIATED_TAPER_AT_BEGINNING_OR_END_OF_LINE for mapping.
    ens_x_coord : SegyHeaderItem
        X coordinate of ensemble position of this trace.
    ens_y_coord : SegyHeaderItem
        Y coordinate of ensemble position of this trace.
    in_line : SegyHeaderItem
        For 3D poststack data this field is for in line number.
    cross_line : SegyHeaderItem
        For 3D poststack data this field is for cross line number.
    shotpoint : SegyHeaderItem
        Shotpoint number.
    shotpoint_scalar : SegyHeaderItem
        Scalar to be applied to the shotpoint number.
    trc_value_measurement_unit : SegyHeaderItem
        Trace value measurement unit. See TRACE_VALUE_MEASUREMENT_UNIT for
        mapping.
    transduction_constant_mantissa : SegyHeaderItem
        Transduction constant mantissa.
    transduction_constant_exponent : SegyHeaderItem
        Transduction constant exponent.
    transduction_units : SegyHeaderItem
        Transduction_units.
    device_identifier : SegyHeaderItem
        Device trace identifier.
    time_scalar : SegyHeaderItem
        Scalar to be applied to times.
    source_type_orientation : SegyHeaderItem
        Source type orientation. See SOURCE_TYPE_ORIENTATION for mapping.
    source_energy_direction_mantissa : SegyHeaderItem
        Source energy direction mantissa.
    source_energy_direction_exponent : SegyHeaderItem
        Source energy direction exponent.
    source_measurement_mantissa : SegyHeaderItem
        Source measurement mantissa.
    source_measurement_exponent : SegyHeaderItem
        Source measurement exponent.
    source_measurement_unit : SegyHeaderItem
        Source measurement unit. See SOURCE_MEASUREMENT_UNIT for mapping.
    undefined233 : SegyHeaderItem
        Undefined.
    undefined237 : SegyHeaderItem
        Undefined.
    """

    def __init__(self):
        super().__init__()
        self.byte_length = 240

        # HEADERS
        self.trc_seq_num_within_line = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,  # nbytes=4,
            start_byte=1,
            description="trace sequence number within line",
        )
        self.trc_seq_num_within_file = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,  # nbytes=4,
            start_byte=5,
            description="trace sequence number within segy file",
        )
        self.field_record_number = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,  # nbytes=4,
            start_byte=9,
            description="original field record number",
        )
        self.trc_num_within_field_record = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,  # nbytes=4,
            start_byte=13,
            description="trace number within the original field record",
        )
        self.energy_src_num = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,  # nbytes=4,
            start_byte=17,
            description="energy source point number",
        )
        self.ensemble_number = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,  # nbytes=4,
            start_byte=21,
            description="ensemble number",
        )
        self.trc_num_within_ensemble = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,  # nbytes=4,
            start_byte=25,
            description="trace number within the ensemble",
        )
        self.trc_identification_code = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=29,
            description="trace identification code",
            map_dict=TRACE_IDENTIFICATION_CODE,
        )
        self.num_vert_summed_traces = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=31,
            description="number of vertically summed traces yielding this \
                trace",
        )
        self.num_horz_summed_traces = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=33,
            description="number of horizontally stacked traces yielding this \
                trace",
        )
        self.data_use = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=35,
            description="data use",
            map_dict=DATA_USE,
            value=1,
        )
        self.offset = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,  # nbytes=4,
            start_byte=37,
            description="distance from center of the source point to the \
                center of the receiver group",
        )
        self.rcv_elevation = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,  # nbytes=4,
            start_byte=41,
            description="receiver group elevation",
        )
        self.src_elevation = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,  # nbytes=4,
            start_byte=45,
            description="surface elevation at source",
        )
        self.src_depth = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,  # nbytes=4,
            start_byte=49,
            description="source depth below surface",
        )
        self.rcv_datum_elevation = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,  # nbytes=4,
            start_byte=53,
            description="datum elevation at receiver group",
        )
        self.src_datum_elevation = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,  # nbytes=4,
            start_byte=57,
            description="datum elevation at source",
        )
        self.src_water_depth = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,  # nbytes=4,
            start_byte=61,
            description="water depth at source",
        )
        self.rcv_water_depth = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,  # nbytes=4,
            start_byte=65,
            description="water depth at group",
        )
        self.z_scalar = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=69,
            description="scalar to be applied to all elevations and depths",
            map_dict=COORDINATE_SCALAR_MULTIPLIER,
            value=1,
        )
        self.xy_scalar = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=71,
            description="scalar to be applied to all coordinates",
            map_dict=COORDINATE_SCALAR_MULTIPLIER,
            value=1,
        )
        self.src_x_coord = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,  # nbytes=4,
            start_byte=73,
            description="source coordinate x",
        )
        self.src_y_coord = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,  # nbytes=4,
            start_byte=77,
            description="source coordinate y",
        )
        self.rcv_x_coord = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,  # nbytes=4,
            start_byte=81,
            description="group coordinate x",
        )
        self.rcv_y_coord = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,  # nbytes=4,
            start_byte=85,
            description="group coordinate y",
        )
        self.coord_units = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=89,
            description="coordinate units",
            map_dict=COORDINATE_UNITS,
            value=1,
        )
        self.weathering_velocity = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=91,
            description="weathering velocity",
        )
        self.subweathering_velocity = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=93,
            description="subweathering velocity",
        )
        self.src_uphole_time = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=95,
            description="uphole time at source in ms",
        )
        self.rcv_uphole_time = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=97,
            description="uphole time at group in ms",
        )
        self.src_static_correction = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=99,
            description="source static correction in ms",
        )
        self.rcv_static_correction = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=101,
            description="group static correction in ms",
        )
        self.total_static_applied = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=103,
            description="total static applied in ms",
        )
        self.lag_time_A = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=105,
            description="lag time A",
        )
        self.lag_time_B = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=107,
            description="lag time B",
        )
        self.delay_recording_time = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=109,
            description="delay recording time",
        )
        self.mute_start_time = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=111,
            description="mute time start time in ms",
        )
        self.mute_end_time = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=113,
            description="mute time end time in ms",
        )
        self.num_samples = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=115,
            description="number of samples in this trace",
        )
        self.sample_interval = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=117,
            description="sample interval in ms for this trace",
        )
        self.gain_type = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=119,
            description="gain type of field instruments",
            map_dict=GAIN_TYPE_OF_FIELD_INSTRUMENTS,
            value=1,
        )
        self.gain_const = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=121,
            description="instrument gain constant",
        )
        self.initial_gain = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=123,
            description="instrument early or initial gain",
        )
        self.correlated = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=125,
            description="correlated",
            map_dict=CORRELATED,
            value=1,
        )
        self.sweep_freq_start = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=127,
            description="sweep frequency at start",
        )
        self.sweep_freq_end = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=129,
            description="sweep frequency at end",
        )
        self.sweep_length = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=131,
            description="sweep length in ms",
        )
        self.sweep_type = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=133,
            description="sweep type",
            map_dict=SWEEP_TYPE,
            value=1,
        )
        self.sweep_taper_length_start = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=135,
            description="sweep trace taper length at start in ms",
        )
        self.sweep_taper_length_end = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=137,
            description="sweep trace taper length at end in ms",
        )
        self.taper_type = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=139,
            description="taper type",
            map_dict=TAPER_TYPE,
            value=1,
        )
        self.alias_filter_freq = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=141,
            description="alias filter frequency",
        )
        self.alias_filter_slope = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=143,
            description="alias filter slope",
        )
        self.notch_filter_freq = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=145,
            description="notch filter frequency",
        )
        self.notch_filter_slope = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=147,
            description="notch filter slope",
        )
        self.low_cut_freq = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=149,
            description="low cut frequency",
        )
        self.high_cut_freq = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=151,
            description="high cut frequency",
        )
        self.low_cut_slope = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=153,
            description="low cut slope",
        )
        self.high_cut_slope = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=155,
            description="high cut_slope",
        )
        self.year = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=157,
            description="year data recorded",
        )
        self.day = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=159,
            description="day of year",
        )
        self.hour = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=161,
            description="hour of day",
        )
        self.minute = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=163,
            description="minute of hour",
        )
        self.second = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=165,
            description="second of minute",
        )
        self.time_basis = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=167,
            description="time basis code",
            map_dict=TIME_BASIS_CODE,
            value=1,
        )
        self.trc_weight = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=169,
            description="trace weighting factor",
        )
        self.group_num = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=171,
            description="geophone group number of roll switch position one",
        )
        self.first_group_num = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=173,
            description="geophone group number of trace number one",
        )
        self.last_group_num = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=175,
            description="geophone group number of last trace",
        )
        self.gap_size = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=177,
            description="gap size",
        )
        self.over_travel = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=179,
            description="over travel associated with taper",
            map_dict=OVER_TRAVEL_ASSOCIATED_TAPER_AT_BEGINNING_OR_END_OF_LINE,
            value=1,
        )
        self.ens_x_coord = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,  # nbytes=4,
            start_byte=181,
            description="x coordinate of ensemble position of this trace",
        )
        self.ens_y_coord = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,  # nbytes=4,
            start_byte=185,
            description="y coordinate of ensemble position of this trace",
        )
        self.in_line = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,  # nbytes=4,
            start_byte=189,
            description="for 3D poststack data this field is for in line \
                number",
        )
        self.cross_line = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,  # nbytes=4,
            start_byte=193,
            description="for 3D poststack data this field is for cross line \
                number",
        )
        self.shotpoint = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,  # nbytes=4,
            start_byte=197,
            description="shotpoint number",
        )
        self.shotpoint_scalar = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=201,
            description="scalar to be applied to the shotpoint number",
        )
        self.trc_value_measurement_unit = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=203,
            description="trace value measurement unit",
            map_dict=TRACE_VALUE_MEASUREMENT_UNIT,
        )
        # The transduction constant is encoded with the mantissa and the power
        # of the exponent, e.g.:
        # transduction_constant =
        # transduction_constant_mantissa * 10 ** transduction_constant_exponent
        self.transduction_constant_mantissa = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,  # nbytes=4,
            start_byte=205,
            description="transduction constant mantissa",
        )
        self.transduction_constant_exponent = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=209,
            description="transduction constant exponent",
        )
        self.transduction_units = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=211,
            description="transduction units",
            map_dict=TRANSDUCTION_UNITS,
        )
        self.device_identifier = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=213,
            description="device trace identifier",
        )
        self.time_scalar = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=215,
            description="scalar to be applied to times",
        )
        self.source_type_orientation = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=217,
            description="source type orientation",
            map_dict=SOURCE_TYPE_ORIENTATION,
        )
        self.source_energy_direction_mantissa = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,  # nbytes=4,
            start_byte=219,
            description="source energy direction mantissa",
        )
        self.source_energy_direction_exponent = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=223,
            description="source energy direction exponent",
        )
        # The source measurement is encoded with the mantissa and the power of
        # the exponent, e.g.:
        # source_measurement =
        # source_measurement_mantissa * 10 ** source_measurement_exponent
        self.source_measurement_mantissa = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,  # nbytes=4,
            start_byte=225,
            description="source measurement mantissa",
        )
        self.source_measurement_exponent = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=229,
            description="source measurement exponent",
        )
        self.source_measurement_unit = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT16,  # nbytes=2,
            start_byte=231,
            description="source measurement unit",
            map_dict=SOURCE_MEASUREMENT_UNIT,
        )
        self.undefined233 = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,  # nbytes=4,
            start_byte=233,
            description="undefined",
        )
        self.undefined237 = SegyHeaderItem(
            sample_format=DATA_SAMPLE_FORMAT_INT32,  # nbytes=4,
            start_byte=237,
            description="undefined",
        )
