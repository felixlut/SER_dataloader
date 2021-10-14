from abc import ABC, abstractmethod
import pandas as pd
from tqdm import tqdm
import librosa
import os


class BaseDataset(ABC):
    def __init__(self, path):
        assert path[-1], "Make sure that the path to the dataset ends with a '/'"

        self.path = path
        self.wav_path = self.path + '/wav/wav/'
        self.wav_tele_path = self.path + '/wav_telephone/wav_telephone/'
        self.df = self.get_df()

    @abstractmethod
    def get_dataset_specific_dict(self, f_name):
        pass

    @abstractmethod
    def _valid_file(self, f_name):
        return True
    
    def _load_duration_dict(self):
        csv_path = self.path + 'wav_2_duration.csv'
        wav_2_duration = {}
        if os.path.isfile(csv_path):
            wav_2_duration = pd.read_csv(csv_path, header=None, index_col=0, squeeze=True).to_dict()

        files = os.listdir(self.wav_path)
        for f_name in tqdm(files, desc='Load Durations'):
            if f_name[:-4] not in wav_2_duration.keys():
                duration = librosa.get_duration(filename=self.wav_path + f_name)
                wav_2_duration[f_name[:-4]] = duration
        
        return wav_2_duration

    def get_df(self):
        tele_exists = os.path.isdir(self.wav_tele_path)
        wav_2_duration = self._load_duration_dict()
        data = []
        for f_name in tqdm(os.listdir(self.wav_path), desc='Load Dataframe'):
            if self._valid_file(f_name):
                # Cut-off the file-extension
                f_name = f_name[:-4]

                # Set the dataset specific fields
                dataset_specific_dict = self.get_dataset_specific_dict(f_name)

                # Set the dataset independent fields            
                dataset_specific_dict['wav_path'] = os.path.abspath(self.wav_path + f_name + '.wav')
                dataset_specific_dict['file_name'] = f_name
                dataset_specific_dict['length'] = wav_2_duration[f_name]
                if tele_exists: dataset_specific_dict['wav_tele_path'] = os.path.abspath(self.wav_tele_path + f_name + '.wav')

                data.append(dataset_specific_dict)

        df = pd.DataFrame(data)
        # Make sure that a set of fields are present in the data
        assert set(['lang', 'wav_path', 'emo', 'length']).issubset(set(df.columns))
        return df
