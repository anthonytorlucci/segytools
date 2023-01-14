from context import segytools

# create data for testing
b_zero2 = int.to_bytes(int(0), length=2, byteorder='little', signed=True)
b_zero4 = int.to_bytes(int(0), length=4, byteorder='little', signed=True)

trace_header_bytearray = bytearray(240)
# fill with zeros to initialize
for i in range(0,240,4):
    trace_header_bytearray[i:i+4] = b_zero4

trace_header_bytearray[0:4] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # trseql
trace_header_bytearray[4:8] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # trseqf
trace_header_bytearray[8:12] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # ffid
trace_header_bytearray[12:16] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # trffid
trace_header_bytearray[16:20] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # shot
trace_header_bytearray[20:24] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # ens
trace_header_bytearray[24:28] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # trcens
trace_header_bytearray[28:30] = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # trid -> "Seismic Data"
trace_header_bytearray[30:32] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # vsum
trace_header_bytearray[32:34] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # hsum
trace_header_bytearray[34:36] = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # datause -> "Production"
trace_header_bytearray[36:40] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # offset
trace_header_bytearray[40:44] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # recelev
trace_header_bytearray[44:48] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # srcelev
trace_header_bytearray[48:52] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # srcdepth
trace_header_bytearray[52:56] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # datmrec
trace_header_bytearray[56:60] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # datmsrc
trace_header_bytearray[60:64] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # h2ozsrc
trace_header_bytearray[64:68] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # h2ozrec
trace_header_bytearray[68:70] = int.to_bytes(int(-100), length=2, byteorder='little', signed=True)  # zsclr -> 0.01
trace_header_bytearray[70:72] = int.to_bytes(int(-100), length=2, byteorder='little', signed=True)  # xysclr -> 0.01
trace_header_bytearray[72:76] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # srcx
trace_header_bytearray[76:80] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # srcy
trace_header_bytearray[80:84] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # recx
trace_header_bytearray[84:88] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # recy
trace_header_bytearray[88:90] = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # coordunits -> "Length (meters or feet)"
trace_header_bytearray[90:92] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # weathvel
trace_header_bytearray[92:94] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # subweathvel
trace_header_bytearray[94:96] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # uptsrc
trace_header_bytearray[96:98] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # uptrec
trace_header_bytearray[98:100] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # srcstat
trace_header_bytearray[100:102] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # recstat
trace_header_bytearray[102:104] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # totstat
trace_header_bytearray[104:106] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # laga
trace_header_bytearray[106:108] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # lagb
trace_header_bytearray[108:110] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # delayt
trace_header_bytearray[110:112] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # mutes
trace_header_bytearray[112:114] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # mutee
trace_header_bytearray[114:116] = int.to_bytes(int(1200), length=2, byteorder='little', signed=True)  # numsmp
trace_header_bytearray[116:118] = int.to_bytes(int(2000), length=2, byteorder='little', signed=True)  # smpint
trace_header_bytearray[118:120] = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # gaintype -> "fixed"
trace_header_bytearray[120:122] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # gainconst
trace_header_bytearray[122:124] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # initgain
trace_header_bytearray[124:126] = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # corrx -> "yes"
trace_header_bytearray[126:128] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # sweepfs
trace_header_bytearray[128:130] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # sweepfe
trace_header_bytearray[130:132] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # sweeplen
trace_header_bytearray[132:134] = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # sweeptype -> "linear"
trace_header_bytearray[134:136] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # sweeptprs
trace_header_bytearray[136:138] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # sweeptpre
trace_header_bytearray[138:140] = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # tprtype -> "linear"
trace_header_bytearray[140:142] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # aliasfilf
trace_header_bytearray[142:144] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # aliasfils
trace_header_bytearray[144:146] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # notchfilf
trace_header_bytearray[146:148] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # notchfils
trace_header_bytearray[148:150] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # lowcutf
trace_header_bytearray[150:152] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # highcutf
trace_header_bytearray[152:154] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # lowcuts
trace_header_bytearray[154:156] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # highcuts
trace_header_bytearray[156:158] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # year
trace_header_bytearray[158:160] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # day
trace_header_bytearray[160:162] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # hour
trace_header_bytearray[162:164] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # minute
trace_header_bytearray[164:166] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # second
trace_header_bytearray[166:168] = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # timebasis -> "Local"
trace_header_bytearray[168:170] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # trcweight
trace_header_bytearray[170:172] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # groupnum
trace_header_bytearray[172:174] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # groupnumfirst
trace_header_bytearray[174:176] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # groupnumlast
trace_header_bytearray[176:178] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # gapsize
trace_header_bytearray[178:180] = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # overtrvl -> "down (or behind)"
trace_header_bytearray[180:184] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # ensx
trace_header_bytearray[184:188] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # ensy
trace_header_bytearray[188:192] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # il
trace_header_bytearray[192:196] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # xl
trace_header_bytearray[196:200] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # shotpoint
trace_header_bytearray[200:202] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # shotptsclr
trace_header_bytearray[202:204] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # trcvalmeas -> "Unknown"
trace_header_bytearray[204:208] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # transconstm
trace_header_bytearray[208:210] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # transconste
trace_header_bytearray[210:212] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # transunits -> "Unknown"
trace_header_bytearray[212:214] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # deviceid
trace_header_bytearray[214:216] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # timesclr
trace_header_bytearray[216:218] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # srctypeor -> "Unknown"
trace_header_bytearray[218:222] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # srcdirm
trace_header_bytearray[222:224] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # srcdire
trace_header_bytearray[224:228] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # srcmeasm
trace_header_bytearray[228:230] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # srcmease
trace_header_bytearray[230:232] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # srcmeasu -> "Unknown"
trace_header_bytearray[232:236] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # 233
trace_header_bytearray[236:240] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # 233
trace_header_bytes = bytes(trace_header_bytearray)



