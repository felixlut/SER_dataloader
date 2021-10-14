from dataloader.base_dataset import BaseDataset


class Cremad(BaseDataset):
    def __init__(self, top_path):
        self.annotation_mapping = {
            'ANG': 'Angry',
            'HAP': 'Happy',
            'SAD': 'Sad',
            'NEU': 'Neutral',
            'DIS': 'Disgusted',
            'FEA': 'Fear',
        }
        self.text_mapping = {
            'IEO': "It's eleven o'clock",
            'TIE': 'That is exactly what happened',
            'IOM': "I'm on my way to the meeting",
            'IWW': 'I wonder what this is about',
            'TAI': 'The airplane is almost full',
            'MTI': 'Maybe tomorrow it will be cold',
            'IWL': 'I would like a new alarm clock',
            'ITH': "I think I have a doctor's appointment",
            'DFA': "Don't forget a jacket",
            'ITS': "I think I've seen this before",
            'TSI': "The surface is slick",
            'WSI': "We'll stop in a couple of minutes",
        }
        super().__init__(top_path + 'cremad/')

    def get_dataset_specific_dict(self, f_name):
        act_id, sentence, emo, intensity = f_name.split('_')
        return {
            'actor_id'  : act_id,
            'lang'      : 'eng',
            'emo'       : self.annotation_mapping[emo],
            'text'      : self.text_mapping[sentence],
            'intensity' : intensity[:-4]
        }
