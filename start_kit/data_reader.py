import json
from config_reader import load_config

config = load_config()

file_path = config['metadata_file']

with open(file_path) as ipf:
    content = json.load(ipf)

cnt_train = 0
cnt_val = 0
cnt_test = 0

for ent in content:
    gloss = ent['gloss']

    for inst in ent['instances']:
        split = inst['split']

        if split == 'train':
            cnt_train += 1
        elif split == 'val':
            cnt_val += 1
        elif split == 'test':
            cnt_test += 1
        else:
            raise ValueError("Invalid split.")

print('total glosses: {}'.format(len(content)))
print('total samples: {}'.format(cnt_train + cnt_val + cnt_test))
