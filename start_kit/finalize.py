from copy import deepcopy
import os
from config_reader import load_config, load_json, save_json


VIDEOS_DIR = 'raw_videos'
assert os.path.isdir(VIDEOS_DIR)


def main():
    config = load_config()
    json_file = config['metadata_file']
    metadata = load_json(json_file)
    new_metadata = []
    total_missing = 0
    total_instances = 0
    for item in metadata:
        instances = item['instances']
        new_item = deepcopy(item)
        new_item['instances'] = []
        new_item['missing_instances'] = []
        missing_count = 0
        for instance in instances:
            if check_instance_exists(instance):
                new_item['instances'].append(instance)
            else:
                new_item['missing_instances'].append(instance)
                missing_count += 1
        new_metadata.append(new_item)
        print('Gloss "%s". Missing instances: %d out of %d (%.2f%%)' % (
            item['gloss'], missing_count, len(instances),
            100.0 * missing_count / len(instances)))
        total_missing += missing_count
        total_instances += len(instances)
    print('\nTotal missing instances: %d out of %d (%.2f%%)' % (
        total_missing, total_instances, 100.0 * total_missing / total_instances))
    save_json(new_metadata, 'WLASL_available.json', indent=2)


def check_instance_exists(instance):
    video_id = instance['video_id']
    return os.path.exists(get_video_path(video_id))


def get_video_path(video_id):
    return os.path.join(VIDEOS_DIR, '%s.mp4' % video_id)


if __name__ == '__main__':
    main()
