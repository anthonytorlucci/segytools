"""
Collection of tools for working with segy data.

The functions in this module will almost always take a segy file as input.
"""

# Copyright 2022 Anthony Torlucci

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

def textual_header(input_segy_file, txt_encoding) -> str:
    """
    Returns the textheader (first 3200 bytes) as a string.

    Parameters
    ----------
    input_segy_file : str | pathlib.Path
        Input segy file path from which to extract the textual header.
    txt_encoding : str
        Must be either 'ebcdic' or 'ascii'

    Raises
    ------
    ValueError
    
    Returns
    -------
    str
    """
    # 'rb' is "read bytes"
    with open(input_segy_file, 'rb') as fobj:
        # read the first 3200 bytes.
        # This will always be 3200 byte textual file header
        b_text_header = fobj.read(3200)
        # print(type(b_text_header))

        textheader = str()
        if txt_encoding == 'ebcdic':
            textheader = b_text_header.decode(encoding='cp500')
        elif txt_encoding == 'ascii':
            textheader = b_text_header.decode(encoding='utf-8')
        else:
            raise ValueError(f"Unable to decode textheader.")
    
        fobj.close()

    return textheader