# trc_seq_num_within_line
def test_segy_trace_header_initialization_trc_seq_num_within_line_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.trc_seq_num_within_line.value
    assert actual == expected

# trc_seq_num_within_trace
def test_segy_trace_header_initialization_trc_seq_num_within_file_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.trc_seq_num_within_file.value
    assert actual == expected

# field_record_number
def test_segy_trace_header_initialization_field_record_number_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.field_record_number.value
    assert actual == expected

# trc_num_within_field_record
def test_segy_trace_header_initialization_trc_num_within_field_record_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.trc_num_within_field_record.value
    assert actual == expected

# energy_src_num
def test_segy_trace_header_initialization_energy_src_num_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.energy_src_num.value
    assert actual == expected

# ensemble_number
def test_segy_trace_header_initialization_ensemble_number_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.ensemble_number.value
    assert actual == expected

# trc_num_within_ensemble
def test_segy_trace_header_initialization_trc_num_within_ensemble_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.trc_num_within_ensemble.value
    assert actual == expected

# trc_identification_code
def test_segy_trace_header_initialization_trc_identification_code_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.trc_identification_code.value
    assert actual == expected

def test_segy_trace_header_initialization_trc_identification_code_mapped_value():
    expected = "Unknown"
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.trc_identification_code.mapped_value
    assert actual == expected

# num_vert_summed_traces
def test_segy_trace_header_initialization_num_vert_summed_traces_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.num_vert_summed_traces.value
    assert actual == expected

# num_horz_summed_traces
def test_segy_trace_header_initialization_num_horz_summed_traces_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.num_horz_summed_traces.value
    assert actual == expected

# data_use
def test_segy_trace_header_initialization_data_use_value():
    expected = 1
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.data_use.value
    assert actual == expected

def test_segy_trace_header_initialization_data_use_mapped_value():
    expected = "Production"
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.data_use.mapped_value
    assert actual == expected

# offset
def test_segy_trace_header_initialization_offset_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.offset.value
    assert actual == expected

# rcv_elevation
def test_segy_trace_header_initialization_rcv_elevation_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.rcv_elevation.value
    assert actual == expected

# src_elevation
def test_segy_trace_header_initialization_src_elevation_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.src_elevation.value
    assert actual == expected

