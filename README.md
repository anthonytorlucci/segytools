# segytools

`segytools` is a simple python library that provides low level tools for analyzing and parsing segy formatted files. It is a fork of [segpy](https://github.com/sixty-north/segpy) using much of the same code with a slightly different api and goal. There is no `read_segy()` function per se because that assumes the data is properly formatted in which case there are other tools much better suited, e.g. [segyio](https://github.com/equinor/segyio). The tools here are designed to aid in the analysis of "non-standard" segy files and converting those files to a more standard form easily read by other third party software.

Currently only segy revision 2 file header and trace header formats are provided. However, custom header containers can be created by inheriting `SegyAbstractHeader`.

Files taken from and potentially modified from [segpy](https://github.com/sixty-north/segpy) are:
* ibm_float.py
* datatypes.py
* toolkit.py
* utils.py

