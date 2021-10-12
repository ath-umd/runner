import os
import subprocess
import glob

dir = '/lustre/athall/Li3YBr6/exp_structures/sub_then_order'
sub = '/lustre/athall/Li3YBr6/exp_structures'

os.chdir(dir)
    
### For setting up relaxations from a number of POSCARs in directory ###
for filename in os.listdir(dir):
    ij = filename[0:3]
    print(ij)
    os.system('(mkdir %s)' % ij) 
    os.chdir((dir+'/%s') % ij)
    os.system(('cp '+dir+'/%s '+dir+'/%s/POSCAR') % (filename,ij))
    os.system('mkdir relax')
    os.system(('cp POSCAR '+dir+'/%s/relax') % ij)
    os.chdir((dir+'/%s/relax') % ij)
    os.system('python /homes/athall/Pymatgen_Related/script/get_vasp_input.py poscar POSCAR')
    os.system(('cp '+sub+'/sub.dt2 '+dir+'/%s/relax/vaspinput') % ij)
    os.chdir((dir+'/%s/relax/vaspinput') % ij)
    os.system('sbatch sub.dt2')
    os.chdir(dir)

n = '1000'
st = '100'
et = ['700','800','900','1000','1100']
temps = [st+'-'+et[0],st+'-'+et[1],st+'-'+et[2],st+'-'+et[3],st+'-'+et[4]]

### For setting up MD from geometric relaxation ###
for i in glob.iglob('*'):
    os.chdir('%s' % i)
    print(i)
    for j in temps:
        os.system('mkdir %s' % j)
        k = i
        #"Your first value is {} your second value is {}".format(amount1, amount2)
        s = "cp "+dir+"/{}/relax/vaspinput/CONTCAR ".format(k)+dir+"/{}/{}/POSCAR".format(i,j) 
        os.system(s)
        os.chdir(dir+'/%s/%s' % (i,j))
        os.system('python /homes/athall/Pymatgen_Related/script/get_vasp_input.py -t md -st '+st+' -et '+j[4:]+' -n '+n+' poscar POSCAR')
        os.system('cp '+sub+'/sub.dt2 '+dir+'/%s/%s/vaspinput' % (i,j))
        os.chdir(dir+'/%s/%s/vaspinput' % (i,j))
        os.system('sbatch sub.dt2')
        os.chdir(dir+'/%s' % i)
    os.chdir(dir)
    

