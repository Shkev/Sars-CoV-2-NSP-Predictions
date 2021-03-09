# COVID-19 Non-structural Protein Predictions
All code is in the root directory. Due to file size limitations of Github, data files are not included but they can be found at [Drugbank.ca](drugbank.ca). File paths should be adjusted to the user's own file layout if code is run.

## Notebooks
Notebooks are listed in the order they should be used in. **THE 'OTHER FILES' SHOULD BE RUN BEFORE THESE ARE USED**

* **feature_extraction:** Takes data and extracts protein and drug features.
* **dataset_creation:** Creates training and testing dataset from the outputs of the feature_extraction notebook
* **lasso_training:** Determines optimal lasso model and trains a lasso model for proteins and drugs. Uses the models to select features and saves the reduced datasets for use in machine learning model training.
* **machine_learning_training:** Trains various machine learning models (CNN, DNN, Random Forest) and shows metrics.
* **covid_prediction:** Uses the trained machine learning models to make predictions for SARS-CoV2 viral proteins.

## Other Files

* **modify_fasta:** Replaces the '|' in the fasta files with spaces for easier processing later. *Should be run before the notebooks are used.*
* **struc_to_smiles:** Extracts SMILES for approved drugs from DrugBank data and writes to a separate `.smi` file. Used to calculate drug descriptors (using [ochem.eu](ochem.eu)).
