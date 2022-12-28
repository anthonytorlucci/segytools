"""
XPS parser
"""
import numpy
from pandas import DataFrame, Series

# H26
# H26      Relation Record Specification
# H26
# H26 DEFINITION OF FIELD            COLS       FORMAT       UNIT
# H26 Record identification          1- 1           A1       none
# H26 Field tape number (l adj)      2- 7          3A2       none
# H26 Field record number            8-11           I4       none
# H26 Field record increment        12-12           I1       none
# H26 Instrument code               13-13           A1       none
# H26 Line name (left adj)          14-29          4A4       none
# H26 Point number (right adj)      30-37          2A4       none
# H26 Point index                   38-38           I1       none
# H26 From channel                  39-42           I4       none
# H26 To channel                    43-46           I4       none
# H26 Channel increment             47-47           I1       none
# H26 Line name (left adj)          48-63          4A4       none
# H26 From receiver (right adj)     64-71          2A4       none
# H26 To receiver (right adj)       72-79          2A4       none
# H26 Receiver index                80-80           A1       none
# H26

class XPSLineItem(object):
    def __init__(self, s: str):
        self.field_tape_number = s[1:7].strip()
        self.field_record_number = s[7:11].strip()
        self.field_record_increment = s[11:12].strip()
        self.instrument_code = s[12:13].strip()
        self.sline_name = s[13:29].strip()
        self.point_number = s[29:37].strip()
        self.point_index = s[37:38].strip()
        self.from_channel = s[38:42].strip()
        self.to_channel = s[42:46].strip()
        self.channel_increment = s[46:47].strip()
        self.rline_name = s[47:63].strip()
        self.from_receiver = s[63:71].strip()
        self.to_receiver = s[71:79].strip()
        self.receiver_index = s[79:80].strip()

    def __str__(self):
        srep = '\nsource receiver spread\n'
        srep += 'Field tape number      : ' + self.field_tape_number + '\n'
        srep += 'Field record number    : ' + self.field_record_number + '\n'
        srep += 'Field record increment : ' + self.field_record_increment + '\n'
        srep += 'Instrument code        : ' + self.instrument_code + '\n'
        srep += 'Source line name       : ' + self.sline_name + '\n'
        srep += 'Point number           : ' + self.point_number + '\n'
        srep += 'Point index            : ' + self.point_index + '\n'
        srep += 'From channel           : ' + self.from_channel + '\n'
        srep += 'To channel             : ' + self.to_channel + '\n'
        srep += 'Channel increment      : ' + self.channel_increment + '\n'
        srep += 'Receiver line name     : ' + self.rline_name + '\n'
        srep += 'From receiver          : ' + self.from_receiver + '\n'
        srep += 'To receiver            : ' + self.to_receiver + '\n'
        srep += 'Receiver index         : ' + self.receiver_index
        return srep

class XPS(object):
    def __init__(self, f: str):
        field_tape_numbers = []
        field_record_numbers = []
        field_record_increments = []
        instrument_codes = []
        sline_names = []
        point_numbers = []
        point_indices = []
        from_channels = []
        to_channels = []
        channel_increments = []
        rline_names = []
        from_receivers = []
        to_receivers = []
        receiver_indices = []
        with open(f, "r") as fobj:
            for cnt, line in enumerate(fobj):
                if not line.startswith("H26"):
                    record = XPSLineItem(line)
                    field_tape_numbers.append(int(record.field_tape_number))
                    field_record_numbers.append(int(record.field_record_number))
                    field_record_increments.append(int(record.field_record_increment))
                    instrument_codes.append(record.instrument_code)
                    sline_names.append(record.sline_name)
                    point_numbers.append(int(record.point_number))
                    point_indices.append(int(record.point_index))
                    from_channels.append(int(record.from_channel))
                    to_channels.append(int(record.to_channel))
                    channel_increments.append(int(record.channel_increment))
                    rline_names.append(record.rline_name)
                    from_receivers.append(int(record.from_receiver))
                    to_receivers.append(int(record.to_receiver))
                    receiver_indices.append(int(record.receiver_index))

            fobj.close()
        # temporary dict for dataframe constructor
        tmp_dict = dict()
        tmp_dict['field_tape_number'] = field_tape_numbers
        tmp_dict['field_record_number'] = field_record_numbers
        tmp_dict['field_record_increment'] = field_record_increments
        tmp_dict['instrument_code'] = instrument_codes
        tmp_dict['sline_name'] = sline_names
        tmp_dict['point_number'] = point_numbers
        tmp_dict['point_index'] = point_indices
        tmp_dict['from_channel'] = from_channels
        tmp_dict['to_channel'] = to_channels
        tmp_dict['channel_increment'] = channel_increments
        tmp_dict['rline_name'] = rline_names
        tmp_dict['from_receiver'] = from_receivers
        tmp_dict['to_receiver'] = to_receivers
        tmp_dict['receiver_index'] = receiver_indices
        self._df = DataFrame(tmp_dict)

    def dataframe(self):
        return self._df

    def source_point(self, ffid: int):
        tmpi = self._df.loc[self._df['field_record_number'] == ffid].index.values
        return self._df.loc[tmpi[0], 'point_number']

    def reciever_station(self, ffid: int, chan: int):
        tmpi = self._df.loc[self._df['field_record_number'] == ffid].index.values
        first_chan = self._df.loc[tmpi[0], 'from_channel']
        last_chan = self._df.loc[tmpi[0], 'to_channel']
        first_rec = self._df.loc[tmpi[0], 'from_receiver']
        last_rec = self._df.loc[tmpi[0], 'to_receiver']
        chan_linspace = numpy.linspace(start=first_chan, stop=last_chan, num=last_chan-first_chan+1, endpoint=True, dtype=numpy.dtype(int))
        recs_linspace = numpy.linspace(start=first_rec, stop=last_rec, num=last_chan-first_chan+1, endpoint=True, dtype=numpy.dtype(int))
        recstation = recs_linspace[numpy.nonzero(chan_linspace == chan)]
        if not recstation.size == 0:
            rvalue = recstation[0]
        else:
            rvalue = 0
        return rvalue

    def receiver_stations(self, ffid: int):
        tmpi = self._df.loc[self._df['field_record_number'] == ffid].index.values
        first_chan = self._df.loc[tmpi[0], 'from_channel']
        last_chan = self._df.loc[tmpi[0], 'to_channel']
        first_rec = self._df.loc[tmpi[0], 'from_receiver']
        last_rec = self._df.loc[tmpi[0], 'to_receiver']
        chan_linspace = numpy.linspace(start=first_chan, stop=last_chan, num=last_chan - first_chan + 1, endpoint=True, dtype=numpy.dtype(int))
        recs_linspace = numpy.linspace(start=first_rec, stop=last_rec, num=last_chan - first_chan + 1, endpoint=True, dtype=numpy.dtype(int))
        sr = Series(data=recs_linspace, index=chan_linspace)
        return sr

# END