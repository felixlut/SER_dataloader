from dataloader.base_dataset import BaseDataset


class Emovo(BaseDataset):
    def __init__(self, top_path):
        self.annotation_mapping = {
            'dis': 'Disgusted',
            'gio': 'Happy',
            'pau': 'Fear',
            'rab': 'Angry',
            'sor': 'Surprised',
            'tri': 'Sad',
            'neu': 'Neutral'
        }
        self.text_mapping = {} # TODO: Add transcripts
        super().__init__(top_path + 'emovodata/')

    def get_dataset_specific_dict(self, f_name):
        emo, act_id, sentence = f_name.split('-')

        return {
            'actor_id'  : act_id,
            'emo'       : self.annotation_mapping[emo],
            'lang'      : 'it',
            # 'text'      : self.text_mapping[sentence], TODO: Add transcript
        }
