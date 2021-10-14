import pandas as pd

from dataloader.base_dataset import BaseDataset


class Oreau(BaseDataset):
    def __init__(self, top_path):
        self.path = top_path + 'oreaudata/'
        self.annotation_mapping = {
            'C': 'Angry',
            'T': 'Sad',
            'J': 'Happy',
            'P': 'Fear',
            'D': 'Disgusted',
            'S': 'Surprised',
            'N': 'Neutral'
        }
        self.actor_dict = pd.read_csv(self.path + 'actors.csv', index_col=0, squeeze=True).to_dict()
        super().__init__(self.path)

    def get_dataset_specific_dict(self, f_name):
        act_id = int(f_name[:2])
        utterance = f_name[2:5]
        emo = f_name[5]
        return {
            'actor_id'  : act_id,
            'emo'       : self.annotation_mapping[emo],
            'lang'      : 'fr',
            'gender'    : self.actor_dict['gender'][act_id] if act_id in self.actor_dict['gender'] else None,
            'age'       : int(self.actor_dict['age'][act_id]) if act_id in self.actor_dict['age'] else None,
        }
