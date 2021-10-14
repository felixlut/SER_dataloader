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
        self.wav_2_transcript = pd.read_csv(self.path + 'wav_2_transcript.csv', header=None, index_col=0, squeeze=True).to_dict()
        self.wav_2_label = pd.read_csv(self.path + 'wav_2_label.csv', header=None, index_col=0, squeeze=True).to_dict()
        self.wav_2_actor = pd.read_csv(self.path + 'wav_2_actor.csv', header=None, index_col=0, squeeze=True).to_dict()
        self.wav_2_sentiment = pd.read_csv(self.path + 'wav_2_sentiment.csv', header=None, index_col=0, squeeze=True).to_dict()
        super().__init__(self.path)

    def _valid_file(self, f_name):
        return f_name in self.wav_2_label

    def get_dataset_specific_dict(self, f_name):
        return {
            'actor_id'      : self.wav_2_actor[f_name],
            'lang'          : 'eng',
            'emo'           : self.wav_2_label[f_name],
            'sentiment'     : self.wav_2_sentiment[f_name],
            'text'          : self.wav_2_transcript[f_name],
            'set'           : next((x for x in ['train', 'test', 'dev'] if x in f_name), None),
        }
