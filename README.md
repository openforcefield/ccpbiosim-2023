# 2023 CCPBioSim Training Week materials

Presenters:

* Danny Cole
* Mat Bieniek
* Matt Thompson

## Agenda

### Main session - Thursday (2pm-5pm)

* Talk - Intro to OpenFF
* Notebook: [Preview](notebooks/preview.ipynb)
* Notebook: [Units](notebooks/units.ipynb)
* (break)
* Notebook: [Force Fields](notebooks/forcefields.ipynb)
* Notebook: [Molecule](notebooks/molecule_cookbook.ipynb)
* Notebook: [Topology](notebooks/topologies.ipynb)
* Experimenting - can you load your own molecules into OpenFF?

### Main session - Friday (9.30am-12pm)

* Notebook: [Interchange](notebooks/interchange.ipynb)
* Notebook: [Protein-ligand systems](notebooks/protein-ligand.ipynb)
* (break)
* Notebook: [Non-protein-ligand systems](notebooks/non_protein.ipynb)
* Experimenting - can you ...
  * parameterize your molecules with an OpenFF force field?
  * run a short simulation in OpenMM?
  * visualize the result?
  * run a short simulation in another engine (GROMACS/Amber/LAMMPS)?

### Main session - Friday (1pm-3pm)

* Talk - BespokeFit
* Notebook: [Bespokefit](https://gist.github.com/Yoshanuikabundi/2860cf864ed1658ceec466bfb599e3fe)
* Notebook: [Protein-lingand system with bespoke parameters](notebooks/bespokefit-protein-ligand.ipynb)
* Experimenting - can you use BespokeFit in one of your own systems?

## Local installation

If there are any issues with the provided cloud-hosted JupyterHub instance, or to use these notebooks outside of the workshop hours, use a Python distribution (we recommend [Mambaforge](https://docs.openforcefield.org/en/latest/install.html#quick-install-guide)) and create an environment from the provided YAML file:

```shell
$ mamba env create --file environment.yaml
$ ...
$ mamba activate openff-env
```

## More resources

* Main [OpenFF docs](https://docs.openforcefield.org/en/latest/)
  * See "Projects" on the left for package-specific documentation
  * Ecosystem-wide [examples](https://docs.openforcefield.org/en/latest/examples.html)
* [SMIRNOFF](https://openforcefield.github.io/standards/standards/smirnoff/) specification
* [Discussions](https://github.com/orgs/openforcefield/discussions) - for general usage questions
