import argparse
import os


def main(dir_path: str) -> None:
    extensions = set()
    for file in os.listdir(dir_path):
        ext = os.path.splitext(file)[-1]
        extensions.add(ext)
    extensions = sorted(extensions)
    for ext in extensions:
        print(ext)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("dirpath", type=str, help="Path to the directory")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_arguments()
    main(args.dirpath)
