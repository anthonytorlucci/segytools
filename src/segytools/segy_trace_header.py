'''
segy trace header
'''

# import python standard modules


# import 3rd party libraries


# import local python
from .segy_abstract_header import SegyAbstractHeader
from .segy_header_item import SegyHeaderItem


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
            nbytes=4, 
            startbyte=1,
            description='trace_sequence_number_within_line',
            signed=True)
        self.trseqf = SegyHeaderItem(
            name='trseqf', 
            nbytes=4, 
            startbyte=5,
            description='trace_sequence_number_within_segy_file',
            signed=True)
        self.ffid = SegyHeaderItem(
            name='ffid', 
            nbytes=4, 
            startbyte=9,
            description='original_field_record_number',
            signed=True)
        self.trffid = SegyHeaderItem(
            name='trffid', 
            nbytes=4, 
            startbyte=13,
            description='trace_number_within_the_original_field_record',
            signed=True)
        self.shot = SegyHeaderItem(
            name='shot', 
            nbytes=4, 
            startbyte=17,
            description='energy_source_point_number',
            signed=True)
        self.ens = SegyHeaderItem(
            name='ens', 
            nbytes=4, 
            startbyte=21,
            description='ensemble_number',
            signed=True)
        self.trcens = SegyHeaderItem(
            name='trcens', 
            nbytes=4, 
            startbyte=25,
            description='trace_number_within_the_ensemble',
            signed=True)
        self.trid = SegyHeaderItem(
            name='trid', 
            nbytes=2, 
            startbyte=29,
            description='trace_identification_code',
            signed=True,
            map_bool=True, 
            map_dict=TRACE_IDENTIFICATION_CODE)
        self.vsum = SegyHeaderItem(
            name='vsum', 
            nbytes=2, 
            startbyte=31,
            description='number_of_vertically_summed_traces_yielding_this_trace',
            signed=True)
        self.hsum = SegyHeaderItem(
            name='hsum', 
            nbytes=2, 
            startbyte=33,
            description='number_of_horizontally_stacked_traces_yielding_this_trace',
            signed=True)
        self.datuse = SegyHeaderItem(
            name='datuse', 
            nbytes=2, 
            startbyte=35,
            description='data_use',
            signed=True,
            map_bool=True, 
            map_dict=DATA_USE)
        self.offset = SegyHeaderItem(
            name='offset', 
            nbytes=4, 
            startbyte=37,
            description='distance_from_center_of_the_source_point_to_the_center_of_the_receiver_group',
            signed=True)
        self.recelev = SegyHeaderItem(
            name='recelev', 
            nbytes=4, 
            startbyte=41,
            description='receiver_group_elevation',
            signed=True)
        self.srcelev = SegyHeaderItem(
            name='srcelev', 
            nbytes=4, 
            startbyte=45,
            description='surface_elevation_at_source',
            signed=True)
        self.srcdepth = SegyHeaderItem(
            name='srcdepth', 
            nbytes=4, 
            startbyte=49,
            description='source_depth_below_surface',
            signed=True)
        self.datmrec = SegyHeaderItem(
            name='datmrec', 
            nbytes=4, 
            startbyte=53,
            description='datum_elevation_at_receiver_group',
            signed=True)
        self.datmsrc = SegyHeaderItem(
            name='datmsrc', 
            nbytes=4, 
            startbyte=57,
            description='datum_elevation_at_source',
            signed=True)
        self.h2ozsrc = SegyHeaderItem(
            name='h2ozsrc', 
            nbytes=4, 
            startbyte=61,
            description='water_depth_at_source',
            signed=True)
        self.h2ozrec = SegyHeaderItem(
            name='h2ozrec', 
            nbytes=4, 
            startbyte=65,
            description='water_depth_at_group',
            signed=True)
        self.zsclr = SegyHeaderItem(
            name='zsclr', 
            nbytes=2, 
            startbyte=69,
            description='scalar_to_be_applied_to_all_elevations_and_depths',
            signed=True,
            map_bool=True, 
            map_dict=COORDINATE_SCALAR_MULTIPLIER)
        self.xysclr = SegyHeaderItem(
            name='xysclr', 
            nbytes=2, 
            startbyte=71,
            description='scalar_to_be_applied_to_all_coordinates',
            signed=True,
            map_bool=True, 
            map_dict=COORDINATE_SCALAR_MULTIPLIER)
        self.srcx = SegyHeaderItem(
            name='srcx', 
            nbytes=4, 
            startbyte=73,
            description='source_coordinate_x',
            signed=True)
        self.srcy = SegyHeaderItem(
            name='srcy', 
            nbytes=4, 
            startbyte=77,
            description='source_coordinate_y',
            signed=True)
        self.recx = SegyHeaderItem(
            name='recx', 
            nbytes=4, 
            startbyte=81,
            description='group_coordinate_x',
            signed=True)
        self.recy = SegyHeaderItem(
            name='recy', 
            nbytes=4, 
            startbyte=85,
            description='group_coordinate_y',
            signed=True)
        self.coordunits = SegyHeaderItem(
            name='coordunits', 
            nbytes=2, 
            startbyte=89,
            description='coordinate_units',
            signed=True,
            map_bool=True, 
            map_dict=COORDINATE_UNITS)
        self.weathvel = SegyHeaderItem(
            name='weathvel', 
            nbytes=2, 
            startbyte=91,
            description='weathering_velocity',
            signed=True)
        self.subweathvel = SegyHeaderItem(
            name='subweathvel', 
            nbytes=2, 
            startbyte=93,
            description='subweathering_velocity',
            signed=True)
        self.uptsrc = SegyHeaderItem(
            name='uptsrc', 
            nbytes=2, 
            startbyte=95,
            description='uphole_time_at_source_in_ms',
            signed=True)
        self.uptrec = SegyHeaderItem(
            name='uptrec', 
            nbytes=2, 
            startbyte=97,
            description='uphole_time_at_group_in_ms',
            signed=True)
        self.srcstat = SegyHeaderItem(
            name='srcstat', 
            nbytes=2, 
            startbyte=99,
            description='source_static_correction_in_ms',
            signed=True)
        self.recstat = SegyHeaderItem(
            name='recstat', 
            nbytes=2, 
            startbyte=101,
            description='group_static_correction_in_ms',
            signed=True)
        self.totstat = SegyHeaderItem(
            name='totstat', 
            nbytes=2, 
            startbyte=103,
            description='total_static_applied_in_ms',
            signed=True)
        self.lagA = SegyHeaderItem(
            name='lagA', 
            nbytes=2, 
            startbyte=105,
            description='lag_time_A',
            signed=True)
        self.lagB = SegyHeaderItem(
            name='lagB', 
            nbytes=2, 
            startbyte=107,
            description='lag_time_B',
            signed=True)
        self.delayt = SegyHeaderItem(
            name='delayt', 
            nbytes=2, 
            startbyte=109,
            description='delay_recording_time',
            signed=True)
        self.mutes = SegyHeaderItem(
            name='mutes', 
            nbytes=2, 
            startbyte=111,
            description='mute_time_start_time_in_ms',
            signed=True)
        self.mutee = SegyHeaderItem(
            name='mutee', 
            nbytes=2, 
            startbyte=113,
            description='mute_time_end_time_in_ms',
            signed=True)
        self.numsmp = SegyHeaderItem(
            name='numsmp', 
            nbytes=2, 
            startbyte=115,
            description='number_of_samples_in_this_trace',
            signed=True)  # verify this matches file header
        self.smpint = SegyHeaderItem(
            name='smpint', 
            nbytes=2, 
            startbyte=117,
            description='sample_interval_in_ms_for_this_trace',
            signed=True) # verify this matches file header
        self.gaintype = SegyHeaderItem(
            name='gaintype', 
            nbytes=2, 
            startbyte=119,
            description='gain_type_of_field_instruments',
            signed=True,
            map_bool=True, 
            map_dict=GAIN_TYPE_OF_FIELD_INSTRUMENTS)
        self.gainconst = SegyHeaderItem(
            name='gainconst', 
            nbytes=2, 
            startbyte=121,
            description='instrument_gain_constant',
            signed=True)
        self.initgain = SegyHeaderItem(
            name='initgain', 
            nbytes=2, 
            startbyte=123,
            description='instrument_early_or_initial_gain',
            signed=True)
        self.corrx = SegyHeaderItem(
            name='corrx', 
            nbytes=2, 
            startbyte=125,
            description='correlated',
            signed=True,
            map_bool=True, 
            map_dict=CORRELATED)
        self.sweepfs = SegyHeaderItem(
            name='sweepfs', 
            nbytes=2, 
            startbyte=127,
            description='sweep_frequency_at_start',
            signed=True)
        self.sweepfe = SegyHeaderItem(
            name='sweepfe', 
            nbytes=2, 
            startbyte=129,
            description='sweep_frequency_at_end',
            signed=True)
        self.sweeplen = SegyHeaderItem(
            name='sweeplen', 
            nbytes=2, 
            startbyte=131,
            description='sweep_length_in_ms',
            signed=True)
        self.sweeptype = SegyHeaderItem(
            name='sweeptype', 
            nbytes=2, 
            startbyte=133,
            description='sweep_type',
            signed=True,
            map_bool=True, 
            map_dict=SWEEP_TYPE)
        self.sweeptprs = SegyHeaderItem(
            name='sweeptprs', 
            nbytes=2, 
            startbyte=135,
            description='sweep_trace_taper_length_at_start_in_ms',
            signed=True)
        self.sweeptpre = SegyHeaderItem(
            name='sweeptpre', 
            nbytes=2, 
            startbyte=137,
            description='sweep_trace_taper_length_at_end_in_ms',
            signed=True)
        self.tprtype = SegyHeaderItem(
            name='tprtype', 
            nbytes=2, 
            startbyte=139,
            description='taper_type',
            signed=True,
            map_bool=True, 
            map_dict=TAPER_TYPE)
        self.aliasfilf = SegyHeaderItem(
            name='aliasfilf', 
            nbytes=2, 
            startbyte=141,
            description='alias_filter_frequency',
            signed=True)
        self.aliasfils = SegyHeaderItem(
            name='aliasfils', 
            nbytes=2, 
            startbyte=143,
            description='alias_filter_slope',
            signed=True)
        self.notchfilf = SegyHeaderItem(
            name='notchfilf', 
            nbytes=2, 
            startbyte=145,
            description='notch_filter_frequency',
            signed=True)
        self.notchfils = SegyHeaderItem(
            name='notchfils', 
            nbytes=2, 
            startbyte=147,
            description='notch_filter_slope',
            signed=True)
        self.lowcutf = SegyHeaderItem(
            name='lowcutf', 
            nbytes=2, 
            startbyte=149,
            description='low_cut_frequency',
            signed=True)
        self.highcutf = SegyHeaderItem(
            name='highcutf', 
            nbytes=2, 
            startbyte=151,
            description='high_cut_frequency',
            signed=True)
        self.lowcuts = SegyHeaderItem(
            name='lowcuts', 
            nbytes=2, 
            startbyte=153,
            description='low_cut_slope',
            signed=True)
        self.highcuts = SegyHeaderItem(
            name='highcuts', 
            nbytes=2, 
            startbyte=155,
            description='high_cut_slope',
            signed=True)
        self.year = SegyHeaderItem(
            name='year', 
            nbytes=2, 
            startbyte=157,
            description='year_data_recorded',
            signed=True)
        self.day = SegyHeaderItem(
            name='day', 
            nbytes=2, 
            startbyte=159,
            description='day_of_year',
            signed=True)
        self.hour = SegyHeaderItem(
            name='hour', 
            nbytes=2, 
            startbyte=161,
            description='hour_of_day',
            signed=True)
        self.minute = SegyHeaderItem(
            name='minute', 
            nbytes=2, 
            startbyte=163,
            description='minute_of_hour',
            signed=True)
        self.second = SegyHeaderItem(
            name='second', 
            nbytes=2, 
            startbyte=165,
            description='second_of_minute',
            signed=True)
        self.timebasis = SegyHeaderItem(
            name='timebasis', 
            nbytes=2, 
            startbyte=167,
            description='time_basis_code',
            signed=True,
            map_bool=True, 
            map_dict=TIME_BASIS_CODE)
        self.trcweight = SegyHeaderItem(
            name='trcweight', 
            nbytes=2, 
            startbyte=169,
            description='trace_weighting_factor',
            signed=True)
        self.groupnum = SegyHeaderItem(
            name='groupnum', 
            nbytes=2, 
            startbyte=171,
            description='geophone_group_number_of_roll_switch_position_one',
            signed=True)
        self.groupnumfirst = SegyHeaderItem(
            name='groupnumfirst', 
            nbytes=2, 
            startbyte=173,
            description='geophone_group_number_of_trace_number_one',
            signed=True)
        self.groupnumlast = SegyHeaderItem(
            name='groupnumlast', 
            nbytes=2, 
            startbyte=175,
            description='geophone_group_number_of_last_trace',
            signed=True)
        self.gapsize = SegyHeaderItem(
            name='gapsize', 
            nbytes=2, 
            startbyte=177,
            description='gap_size',
            signed=True)
        self.overtrvl = SegyHeaderItem(
            name='overtrvl', 
            nbytes=2, 
            startbyte=179,
            description='over_travel_associated_with_taper',
            signed=True,
            map_bool=True, 
            map_dict=OVER_TRAVEL_ASSOCIATED_TAPER_AT_BEGINNING_OR_END_OF_LINE)
        self.ensx = SegyHeaderItem(
            name='ensx', 
            nbytes=4, 
            startbyte=181,
            description='x_coordinate_of_ensemble_position_of_this_trace',
            signed=True)
        self.ensy = SegyHeaderItem(
            name='ensy', 
            nbytes=4, 
            startbyte=185,
            description='y_coordinate_of_ensemble_position_of_this_trace',
            signed=True)
        self.il = SegyHeaderItem(
            name='il', 
            nbytes=4, 
            startbyte=189,
            description='for_3d_poststack_data_this_field_is_for_in_line_number',
            signed=True)
        self.xl = SegyHeaderItem(
            name='xl', 
            nbytes=4, 
            startbyte=193,
            description='for_3d_poststack_data_this_field_is_for_cross_line_number',
            signed=True)
        self.shotpoint = SegyHeaderItem(
            name='shotpoint', 
            nbytes=4, 
            startbyte=197,
            description='shotpoint_number',
            signed=True)
        self.shotptsclr = SegyHeaderItem(
            name='shotptsclr', 
            nbytes=2, 
            startbyte=201,
            description='scalar_to_be_applied_to_the_shotpoint_number',
            signed=True)
        self.trcvalmeas = SegyHeaderItem(
            name='trcvalmeas', 
            nbytes=2, 
            startbyte=203,
            description='trace_value_measurement_unit',
            signed=True,
            map_bool=True, 
            map_dict=TRACE_VALUE_MEASUREMENT_UNIT)
        # The transduction constant is encoded with the mantissa and the power of
        # the exponent, e.g.:
        # transduction_constant =
        # transduction_constant_mantissa * 10 ** transduction_constant_exponent
        self.transconstm = SegyHeaderItem(
            name='transconstm', 
            nbytes=4, 
            startbyte=205,
            description='transduction_constant_mantissa',
            signed=True)
        self.transconste = SegyHeaderItem(
            name='transconste', 
            nbytes=2, 
            startbyte=209,
            description='transduction_constant_exponent',
            signed=True)
        self.transunits = SegyHeaderItem(
            name='transunits', 
            nbytes=2, 
            startbyte=211,
            description='transduction_units',
            signed=True,
            map_bool=True, 
            map_dict=TRANSDUCTION_UNITS)
        self.deviceid = SegyHeaderItem(
            name='deviceid', 
            nbytes=2, 
            startbyte=213,
            description='device_trace_identifier',
            signed=True)
        self.timesclr = SegyHeaderItem(
            name='timesclr', 
            nbytes=2, 
            startbyte=215,
            description='scalar_to_be_applied_to_times',
            signed=True)
        self.srctypeor = SegyHeaderItem(
            name='srctypeor', 
            nbytes=2, 
            startbyte=217,
            description='source_type_orientation',
            signed=True,
            map_bool=True, 
            map_dict=SOURCE_TYPE_ORIENTATION)
        self.srcdirm = SegyHeaderItem(
            name='srcdirm', 
            nbytes=4, 
            startbyte=219,
            description='source_energy_direction_mantissa',
            signed=True)
        self.srcdire = SegyHeaderItem(
            name='srcdire', 
            nbytes=2, 
            startbyte=223,
            description='source_energy_direction_exponent',
            signed=True)
        # The source measurement is encoded with the mantissa and the power of
        # the exponent, e.g.:
        # source_measurement =
        # source_measurement_mantissa * 10 ** source_measurement_exponent
        self.srcmeasm = SegyHeaderItem(
            name='srcmeasm', 
            nbytes=4, 
            startbyte=225,
            description='source_measurement_mantissa',
            signed=True)
        self.srcmease = SegyHeaderItem(
            name='srcmease', 
            nbytes=2, 
            startbyte=229,
            description='source_measurement_exponent',
            signed=True)
        self.srcmeasu = SegyHeaderItem(
            name='srcmeasu', 
            nbytes=2, 
            startbyte=231,
            description='source_measurement_unit',
            signed=True,
            map_bool=True, 
            map_dict=SOURCE_MEASUREMENT_UNIT)
        self.unknown233 = SegyHeaderItem(
            name='unknown233', 
            nbytes=4, 
            startbyte=233,
            description='unknown',
            signed=True)
        self.unknown237 = SegyHeaderItem(
            name='unknown237', 
            nbytes=4, 
            startbyte=237,
            description='unknown',
            signed=True)

    def __str__(self):
        s = '\nsegy trace header values\n'
        s += str(self.trseql) + '\n'
        s += str(self.trseqf) + '\n'
        s += str(self.ffid) + '\n'
        s += str(self.trffid) + '\n'
        s += str(self.shot) + '\n'
        s += str(self.ens) + '\n'
        s += str(self.trcens) + '\n'
        s += str(self.trid) + '\n'
        s += str(self.vsum) + '\n'
        s += str(self.hsum) + '\n'
        s += str(self.datuse) + '\n'
        s += str(self.offset) + '\n'
        s += str(self.recelev) + '\n'
        s += str(self.srcelev) + '\n'
        s += str(self.srcdepth) + '\n'
        s += str(self.datmrec) + '\n'
        s += str(self.datmsrc) + '\n'
        s += str(self.h2ozsrc) + '\n'
        s += str(self.h2ozrec) + '\n'
        s += str(self.zsclr) + '\n'
        s += str(self.xysclr) + '\n'
        s += str(self.srcx) + '\n'
        s += str(self.srcy) + '\n'
        s += str(self.recx) + '\n'
        s += str(self.recy) + '\n'
        s += str(self.coordunits) + '\n'
        s += str(self.weathvel) + '\n'
        s += str(self.subweathvel) + '\n'
        s += str(self.uptsrc) + '\n'
        s += str(self.uptrec) + '\n'
        s += str(self.srcstat) + '\n'
        s += str(self.recstat) + '\n'
        s += str(self.totstat) + '\n'
        s += str(self.lagA) + '\n'
        s += str(self.lagB) + '\n'
        s += str(self.delayt) + '\n'
        s += str(self.mutes) + '\n'
        s += str(self.mutee) + '\n'
        s += str(self.numsmp) + '\n'
        s += str(self.smpint) + '\n'
        s += str(self.gaintype) + '\n'
        s += str(self.gainconst) + '\n'
        s += str(self.initgain) + '\n'
        s += str(self.corrx) + '\n'
        s += str(self.sweepfs) + '\n'
        s += str(self.sweepfe) + '\n'
        s += str(self.sweeplen) + '\n'
        s += str(self.sweeptype) + '\n'
        s += str(self.sweeptprs) + '\n'
        s += str(self.sweeptpre) + '\n'
        s += str(self.tprtype) + '\n'
        s += str(self.aliasfilf) + '\n'
        s += str(self.aliasfils) + '\n'
        s += str(self.notchfilf) + '\n'
        s += str(self.notchfils) + '\n'
        s += str(self.lowcutf) + '\n'
        s += str(self.highcutf) + '\n'
        s += str(self.lowcuts) + '\n'
        s += str(self.highcuts) + '\n'
        s += str(self.year) + '\n'
        s += str(self.day) + '\n'
        s += str(self.hour) + '\n'
        s += str(self.minute) + '\n'
        s += str(self.second) + '\n'
        s += str(self.timebasis) + '\n'
        s += str(self.trcweight) + '\n'
        s += str(self.groupnum) + '\n'
        s += str(self.groupnumfirst) + '\n'
        s += str(self.groupnumlast) + '\n'
        s += str(self.gapsize) + '\n'
        s += str(self.overtrvl) + '\n'
        s += str(self.ensx) + '\n'
        s += str(self.ensy) + '\n'
        s += str(self.il) + '\n'
        s += str(self.xl) + '\n'
        s += str(self.shotpoint) + '\n'
        s += str(self.shotptsclr) + '\n'
        s += str(self.trcvalmeas) + '\n'
        s += str(self.transconstm) + '\n'
        s += str(self.transconste) + '\n'
        s += str(self.transunits) + '\n'
        s += str(self.deviceid) + '\n'
        s += str(self.timesclr) + '\n'
        s += str(self.srctypeor) + '\n'
        s += str(self.srcdirm) + '\n'
        s += str(self.srcdire) + '\n'
        s += str(self.srcmeasm) + '\n'
        s += str(self.srcmease) + '\n'
        s += str(self.srcmeasu) + '\n'
        s += str(self.unknown233) + '\n'
        s += str(self.unknown237)
        return s


    # --- METHODS ---
    def set_scalar_corrected_cooridinates(self):
        """Modifies the coordinates by scaling with the scaler value.""" 
        if self.zsclr.value != 1:
            sclr = self.zsclr.value
            self.recelev.value = self.recelev.value * sclr
            self.srcelev.value = self.srcelev.value * sclr
            self.srcdepth.value = self.srcdepth.value * sclr
            self.datmsrc.value = self.datmsrc.value * sclr
            self.datmrec.value = self.datmrec.value * sclr
            self.h2ozsrc.value = self.h2ozsrc.value * sclr
            self.h2ozrec.value = self.h2ozrec.value * sclr

        if self.xysclr.value != 1:
            sclr = self.xysclr.value
            self.srcx.value = self.srcx.value * sclr
            self.srcy.value = self.srcy.value * sclr
            self.recx.value = self.recx.value * sclr
            self.recy.value = self.recy.value * sclr

    def set_trace_header_values(self, bsgy, endianess):
        """Set the trace header values for each segy header item from the segy data (bytes).

        Parameters
        ----------
        bsgy : bytes
            Byte data from the segy file.
        endianess : str
            Must be either 'big' or 'little'.
        """
        # bsgy is type bytes
        file_key_obj_dict = self.key_object_dict()
        for name, obj in file_key_obj_dict.items():
            bobj = bsgy[obj.startbyte - 1:obj.startbyte + obj.nbytes - 1]
            obj.value = int.from_bytes(bobj, byteorder=endianess, signed=obj.signed)

            if obj.map_bool is True:
                self.set_key_property(obj.name, 'value', self.mapped_value(obj.name))

    def to_bytes(self, endianess, byte_length=240):
        """Convert the object to a bytes object.
        
        Parameters
        ----------
        endianess : str
            Must be either 'big' or 'little'
        byte_length : int
            Number of bytes in the output bytes object.
        """
        return self._to_bytes(endianess=endianess, byte_length=byte_length)