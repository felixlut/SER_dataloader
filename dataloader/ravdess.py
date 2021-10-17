from dataloader.base_dataset import BaseDataset


class Ravdess(BaseDataset):
    def __init__(self, top_path):
        self.annotation_mapping = {
            '01': 'Neutral',
            '02': 'Calm',
            '03': 'Happy',
            '04': 'Sad',
            '05': 'Angry',
            '06': 'Fear',
            '07': 'Disgusted',
            '08': 'Surprised',
        }
        self.text_mapping = {
            '01': "Kids are talking by the door",
            '02': "Dogs are sitting by the door",
        }
        super().__init__(top_path + 'ravdess/')

    def get_dataset_specific_dict(self, f_name):
        mod, vocal, emo, intensity, sentence, rep, act_id = f_name.split('-')
        return {
            'actor_id'  : act_id,
            'lang'      : 'eng',
            'emo'       : self.annotation_mapping[emo],
            'text'      : self.text_mapping[sentence],
            'gender'    : 'F' if int(act_id) % 2 == 0 else 'M',
            'dataset'   : 'ravdess',
        }
