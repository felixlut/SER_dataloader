# SER_dataloader
This project is part of a master's thesis for the: course DA231X - Degree Project in Computer Science and Engineering, Second Cycle 30hp

These scripts are meant to load and transform datasets into Dataframes for ease of use (that is, no actual data, just preparation scripts). The data is loaded by reading file_names from the corresponding dataset-directories (see below how for directory structure). 

## Get Started
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
        - wav (contains all the wav_files, in the original quality)
        - wav_telephone (wav_files after phone_filter)