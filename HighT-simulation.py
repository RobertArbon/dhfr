from __future__ import print_function
import sys
import mdtraj as md
from simtk.openmm import app
import simtk.openmm as mm
from simtk import unit

if len(sys.argv) != 3:
    print('usage %s <cuda device index> < temp > ')
    exit(1)

temp = sys.argv[2]

pdb = md.load('5dfr_minimized.pdb')
forcefield = app.ForceField('amber99sbildn.xml', 'amber99_obc.xml')

system = forcefield.createSystem(pdb.topology.to_openmm(), nonbondedMethod=app.CutoffNonPeriodic,
    nonbondedCutoff=2.0*unit.nanometers, constraints=app.HBonds)
integrator = mm.LangevinIntegrator(temp*unit.kelvin, 91.0/unit.picoseconds,
    2.0*unit.femtoseconds)
integrator.setConstraintTolerance(0.00001)

platform = mm.Platform.getPlatformByName('CUDA')
properties = {'CudaPrecision': 'mixed', 'CudaDeviceIndex': sys.argv[1]}
simulation = app.Simulation(pdb.topology.to_openmm(), system, integrator, platform, properties)
simulation.context.setPositions(pdb.xyz[0])

simulation.context.setVelocitiesToTemperature(temp*unit.kelvin)

nsteps = int((500*unit.nanoseconds) / (2*unit.femtoseconds))
interval = int((1*unit.nanoseconds) / (2*unit.femtoseconds))

simulation.reporters.append(app.StateDataReporter(open('trajectory-%sK.log' % sys.argv[2], 'w', 0),
    interval, step=True, time=True, progress=True,
    potentialEnergy=True, temperature=True, remainingTime=True,
    speed=True, totalSteps=nsteps, separator='\t'))

# equilibrate
simulation.step(int(10*unit.nanoseconds / (2*unit.femtoseconds)))

# now add the trajectory reporter.
simulation.reporters.append(app.PDBReporter('5dfr-trajectory-%sK.pdb' % sys.argv[2], interval))
simulation.step(nsteps)
