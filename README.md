# segytools

`segytools` is a simple python library that provides low level tools for analyzing and parsing segy formatted files. There is no `read_segy()` function per se because that assumes the data is properly formatted in which case there are other tools much better suited, e.g. [segyio](https://github.com/equinor/segyio). The tools here are designed to aid in the analysis of "non-standard" segy files and converting those files to a more standard form easily read by other third party software.

Currently only segy revision 2 file header and trace header formats are provided. However, custom header containers can be created by inheriting `SegyAbstractHeader`.

Originally, much of the work had been derived from another open-source segy package [segpy](https://github.com/sixty-north/segpy), but version `0.1.0` has been almost completely rewritten. IBM float conversion is done with [enthought/ibm2ieee](https://github.com/enthought/ibm2ieee).
