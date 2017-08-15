from __future__ import print_function
import sys
import mdtraj as md
from simtk.openmm import app
import simtk.openmm as mm
from simtk import unit

if len(sys.argv) != 8:
    print('usage %s <cuda device index> < temp K > < t_equil ns > < t_sim ns > < fric 1/ps > < pdb > < frame > ')
    exit(1)

temp = float(sys.argv[2])
t_equil = float(sys.argv[3])
t_sim = float(sys.argv[4])
fric = float(sys.argv[5])
pdb_str = sys.argv[6]
pdb_frame = int(sys.argv[7])

pdb = md.load(pdb_str)
forcefield = app.ForceField('amber99sbildn.xml', 'amber99_obc.xml')

system = forcefield.createSystem(pdb.topology.to_openmm(), nonbondedMethod=app.CutoffNonPeriodic,
    nonbondedCutoff=2.0*unit.nanometers, constraints=app.HBonds)
integrator = mm.LangevinIntegrator(temp*unit.kelvin, fric/unit.picoseconds,
    2.0*unit.femtoseconds)
integrator.setConstraintTolerance(0.00001)

platform = mm.Platform.getPlatformByName('CUDA')
properties = {'CudaPrecision': 'mixed', 'CudaDeviceIndex': sys.argv[1]}
simulation = app.Simulation(pdb.topology.to_openmm(), system, integrator, platform, properties)
simulation.context.setPositions(pdb.xyz[pdb_frame])

simulation.context.setVelocitiesToTemperature(temp*unit.kelvin)

nsteps = int((t_sim*unit.nanoseconds) / (2*unit.femtoseconds))
interval = int((1*unit.nanoseconds) / (2*unit.femtoseconds))

simulation.reporters.append(app.StateDataReporter(open('trajectory-{0}K-{1}.log'.format(sys.argv[2], pdb_frame), 'w'),
    interval, step=True, time=True, progress=True,
    potentialEnergy=True, temperature=True, remainingTime=True,
    speed=True, totalSteps=nsteps, separator='\t'))

# equilibrate
simulation.step(int(t_equil*unit.nanoseconds / (2*unit.femtoseconds)))

# now add the trajectory reporter.
simulation.reporters.append(app.DCDReporter('5dfr-trajectory-{0}K-{1}.dcd'.format(sys.argv[2],pdb_frame), interval))
simulation.step(nsteps)
