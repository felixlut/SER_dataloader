import pandas as pd
import os
from tqdm import tqdm

from . import util


class Esd:

    def __init__(self, top_path):
        self.path = top_path + 'esd-data/'
        self.df = self.get_df()


    def get_df(self):
        wav_path = self.path + '/wav/wav/'
        wav_2_duration = util._get_duration_dict(wav_path, self.path + 'wav_2_duration.csv')
        wav_2_label = pd.read_csv(self.path + 'wav_2_label.csv', header=None, index_col=0, squeeze=True).to_dict()
        wav_2_set = pd.read_csv(self.path + 'wav_2_set.csv', header=None, index_col=0, squeeze=True).to_dict()
        data = []
        for f_name in tqdm(os.listdir(wav_path), desc='Dataframe'):
            f_path = wav_path + f_name
            f_path = os.path.abspath(f_path)
            emo = wav_2_label[f_name[:-4]]
            act_id = int(f_name[:4])

            data.append({
                'actor_id'  : act_id,
                'lang'      : 'chi' if act_id <= 10 else 'eng',
                'set'       : wav_2_set[f_name[:-4]],
                'wav_path'  : f_path,
                'file_name' : f_name[:-4],
                'emo'       : emo,
                'length'    : wav_2_duration[f_name[:-4]]
            })
        
        return pd.DataFrame(data)
