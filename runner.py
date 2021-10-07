import os
import subprocess
#dirs = range(0,66)

dir = '/lustre/athall/LLZO/cubic/Ta/bulk_mod/vol_relax/rand_100'

os.chdir('/lustre/athall/LLZO/cubic/Ta/bulk_mod/vol_relax/rand_100')
in_dir = os.system('ls')
for filename in os.listdir('/lustre/athall/LLZO/cubic/Ta/bulk_mod/vol_relax/rand_100'):
    ij = filename[5:8]
    print(ij)
    os.system('(mkdir %s)' % ij) 
    os.chdir(('/lustre/athall/LLZO/cubic/Ta/bulk_mod/vol_relax/rand_100/%s') % ij)
    os.system(('cp /lustre/athall/LLZO/cubic/Ta/bulk_mod/vol_relax/rand_100/%s /lustre/athall/LLZO/cubic/Ta/bulk_mod/vol_relax/rand_100/%s/POSCAR') % (filename,ij))
    os.system('mkdir relax')
    os.system(('cp POSCAR /lustre/athall/LLZO/cubic/Ta/bulk_mod/vol_relax/rand_100/%s/relax') % ij)
    os.chdir(('/lustre/athall/LLZO/cubic/Ta/bulk_mod/vol_relax/rand_100/%s/relax') % ij)
    os.system('python /homes/athall/Pymatgen_Related/script/get_vasp_input.py poscar POSCAR')
    os.system(('cp /lustre/athall/LLZO/cubic/Ta/bulk_mod/vol_relax/sub.dt2 /lustre/athall/LLZO/cubic/Ta/bulk_mod/vol_relax/rand_100/%s/relax/vaspinput') % ij)
    os.chdir(('/lustre/athall/LLZO/cubic/Ta/bulk_mod/vol_relax/rand_100/%s/relax/vaspinput') % ij)
    os.system('sbatch sub.dt2')
    os.chdir('/lustre/athall/LLZO/cubic/Ta/bulk_mod/vol_relax/rand_100')
