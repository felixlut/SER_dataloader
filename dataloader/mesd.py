from dataloader.base_dataset import BaseDataset


class Mesd(BaseDataset):
    def __init__(self, top_path):
        self.annotation_mapping = {
            'Anger'     : 'Angry',
            'Disgust'   : 'Disgusted',
            'Fear'      : 'Fear',
            'Happiness' : 'Happy',
            'Neutral'   : 'Neutral',
            'Sadness'   : 'Sad',
        }
        super().__init__(top_path + 'mesddata/')

    def get_dataset_specific_dict(self, f_name):
        emo, gender, corpus, text = f_name.split('_', 3)
        return {
            'emo'       : self.annotation_mapping[emo],
            'lang'      : 'spanish (Mexico)',
            'gender'    : gender,
            'corpus'    : corpus,
            'text'      : text
        }
