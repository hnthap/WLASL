import argparse
import json
import os
from config_reader import load_config


if __name__ == '__main__':
    config = load_config()

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('k', type=int, help='Number of glosses')
    parser.add_argument('--json_file', type=str, help='Path to the JSON file',
                        default=config['metadata_file'])
    args = parser.parse_args()

    # Validate arguments
    assert os.path.exists(args.json_file)
    assert isinstance(args.k, int) and args.k > 0 and args.k <= 2000

    # Open original metadata file
    with open(args.json_file, 'rt') as f:
        content = json.load(f)

    # Generate new metadata file
    path, ext = os.path.splitext(args.json_file)
    output_file = path + '.' + str(args.k) + ext
    with open(output_file, 'wt') as f:
        json.dump(content[:args.k], f, indent=4)

    # Simple test
    with open(output_file, 'rt') as f:
        glosses = json.load(f)
        assert len(glosses) == args.k, f'{len(glosses)}, {args.k}'
