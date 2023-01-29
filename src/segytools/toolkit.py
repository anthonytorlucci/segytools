"""Collection of tools for working with segy data"""

# standard
import textwrap

# third party

# local


def format_textheader_string(textheader):
    """Format the textheader to have each line be 80 characters long and
    return a single string.

    Parameters
    ----------
    textheader : str
        The textual header string after decoding.

    Returns
    -------
    str
        Textual header with 80 characters per line.
    """
    return "\n".join(textwrap.wrap(textheader, 80))
