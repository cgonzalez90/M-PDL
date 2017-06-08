#
# Program, li_shuttle.py to launch the tasks for the benchmark's lightdock
# Author,  CGG
# Date,    19-MAY-2017
# Place,   BSC
#

import os
print 'lightdock shuttle launched ...'

#################
# Jobs generation
#################
# open main file with proteins
f_in  = open ('complex.list', 'rt')
# we read all records from main file
for protein in f_in:
    protein = protein[0:4]
    print protein,
# we read de template file and write the new files
    f_temp = open ('job.cmd', 'rt')
    f_out  = open (protein[0:4]+'_job.cmd', 'wt')
    for line in f_temp:
        if (line[0:6] == 'mpirun'):
            line = line.replace("RRRR", protein[0:4])
            line = line.replace("LLLL", protein[0:4])
        f_out.write (line)
    f_out.close()
    f_temp.close()
# close main file
f_in.close()
print ' '

#######################
# Jobs move and enqueue
#######################
# first we move
# open main file with proteins
f_in  = open ('complex.list', 'rt')
# we read all records from main file
for protein in f_in:
# we move the .cmd to their targets directories
    cmd = 'mv -v ' + protein[0:4] + '_job.cmd ./' + protein[0:4] + '/'
    os.system(cmd)
# second we change the directory and launch de job, all together!
    cmd = 'cd ./' + protein[0:4] + '/' + '\n' + 'bsub < ' + protein[0:4] + '_job.cmd'
    print cmd
    os.system(cmd)
    print '---oo0oo---'
# close main file
f_in.close()

print
print 'lightdock shuttle finished !'



