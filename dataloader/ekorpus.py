import pandas as pd

from dataloader.base_dataset import BaseDataset


class Ekorpus(BaseDataset):
    def __init__(self, top_path):
        self.path = top_path + 'ekorpus/'
        self.wav_2_label = pd.read_csv(self.path + 'wav_2_label.csv', index_col=0, squeeze=True).to_dict()
        super().__init__(self.path)

    def get_dataset_specific_dict(self, f_name):
        return {
            'lang'      : 'est',
            'emo'       : self.wav_2_label[f_name],
            'dataset'   : 'ekorpus',
        }
