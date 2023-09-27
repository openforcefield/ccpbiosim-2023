# 2023 CCPBioSim Training Week materials

## Agenda

### Main session - Thursday (2pm-5pm)

* TALK - Intro to OpenFF (DC, ~30mins)
* Notebook: Preview (MT, ~20 min, condensed toolkit showcase, may be good to show that traj can be opened in VMD/whatever viewer they learned in the earlier ABMER workshop))
* Notebook: Units (MT ~15 min)
* (break)
* Notebook: (~25 mins) Force fields
* Notebook: Molecule cookbook (~30 mins, includes Topology.from_pdb and Topology.from_openmm/mdtraj)
* Notebook: (~30 mins) Topologies
* EXPERIMENTING - leave time for users to try out their own molecules, troubleshooting

### Main session - Friday (9.30am-12pm)

TALK - modifying force fields (DEXP), maybe rosemary, v-sites & nagl (DC/MT?)

* Creating, exploring Interchange objects (~25 mins)
  * Running single-point energies or simulations in OpenMM, GROMACS, Amber
* Preparing protein-ligand systems (~15 mins)
* Not-protein-ligand simulations (~30 mins, JW will send this by tonight or inform MT that he failed)
  * Nagl for big organic molecules
  * Solvating/box-packing with PackMol
  * (maybe) running in different simulation engines
* (MT sprints to airport)

### Main session - Friday (1pm-3pm)

* TALK - BespokeFit (DC, ~15mins)
* Bespokefit workshop (DC/MB)
* EXPERIMENTING - leave time for users to try out their own molecules, troubleshooting

## Local installation

If there are any issues with the provided cloud-hosted JupyterHub instance, or to use these notebooks outside of the workshop hours, use a Python distribution (we recommend [Mambaforge](https://docs.openforcefield.org/en/latest/install.html#quick-install-guide)) and create an environment from the provided YAML file:

```shell
$ mamba env create --file environment.yaml
$ ...
$ mamba activate openff-env
```
