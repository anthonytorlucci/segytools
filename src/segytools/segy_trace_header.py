'''
segy trace header
'''

# import python standard modules


# import 3rd party libraries


# import local python
from segytools.segy_abstract_header import SegyAbstractHeader
from segytools.segy_header_item import SegyHeaderItem


# bytes 29-30
TRACE_IDENTIFICATION_CODE = {
    -1: 'Other',
    0: 'Unknown',
    1: 'Seismic Data',
    2: 'Dead',
    3: 'Dummy',
    4: 'Time break',
    5: 'Uphole',
    6: 'Sweep',
    7: 'Timing',
    8: 'Waterbreak',
    9: 'Near-field gun signature',
    10: 'Far-field gun signature',
    11: 'Seismic pressure sensor',
    12: 'Multi-component seismic sensor - Vertical component',
    13: 'Multi-component seismic sensor - Cross-line component',
    14: 'Multi-component seismic sensor - In-line component',
    15: 'Rotated multi-component seismic sensor - Vertical component',
    16: 'Rotated multi-component seismic sensor - Transverse component',
    17: 'Rotated multi-component seismic sensor - Radial component',
    18: 'Vibrator reaction mass',
    19: 'Vibrator baseplate',
    20: 'Vibrator estimated ground force',
    21: 'Vibrator reference',
    22: 'Time-Velocity Pairs'
}

# bytes 35-36
DATA_USE = {
    1: 'Production',
    2: 'Test'
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
    10000: 10000
}

# bytes 89-90
COORDINATE_UNITS = {
    1: 'Length (meters or feet)',
    2: 'Seconds or arc',
    3: 'Decimal degrees',
    4: 'Degrees, minutes, seconds (DMS)'
}
# TODO: properly handle anything other than length; most routines are based on Cartesian system

# bytes 119-120
GAIN_TYPE_OF_FIELD_INSTRUMENTS = {
    1: 'fixed',
    2: 'binary',
    3: 'floating point',
    4: 'optional use'
}

# bytes 125-126
CORRELATED = {
    1: 'yes',
    2: 'no'
}

# bytes 133-134
SWEEP_TYPE = {
    1: 'linear',
    2: 'parabolic',
    3: 'exponential',
    4: 'other'
}

# bytes 139-140
TAPER_TYPE = {
    1: 'linear',
    2: 'cos**2',
    3: 'other'
}

# bytes 167-168
TIME_BASIS_CODE = {
    1: 'Local',
    2: 'GMT (Greenwich Mean Time)',
    3: 'Other',
    4: 'UTC (Coordinated Universal Time)'
}

# bytes 179-180
OVER_TRAVEL_ASSOCIATED_TAPER_AT_BEGINNING_OR_END_OF_LINE = {
    1: 'down (or behind)',
    2: 'up (or ahead)'
}

# bytes 203-204
TRACE_VALUE_MEASUREMENT_UNIT = {
    -1: 'Other',
    0: 'Unknown',
    1: 'Pascal (Pa)',
    2: 'Volts (v)',
    3: 'Millivolts (mV)',
    4: 'Amperes (A)',
    5: 'Meters (m)',
    6: 'Meters per second (m/s)',
    7: 'Meters per second squared (m/(s**2))',
    8: 'Newton (N)',
    9: 'Watt (W)'
}

# bytes 211-212
TRANSDUCTION_UNITS = {
    -1: 'Other',
    0: 'Unknown',
    1: 'Pascal (Pa)',
    2: 'Volts (v)',
    3: 'Millivolts (mV)',
    4: 'Amperes (A)',
    5: 'Meters (m)',
    6: 'Meters per second (m/s)',
    7: 'Meters per second squared (m/(s**2))',
    8: 'Newton (N)',
    9: 'Watt (W)'
}

# bytes 217-218
SOURCE_TYPE_ORIENTATION ={
    -1: 'Other',
    0: 'Unknown',
    1: 'Vibratory - Vertical orientation',
    2: 'Vibratory - Cross-line orientation',
    3: 'Vibratory - In-line-orientation',
    4: 'Impulsive - Vertical orientation',
    5: 'Impulsive - Cross-line orientation',
    6: 'Impulsive - In-line-orientation',
    7: 'Distributed Impulsive - Vertical orientation',
    8: 'Distributed Impulsive - Cross-line orientation',
    9: 'Distributed Impulsive - In-line-orientation',
}

