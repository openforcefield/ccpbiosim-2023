# 2023 CCPBioSim Training Week materials

## Agenda

### Main session - Thursday (2pm-5pm)

* TALK - Intro to OpenFF (DC, ~30mins)
* Notebook: Preview
* Notebook: Units
* Notebook: Force fields
* Notebook: Molecule cookbook
* Notebook: Topologies
* EXPERIMENTING - leave time for users to try out their own molecules, troubleshooting

### Main session - Friday (9.30am-12pm)

TALK - modifying force fields (DEXP), maybe rosemary, v-sites & nagl (DC/MT?)

* Creating, exploring Interchange objects
* Preparing protein-ligand systems
  * Load protein/ligand/force field
  * Solvating/box-packing
  * Running single-point energies or simulations in OpenMM, GROMACS, Amber

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
