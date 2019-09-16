#!/usr/bin/env python3

"""
"""
import argparse
from simulation import data_import
from simulation import simulation
parser = argparse.ArgumentParser(description='Simulation')

parser.add_argument('mass', metavar='m', help='Mass (Kg) of the particle to simulate', type=float)
parser.add_argument('charge', metavar='q', help='Electric charge (C) of the particle to simulate', type=float)
parser.add_argument('velocity', metavar='vo', help='Initial velocity (m/s) of the particle to simulate', type=float)
parser.add_argument('data', metavar='p', help='Path to file with V(x) function data')

parser.add_argument('-v', '--verbose', help='Verbose mode', action='store_true')
parser.add_argument('-ng', '--nographics', help='No graphics mode', action='store_true')



if __name__ == "__main__":
    args=parser.parse_args()
    simulation = simulation.Simulation(args.mass, args.charge, args.velocity)
    simulation.simulate(data_import.read_csv(args.data))
    


