from ase.io import read, write
import os

# Read system or build using ase.Atoms objects.
atoms = read('/home/alex/Downloads/Structure2D_CID_16217328.sdf')

name = 'w_complex'  # Name of the generated .inp file.
header = '! B3LYP def2-SVP Opt'  # Header instructions containing calc. parameters.
charge = 0  # Charge of the system.
spin = 1  # Spin multiplicity of the system.

# Writes the .xyz file containing atomic coordinates.
write('xyz.xyz', atoms, format='xyz')

# Writes the .inp file with header, label, charge and spin multiplicity.
inp = open(name + '.inp', 'w')
inp.write(header + '\n# ' + name + '\n' + '*xyz ' + str(charge) + ' ' + str(spin) + '\n')

# Write the atomic positions in .inp file, read from created xyz.xyz file.
with open('xyz.xyz', 'r') as file:
    file = file.readlines()
    for i, line in enumerate(file):
        if i > 1:
            inp.write(line)

inp.write('*')  # End of .inp file.

# Delete useless .xyz file.
os.remove('xyz.xyz')
