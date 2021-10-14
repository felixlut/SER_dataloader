import pandas as pd
import os
from tqdm import tqdm

from . import util


class Emodb:

    def __init__(self, top_path):
        self.path = top_path + 'emodb-data'
        self.annotation_mapping = {
            'N': 'Neutral',
            'F': 'Happy',
            'T': 'Sad',
            'W': 'Angry',
            'L': 'Bored',
            'E': 'Disgusted',
            'A': 'Fear'
        }
        self.df = self.get_df()


    def get_df(self):
        wav_path = self.path + '/wav/wav/'
        wav_tele_path = self.path + '/wav_telephone/wav_telephone/'
        wav_2_duration = util._get_duration_dict(wav_path, self.path + 'wav_2_duration.csv')
        data = []
        for f_name in tqdm(os.listdir(wav_path)):
            act_id = f_name[:2]
            emo = f_name[5]
            emo = self.annotation_mapping[emo]
            f_path = wav_path + f_name
            f_path = os.path.abspath(f_path)

            data.append({
                'actor_id'      : act_id,
                'lang'          : 'ger',
                'wav_path'      : f_path,
                'wav_tele_path' : wav_tele_path + f_name,
                'file_name'     : f_name,
                'emo'           : emo,
                'length'        : wav_2_duration[f_name[:-4]]
            })

        return pd.DataFrame(data)
