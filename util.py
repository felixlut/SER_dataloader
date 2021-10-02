import os
import librosa
import tqdm
import pandas as pd

def _get_duration_dict(path):
    csv_path = path + 'wav_2_duration.csv'
    if os.path.isfile(csv_path):
        return pd.read_csv(csv_path, header=None, index_col=0, squeeze=True).to_dict()

    wav_2_duration = {}
    files = os.listdir(path + '/wav/')
    for f_name in tqdm(files):
        y, sr = librosa.load(path + '/wav/' + f_name)
        duration = librosa.get_duration(y=y, sr=sr)
        wav_2_duration[f_name] = duration

    df = pd.DataFrame.from_dict(wav_2_duration, orient='index')
    df.to_csv('wav_2_duration.csv')

    return wav_2_duration
