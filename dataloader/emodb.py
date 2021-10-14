from .base_dataset import BaseDataset


class Emodb(BaseDataset):
    def __init__(self, top_path):
        annotation_mapping = {
            'N': 'Neutral',
            'F': 'Happy',
            'T': 'Sad',
            'W': 'Angry',
            'L': 'Bored',
            'E': 'Disgusted',
            'A': 'Fear'
        }
        super().__init__(top_path + 'emodb-data', annotation_mapping)

    def get_dataset_specific_dict(self, f_name):
        return {
            'actor_id'  : f_name[:2],
            'emo'       : self.annotation_mapping[f_name[5]],
            'lang'      : 'ger',
        }