# bytes 231-232
SOURCE_MEASUREMENT_UNIT = {
    -1 : 'Other',
    0: 'Unknown',
    1: 'Joule (J)',
    2: 'Kilowatt (kW)',
    3: 'Pascal (P)',
    4: 'Bar (Bar)',
    5: 'Newton (N)',
    6: 'Kilograms (kg)'
}

class SegyTraceHeaderRev2(SegyAbstractHeader):
    """Segy Trace Header container based on segy format revision 2"""

    def __init__(self):
        super().__init__()
        self.byte_length = 240

        # HEADERS
        self.trseql = SegyHeaderItem(
            name='trseql', 
            sample_format=DataSampleFormat.INT32, # nbytes=4, 
            start_byte=1,
            description='trace_sequence_number_within_line',
            is_signed=True)
        self.trseqf = SegyHeaderItem(
            name='trseqf', 
            sample_format=DataSampleFormat.INT32, # nbytes=4, 
            start_byte=5,
            description='trace_sequence_number_within_segy_file',
            is_signed=True)
        self.ffid = SegyHeaderItem(
            name='ffid', 
            sample_format=DataSampleFormat.INT32, # nbytes=4, 
            start_byte=9,
            description='original_field_record_number',
            is_signed=True)
        self.trffid = SegyHeaderItem(
            name='trffid', 
            sample_format=DataSampleFormat.INT32, # nbytes=4, 
            start_byte=13,
            description='trace_number_within_the_original_field_record',
            is_signed=True)
        self.shot = SegyHeaderItem(
            name='shot', 
            sample_format=DataSampleFormat.INT32, # nbytes=4, 
            start_byte=17,
            description='energy_source_point_number',
            is_signed=True)
        self.ens = SegyHeaderItem(
            name='ens', 
            sample_format=DataSampleFormat.INT32, # nbytes=4, 
            start_byte=21,
            description='ensemble_number',
            is_signed=True)
        self.trcens = SegyHeaderItem(
            name='trcens', 
            sample_format=DataSampleFormat.INT32, # nbytes=4, 
            start_byte=25,
            description='trace_number_within_the_ensemble',
            is_signed=True)
        self.trid = SegyHeaderItem(
            name='trid', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=29,
            description='trace_identification_code',
            is_signed=True,
            map_bool=True, 
            map_dict=TRACE_IDENTIFICATION_CODE)
        self.vsum = SegyHeaderItem(
            name='vsum', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=31,
            description='number_of_vertically_summed_traces_yielding_this_trace',
            is_signed=True)
        self.hsum = SegyHeaderItem(
            name='hsum', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=33,
            description='number_of_horizontally_stacked_traces_yielding_this_trace',
            is_signed=True)
        self.datuse = SegyHeaderItem(
            name='datuse', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=35,
            description='data_use',
            is_signed=True,
            map_bool=True, 
            map_dict=DATA_USE)
        self.offset = SegyHeaderItem(
            name='offset', 
            sample_format=DataSampleFormat.INT32, # nbytes=4, 
            start_byte=37,
            description='distance_from_center_of_the_source_point_to_the_center_of_the_receiver_group',
            is_signed=True)
        self.recelev = SegyHeaderItem(
            name='recelev', 
            sample_format=DataSampleFormat.INT32, # nbytes=4, 
            start_byte=41,
            description='receiver_group_elevation',
            is_signed=True)
        self.srcelev = SegyHeaderItem(
            name='srcelev', 
            sample_format=DataSampleFormat.INT32, # nbytes=4, 
            start_byte=45,
            description='surface_elevation_at_source',
            is_signed=True)
        self.srcdepth = SegyHeaderItem(
            name='srcdepth', 
            sample_format=DataSampleFormat.INT32, # nbytes=4, 
            start_byte=49,
            description='source_depth_below_surface',
            is_signed=True)
        self.datmrec = SegyHeaderItem(
            name='datmrec', 
            sample_format=DataSampleFormat.INT32, # nbytes=4, 
            start_byte=53,
            description='datum_elevation_at_receiver_group',
            is_signed=True)
        self.datmsrc = SegyHeaderItem(
            name='datmsrc', 
            sample_format=DataSampleFormat.INT32, # nbytes=4, 
            start_byte=57,
            description='datum_elevation_at_source',
            is_signed=True)
        self.h2ozsrc = SegyHeaderItem(
            name='h2ozsrc', 
            sample_format=DataSampleFormat.INT32, # nbytes=4, 
            start_byte=61,
            description='water_depth_at_source',
            is_signed=True)
        self.h2ozrec = SegyHeaderItem(
            name='h2ozrec', 
            sample_format=DataSampleFormat.INT32, # nbytes=4, 
            start_byte=65,
            description='water_depth_at_group',
            is_signed=True)
        self.zsclr = SegyHeaderItem(
            name='zsclr', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=69,
            description='scalar_to_be_applied_to_all_elevations_and_depths',
            is_signed=True,
            map_bool=True, 
            map_dict=COORDINATE_SCALAR_MULTIPLIER)
        self.xysclr = SegyHeaderItem(
            name='xysclr', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=71,
            description='scalar_to_be_applied_to_all_coordinates',
            is_signed=True,
            map_bool=True, 
            map_dict=COORDINATE_SCALAR_MULTIPLIER)
        self.srcx = SegyHeaderItem(
            name='srcx', 
            sample_format=DataSampleFormat.INT32, # nbytes=4, 
            start_byte=73,
            description='source_coordinate_x',
            is_signed=True)
        self.srcy = SegyHeaderItem(
            name='srcy', 
            sample_format=DataSampleFormat.INT32, # nbytes=4, 
            start_byte=77,
            description='source_coordinate_y',
            is_signed=True)
        self.recx = SegyHeaderItem(
            name='recx', 
            sample_format=DataSampleFormat.INT32, # nbytes=4, 
            start_byte=81,
            description='group_coordinate_x',
            is_signed=True)
        self.recy = SegyHeaderItem(
            name='recy', 
            sample_format=DataSampleFormat.INT32, # nbytes=4, 
            start_byte=85,
            description='group_coordinate_y',
            is_signed=True)
        self.coordunits = SegyHeaderItem(
            name='coordunits', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=89,
            description='coordinate_units',
            is_signed=True,
            map_bool=True, 
            map_dict=COORDINATE_UNITS)
        self.weathvel = SegyHeaderItem(
            name='weathvel', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=91,
            description='weathering_velocity',
            is_signed=True)
        self.subweathvel = SegyHeaderItem(
            name='subweathvel', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=93,
            description='subweathering_velocity',
            is_signed=True)
        self.uptsrc = SegyHeaderItem(
            name='uptsrc', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=95,
            description='uphole_time_at_source_in_ms',
            is_signed=True)
        self.uptrec = SegyHeaderItem(
            name='uptrec', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=97,
            description='uphole_time_at_group_in_ms',
            is_signed=True)
        self.srcstat = SegyHeaderItem(
            name='srcstat', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=99,
            description='source_static_correction_in_ms',
            is_signed=True)
        self.recstat = SegyHeaderItem(
            name='recstat', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=101,
            description='group_static_correction_in_ms',
            is_signed=True)
        self.totstat = SegyHeaderItem(
            name='totstat', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=103,
            description='total_static_applied_in_ms',
            is_signed=True)
        self.lagA = SegyHeaderItem(
            name='lagA', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=105,
            description='lag_time_A',
            is_signed=True)
        self.lagB = SegyHeaderItem(
            name='lagB', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=107,
            description='lag_time_B',
            is_signed=True)
        self.delayt = SegyHeaderItem(
            name='delayt', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=109,
            description='delay_recording_time',
            is_signed=True)
        self.mutes = SegyHeaderItem(
            name='mutes', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=111,
            description='mute_time_start_time_in_ms',
            is_signed=True)
        self.mutee = SegyHeaderItem(
            name='mutee', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=113,
            description='mute_time_end_time_in_ms',
            is_signed=True)
        self.numsmp = SegyHeaderItem(
            name='numsmp', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=115,
            description='number_of_samples_in_this_trace',
            is_signed=True)  # verify this matches file header
        self.smpint = SegyHeaderItem(
            name='smpint', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=117,
            description='sample_interval_in_ms_for_this_trace',
            is_signed=True) # verify this matches file header
        self.gaintype = SegyHeaderItem(
            name='gaintype', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=119,
            description='gain_type_of_field_instruments',
            is_signed=True,
            map_bool=True, 
            map_dict=GAIN_TYPE_OF_FIELD_INSTRUMENTS)
        self.gainconst = SegyHeaderItem(
            name='gainconst', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=121,
            description='instrument_gain_constant',
            is_signed=True)
        self.initgain = SegyHeaderItem(
            name='initgain', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=123,
            description='instrument_early_or_initial_gain',
            is_signed=True)
        self.corrx = SegyHeaderItem(
            name='corrx', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=125,
            description='correlated',
            is_signed=True,
            map_bool=True, 
            map_dict=CORRELATED)
        self.sweepfs = SegyHeaderItem(
            name='sweepfs', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=127,
            description='sweep_frequency_at_start',
            is_signed=True)
        self.sweepfe = SegyHeaderItem(
            name='sweepfe', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=129,
            description='sweep_frequency_at_end',
            is_signed=True)
        self.sweeplen = SegyHeaderItem(
            name='sweeplen', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=131,
            description='sweep_length_in_ms',
            is_signed=True)
        self.sweeptype = SegyHeaderItem(
            name='sweeptype', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=133,
            description='sweep_type',
            is_signed=True,
            map_bool=True, 
            map_dict=SWEEP_TYPE)
        self.sweeptprs = SegyHeaderItem(
            name='sweeptprs', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=135,
            description='sweep_trace_taper_length_at_start_in_ms',
            is_signed=True)
        self.sweeptpre = SegyHeaderItem(
            name='sweeptpre', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=137,
            description='sweep_trace_taper_length_at_end_in_ms',
            is_signed=True)
        self.tprtype = SegyHeaderItem(
            name='tprtype', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=139,
            description='taper_type',
            is_signed=True,
            map_bool=True, 
            map_dict=TAPER_TYPE)
        self.aliasfilf = SegyHeaderItem(
            name='aliasfilf', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=141,
            description='alias_filter_frequency',
            is_signed=True)
        self.aliasfils = SegyHeaderItem(
            name='aliasfils', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=143,
            description='alias_filter_slope',
            is_signed=True)
        self.notchfilf = SegyHeaderItem(
            name='notchfilf', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=145,
            description='notch_filter_frequency',
            is_signed=True)
        self.notchfils = SegyHeaderItem(
            name='notchfils', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=147,
            description='notch_filter_slope',
            is_signed=True)
        self.lowcutf = SegyHeaderItem(
            name='lowcutf', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=149,
            description='low_cut_frequency',
            is_signed=True)
        self.highcutf = SegyHeaderItem(
            name='highcutf', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=151,
            description='high_cut_frequency',
            is_signed=True)
        self.lowcuts = SegyHeaderItem(
            name='lowcuts', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=153,
            description='low_cut_slope',
            is_signed=True)
        self.highcuts = SegyHeaderItem(
            name='highcuts', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=155,
            description='high_cut_slope',
            is_signed=True)
        self.year = SegyHeaderItem(
            name='year', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=157,
            description='year_data_recorded',
            is_signed=True)
        self.day = SegyHeaderItem(
            name='day', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=159,
            description='day_of_year',
            is_signed=True)
        self.hour = SegyHeaderItem(
            name='hour', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=161,
            description='hour_of_day',
            is_signed=True)
        self.minute = SegyHeaderItem(
            name='minute', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=163,
            description='minute_of_hour',
            is_signed=True)
        self.second = SegyHeaderItem(
            name='second', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=165,
            description='second_of_minute',
            is_signed=True)
        self.timebasis = SegyHeaderItem(
            name='timebasis', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=167,
            description='time_basis_code',
            is_signed=True,
            map_bool=True, 
            map_dict=TIME_BASIS_CODE)
        self.trcweight = SegyHeaderItem(
            name='trcweight', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=169,
            description='trace_weighting_factor',
            is_signed=True)
        self.groupnum = SegyHeaderItem(
            name='groupnum', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=171,
            description='geophone_group_number_of_roll_switch_position_one',
            is_signed=True)
        self.groupnumfirst = SegyHeaderItem(
            name='groupnumfirst', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=173,
            description='geophone_group_number_of_trace_number_one',
            is_signed=True)
        self.groupnumlast = SegyHeaderItem(
            name='groupnumlast', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=175,
            description='geophone_group_number_of_last_trace',
            is_signed=True)
        self.gapsize = SegyHeaderItem(
            name='gapsize', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=177,
            description='gap_size',
            is_signed=True)
        self.overtrvl = SegyHeaderItem(
            name='overtrvl', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=179,
            description='over_travel_associated_with_taper',
            is_signed=True,
            map_bool=True, 
            map_dict=OVER_TRAVEL_ASSOCIATED_TAPER_AT_BEGINNING_OR_END_OF_LINE)
        self.ensx = SegyHeaderItem(
            name='ensx', 
            sample_format=DataSampleFormat.INT32, # nbytes=4, 
            start_byte=181,
            description='x_coordinate_of_ensemble_position_of_this_trace',
            is_signed=True)
        self.ensy = SegyHeaderItem(
            name='ensy', 
            sample_format=DataSampleFormat.INT32, # nbytes=4, 
            start_byte=185,
            description='y_coordinate_of_ensemble_position_of_this_trace',
            is_signed=True)
        self.il = SegyHeaderItem(
            name='il', 
            sample_format=DataSampleFormat.INT32, # nbytes=4, 
            start_byte=189,
            description='for_3d_poststack_data_this_field_is_for_in_line_number',
            is_signed=True)
        self.xl = SegyHeaderItem(
            name='xl', 
            sample_format=DataSampleFormat.INT32, # nbytes=4, 
            start_byte=193,
            description='for_3d_poststack_data_this_field_is_for_cross_line_number',
            is_signed=True)
        self.shotpoint = SegyHeaderItem(
            name='shotpoint', 
            sample_format=DataSampleFormat.INT32, # nbytes=4, 
            start_byte=197,
            description='shotpoint_number',
            is_signed=True)
        self.shotptsclr = SegyHeaderItem(
            name='shotptsclr', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=201,
            description='scalar_to_be_applied_to_the_shotpoint_number',
            is_signed=True)
        self.trcvalmeas = SegyHeaderItem(
            name='trcvalmeas', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=203,
            description='trace_value_measurement_unit',
            is_signed=True,
            map_bool=True, 
            map_dict=TRACE_VALUE_MEASUREMENT_UNIT)
        # The transduction constant is encoded with the mantissa and the power of
        # the exponent, e.g.:
        # transduction_constant =
        # transduction_constant_mantissa * 10 ** transduction_constant_exponent
        self.transconstm = SegyHeaderItem(
            name='transconstm', 
            sample_format=DataSampleFormat.INT32, # nbytes=4, 
            start_byte=205,
            description='transduction_constant_mantissa',
            is_signed=True)
        self.transconste = SegyHeaderItem(
            name='transconste', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=209,
            description='transduction_constant_exponent',
            is_signed=True)
        self.transunits = SegyHeaderItem(
            name='transunits', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=211,
            description='transduction_units',
            is_signed=True,
            map_bool=True, 
            map_dict=TRANSDUCTION_UNITS)
        self.deviceid = SegyHeaderItem(
            name='deviceid', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=213,
            description='device_trace_identifier',
            is_signed=True)
        self.timesclr = SegyHeaderItem(
            name='timesclr', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=215,
            description='scalar_to_be_applied_to_times',
            is_signed=True)
        self.srctypeor = SegyHeaderItem(
            name='srctypeor', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=217,
            description='source_type_orientation',
            is_signed=True,
            map_bool=True, 
            map_dict=SOURCE_TYPE_ORIENTATION)
        self.srcdirm = SegyHeaderItem(
            name='srcdirm', 
            sample_format=DataSampleFormat.INT32, # nbytes=4, 
            start_byte=219,
            description='source_energy_direction_mantissa',
            is_signed=True)
        self.srcdire = SegyHeaderItem(
            name='srcdire', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=223,
            description='source_energy_direction_exponent',
            is_signed=True)
        # The source measurement is encoded with the mantissa and the power of
        # the exponent, e.g.:
        # source_measurement =
        # source_measurement_mantissa * 10 ** source_measurement_exponent
        self.srcmeasm = SegyHeaderItem(
            name='srcmeasm', 
            sample_format=DataSampleFormat.INT32, # nbytes=4, 
            start_byte=225,
            description='source_measurement_mantissa',
            is_signed=True)
        self.srcmease = SegyHeaderItem(
            name='srcmease', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=229,
            description='source_measurement_exponent',
            is_signed=True)
        self.srcmeasu = SegyHeaderItem(
            name='srcmeasu', 
            sample_format=DataSampleFormat.INT16, # nbytes=2, 
            start_byte=231,
            description='source_measurement_unit',
            is_signed=True,
            map_bool=True, 
            map_dict=SOURCE_MEASUREMENT_UNIT)
        self.unknown233 = SegyHeaderItem(
            name='unknown233', 
            sample_format=DataSampleFormat.INT32, # nbytes=4, 
            start_byte=233,
            description='unknown',
            is_signed=True)
        self.unknown237 = SegyHeaderItem(
            name='unknown237', 
            sample_format=DataSampleFormat.INT32, # nbytes=4, 
            start_byte=237,
            description='unknown',
            is_signed=True)


    # --- METHODS ---
    # TODO: move to toolkit
    # def set_scalar_corrected_cooridinates(self):
    #     """Modifies the coordinates by scaling with the scaler value.""" 
    #     if self.zsclr.value != 1:
    #         sclr = self.zsclr.value
    #         self.recelev.value = self.recelev.value * sclr
    #         self.srcelev.value = self.srcelev.value * sclr
    #         self.srcdepth.value = self.srcdepth.value * sclr
    #         self.datmsrc.value = self.datmsrc.value * sclr
    #         self.datmrec.value = self.datmrec.value * sclr
    #         self.h2ozsrc.value = self.h2ozsrc.value * sclr
    #         self.h2ozrec.value = self.h2ozrec.value * sclr

    #     if self.xysclr.value != 1:
    #         sclr = self.xysclr.value
    #         self.srcx.value = self.srcx.value * sclr
    #         self.srcy.value = self.srcy.value * sclr
    #         self.recx.value = self.recx.value * sclr
    #         self.recy.value = self.recy.value * sclr

    # def set_trace_header_values(self, bsgy, endianess):
    #     """Set the trace header values for each segy header item from the segy data (bytes).

    #     Parameters
    #     ----------
    #     bsgy : bytes
    #         Byte data from the segy file.
    #     endianess : str
    #         Must be either 'big' or 'little'.
    #     """
    #     # bsgy is type bytes
    #     file_key_obj_dict = self.key_object_dict()
    #     for name, obj in file_key_obj_dict.items():
    #         bobj = bsgy[obj.start_byte - 1:obj.start_byte + obj.nbytes - 1]
    #         obj.value = int.from_bytes(bobj, byteorder=endianess, signed=obj.is_signed)

    #         if obj.map_bool is True:
    #             self.set_key_property(obj.name, 'value', self.mapped_value(obj.name))

    # def to_bytes(self, endianess, byte_length=240):
    #     """Convert the object to a bytes object.
        
    #     Parameters
    #     ----------
    #     endianess : str
    #         Must be either 'big' or 'little'
    #     byte_length : int
    #         Number of bytes in the output bytes object.
    #     """
    #     return self._to_bytes(endianess=endianess, byte_length=byte_length)