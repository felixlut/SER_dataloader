from dataloader.base_dataset import BaseDataset


class Emodb(BaseDataset):
    def __init__(self, top_path):
        self.actor_2_gender = {
            '03': 'M', 
            '08': 'F', 
            '09': 'F', 
            '10': 'M', 
            '11': 'M', 
            '12': 'M', 
            '13': 'F', 
            '14': 'F', 
            '15': 'M', 
            '16': 'F', 
        }
        self.annotation_mapping = {
            'N': 'Neutral',
            'F': 'Happy',
            'T': 'Sad',
            'W': 'Angry',
            'L': 'Bored',
            'E': 'Disgusted',
            'A': 'Fear'
        }
        super().__init__(top_path + 'emodb-data/')

    def get_dataset_specific_dict(self, f_name):
        act_id = f_name[:2]
        return {
            'actor_id'  : str(act_id),
            'emo'       : self.annotation_mapping[f_name[5]],
            'gender'    : self.actor_2_gender[act_id],
            'lang'      : 'ger',
            'dataset'   : 'emodb',
        }
