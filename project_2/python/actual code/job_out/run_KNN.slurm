#!/bin/sh
#SBATCH -J run_KNN.slurm # Name for your job
#SBATCH -n 1# Number of tasks when using MPI. Default is 1, and SLURM assumes the usage of 1 cpu per task.
#SBATCH -N 1 # Number of nodes to spread cores across - default is 1 - if you are not using MPI this should likely be 1
#SBATCH --mem 2000 # Megabytes of memory requested. Default is 2000/task.
#SBATCH -t 0:5:00 # Runtime in days-hours:minutes:seconds. 
#SBATCH -p express # Partition to submit to the standard compute node partition(defq) or the express node partition(express)
#SBATCH -o nb-%j.out.txt # Standard output (stdout) goes to this file (what would print to the screen if you were running the command locally)
#SBATCH -e nb-%j.err.txt # Standard error (stderr) goes to this file (errors that would print to the screen if you were running the command locally)

module load Python/3.5.1-foss-2016a  #if you want to load a module use this and the above common with the module name you wanted loaded.
date 
python3 ../driver.py <<< 5   1  19 
date
