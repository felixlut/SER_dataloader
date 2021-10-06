import pandas as pd
import os
from tqdm import tqdm

from . import util


class Meld:

    def __init__(self, top_path):
        self.path = top_path + 'melddata/'
        self.annotation_mapping = {
            'anger'     : 'Angry',
            'joy'       : 'Happy',
            'sadness'   : 'Sad',
            'neutral'   : 'Neutral',
            'fear'      : 'Fear',
            'surprise'  : 'Surprised',
            'disgust'   : 'Disgusted',
        }
        self.df = self.get_df()

    def get_df(self):
        wav_path = self.path + '/wav/wav/'
        file_2_transcript = pd.read_csv(self.path + 'wav_2_transcript.csv', header=None, index_col=0, squeeze=True).to_dict()
        wav_2_label = pd.read_csv(self.path + 'wav_2_label.csv', header=None, index_col=0, squeeze=True).to_dict()
        wav_2_duration = util._get_duration_dict(wav_path, self.path + 'wav_2_duration.csv')
        wav_2_actor = pd.read_csv(self.path + 'wav_2_actor.csv', header=None, index_col=0, squeeze=True).to_dict()
        wav_2_sentiment = pd.read_csv(self.path + 'wav_2_sentiment.csv', header=None, index_col=0, squeeze=True).to_dict()
        data = []
        for f_name in tqdm(os.listdir(wav_path), desc='Dataframe'):
            f_path = wav_path + f_name
            f_path = os.path.abspath(f_path)

            emo = wav_2_label[f_name[:-4]]
            emo = self.annotation_mapping[emo]
            set_str = None
            if 'train' in f_name:
                set_str = 'train'
            if 'test' in f_name:
                set_str = 'test'
            if 'dev' in f_name:
                set_str = 'dev'

            data.append({
                'actor_id'      : wav_2_actor[f_name[:-4]],
                'lang'          : 'eng',
                'wav_path'      : f_path,
                'file_name'     : f_name,
                'emo'           : emo,
                'sentiment'     : wav_2_sentiment[f_name[:-4]],
                'text'          : file_2_transcript[f_name[:-4]],
                'length'        : wav_2_duration[f_name[:-4]],
                'set'           : set_str,
            })

        return pd.DataFrame(data)
