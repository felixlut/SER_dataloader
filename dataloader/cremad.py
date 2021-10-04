import pandas as pd
import os
from tqdm import tqdm

from . import util


class Cremad:

    def __init__(self, top_path):
        self.path = top_path + 'cremad/'
        self.annotation_mapping = {
            'ANG': 'Angry',
            'HAP': 'Happy',
            'SAD': 'Sad',
            'NEU': 'Neutral',
            'DIS': 'Disgusted',
            'FEA': 'Fear',
        }
        self.text_mapping = {
            'IEO': "It's eleven o'clock",
            'TIE': 'That is exactly what happened',
            'IOM': "I'm on my way to the meeting",
            'IWW': 'I wonder what this is about',
            'TAI': 'The airplane is almost full',
            'MTI': 'Maybe tomorrow it will be cold',
            'IWL': 'I would like a new alarm clock',
            'ITH': "I think I have a doctor's appointment",
            'DFA': "Don't forget a jacket",
            'ITS': "I think I've seen this before",
            'TSI': "The surface is slick",
            'WSI': "We'll stop in a couple of minutes",
        }
        self.df = self.get_df()


    def get_df(self):
        wav_path = self.path + '/wav/wav/'
        wav_2_duration = util._get_duration_dict(wav_path, self.path + 'wav_2_duration.csv')
        data = []
        for f_name in tqdm(os.listdir(wav_path), desc='Dataframe'):
            split = f_name.split('_')
            act_id, sentence, emo, intensity = split
            f_path = wav_path + f_name

            emo = self.annotation_mapping[emo]
            data.append({
                'actor_id'  : act_id,
                'lang'      : 'eng',
                'wav_path'  : f_path,
                'file_name' : f_name,
                'emo'       : emo,
                'length'    : wav_2_duration[f_name[:-4]],
                'text'      : self.text_mapping[sentence],
                'intensity' : intensity[:-4],
            })
        
        return pd.DataFrame(data)
