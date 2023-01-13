from context import segytools

from segytools.segy_trace_header import SegyTraceHeaderRev2

# create data for testing
b_zero2 = int.to_bytes(int(0), length=2, byteorder='little', signed=True)
b_zero4 = int.to_bytes(int(0), length=4, byteorder='little', signed=True)

file_header_bytearray = bytearray(240)
# fill with zeros to initialize
for i in range(0,240,4):
    file_header_bytearray[i:i+4] = b_zero4

file_header_bytearray[0:4] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # trseql
file_header_bytearray[4:8] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # trseqf
file_header_bytearray[8:12] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # ffid
file_header_bytearray[12:16] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # trffid
file_header_bytearray[16:20] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # shot
file_header_bytearray[20:24] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # ens
file_header_bytearray[24:28] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # trcens
file_header_bytearray[28:30] = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # trid -> "Seismic Data"
file_header_bytearray[30:32] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # vsum
file_header_bytearray[32:34] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # hsum
file_header_bytearray[34:36] = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # datause -> "Production"
file_header_bytearray[36:40] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # offset
file_header_bytearray[40:44] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # recelev
file_header_bytearray[44:48] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # srcelev
file_header_bytearray[48:52] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # srcdepth
file_header_bytearray[52:56] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # datmrec
file_header_bytearray[56:60] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # datmsrc
file_header_bytearray[60:64] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # h2ozsrc
file_header_bytearray[64:68] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # h2ozrec
file_header_bytearray[68:70] = int.to_bytes(int(-100), length=2, byteorder='little', signed=True)  # zsclr -> 0.01
file_header_bytearray[70:72] = int.to_bytes(int(-100), length=2, byteorder='little', signed=True)  # xysclr -> 0.01
file_header_bytearray[72:76] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # srcx
file_header_bytearray[76:80] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # srcy
file_header_bytearray[80:84] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # recx
file_header_bytearray[84:88] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # recy
file_header_bytearray[88:90] = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # coordunits -> "Length (meters or feet)"
file_header_bytearray[90:92] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # weathvel
file_header_bytearray[92:94] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # subweathvel
file_header_bytearray[94:96] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # uptsrc
file_header_bytearray[96:98] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # uptrec
file_header_bytearray[98:100] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # srcstat
file_header_bytearray[100:102] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # recstat
file_header_bytearray[102:104] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # totstat
file_header_bytearray[104:106] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # laga
file_header_bytearray[106:108] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # lagb
file_header_bytearray[108:110] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # delayt
file_header_bytearray[110:112] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # mutes
file_header_bytearray[112:114] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # mutee
file_header_bytearray[114:116] = int.to_bytes(int(1200), length=2, byteorder='little', signed=True)  # numsmp
file_header_bytearray[116:118] = int.to_bytes(int(2000), length=2, byteorder='little', signed=True)  # smpint
file_header_bytearray[118:120] = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # gaintype -> "fixed"
file_header_bytearray[120:122] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # gainconst
file_header_bytearray[122:124] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # initgain
file_header_bytearray[124:126] = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # corrx -> "yes"
file_header_bytearray[126:128] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # sweepfs
file_header_bytearray[128:130] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # sweepfe
file_header_bytearray[130:132] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # sweeplen
file_header_bytearray[132:134] = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # sweeptype -> "linear"
file_header_bytearray[134:136] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # sweeptprs
file_header_bytearray[136:138] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # sweeptpre
file_header_bytearray[138:140] = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # tprtype -> "linear"
file_header_bytearray[140:142] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # aliasfilf
file_header_bytearray[142:144] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # aliasfils
file_header_bytearray[144:146] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # notchfilf
file_header_bytearray[146:148] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # notchfils
file_header_bytearray[148:150] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # lowcutf
file_header_bytearray[150:152] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # highcutf
file_header_bytearray[152:154] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # lowcuts
file_header_bytearray[154:156] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # highcuts
file_header_bytearray[156:158] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # year
file_header_bytearray[158:160] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # day
file_header_bytearray[160:162] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # hour
file_header_bytearray[162:164] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # minute
file_header_bytearray[164:166] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # second
file_header_bytearray[166:168] = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # timebasis -> "Local"
file_header_bytearray[168:170] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # trcweight
file_header_bytearray[170:172] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # groupnum
file_header_bytearray[172:174] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # groupnumfirst
file_header_bytearray[174:176] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # groupnumlast
file_header_bytearray[176:178] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # gapsize
file_header_bytearray[178:180] = int.to_bytes(int(1), length=2, byteorder='little', signed=True)  # overtrvl -> "down (or behind)"
file_header_bytearray[180:184] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # ensx
file_header_bytearray[184:188] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # ensy
file_header_bytearray[188:192] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # il
file_header_bytearray[192:196] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # xl
file_header_bytearray[196:200] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # shotpoint
file_header_bytearray[200:202] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # shotptsclr
file_header_bytearray[202:204] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # trcvalmeas -> "Unknown"
file_header_bytearray[204:208] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # transconstm
file_header_bytearray[208:210] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # transconste
file_header_bytearray[210:212] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # transunits -> "Unknown"
file_header_bytearray[212:214] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # deviceid
file_header_bytearray[214:216] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # timesclr
file_header_bytearray[216:218] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # srctypeor -> "Unknown"
file_header_bytearray[218:222] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # srcdirm
file_header_bytearray[222:224] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # srcdire
file_header_bytearray[224:228] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # srcmeasm
file_header_bytearray[228:230] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # srcmease
file_header_bytearray[230:232] = int.to_bytes(int(0), length=2, byteorder='little', signed=True)  # srcmeasu -> "Unknown"
file_header_bytearray[232:236] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # 233
file_header_bytearray[236:240] = int.to_bytes(int(0), length=4, byteorder='little', signed=True)  # 233

