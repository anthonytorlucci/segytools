"""segytools"""

from importlib.metadata import version
__version__ = version("segytools")

from .segy_header_item import SegyHeaderItem
from .segy_abstract_header import SegyAbstractHeader
from .segy_file_header import SegyFileHeaderRev2
from .segy_trace_header import SegyTraceHeaderRev2
