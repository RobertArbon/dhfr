#!/bin/bash -login
#SBATCH --nodes=1
#SBATCH --gres=gpu:2
#SBATCH --partition gpu
#SBATCH --job-name=gpujob

module load CUDA/8.0.44 
#  -h, --help            show this help message and exit
#  --platform=PLATFORM   name of the platform to benchmark
#  --test=TEST           the test to perform: gbsa, rf, pme, amoebagk, or
#                        amoebapme [default: all]
#  --pme-cutoff=CUTOFF   direct space cutoff for PME in nm [default: 0.9]
#  --seconds=SECONDS     target simulation length in seconds [default: 60]
#  --polarization=POLARIZATION
#                        the polarization method for AMOEBA: direct,
#                        extrapolated, or mutual [default: mutual]
#  --mutual-epsilon=EPSILON
#                        mutual induced epsilon for AMOEBA [default: 1e-5]
#  --heavy-hydrogens     repartition mass to allow a larger time step
#  --device=DEVICE       device index for CUDA or OpenCL
#  --precision=PRECISION
#                        precision mode for CUDA or OpenCL: single, mixed, or
#                        double [default: single]
nvidia-smi
cd $SLURM_SUBMIT_DIR
echo $SLURM_JOB_NODELIST
python benchmark.py --platform=CUDA --test=gbsa --precision=mixed &> log

