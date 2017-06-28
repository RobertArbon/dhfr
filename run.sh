#!/bin/bash

# print('usage %s <cuda device index> < temp K > < t_equil ns > < t_sim ns > ')

python simulation.py 1 325 10 500 &> dhfr-325.log &
python simulation.py 2 350 10 500 &> dhfr-350.log &
python simulation.py 3 375 10 500 &> dhfr-375.log &
python simulation.py 0 400 10 500 &> dhfr-400.log &
