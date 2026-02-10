<!-- markdownlint-disable-file MD033 MD024 -->
# Command Line Interface

## Using Hexon

Usage: `hexon [OPTIONS] TYPE:{rect|hex}`

Arguments:

- type: one of `rect`or `hex` \[required\]

Options:

- `--output       -o    PATH`  Output file
- `--png-output   -p    PATH`  PNG output file
- `--radius       -r    INTEGER`  Radius for hex map [default: 1]
- `--width        -w    INTEGER`  Width for rect map [default: 6]
- `--height       -h    INTEGER`  Height for rect map [default: 4]
- `--hex-size     -s    INTEGER`  Hex size [default: 10]
- `--orientation  -O    [pointy|flat]`  Orientation of the hexagons. `pointy` : pointy corner up, `flat` : flat side up [default: pointy]
- `--help`  Show this message and exit.
