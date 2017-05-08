# bbmap - Broadbandmap.gov API exercise

**Author**: Andy Cunningham - 5/8/17

A CLI utility written in Python to retrieve demographic data for a specified set of U.S. states from a public API and outputs that data in a specified format.

- **[Requirements](https://github.com/acunning1/bbmap#requirements)**
- **[Installation](https://github.com/acunning1/bbmap#installation)**
- **[Usage](https://github.com/acunning1/bbmap#usage)**
- **[Assumptions](https://github.com/acunning1/bbmap#assumptions)**

## Requirements:
- Python 2.7.x: https://www.python.org/
- Python libraries:
    - **[argparse](https://docs.python.org/3/library/argparse.html)** (default)
    - **[csv](https://docs.python.org/3/library/csv.html)** (default)
    - **[requests](http://docs.python-requests.org/en/master/)**
      - **[urllib3](https://urllib3.readthedocs.io/en/latest/)**
    - **[numpy](http://www.numpy.org/)**

## Installation

###Step 1 - Verify Python installation requirement:

**Python 2.7.x**

```
$ python
Python 2.7.13 (default, Apr  4 2017, 08:47:57)
[GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.38)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
```

If no Python (or old version) is found, [install/update](http://docs.python-guide.org/en/latest/starting/installation/) using package manager of choice:

For example, using **[homebrew](https://brew.sh/)**:

```
$ brew install python
```

>`!` Note: Once Python has been installed or updated, you may need to log out and back in for changes to take effect

###Step 2 - Install required Python libraries:

Python libraries:
    - **[argparse](https://docs.python.org/3/library/argparse.html)** (default)
    - **[csv](https://docs.python.org/3/library/csv.html)** (default)
    - **[requests](http://docs.python-requests.org/en/master/)**
      - **[urllib3](https://urllib3.readthedocs.io/en/latest/)**
    - **[numpy](http://www.numpy.org/)**

The **[argparse](https://docs.python.org/3/library/argparse.html)** and **[csv](https://docs.python.org/3/library/csv.html)** libraries should be installed by default.

The following additional libraries will likely need to be installed using `pip install`:

>`!` Note: If `pip install` fails, follow instructions for [installing/updating](http://docs.python-guide.org/en/latest/starting/installation/) Python above.

- `requests`
- `urllib3` (dependency for `requests`)
- `numpy`

```
$ pip install requests, urllib3, numpy
```

###Step 3 - Clone or download repository

For detailed instructions, refer to GitHub documentation:

https://help.github.com/articles/cloning-a-repository/

## Usage

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
`<geographyName>`, `<population>`, `<households>`, `<incomeBelowPoverty>`, `<medianIncome>`

```
bbmap $ python bbmap.py <state1>,<state2>,<state3> -c
```

```
bbmap $ python bbmap.py <state1>,<state2>,<state3> --csv
```

## Assumptions
- User is expected to be running on macOS X
- Exercise permits use of a math lib for weighted average calculation
- Weighted average uses number of households as weights rather than population
- User is familiar enough with CLI operation to encapsulate input of states with whitespaces in quotations, i.e. 'new york'
- Weighted average should be displayed as a percentage float, rather than 0 integer
- Additional text regarding output to improve clarity/usability is desired
