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

def test_segy_file_header_initialization_lineno_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.lineno.value
    assert actual == expected

def test_segy_file_header_initialization_reelno_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.reelno.value
    assert actual == expected

def test_segy_file_header_initialization_ntrcens_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.ntrcens.value
    assert actual == expected

def test_segy_file_header_initialization_ntrcaux_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.ntrcaux.value
    assert actual == expected

def test_segy_file_header_initialization_smpint_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.smpint.value
    assert actual == expected

def test_segy_file_header_initialization_smpinto_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.smpinto.value
    assert actual == expected

def test_segy_file_header_initialization_numsmp_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.numsmp.value
    assert actual == expected

def test_segy_file_header_initialization_numsmpo_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.numsmpo.value
    assert actual == expected

def test_segy_file_header_initialization_dsfmt_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.dsfmt.value
    assert actual == expected

def test_segy_file_header_initialization_dsfmt_mapped_value():
    expected = "undefined"
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.dsfmt.mapped_value
    assert actual == expected

def test_segy_file_header_initialization_fold_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.fold.value
    assert actual == expected

def test_segy_file_header_initialization_sortcode_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.sortcode.value
    assert actual == expected

def test_segy_file_header_initialization_sortcode_mapped_value():
    expected = "Unknown"
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.sortcode.mapped_value
    assert actual == expected

def test_segy_file_header_initialization_vsumcode_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.vsumcode.value
    assert actual == expected

def test_segy_file_header_initialization_sweepfs_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.sweepfs.value
    assert actual == expected

def test_segy_file_header_initialization_sweepfe_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.sweepfe.value
    assert actual == expected

def test_segy_file_header_initialization_sweeplen_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.sweeplen.value
    assert actual == expected

def test_segy_file_header_initialization_sweepcode_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.sweepcode.value
    assert actual == expected

def test_segy_file_header_initialization_sweepcode_mapped_value():
    expected = "undefined"
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.sweepcode.mapped_value
    assert actual == expected

def test_segy_file_header_initialization_sweepchan_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.sweepchan.value
    assert actual == expected

def test_segy_file_header_initialization_sweeptprs_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.sweeptprs.value
    assert actual == expected

def test_segy_file_header_initialization_sweeptpre_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.sweeptpre.value
    assert actual == expected

def test_segy_file_header_initialization_tprtype_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.tprtype.value
    assert actual == expected

def test_segy_file_header_initialization_tprtype_mapped_value():
    expected = "undefined"
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.tprtype.mapped_value
    assert actual == expected

def test_segy_file_header_initialization_corrtrc_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.corrtrc.value
    assert actual == expected

def test_segy_file_header_initialization_corrtrc_mapped_value():
    expected = "undefined"
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.corrtrc.mapped_value
    assert actual == expected

def test_segy_file_header_initialization_bingain_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.bingain.value
    assert actual == expected

def test_segy_file_header_initialization_bingain_mapped_value():
    expected = "undefined"
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.bingain.mapped_value
    assert actual == expected

def test_segy_file_header_initialization_amprec_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.amprec.value
    assert actual == expected

def test_segy_file_header_initialization_amprec_mapped_value():
    expected = "undefined"
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.amprec.mapped_value
    assert actual == expected

def test_segy_file_header_initialization_meassys_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.meassys.value
    assert actual == expected

def test_segy_file_header_initialization_meassys_mapped_value():
    expected = "undefined"
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.meassys.mapped_value
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

def test_segy_file_header_initialization_vpolarity_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.vpolarity.value
    assert actual == expected

def test_segy_file_header_initialization_vpolarity_mapped_value():
    expected = "undefined"
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.vpolarity.mapped_value
    assert actual == expected

def test_segy_file_header_initialization_segyrev_value():
    expected = 2
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.segyrev.value
    assert actual == expected

def test_segy_file_header_initialization_fixedlen_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.fixedlen.value
    assert actual == expected

def test_segy_file_header_initialization_ntxthead_value():
    expected = 0
    file_header = segytools.SegyFileHeaderRev2()
    actual = file_header.ntxthead.value
    assert actual == expected

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

