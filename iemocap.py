import pandas as pd
import os
from tqdm import tqdm
import librosa

class Iemocap:

    def __init__(self, top_path):
        self.path = top_path + 'iemocap'
        self.df = self.get_df()


    def _get_label_dict(self):
        if os.path.isfile(self.path + 'wav_2_label.csv'):
            return pd.read_csv(self.path + 'wav_2_label.csv', header=None, index_col=0, squeeze=True).to_dict()

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
        
        return wav_to_label

    
    def _get_transcript_dict(self):
        csv_path = self.path + 'wav_2_transcript.csv'
        if os.path.isfile(csv_path):
            return pd.read_csv(csv_path, header=None, index_col=0, squeeze=True).to_dict()

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
        df.to_csv('wav_2_transcript.csv')

        return wav_to_transcript


    def _get_duration_dict(self):
        csv_path = self.path + 'wav_2_duration.csv'
        if os.path.isfile(csv_path):
            return pd.read_csv(csv_path, header=None, index_col=0, squeeze=True).to_dict()

        wav_2_duration = {}
        files = os.listdir(self.path + '/wav/')
        for f_name in tqdm(files):
            y, sr = librosa.load(self.path + '/wav/' + f_name)
            duration = librosa.get_duration(y=y, sr=sr)
            wav_2_duration[f_name] = duration

        df = pd.DataFrame.from_dict(wav_2_duration, orient='index')
        df.to_csv('wav_2_duration.csv')

        return wav_2_duration


    def get_df(self):
        file_2_transcript = self._get_transcript_dict()
        wav_2_label = self._get_label_dict()
        wav_2_duration = self._get_duration_dict()
        data = []
        for f_name in tqdm(os.listdir(self.path + '/wav/')):
            f_path = self.path + '/wav/' + f_name
            f_path = os.path.abspath(f_path)

            emo = wav_2_label[f_name[:-4]]
            actor_id = f_name[2:5]

            if f_name in wav_2_duration.keys():
                duration = wav_2_duration[f_name] 
            else:
                y, sr = librosa.load(self.path + '/wav/' + f_name)
                duration = librosa.get_duration(y=y, sr=sr)

            data.append({
                'impro/script'  : 'impro' if 'impro' in f_name else 'script',
                'session'       : actor_id[:-1],
                'actor_id'      : actor_id,
                'gender'        : actor_id[-1:],
                'lang'          : 'eng',
                'wav_path'      : f_path,
                'file_name'     : f_name,
                'emo'           : emo,
                'text'          : file_2_transcript[f_name[:-4]],
                'length'        : duration,
            })

        return pd.DataFrame(data)
