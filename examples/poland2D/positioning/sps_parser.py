"""
SPS parser
"""
from pandas import DataFrame

# H26
# H26      Relation Record Specification
# H26
# H26 DEFINITION OF FIELD            COLS       FORMAT       UNIT
# H26 Record identification          1- 1           A1       none
# H26 Line name (l adj)              2-17          4A4       none
# H26 Point number (right adj)      18-25          2A4       none
# H26 Point index                   26-26           I1       none
# H26 Point code                    27-28           A2       none
# H26 Static correction             29-32           I4       Msec
# H26 Point depth                   33-36          F4.1      Metre
# H26 Seismic datum                 37-40           I4       Metre
# H26 Uphole time                   41-42           I2       Msec
# H26 Water depth                   43-46          F4.1      Metre
# H26 Map grid easting              47-55          F9.1      none
# H26 Map grid northing             56-65          F10.1     none
# H26 Surface elevation             66-71          F6.1      Metre
# H26 Day of year                   72-74           I3       none
# H26 Time hhmmss                   75-80          3I2       none
# H26


class SPSLineItem(object):
    def __init__(self, s: str):
        self.line_name = s[1:17].strip()
        self.point_number = s[17:25].strip()
        self.point_index = s[25:26].strip()
        self.point_code = s[26:28].strip()
        self.static_correction = s[28:32].strip()
        self.point_depth = s[32:36].strip()
        self.seismic_datum = s[36:40].strip()
        self.uphole_time = s[40:42].strip()
        self.water_depth = s[42:46].strip()
        self.map_grid_easting = s[46:55].strip()
        self.map_grid_northing = s[55:65].strip()
        self.surface_elevation = s[65:71].strip()

    def __str__(self):
        srep = '\nsource point\n'
        srep += "Line name         : " + self.line_name + '\n'
        srep += "Point number      : " + self.point_number + '\n'
        srep += "Point index       : " + self.point_index + '\n'
        srep += "Point code        : " + self.point_code + '\n'
        srep += "Static correction : " + self.static_correction + '\n'
        srep += "Point depth       : " + self.point_depth + '\n'
        srep += "Seismic datum     : " + self.seismic_datum + '\n'
        srep += "Uphole time       : " + self.uphole_time + '\n'
        srep += "Water depth       : " + self.water_depth + '\n'
        srep += "Map grid easting  : " + self.map_grid_easting + '\n'
        srep += "Map grid northing : " + self.map_grid_northing + '\n'
        srep += "Surface elevation : " + self.surface_elevation
        return srep


class SPS(object):
    def __init__(self, f: str):
        line_names = []
        point_numbers = []
        point_indices = []
        point_codes = []
        static_corrections = []
        point_depths = []
        seismic_datums = []
        uphole_times = []
        water_depths = []
        map_grid_eastings = []
        map_grid_northings = []
        surface_elevations = []
        with open(f, "r") as fobj:
            for cnt, line in enumerate(fobj):
                if not line.startswith("H26"):
                    record = SPSLineItem(line)
                    line_names.append(record.line_name)
                    point_numbers.append(int(record.point_number))
                    point_indices.append(int(record.point_index))
                    point_codes.append(record.point_code)
                    static_corrections.append(float(record.static_correction))
                    point_depths.append(float(record.point_depth))
                    seismic_datums.append(float(record.seismic_datum))
                    uphole_times.append(float(record.uphole_time))
                    water_depths.append(float(record.water_depth))
                    map_grid_eastings.append(float(record.map_grid_easting))
                    map_grid_northings.append(float(record.map_grid_northing))
                    surface_elevations.append(float(record.surface_elevation))

            fobj.close()
        # temporary dict for dataframe constructor
        tmp_dict = dict()
        tmp_dict['line_name'] = line_names
        tmp_dict['point_number'] = point_numbers
        tmp_dict['point_index'] = point_indices
        tmp_dict['point_code'] = point_codes
        tmp_dict['static_correction'] = static_corrections
        tmp_dict['point_depth'] = point_depths
        tmp_dict['seismic_datum'] = seismic_datums
        tmp_dict['uphole_time'] = uphole_times
        tmp_dict['water_depth'] = water_depths
        tmp_dict['map_grid_easting'] = map_grid_eastings
        tmp_dict['map_grid_northing'] = map_grid_northings
        tmp_dict['surface_elevation'] = surface_elevations
        self._df = DataFrame(tmp_dict)

    def dataframe(self):
        return self._df

    def source_x(self, source_point: int):
        tmpi = self._df.loc[
            self._df['point_number'] == source_point].index.values
        return self._df.loc[tmpi[0], 'map_grid_easting']

    def source_y(self, source_point: int):
        tmpi = self._df.loc[
            self._df['point_number'] == source_point].index.values
        return self._df.loc[tmpi[0], 'map_grid_northing']

    def source_elevation(self, source_point: int):
        tmpi = self._df.loc[
            self._df['point_number'] == source_point].index.values
        return self._df.loc[tmpi[0], 'surface_elevation']

    def source_static(self, source_point: int):
        tmpi = self._df.loc[
            self._df['point_number'] == source_point].index.values
        return self._df.loc[tmpi[0], 'static_correction']

# END