def test_segy_trace_header_initialization_trseql_value():
    expected = 0
    trace_header = SegyTraceHeaderRev2()
    actual = trace_header.trseql.value
    assert actual == expected

def test_segy_trace_header_initialization_trseqf_value():
    expected = 0
    trace_header = SegyTraceHeaderRev2()
    actual = trace_header.trseqf.value
    assert actual == expected

def test_segy_trace_header_initialization_ffid_value():
    expected = 0
    trace_header = SegyTraceHeaderRev2()
    actual = trace_header.ffid.value
    assert actual == expected

def test_segy_trace_header_initialization_trffid_value():
    expected = 0
    trace_header = SegyTraceHeaderRev2()
    actual = trace_header.trffid.value
    assert actual == expected

def test_segy_trace_header_initialization_energysrcnum_value():
    expected = 0
    trace_header = SegyTraceHeaderRev2()
    actual = trace_header.energysrcnum.value
    assert actual == expected

def test_segy_trace_header_initialization_ens_value():
    expected = 0
    trace_header = SegyTraceHeaderRev2()
    actual = trace_header.ens.value
    assert actual == expected

def test_segy_trace_header_initialization_trcens_value():
    expected = 0
    trace_header = SegyTraceHeaderRev2()
    actual = trace_header.trcens.value
    assert actual == expected

def test_segy_trace_header_initialization_trid_value():
    expected = 0
    trace_header = SegyTraceHeaderRev2()
    actual = trace_header.ffid.value
    assert actual == expected

def test_segy_trace_header_initialization_trid_mapped_value():
    expected = "Unknown"
    trace_header = SegyTraceHeaderRev2()
    actual = trace_header.trid.mapped_value
    assert actual == expected

def test_segy_trace_header_initialization_vsum_value():
    expected = 0
    trace_header = SegyTraceHeaderRev2()
    actual = trace_header.vsum.value
    assert actual == expected

def test_segy_trace_header_initialization_hsum_value():
    expected = 0
    trace_header = SegyTraceHeaderRev2()
    actual = trace_header.hsum.value
    assert actual == expected

def test_segy_trace_header_initialization_datuse_value():
    expected = 1
    trace_header = SegyTraceHeaderRev2()
    actual = trace_header.datuse.value
    assert actual == expected

def test_segy_trace_header_initialization_datuse_mapped_value():
    expected = "Production"
    trace_header = SegyTraceHeaderRev2()
    actual = trace_header.datuse.mapped_value
    assert actual == expected

def test_segy_trace_header_initialization_offset_value():
    expected = 0
    trace_header = SegyTraceHeaderRev2()
    actual = trace_header.offset.value
    assert actual == expected

def test_segy_trace_header_initialization_recelev_value():
    expected = 0
    trace_header = SegyTraceHeaderRev2()
    actual = trace_header.recelev.value
    assert actual == expected

def test_segy_trace_header_initialization_srcelev_value():
    expected = 0
    trace_header = SegyTraceHeaderRev2()
    actual = trace_header.srcelev.value
    assert actual == expected

def test_segy_trace_header_initialization_srcdepth_value():
    expected = 0
    trace_header = SegyTraceHeaderRev2()
    actual = trace_header.srcdepth.value
    assert actual == expected

def test_segy_trace_header_initialization_datmrec_value():
    expected = 0
    trace_header = SegyTraceHeaderRev2()
    actual = trace_header.datmrec.value
    assert actual == expected

def test_segy_trace_header_initialization_datmsrc_value():
    expected = 0
    trace_header = SegyTraceHeaderRev2()
    actual = trace_header.datmsrc.value
    assert actual == expected

def test_segy_trace_header_initialization_h2ozsrc_value():
    expected = 0
    trace_header = SegyTraceHeaderRev2()
    actual = trace_header.h2ozsrc.value
    assert actual == expected

def test_segy_trace_header_initialization_h2ozrec_value():
    expected = 0
    trace_header = SegyTraceHeaderRev2()
    actual = trace_header.h2ozrec.value
    assert actual == expected




def test_segy_trace_header_trid_vlue_setter_mapped_value():
    expected = "Seismic Data"
    trace_header = SegyTraceHeaderRev2()
    trace_header.trid.value = 1
    actual = trace_header.trid.mapped_value
    assert actual == expected


# TODO: set_header_values() numsmp==1200 
# TODO: set_header_values() numsmp==1200 smpint=2000
# TODO: set_header_values() zsclr.mapped_value == -100
# TODO: set_header_values() xysclr.mapped_value == -100
# TODO: set_header_values() trid.mapped_value == "Seismic Data"

