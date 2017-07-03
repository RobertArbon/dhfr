#!/bin/bash

# print('usage %s <cuda device index> < temp K > < t_equil ns > < t_sim ns > ')
# print('usage %s <cuda device index> < temp K > < t_equil ns > < t_sim ns > < fric 1/ps > < pdb > < frame > ')


#python simulation.py 1 325 10 500 &> dhfr-325.log &
#python simulation.py 2 350 10 500 &> dhfr-350.log &
#python simulation.py 3 375 10 500 &> dhfr-375.log &
#python simulation.py 0 400 10 500 &> dhfr-400.log &

#python simulation.py 1 325 10 500 1 &> dhfr-325K-fric1.log &
#python simulation.py 2 350 10 500 1 &> dhfr-350K-fric1.log &
#python simulation.py 3 375 10 500 1 &> dhfr-375K-fric1.log &
#python simulation.py 0 400 10 500 1 &> dhfr-400K-fric1.log &

python simulation.py 1 325 10 2500 1 start-325.pdb -1 &> dhfr-325K-fric1-2.log &
python simulation.py 2 350 10 2500 1 start-350.pdb -1 &> dhfr-350K-fric1-2.log &
python simulation.py 3 375 10 2500 1 start-375.pdb -1 &> dhfr-375K-fric1-2.log &
python simulation.py 0 400 10 2500 1 start-400.pdb -1 &> dhfr-400K-fric1-2.log &
