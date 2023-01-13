from context import segytools

# create data for testing
b_zero2 = int.to_bytes(int(0), length=2, byteorder='little', signed=True)
b_zero4 = int.to_bytes(int(0), length=4, byteorder='little', signed=True)

file_header_bytearray = bytearray(400)
# fill with zeros to initialize
for i in range(0,400,4):
    file_header_bytearray[i:i+4] = b_zero4

file_header_bytearray[0:4] = int.to_bytes(int(0), length=4, byteorder='little', signed=True) # jobid
file_header_bytearray[4:8] = int.to_bytes(int(0), length=4, byteorder='little', signed=True) # lineno
file_header_bytearray[8:12] = int.to_bytes(int(0), length=4, byteorder='little', signed=True) # reelno
file_header_bytearray[12:14] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # ntrcens
file_header_bytearray[14:16] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # ntrcaux
file_header_bytearray[16:18] = int.to_bytes(int(2000), length=2, byteorder='little', signed=True)  # smpint -> defualt value = 2000 microseconds or 2 milliseconds
file_header_bytearray[18:20] = int.to_bytes(int(2000), length=2, byteorder='little', signed=True)  # smpinto
file_header_bytearray[20:22] = int.to_bytes(int(2), length=2, byteorder='little', signed=True)  # numsmp
file_header_bytearray[22:24] = int.to_bytes(int(2), length=2, byteorder='little', signed=True)  # numsmpo
file_header_bytearray[24:26] = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # dsfmt -> 0:"undefined"; 1=ibm, 5=ieee NOTE: this must be set properly to read trace data!
file_header_bytearray[26:28] = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # fold
file_header_bytearray[28:30] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # sortcode -> 0:"Unknown"
file_header_bytearray[30:32] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # vsumcode
file_header_bytearray[32:34] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # sweepfs
file_header_bytearray[34:36] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # sweepfw
file_header_bytearray[36:38] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # sweeplen
file_header_bytearray[38:40] = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # sweepcode -> 0:"undefined"
file_header_bytearray[40:42] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # sweepchan
file_header_bytearray[42:44] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # sweeptprs
file_header_bytearray[44:46] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # sweeptpre
file_header_bytearray[46:48] = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # tprtype -> 0:"undefined"
file_header_bytearray[48:50] = int.to_bytes(int(2), length=2, byteorder='little', signed=True)  # corrtrc -> 0:"undefined"
file_header_bytearray[50:52] = int.to_bytes(int(2), length=2, byteorder='little', signed=True)  # bingain -> 0:"undefined"
file_header_bytearray[52:54] = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # amprec -> 0:"undefined"
file_header_bytearray[54:56] = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # meassys -> 0:"undefined"
file_header_bytearray[56:58] = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # polarity -> 0:"undefined"
file_header_bytearray[58:60] = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # vpolarity -> 0:"undefined"
file_header_bytearray[300:302] = int.to_bytes(int(2), length=2, byteorder='little', signed=True)  # segyrev -> default value=2
file_header_bytearray[302:304] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # fixedlen
file_header_bytearray[304:306] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # ntxthead


def test_segy_file_header_initialization_jobid_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.jobid.value
    assert actual == expected

def test_segy_file_header_initialization_line_number_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.line_number.value
    assert actual == expected

def test_segy_file_header_initialization_reel_number_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.reel_number.value
    assert actual == expected

def test_segy_file_header_initialization_num_traces_per_ensemble_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.num_traces_per_ensemble.value
    assert actual == expected

def test_segy_file_header_initialization_num_aux_traces_per_ensemble_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.num_aux_traces_per_ensemble.value
    assert actual == expected

def test_segy_file_header_initialization_sample_interval_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.sample_interval.value
    assert actual == expected

def test_segy_file_header_initialization_original_sample_interval_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.original_sample_interval.value
    assert actual == expected

def test_segy_file_header_initialization_num_samples_per_trace_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.num_samples_per_trace.value
    assert actual == expected

def test_segy_file_header_initialization_original_num_samples_per_trace_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.original_num_samples_per_trace.value
    assert actual == expected

def test_segy_file_header_initialization_data_sample_format_code_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.data_sample_format_code.value
    assert actual == expected

