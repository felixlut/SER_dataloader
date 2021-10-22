from dataloader.base_dataset import BaseDataset


class Polish(BaseDataset):
    def __init__(self, top_path):
        self.annotation_mapping = {
            'a': 'Angry',
            'n': 'Neutral',
            's': 'Fear',
        }
        super().__init__(top_path + 'polish/')

    def get_dataset_specific_dict(self, f_name):
        act_id, rest = f_name.split('.', 1)
        gender = act_id[0]
        emo = rest[0]
        return {
            'actor_id'  : act_id,
            'lang'      : 'pol',
            'gender'    : gender,
            'emo'       : self.annotation_mapping[emo],
            'dataset'   : 'polish',
        }
