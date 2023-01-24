# G4MP2 Ionization Potentials

This repository contains the code used by Dandu et al. in "Prediction of Ionization Potentials of Organic Molecules using Quantum Chemistry Assisted Machine Learning."

## Installation

The environment for the code is described in `environment.yml`.
Install it using Anaconda:

```bash
conda env create --file environment.yml
```

The environment is designed to work on Linux systems (e.g., Ubuntu, Windows Subsystem for Linux), and may also work on OS X.


## Layout

The `data` contains the datasets used in our study. 

`FHCL_DELTA` and `SCHNET_DELTA` contain the scripts we used to create machine learning models.
