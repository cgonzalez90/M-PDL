#!/bin/bash
#BSUB -n 128
#BSUB -R "span[ptile=8]"
#BSUB -o lightdock.out
#BSUB -e lightdock.err
#BSUB -J 1PPE
#BSUB -W 18:00
#BSUB -q bsc_ls
module load intel openmpi python mkl
mpirun lightdock RRRR_rec.pdb LLLL_lig.pdb 400 300 200 -f glowworm.conf -mpi -s scoring.conf -nm
