#!/bin/bash

START=701
END=800
for ((i=START; i<=END; i=i+4))
do
    sbatch --export=framen=$i --job-name=DFR-$i submit.sh
done
