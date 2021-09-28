import pandas as pd
import os
import tqdm

def __init__(self, top_path, anno_map=None):
    self.path = top_path + 'iemocap'
    self.df = self.get_df(anno_map)


def _get_label_dict(path):
    labels = ['neu', 'fru', 'hap', 'sad', 'ang', 'fea', 'exc', 'sur', 'dis', 'xxx', 'oth']
    sessions = ['Session' + str(i) for i in range(1, 6)]
    wav_to_label = {}
    for sess in sessions:
        directory = path + sess + '/dialog/EmoEvaluation/'
        for file_name in os.listdir(directory):            
            if file_name[-4:] == '.txt':
                out = open(directory + file_name).read().split()
                pairs = [(out[i-1], out[i]) for i, word in enumerate(out) if word in labels]
                                
                for f, emo in pairs:
                    wav_to_label[f] = emo
    
    return wav_to_label

def get_df(top_path, anno_map=None):
    path = top_path + '/iemocap/'
    if anno_map is None:
        anno_map = {
            'ang': 'Angry',
            'hap': 'Happy',
            'exc': 'Happy', # Excited is counted as Happy
            'sad': 'Sad',
            'neu': 'Neutral',
        }

    text_df = pd.read_csv(path + 'transcriptions.csv')
    file_2_transcript = text_df.set_index('file')['text'].to_dict()
    wav_to_label = _get_label_dict()
    data = []
    sessions = ['Session' + str(i) for i in range(1, 6)]
    for sess in tqdm(sessions):
        directory = path + sess + '/sentences/wav/'
        for sub_dir in os.listdir(directory):
            for file_name in os.listdir(os.path.join(directory, sub_dir)):
                if '.pk' in file_name:
                    continue

                file_path = directory + sub_dir + os.sep + file_name
                emo = wav_to_label[file_name[:-4]]
                if emo in anno_map.keys():
                    emo = anno_map[emo]
                    actor_id = str(sess[-1:]).zfill(2) + sub_dir[5]
                    data.append({
                        'impro/script'  : 'impro' if 'impro' in file_name else 'script',
                        'session'       : sess[-1:],
                        'actor_id'      : actor_id,
                        'gender'        : actor_id[-1:],
                        'lang'          : 'eng',
                        'wav_path'      : file_path,
                        'file_name'     : file_name,
                        'emo'           : emo,
                        'text'          : file_2_transcript[file_name]
                    })
    
    return pd.DataFrame(data)
