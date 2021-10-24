import pandas as pd

from dataloader.base_dataset import BaseDataset


class Cremad(BaseDataset):
    def __init__(self, top_path):
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
        self.path = top_path + 'cremad/'
        self.actor_2_age = pd.read_csv(self.path + 'actor_2_age.csv', index_col=0, squeeze=True).to_dict()
        self.actor_2_gender = pd.read_csv(self.path + 'actor_2_gender.csv', index_col=0, squeeze=True).to_dict()
        super().__init__(self.path)

    def get_dataset_specific_dict(self, f_name):
        act_id, sentence, emo, intensity = f_name.split('_')
        return {
            'actor_id'  : act_id,
            'lang'      : 'eng',
            'emo'       : self.annotation_mapping[emo],
            'text'      : self.text_mapping[sentence],
            'intensity' : intensity,
            'dataset'   : 'cremad',
            'gender'    : 'F' if self.actor_2_gender[int(act_id)] == 'Female' else 'M',
            'age'       : self.actor_2_age[int(act_id)],
        }
