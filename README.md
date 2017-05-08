# bbmap - Broadbandmap.gov API exercise

### About

A command-line utility written in Python that retrieves demographic data for a specified set of U.S. states from a public API and outputs that data in the requested format.

### Installation

>to do

### Usage

From the command-line while in the project directory, input the following...

**For help or instructions**:

```
bbmap $ python bbmap.py -h
```

**To request a weighted average for a comma-delimited list of state names**:

Default, no options

```
bbmap $ python bbmap.py <state1>,<state2>,<state3>
```

Using -a or --avg optional input flags

```
bbmap $ python bbmap.py <state1>,<state2>,<state3> -a
```
```
bbmap $ python bbmap.py <state1>,<state2>,<state3> --avg
```

**To request a csv export file for a comma-delimited list of state names**:

*CSV contents*:
`<state name>`, `<population>`, `<households>`, `<income below poverty>`, `<median income>`

```
bbmap $ python bbmap.py <state1>,<state2>,<state3> -c
```

```
bbmap $ python bbmap.py <state1>,<state2>,<state3> --csv
```

### Assumptions
- Exercise permits use of a math lib for weighted average calculation
- Weighted average uses number of households as weights rather than population
- User is familiar enough with CLI operation to encapsulate input of states with whitespaces in quotations, i.e. 'new york'
- Weighted average should be displayed as a percentage float, rather than 0 integer
- Additional text regarding output to improve clarity/usability is desired
