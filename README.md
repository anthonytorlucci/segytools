# segytools

`segytools` is a simple python library that provides low level tools for analyzing and parsing segy formatted files. The tools here are esigned to aid in the analysis of "non-standard" segy files.

*IMPORTANT:* There is no `read_segy()` function per se because that assumes the data is properly formatted in which case there are other tools much better suited, e.g. [segyio](https://github.com/equinor/segyio).

Much of the project borrows from another open-source project [segpy](https://github.com/sixty-north/segpy). The files in the directory segpy are taken directly from that project.