# src_depth
def test_segy_trace_header_initialization_src_depth_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.src_depth.value
    assert actual == expected

# rcv_datum_elevation
def test_segy_trace_header_initialization_rcv_datum_elevation_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.rcv_datum_elevation.value
    assert actual == expected

# src_datum_elevation
def test_segy_trace_header_initialization_src_datum_elevation_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.src_datum_elevation.value
    assert actual == expected

# src_water_depth
def test_segy_trace_header_initialization_src_water_depth_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.src_water_depth.value
    assert actual == expected

# rcv_water_depth
def test_segy_trace_header_initialization_rcv_water_depth_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.rcv_water_depth.value
    assert actual == expected

# z_scalar
def test_segy_trace_header_initialization_z_scalar_value():
    expected = 1
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.z_scalar.value
    assert actual == expected

# xy_scalar
def test_segy_trace_header_initialization_xy_scalar_value():
    expected = 1
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.xy_scalar.value
    assert actual == expected

# src_x_coord
def test_segy_trace_header_initialization_src_x_coord_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.src_x_coord.value
    assert actual == expected

# src_y_coord
def test_segy_trace_header_initialization_src_y_coord_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.src_y_coord.value
    assert actual == expected

# rcv_x_coord
def test_segy_trace_header_initialization_rcv_x_coord_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.rcv_x_coord.value
    assert actual == expected

# rcv_y_coord
def test_segy_trace_header_initialization_rcv_y_coord_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.rcv_y_coord.value
    assert actual == expected

# coord_units
def test_segy_trace_header_initialization_coord_units_value():
    expected = 1
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.coord_units.value
    assert actual == expected

# weathering_velocity
def test_segy_trace_header_initialization_weathering_velocity_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.weathering_velocity.value
    assert actual == expected

# subweathering_velocity
def test_segy_trace_header_initialization_subweathering_velocity_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.subweathering_velocity.value
    assert actual == expected

# src_uphole_time
def test_segy_trace_header_initialization_src_uphole_time_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.src_uphole_time.value
    assert actual == expected

# rcv_uphole_time
def test_segy_trace_header_initialization_rcv_uphole_time_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.rcv_uphole_time.value
    assert actual == expected

# src_static_correction
def test_segy_trace_header_initialization_src_static_correction_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.src_static_correction.value
    assert actual == expected

# rcv_static_correction
def test_segy_trace_header_initialization_rcv_static_correction_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.rcv_static_correction.value
    assert actual == expected

# total_static_applied
def test_segy_trace_header_initialization_total_static_applied_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.total_static_applied.value
    assert actual == expected

# lag_time_A
def test_segy_trace_header_initialization_lag_time_A_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.lag_time_A.value
    assert actual == expected

# lag_time_B
def test_segy_trace_header_initialization_lag_time_B_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.lag_time_B.value
    assert actual == expected

# delay_recording_time
def test_segy_trace_header_initialization_delay_recording_time_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.delay_recording_time.value
    assert actual == expected

# mute_start_time
def test_segy_trace_header_initialization_mute_start_time_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.mute_start_time.value
    assert actual == expected

# mute_end_time
def test_segy_trace_header_initialization_mute_end_time_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.mute_end_time.value
    assert actual == expected

# num_samples (should be read/set in every case; custom trace headers should have this)
def test_segy_trace_header_initialization_num_samples_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.num_samples.value
    assert actual == expected

# sample_interval
def test_segy_trace_header_initialization_sample_interval_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.sample_interval.value
    assert actual == expected

# gain_type
def test_segy_trace_header_initialization_gain_type_value():
    expected = 1
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.gain_type.value
    assert actual == expected

# gain_const
def test_segy_trace_header_initialization_gain_const_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.gain_const.value
    assert actual == expected

# initial_gain
def test_segy_trace_header_initialization_initial_gain_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.initial_gain.value
    assert actual == expected

# correlated
def test_segy_trace_header_initialization_correlated_value():
    expected = 1
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.correlated.value
    assert actual == expected

