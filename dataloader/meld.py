import pandas as pd

from dataloader.base_dataset import BaseDataset


class Meld(BaseDataset):
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
        self.main_characters = {'Rachel', 'Monica', 'Ross', 'Joey', 'Chandler', 'Phoebe'}
        self.wav_2_transcript = pd.read_csv(self.path + 'wav_2_transcript.csv', index_col=0, squeeze=True).to_dict()
        self.wav_2_label = pd.read_csv(self.path + 'wav_2_label.csv', index_col=0, squeeze=True).to_dict()
        self.wav_2_actor = pd.read_csv(self.path + 'wav_2_actor.csv', index_col=0, squeeze=True).to_dict()
        self.wav_2_sentiment = pd.read_csv(self.path + 'wav_2_sentiment.csv', index_col=0, squeeze=True).to_dict()
        super().__init__(self.path)

    def _valid_file(self, f_name):
        return f_name in self.wav_2_label

    def get_dataset_specific_dict(self, f_name):
        act_id = self.wav_2_actor[f_name]
        return {
            'actor_id'      : act_id if act_id in self.main_characters else 'Other',
            'lang'          : 'eng',
            'emo'           : self.wav_2_label[f_name],
            'sentiment'     : self.wav_2_sentiment[f_name],
            'text'          : self.wav_2_transcript[f_name],
            'set'           : next((x for x in ['train', 'test', 'dev'] if x in f_name), None),
        }
