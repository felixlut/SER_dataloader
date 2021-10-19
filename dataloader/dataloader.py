import importlib
import pandas as pd


class Dataloader:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.implemented_datasets = ['iemocap', 'emodb', 'ravdess', 'esd', 'cremad', 'meld', 'mesd', 'oreau', 'emovo']


    def load_dataset(self, dataset, force_reload=False):
        if dataset not in self.implemented_datasets:
            raise NotImplementedError("{} not in {}!".format(dataset, self.implemented_datasets))

        if force_reload or not hasattr(self, dataset):
            mod_name = '.' + dataset
            cls = getattr(importlib.import_module(mod_name, package='dataloader'), dataset.capitalize())
            setattr(self, dataset, cls(self.dataset_path))
        
        return getattr(self, dataset).df
    
    def load_all_datasets(self):
        all_dfs = []
        for subset in self.implemented_datasets:
            all_dfs.append(self.load_dataset(subset))
        
        return pd.concat(all_dfs, axis=0, ignore_index=True)