# sweep_freq_start
def test_segy_trace_header_initialization_sweep_freq_start_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.sweep_freq_start.value
    assert actual == expected

# sweep_freq_end
def test_segy_trace_header_initialization_sweep_freq_end_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.sweep_freq_end.value
    assert actual == expected

# sweep_length
def test_segy_trace_header_initialization_sweep_length_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.sweep_length.value
    assert actual == expected

# sweep_type
def test_segy_trace_header_initialization_sweep_type_value():
    expected = 1
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.sweep_type.value
    assert actual == expected

# sweep_taper_length_start
def test_segy_trace_header_initialization_sweep_taper_length_start_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.sweep_taper_length_start.value
    assert actual == expected

# sweep_taper_length_end
def test_segy_trace_header_initialization_sweep_taper_length_end_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.sweep_taper_length_end.value
    assert actual == expected

# taper_type
def test_segy_trace_header_initialization_taper_type_value():
    expected = 1
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.taper_type.value
    assert actual == expected

# alias_filter_freq
def test_segy_trace_header_initialization_alias_filter_freq_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.alias_filter_freq.value
    assert actual == expected

# alias_filter_slope
def test_segy_trace_header_initialization_alias_filter_slope_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.alias_filter_slope.value
    assert actual == expected

# notch_filter_freq
def test_segy_trace_header_initialization_notch_filter_freq_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.notch_filter_freq.value
    assert actual == expected

# notch_filter_slope
def test_segy_trace_header_initialization_notch_filter_slope_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.notch_filter_slope.value
    assert actual == expected

# low_cut_freq
def test_segy_trace_header_initialization_low_cut_freq_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.low_cut_freq.value
    assert actual == expected

# high_cut_freq
def test_segy_trace_header_initialization_high_cut_freq_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.high_cut_freq.value
    assert actual == expected

# low_cut_slope
def test_segy_trace_header_initialization_low_cut_slope_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.low_cut_slope.value
    assert actual == expected

# high_cut_slope
def test_segy_trace_header_initialization_high_cut_slope_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.high_cut_slope.value
    assert actual == expected

# year
def test_segy_trace_header_initialization_year_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.year.value
    assert actual == expected

# day
def test_segy_trace_header_initialization_day_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.day.value
    assert actual == expected

# hour
def test_segy_trace_header_initialization_hour_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.hour.value
    assert actual == expected

# minute
def test_segy_trace_header_initialization_minute_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.minute.value
    assert actual == expected

# second
def test_segy_trace_header_initialization_second_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.second.value
    assert actual == expected

# time_basis
def test_segy_trace_header_initialization_time_basis_value():
    expected = 1
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.time_basis.value
    assert actual == expected

# trc_weight
def test_segy_trace_header_initialization_trc_weight_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.trc_weight.value
    assert actual == expected

# group_num
def test_segy_trace_header_initialization_group_num_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.group_num.value
    assert actual == expected

# first_group_num
def test_segy_trace_header_initialization_first_group_num_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.first_group_num.value
    assert actual == expected

# last_group_num
def test_segy_trace_header_initialization_last_group_num_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.last_group_num.value
    assert actual == expected

# gap_size
def test_segy_trace_header_initialization_gap_size_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.gap_size.value
    assert actual == expected

# over_travel
def test_segy_trace_header_initialization_over_travel_value():
    expected = 1
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.over_travel.value
    assert actual == expected

# ens_x_coord
def test_segy_trace_header_initialization_ens_x_coord_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.ens_x_coord.value
    assert actual == expected

# ens_y_coord
def test_segy_trace_header_initialization_ens_y_coord_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.ens_y_coord.value
    assert actual == expected

# in_line
def test_segy_trace_header_initialization_in_line_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.in_line.value
    assert actual == expected

# cross_line
def test_segy_trace_header_initialization_cross_line_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.cross_line.value
    assert actual == expected

# shotpoint
def test_segy_trace_header_initialization_shotpoint_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.shotpoint.value
    assert actual == expected

