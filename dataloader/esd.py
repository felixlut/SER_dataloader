import os
import pandas as pd

from dataloader.base_dataset import BaseDataset


class Esd(BaseDataset):
    def __init__(self, top_path):
        self.annotation_mapping = {
            'N': 'Neutral',
            'F': 'Happy',
            'T': 'Sad',
            'W': 'Angry',
            'L': 'Bored',
            'E': 'Disgusted',
            'A': 'Fear'
        }
        self.wav_2_label = pd.read_csv(self.path + 'wav_2_label.csv', header=None, index_col=0, squeeze=True).to_dict()
        self.wav_2_set = pd.read_csv(self.path + 'wav_2_set.csv', header=None, index_col=0, squeeze=True).to_dict()
        super().__init__(top_path + 'emodb-data/')

    def get_dataset_specific_dict(self, f_name):
        act_id = int(f_name)
        return {
            'actor_id'  : act_id,
            'lang'      : 'chi' if act_id <= 10 else 'eng',
            'set'       : self.wav_2_set[f_name],
            'emo'       : self.wav_2_label[f_name],
        }
