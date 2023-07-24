# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## v0.2.1 (2023-07-24)

### Added
- added license to each file (issue #17)

### Changed
- replace `endianess` with `byteorder` in segy_abstract_header and segy_header_item (issue #12)

### Removed

## v0.2.0 (2023-06-04)

### Added
- read_trace_data() funtion to convert byte string to numpy array.

## v0.1.2 (2023-06-03)

### Added
- new Poland2D examples.

## v0.1.1 (2023-06-02)

### Added
- add logger option

## v0.1.0 (2023-01-15)
First minor revision.

### Fixed

### Added
- toolkit: format_text_header_string() function to format a text header string to 80 characters per line.
- test_segy_header_item: value test

### Documentation
- updated doc strings for all classes and functions using numpy doc style.
- Initialize documentation with sphinx.

