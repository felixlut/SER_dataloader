import os
import pandas as pd

from .base_dataset import BaseDataset


class Iemocap(BaseDataset):
    def __init__(self, top_path):
        self.path = top_path + 'iemocap/'
        self.annotation_mapping = {
            'ang': 'Angry',
            'hap': 'Happy',
            'exc': 'Excited', 
            'sad': 'Sad',
            'neu': 'Neutral',
            'fru': 'Frustrated',
            'fea': 'Fear',
            'sur': 'Surprised',
            'dis': 'Disgusted',
            'xxx': 'xxx',
            'oth': 'Other',
        }
        self.file_2_transcript = self._get_transcript_dict()
        self.wav_2_label = self._get_label_dict()
        super().__init__(self.path, self.annotation_mapping)

    def _get_label_dict(self):
        if os.path.isfile(self.path + 'wav_2_label.csv'):
            return pd.read_csv(self.path + 'wav_2_label.csv', header=None, index_col=0, squeeze=True).to_dict()
        else:
            raise NotImplementedError("wav_2_label.csv not found, and labels cant be extracted from current dataset version")

        # This code only works on the original dataset
        labels = ['neu', 'fru', 'hap', 'sad', 'ang', 'fea', 'exc', 'sur', 'dis', 'xxx', 'oth']
        sessions = ['Session' + str(i) for i in range(1, 6)]
        wav_to_label = {}
        for sess in sessions:
            directory = self.path + sess + '/dialog/EmoEvaluation/'
            for file_name in os.listdir(directory):            
                if file_name[-4:] == '.txt':
                    out = open(directory + file_name).read().split()
                    pairs = [(out[i-1], out[i]) for i, word in enumerate(out) if word in labels]
                                    
                    for f, emo in pairs:
                        wav_to_label[f] = emo

        df = pd.DataFrame.from_dict(wav_to_label, orient='index')
        df = df.sort_index()
        df.to_csv('wav_2_label.csv')        
        return wav_to_label

    
    def _get_transcript_dict(self):
        csv_path = self.path + 'wav_2_transcript.csv'
        if os.path.isfile(csv_path):
            return pd.read_csv(csv_path, header=None, index_col=0, squeeze=True).to_dict()
        else:
            raise NotImplementedError("wav_2_transcript.csv not found, and transcripts cant be extracted from current dataset version")

        # This code only works on the original dataset
        file_names = [f_name[:-4] for f_name in os.listdir(self.path + '/wav/')]
        sessions = ['Session' + str(i) for i in range(1, 6)]
        wav_to_transcript = {}
        for sess in sessions:
            directory = self.path + sess + '/dialog/transcriptions/'
            for file_name in os.listdir(directory):
                out = open(directory + file_name).readlines()
                
                for line in out:
                    line = line.strip().split(' ', 2)
                    if line[0] in file_names:
                        wav_to_transcript[line[0]] = line[2]

        df = pd.DataFrame.from_dict(wav_to_transcript, orient='index')
        df = df.sort_index()
        df.to_csv('wav_2_transcript.csv')
        return wav_to_transcript

    def get_dataset_specific_dict(self, f_name):
        actor_id = f_name[3:6]
        return {
            'impro/script'  : 'impro' if 'impro' in f_name else 'script',
            'session'       : actor_id[1],
            'actor_id'      : actor_id,
            'gender'        : actor_id[-1:],
            'lang'          : 'eng',
            'emo'           : self.annotation_mapping[self.wav_2_label[f_name]],
            'text'          : self.file_2_transcript[f_name],
        }
