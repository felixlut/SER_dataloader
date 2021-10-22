from dataloader.base_dataset import BaseDataset


class Emouerj(BaseDataset):
    def __init__(self, top_path):
        self.annotation_mapping = {
            'a': 'Angry',
            'h': 'Happy',
            's': 'Sad',
            'n': 'Neutral',
        }
        super().__init__(top_path + 'emouerj/')

    def get_dataset_specific_dict(self, f_name):
        gender = 'F' if f_name[0] == 'w' else 'M'
        act_id = f_name[:3]
        emo = self.annotation_mapping[f_name[3]]
        return {
            'actor_id'  : act_id,
            'lang'      : 'por',
            'gender'    : gender,
            'emo'       : emo,
            'dataset'   : 'emouerj',
        }
