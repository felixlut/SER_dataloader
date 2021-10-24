import pandas as pd

from dataloader.base_dataset import BaseDataset


class Esd(BaseDataset):
    def __init__(self, top_path):
        self.actor_2_gender = {
            1: 'F', 2: 'F', 3: 'F', 4: 'M', 5: 'M', 6: 'M', 7: 'F', 8: 'M', 9: 'F', 10: 'M',
            11: 'M', 12: 'M', 13: 'M', 14: 'M', 15: 'F', 16: 'F', 17: 'F', 18: 'F', 19: 'F', 20: 'M',
        }
        self.path = top_path + 'esd-data/'
        self.wav_2_label = pd.read_csv(self.path + 'wav_2_label.csv', index_col=0, squeeze=True).to_dict()
        self.wav_2_set = pd.read_csv(self.path + 'wav_2_set.csv', index_col=0, squeeze=True).to_dict()
        super().__init__(self.path)

    def get_dataset_specific_dict(self, f_name):
        act_id = int(f_name[:4])
        lang = 'chi' if act_id <= 10 else 'eng'
        return {
            'actor_id'  : act_id,
            'lang'      : lang,
            'gender'    : self.actor_2_gender[int(act_id)],
            'set'       : self.wav_2_set[f_name],
            'emo'       : self.wav_2_label[f_name],
            'dataset'   : 'esd' + '-' + lang,
        }