# shotpoint_scalar
def test_segy_trace_header_initialization_shotpoint_scalar_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.shotpoint_scalar.value
    assert actual == expected

# trc_value_measurement_unit
def test_segy_trace_header_initialization_trc_value_measurement_unit_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.trc_value_measurement_unit.value
    assert actual == expected

# transduction_constant_mantissa
def test_segy_trace_header_initialization_transduction_constant_mantissa_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.transduction_constant_mantissa.value
    assert actual == expected

# transduction_constant_exponent
def test_segy_trace_header_initialization_transduction_constant_exponent_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.transduction_constant_exponent.value
    assert actual == expected

# transduction_units
def test_segy_trace_header_initialization_transduction_units_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.transduction_units.value
    assert actual == expected

# device_identifier
def test_segy_trace_header_initialization_device_identifier_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.device_identifier.value
    assert actual == expected

# time_scalar
def test_segy_trace_header_initialization_time_scalar_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.time_scalar.value
    assert actual == expected

# source_type_orientation
def test_segy_trace_header_initialization_source_type_orientation_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.source_type_orientation.value
    assert actual == expected

# source_energy_direction_mantissa
def test_segy_trace_header_initialization_source_energy_direction_mantissa_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.source_energy_direction_mantissa.value
    assert actual == expected

# source_energy_direction_exponent
def test_segy_trace_header_initialization_source_energy_direction_exponent_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.source_energy_direction_exponent.value
    assert actual == expected

# source_measurement_mantissa
def test_segy_trace_header_initialization_source_measurement_mantissa_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.source_measurement_mantissa.value
    assert actual == expected

# source_measurement_exponent
def test_segy_trace_header_initialization_source_measurement_exponent_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.source_measurement_exponent.value
    assert actual == expected

# source_measurement_unit
def test_segy_trace_header_initialization_source_measurement_unit_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.source_measurement_unit.value
    assert actual == expected

# undefined233
def test_segy_trace_header_initialization_undefined233_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.undefined233.value
    assert actual == expected

# undefined237
def test_segy_trace_header_initialization_undefined237_value():
    expected = 0
    trace_header = segytools.SegyTraceHeaderRev2()
    actual = trace_header.undefined237.value
    assert actual == expected

def test_segy_trace_header_trid_vlue_setter_mapped_value():
    expected = "Seismic Data"
    trace_header = segytools.SegyTraceHeaderRev2()
    trace_header.trc_identification_code.value = 1
    actual = trace_header.trc_identification_code.mapped_value
    assert actual == expected


def test_segy_trace_header_set_header_values_num_samples():
    expected = 1200
    trace_header = segytools.SegyTraceHeaderRev2()
    trace_header.set_header_values(buf=trace_header_bytes, endianess='<')
    actual = trace_header.num_samples.value
    assert actual == expected
    
def test_segy_trace_header_set_header_values_num_samples():
    expected = 2000
    trace_header = segytools.SegyTraceHeaderRev2()
    trace_header.set_header_values(buf=trace_header_bytes, endianess='<')
    actual = trace_header.sample_interval.value
    assert actual == expected

def test_segy_trace_header_set_header_values_z_scalar():
    expected = 0.01
    trace_header = segytools.SegyTraceHeaderRev2()
    trace_header.set_header_values(buf=trace_header_bytes, endianess='<')
    actual = trace_header.z_scalar.mapped_value
    assert actual == expected

def test_segy_trace_header_set_header_values_xy_scalar():
    expected = 0.01
    trace_header = segytools.SegyTraceHeaderRev2()
    trace_header.set_header_values(buf=trace_header_bytes, endianess='<')
    actual = trace_header.xy_scalar.mapped_value
    assert actual == expected
# TODO: set_header_values() trid.mapped_value == "Seismic Data"
def test_segy_trace_header_set_header_values_trc_identification_code():
    expected = "Seismic Data"
    trace_header = segytools.SegyTraceHeaderRev2()
    trace_header.set_header_values(buf=trace_header_bytes, endianess='<')
    actual = trace_header.trc_identification_code.mapped_value
    assert actual == expected

