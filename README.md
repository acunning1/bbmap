# bbmap - Broadbandmap.gov API exercise

**Author**: Andy Cunningham - 5/8/17

A CLI utility written in Python to retrieve demographic data for a specified set of U.S. states from a public API and output that data in a specified format.

- **[Assumptions](https://github.com/acunning1/bbmap#assumptions)**
- **[Requirements](https://github.com/acunning1/bbmap#requirements)**
- **[Installation](https://github.com/acunning1/bbmap#installation)**
- **[Usage](https://github.com/acunning1/bbmap#usage)**

## Assumptions
- Exercise permits use of a math lib for weighted average calculation
- Weighted average uses number of households as weights rather than population
- User is familiar enough with CLI operation to encapsulate input of states with whitespaces in quotations, i.e. 'new york'
- Weighted average should be displayed as a percentage float, rather than 0 integer
- Additional text regarding output to improve clarity/usability is desired

## Requirements:
- Python 2.7.x: https://www.python.org/
- Python libraries:
    - **[argparse](https://docs.python.org/3/library/argparse.html)** (default)
    - **[csv](https://docs.python.org/3/library/csv.html)** (default)
    - **[requests](http://docs.python-requests.org/en/master/)**
      - **[urllib3](https://urllib3.readthedocs.io/en/latest/)**
    - **[numpy](http://www.numpy.org/)**

## Installation

- **[Step 1 - Verify Python installation requirement](https://github.com/acunning1/bbmap#step-1---verify-python-installation-requirement)**
- **[Step 2 - Install required Python libraries](https://github.com/acunning1/bbmap#step-2---install-required-python-libraries)**
- **[Step 3 - Clone or download repository](https://github.com/acunning1/bbmap#step-3---clone-or-download-repository)**
- **[Troubleshooting](https://github.com/acunning1/bbmap#troubleshooting)**

### Step 1 - Verify Python installation requirement:

**Python 2.7.x**

```
$ python
Python 2.7.13 (default, Apr  4 2017, 08:47:57)
[GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.38)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
```

If no Python (or old version) is found, [install/update](https://www.python.org/downloads/mac-osx/) using the Python installer at https://www.python.org/downloads/mac-osx/.

### Step 2 - Install required Python libraries:

* **[argparse](https://docs.python.org/3/library/argparse.html)** (default) - Accepts arguments from command-line
* **[csv](https://docs.python.org/3/library/csv.html)** (default) - Writes results to CSV file
* **[requests](http://docs.python-requests.org/en/master/)** - Performs API requests
* **[urllib3](https://urllib3.readthedocs.io/en/latest/)** - Dependency for **requests** library SSL connection
* **[numpy](http://www.numpy.org/)** - Performs weighted average calculation

The **[argparse](https://docs.python.org/3/library/argparse.html)** and **[csv](https://docs.python.org/3/library/csv.html)** libraries should be installed by default.

The following additional libraries will likely need to be installed using `pip install`:

* **[requests](http://docs.python-requests.org/en/master/)**
* SSL Dependency: **[urllib3](https://urllib3.readthedocs.io/en/latest/)**
* **[numpy](http://www.numpy.org/)**

```
$ pip install requests urllib3 numpy
```

>`!` Note: If `pip install` fails, follow instructions for [installing/updating](http://docs.python-guide.org/en/latest/starting/installation/) Python above.

If needed, you can confirm installation status and versions of these libraries using `pip show`:

```
$ pip show requests urllib3 numpy
```

### Step 3 - Clone or download repository

For detailed instructions, refer to GitHub documentation:

https://help.github.com/articles/cloning-a-repository/

### Troubleshooting:

**1) ImportError: No Module named requests**

Verify `PYTHONPATH` is properly pointing to where pip has installed the **requests** package

Quick fix:

```
$ export PYTHONPATH="${PYTHONPATH}/usr/local/lib/python2.7/site-packages:/usr/lib/python2.7/site-packages"
```

**2) SNIMissingWarning; InsecurePlatformWarning**

See related `urllib3` documentation:
http://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings

**3) python importerror dlopen symbol not found**

Possible issue due to installing Python using `brew`.

Quick fix:

```
brew unlink python && brew link python
```

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
