#!/bin/bash -login
#SBATCH --nodes=1
#SBATCH --gres=gpu:2
#SBATCH --partition gpu
#SBATCH --job-name=dhfr
#SBATCH --time=2-00:00:00
#SBATCH --mem=20000
module load CUDA/8.0.44 
nvidia-smi
cd $SLURM_SUBMIT_DIR
echo $SLURM_JOB_NODELIST
#python simulation.py 1 325 10 2500 1 start-325.pdb -1 &> dhfr-325K-fric1-2.log &
temp=300
equil=10
simt=1000
fric=91
traj=5dfr-trajectory-375K.pdb

python simulation.py 0 $temp $equil $simt $fric $traj $framen > $framen.log &

framen=$(( framen + 2 ))
python simulation.py 1 $temp $equil $simt $fric $traj $framen > $framen.log 
 


