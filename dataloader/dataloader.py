import importlib


class Dataloader:
    
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.implemented_datasets = ['iemocap', 'emodb', 'ravdess', 'esd', 'crema-d']


    def load_dataset(self, dataset):
        if dataset not in self.implemented_datasets:
            raise NotImplementedError("{} not in {}!".format(dataset, self.implemented_datasets))

        if not hasattr(self, dataset):
            mod_name = '.' + dataset
            cls = getattr(importlib.import_module(mod_name, package='dataloader'), dataset.capitalize())
            setattr(self, dataset, cls(self.dataset_path))
        
        return getattr(self, dataset).df
