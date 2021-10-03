import os
import librosa
from tqdm import tqdm
import pandas as pd

def _get_duration_dict(wav_path, csv_path=None):
    wav_2_duration = {}
    if csv_path is not None and os.path.isfile(csv_path):
        wav_2_duration = pd.read_csv(csv_path, header=None, index_col=0, squeeze=True).to_dict()

    files = os.listdir(wav_path)
    for f_name in tqdm(files, desc='Duration'):
        if f_name[:-4] not in wav_2_duration.keys():
            duration = librosa.get_duration(filename=wav_path + f_name)
            wav_2_duration[f_name[:-4]] = duration

    df = pd.DataFrame.from_dict(wav_2_duration, orient='index')
    df = df.sort_index()
    df.to_csv('wav_2_duration.csv')

    return wav_2_duration
