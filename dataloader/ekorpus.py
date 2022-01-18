import pandas as pd
import textgrid
from tqdm import tqdm


from dataloader.base_dataset import BaseDataset


class Ekorpus(BaseDataset):
    def __init__(self, top_path):
        self.path = top_path + 'ekorpus/'
        self.wav_2_label = pd.read_csv(self.path + 'wav_2_label.csv', index_col=0, squeeze=True).to_dict()
        self.annotation_mapping = {
            'anger'     : 'Angry',
            'neutral'   : 'Neutral',
            'sadness'   : 'Sad',
            'joy'       : 'Happy',
        }

        super().__init__(self.path)

    def get_labels():
        # Read a TextGrid object from a file.
        wav_2_label = {}
        for f_name in tqdm(os.listdir('/kaggle/input/ekorpus'), desc='Load Dataframe'):
            f_path = '/kaggle/input/ekorpus/' + f_name
            if f_name[-4:] == 'Grid':
                tg = textgrid.TextGrid.fromFile(f_path)
                wav_2_label[f_name[:-9]] = tg[-1][0].mark
                
        return wav_2_label

    def get_dataset_specific_dict(self, f_name):
        return {
            'lang'      : 'est',
            'emo'       : self.annotation_mapping[self.wav_2_label[int(f_name)]],
            'dataset'   : 'ekorpus',
        }
