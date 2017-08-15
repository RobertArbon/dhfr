import mdtraj as md

traj = md.load('5dfr-trajectory-500K.pdb')
traj[0].save('dhfr_top.pdb')

