# Particle movement simulator

Simulates the movement of a particle on one dimension under the presence of an electric potencial function V(x). Includes a "real time" graph view for the generated position vs time function. Project part of physics class 2019 [UVG](https://uvg.ed.gt)

# Table of content
1. [Installation](#Installation)
1. [Technical explanation](#Technical-explanation)
1. [Usage](#Usage)
1. [License](#License)

## Installation

Clone the git repo:

```
$ git clone url
```

Installing requirements:

```
$ cd particle-movement
$ pip install -r requirements.txt
```
## Technical explanation
Missing

## Usage

**Usage:** main.py [-h] [-v] [-ng] m q vo p

### Positional arguments:
 1. **m** Mass (`Kg`) of the particle to simulate
 1. **q** Electric charge (`C`) of the particle to simulate
 1. **vo** Initial velocity (`m/s`) of the particle to simulate
 1. **p** Path to file with V(x) function data

### Optional arguments:
  * -**h, --help** show this help message and exit
  * **-v, --verbose** Verbose mode
  * **-ng, --nographics** No graphics mode

### Data formatting

The file with the data is expected to be a .csv file with the x,y,v values, where all x,y and v are numeric values. A sample file would look like this:
```
x,v
0,1
1,3
```

### Usage example

Let's simulate the movement of a particle with mass `9.10938188e10-31 Kg`, `−1.6021766208e10−19 C` and an initial velocity of `1.25e-6 m/s`.

The data file describing the V(x) function can be found [here](url).

```
$ python3 main.py 9.10938188e10-31 −1.6021766208e10−19 1.25e-6 ./data.csv
```

The result of the previous command would be:
[!Insert gif]

## License
Copyright (c) 2019-present Josue Valenzuela

[MIT License](http://en.wikipedia.org/wiki/MIT_License)