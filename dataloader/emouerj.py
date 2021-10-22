from dataloader.base_dataset import BaseDataset


class Cremad(BaseDataset):
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
        act_id = f_name[1:2]
        emo = self.annotation_mapping[f_name[3]]
        return {
            'actor_id'  : act_id,
            'lang'      : 'por',
            'emo'       : self.annotation_mapping[emo],
            'dataset'   : 'emouerj',
        }
