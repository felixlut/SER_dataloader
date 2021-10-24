from dataloader.base_dataset import BaseDataset


class Subesco(BaseDataset):
    def __init__(self, top_path):
        self.annotation_mapping = {
            'ANGRY'     : 'Angry',
            'HAPPY'     : 'Happy',
            'SAD'       : 'Sad',
            'NEUTRAL'   : 'Neutral',
            'DISGUST'   : 'Disgusted',
            'FEAR'      : 'Fear',
            'SURPRISE'  : 'Surprised',
        }
        super().__init__(top_path + 'subesco/')

    def get_dataset_specific_dict(self, f_name):
        gender, speaker_num, speaker_name, sentence, sentence_num, emo, take_num = f_name.split('_')
        act_id = gender + speaker_num
        
        return {
            'actor_id'  : act_id,
            'lang'      : 'ban',
            'gender'    : gender,
            'emo'       : self.annotation_mapping[emo],
            'dataset'   : 'subesco',
        }
