import pandas as pd
import os
from tqdm import tqdm

from . import util


class CremaD:

    def __init__(self, top_path):
        self.path = top_path + 'cremad/'
        self.df = self.get_df()


    def get_df(self):
        annotation_mapping = {
            'ANG': 'Angry',
            'HAP': 'Happy',
            'SAD': 'Sad',
            'NEU': 'Neutral',
            'DIS': 'Disgusted',
            'FEA': 'Fear',
        }

        wav_path = self.path + '/wav/wav/'
        wav_2_duration = util._get_duration_dict(wav_path, self.path + 'wav_2_duration.csv')
        data = []
        for f_name in tqdm(os.listdir(wav_path), desc='Dataframe'):
            split = f_name.split('_')
            act_id, sentence, emo, intensity = split
            f_path = wav_path + f_name

            emo = annotation_mapping[emo]
            data.append({
                'actor_id'  : act_id,
                'lang'      : 'eng',
                'wav_path'  : f_path,
                'file_name' : f_name,
                'emo'       : emo,
                'length'    : wav_2_duration[f_name[:-4]],
                'text'      : sentence,
                'intensity' : intensity,
            })
        
        return pd.DataFrame(data)
