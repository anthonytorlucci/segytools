from context import segytools

# create data for testing
b_zero2 = int.to_bytes(int(0), length=2, byteorder='little', signed=True)
b_zero4 = int.to_bytes(int(0), length=4, byteorder='little', signed=True)

file_header_bytearray = bytearray(400)
# fill with zeros to initialize
for i in range(0,400,4):
    file_header_bytearray[i:i+4] = b_zero4


b_jobid = int.to_bytes(int(0), length=4, byteorder='little', signed=True)
file_header_bytearray[0:4] = b_jobid

b_lineno = int.to_bytes(int(0), length=4, byteorder='little', signed=True)
file_header_bytearray[4:8] = b_lineno

b_reelno = int.to_bytes(int(0), length=4, byteorder='little', signed=True)
file_header_bytearray[8:12] = b_reelno

b_ntrcens = int.to_bytes(int(0), length=2, byteorder='little', signed=True)
file_header_bytearray[12:14] = b_ntrcens

b_ntrcaux = int.to_bytes(int(0), length=2, byteorder='little', signed=True)
file_header_bytearray[14:16] = b_ntrcaux

b_smpint = int.to_bytes(int(2000), length=2, byteorder='little', signed=True)  # 2000 microseconds or 2 milliseconds
file_header_bytearray[16:18] = b_smpint

b_smpinto = int.to_bytes(int(2000), length=2, byteorder='little', signed=True)
file_header_bytearray[18:20] = b_smpinto

b_numsmp = int.to_bytes(int(2), length=2, byteorder='little', signed=True)
file_header_bytearray[20:22] = b_numsmp

b_numsmpo = int.to_bytes(int(2), length=2, byteorder='little', signed=True)
file_header_bytearray[22:24] = b_numsmpo

b_dsfmt = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # 1=ibm, 5=ieee
file_header_bytearray[24:26] = b_dsfmt

b_fold = int.to_bytes(int(1), length=2, byteorder='little', signed=True)
file_header_bytearray[26:28] = b_fold

b_sortcode = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # see mapping TRACE_SORTING_CODE in segy_file_header.py
file_header_bytearray[28:30] = b_sortcode

b_vsumcode = int.to_bytes(int(0), length=2, byteorder='little', signed=True)
file_header_bytearray[30:32] = b_vsumcode

b_sweepfs = int.to_bytes(int(0), length=2, byteorder='little', signed=True)
file_header_bytearray[32:34] = b_sweepfs

b_sweepfw = int.to_bytes(int(0), length=2, byteorder='little', signed=True)
file_header_bytearray[34:36] = b_sweepfw

b_sweeplen = int.to_bytes(int(0), length=2, byteorder='little', signed=True)
file_header_bytearray[36:38] = b_sweeplen

b_sweepcode = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # see mapping SWEEP_TYPE_CODE in segy_file_header.py
file_header_bytearray[38:40] = b_sweepcode

b_sweepchan = int.to_bytes(int(0), length=2, byteorder='little', signed=True)
file_header_bytearray[40:42] = b_sweepchan

b_sweeptprs = int.to_bytes(int(0), length=2, byteorder='little', signed=True)
file_header_bytearray[42:44] = b_sweeptprs

b_sweeptpre = int.to_bytes(int(0), length=2, byteorder='little', signed=True)
file_header_bytearray[44:46] = b_sweeptpre

b_tprtype = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # see mapping TAPER_TYPE in segy_file_header.py
file_header_bytearray[46:48] = b_tprtype

b_corrtrc = int.to_bytes(int(2), length=2, byteorder='little', signed=True)  # see mapping CORRELATED_DATA_TRACES in segy_file_header.py
file_header_bytearray[48:50] = b_corrtrc

b_bingain = int.to_bytes(int(2), length=2, byteorder='little', signed=True)  # see mapping BINARY_GAIN_RECOVERED in segy_file_header.py
file_header_bytearray[50:52] = b_bingain

b_amprec = int.to_bytes(int(1), length=2, byteorder='little', signed=True) # see mapping AMPLITUDE_RECOVERY_METHOD in segy_file_header.py
file_header_bytearray[52:54] = b_amprec

b_meassys = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # see mapping MEASUREMENT_SYSTEM in segy_file_header.py
file_header_bytearray[54:56] = b_meassys

b_polarity = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # see mapping IMPULSE_SIGNAL_POLARITY in segy_file_header.py
file_header_bytearray[56:58] = b_polarity

b_vpolarity = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # see mapping VIBRATORY_POLARITY_CODE in segy_file_header.py
file_header_bytearray[58:60] = b_vpolarity

b_segyrev = int.to_bytes(int(2), length=2, byteorder='little', signed=True)
file_header_bytearray[300:302] = b_segyrev

b_fixedlen = int.to_bytes(int(0), length=2, byteorder='little', signed=True)
file_header_bytearray[302:304] = b_fixedlen

b_ntxthead = int.to_bytes(int(0), length=2, byteorder='little', signed=True)
file_header_bytearray[304:306] = b_ntxthead

def test_segy_file_header_mapped_sample_format():
    expected = 'ibm'
    file_header = segytools.segy_file_header.SegyFileHeaderRev2()
    file_header.set_header_values(buf=bytes(file_header_bytearray), endianess='<')
    actual = file_header.dsfmt.mapped_value
    assert actual == expected

def test_segy_file_header_segy_type():
    expected = 'ibm'
    file_header = segytools.segy_file_header.SegyFileHeaderRev2()
    file_header.set_header_values(buf=bytes(file_header_bytearray), endianess='<')
    actual = file_header.segy_type()
    assert actual == expected

