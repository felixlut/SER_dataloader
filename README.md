# SER_dataloader
This project is part of a master's thesis for the: course DA231X - Degree Project in Computer Science and Engineering, Second Cycle 30hp

These scripts are meant to load and transform datasets into Dataframes for ease of use (that is, no actual data, just preparation scripts). The data is loaded by reading file_names from the corresponding dataset-directories (see below how for directory structure). 

## Get Started
### Install
Install with pip:
```
pip install git+https://github.com/felixlut/SER_dataloader.git@main
```


### Usage
The package is meant to be accessed via python like this:

```python
from dataloader import Dataloader
dataset_name = 'cremad' # /cremad/emodb/...
data = Dataloader(data_args.data_path, force_reload=False) # After the first instance of this command, the dataset is cached. force_reload=True for circumventing the caching
dataset_as_df = data.load_dataset(dataset_name)
```

## Data
The data is supposed to be stored in ```.../datasets/{dataset_name}```, and should have the below described structure overall. 
- dataset_name
    - files:
        - train.csv (pre-defined train/test/val splits)
        - test.csv
        - val.csv
        - Maybe addition csv files storing dataset-specific info (ex. actor_2_gender.csv) 
    - directories (either or both are fine):
        - wav/wav/ (contains all the wav_files, in the original quality)
        - wav_telephone/wav_telephone (wav_files after phone_filter)
        - (Yes, 2 layers of wav(_telephone), kaggle datahandling is weird)
    
### Supported Datasets
The following datasets are supported, and have to have the same directory name mentioned below (don't mind the inconsistency of the ```data``` postfix, kaggle is once again coming through with only the highest quality of data-handling). These can also be derived from the correspponding scripts.
* **Dataset - dataset_directory_name**
* [Cremad-D](https://github.com/CheyneyComputerScience/CREMA-D) - ```cremad```
* [ESD](https://github.com/HLTSingapore/Emotional-Speech-Data) - ```esd-data```
* [Subesco](https://zenodo.org/record/4526477) - ```subesco```
* [emoDB](https://www.kaggle.com/piyushagni5/berlin-database-of-emotional-speech-emodb) - ```emodb-data```
* [MESD](https://data.mendeley.com/datasets/cy34mh68j9/1) - ```mesddata```
* [EMOVO](http://voice.fub.it/activities/corpora/emovo/index.html) - ```emovodata```
* [Oréau](https://zenodo.org/record/4405783) - ```oreaudata```
* [emoUERJ](https://zenodo.org/record/5427549) - ```emouerj```
