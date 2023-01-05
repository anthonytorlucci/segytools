from context import segytools

def test_segy_header_item_value_initialization():
    expected = int(0)
    hdr_item = segytools.segy_header_item.SegyHeaderItem(name='example', value=expected)
    actual = hdr.item.value
    assert actual == expected, "SegyHeaderItem value incorrectly initialized."