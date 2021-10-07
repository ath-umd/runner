import os
import subprocess
#dirs = range(0,66)

dir = '/lustre/athall/LLZO/cubic/Ta/bulk_mod/408'
sub = '/lustre/athall/LLZO/cubic/Ta/bulk_mod'
os.chdir(dir)
in_dir = os.system('ls')
for filename in os.listdir(dir):
    ij = filename[0:4]
#    print(ij)
    os.system('(mkdir %s)' % ij) 
    os.chdir((dir+'/%s') % ij)
    os.system(('cp '+dir+'/%s '+dir+'/%s/POSCAR') % (filename,ij))
    os.system('mkdir relax')
    os.system(('cp POSCAR '+dir+'/%s/relax') % ij)
    os.chdir((dir+'/%s/relax') % ij)
    os.system('python /homes/athall/Pymatgen_Related/script/get_vasp_input.py -t bulkmod poscar POSCAR')
    os.system(('cp '+sub+'/sub.dt2 '+dir+'/%s/relax/vaspinput') % ij)
    os.chdir((dir+'/%s/relax/vaspinput') % ij)
    os.system('sbatch sub.dt2')
    os.chdir(dir)
