from collections import Counter

from openff.toolkit import Topology


def count(topology: Topology):
    for smiles, count in Counter(mol.to_smiles() for mol in topology.molecules).items():
        if len(smiles) > 1000:
            name = "protein"
        elif len(smiles) > 10:
            name = "ligand"
        else:
            name = smiles
        print(f"{name} : {count} molecule(s)")