def test_segy_file_header_initialization_data_sample_format_code_mapped_value():
    expected = "undefined"
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.data_sample_format_code.mapped_value
    assert actual == expected

def test_segy_file_header_initialization_fold_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.fold.value
    assert actual == expected

def test_segy_file_header_initialization_sort_code_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.sort_code.value
    assert actual == expected

def test_segy_file_header_initialization_sort_code_mapped_value():
    expected = "Unknown"
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.sort_code.mapped_value
    assert actual == expected

def test_segy_file_header_initialization_vertical_sum_code_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.vertical_sum_code.value
    assert actual == expected

def test_segy_file_header_initialization_sweep_freq_start_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.sweep_freq_start.value
    assert actual == expected

def test_segy_file_header_initialization_sweep_freq_end_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.sweep_freq_end.value
    assert actual == expected

def test_segy_file_header_initialization_sweep_length_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.sweep_length.value
    assert actual == expected

def test_segy_file_header_initialization_sweep_code_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.sweep_code.value
    assert actual == expected

def test_segy_file_header_initialization_sweep_code_mapped_value():
    expected = "undefined"
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.sweep_code.mapped_value
    assert actual == expected

def test_segy_file_header_initialization_sweep_chan_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.sweep_chan.value
    assert actual == expected

def test_segy_file_header_initialization_sweep_taper_length_start_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.sweep_taper_length_start.value
    assert actual == expected

def test_segy_file_header_initialization_sweep_taper_length_end_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.sweep_taper_length_end.value
    assert actual == expected

def test_segy_file_header_initialization_taper_type_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.taper_type.value
    assert actual == expected

def test_segy_file_header_initialization_taper_type_mapped_value():
    expected = "undefined"
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.taper_type.mapped_value
    assert actual == expected

def test_segy_file_header_initialization_correlated_traces_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.correlated_traces.value
    assert actual == expected

def test_segy_file_header_initialization_correlated_traces_mapped_value():
    expected = "undefined"
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.correlated_traces.mapped_value
    assert actual == expected

def test_segy_file_header_initialization_binary_gain_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.binary_gain.value
    assert actual == expected

def test_segy_file_header_initialization_binary_gain_mapped_value():
    expected = "undefined"
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.binary_gain.mapped_value
    assert actual == expected

def test_segy_file_header_initialization_amp_recovery_method_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.amp_recovery_method.value
    assert actual == expected

def test_segy_file_header_initialization_amp_recovery_method_mapped_value():
    expected = "undefined"
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.amp_recovery_method.mapped_value
    assert actual == expected

def test_segy_file_header_initialization_measurement_system_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.measurement_system.value
    assert actual == expected

def test_segy_file_header_initialization_measurement_system_mapped_value():
    expected = "undefined"
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.measurement_system.mapped_value
    assert actual == expected

def test_segy_file_header_initialization_polarity_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.polarity.value
    assert actual == expected

def test_segy_file_header_initialization_polarity_mapped_value():
    expected = "undefined"
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.polarity.mapped_value
    assert actual == expected

def test_segy_file_header_initialization_vibe_polarity_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.vibe_polarity.value
    assert actual == expected

def test_segy_file_header_initialization_vibe_polarity_mapped_value():
    expected = "undefined"
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.vibe_polarity.mapped_value
    assert actual == expected

def test_segy_file_header_initialization_segy_revision_value():
    expected = 2
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.segy_revision.value
    assert actual == expected

def test_segy_file_header_initialization_fixed_length_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.fixed_length.value
    assert actual == expected

def test_segy_file_header_initialization_num_txt_headers_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.num_txt_headers.value
    assert actual == expected

def test_segy_file_header_mapped_sample_format():
    expected = 'ibm'
    file_header = segytools.segy_file_header.SegyFileHeaderRev2()
    file_header.set_header_values(buf=bytes(file_header_bytearray), endianess='<')
    actual = file_header.data_sample_format_code.mapped_value
    assert actual == expected

def test_segy_file_header_segy_type():
    expected = 'ibm'
    file_header = segytools.segy_file_header.SegyFileHeaderRev2()
    file_header.set_header_values(buf=bytes(file_header_bytearray), endianess='<')
    actual = file_header.segy_type()
    assert actual == expected

