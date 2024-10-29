import argparse
import os
import json
from shutil import copyfile


def parse_args():
    parser = argparse.ArgumentParser(description='Process Arcade Stenosis dataset.')
    parser.add_argument('input_dir', type=str, help='Path to the input data directory')
    parser.add_argument('output_dir', type=str, help='Path to the output data directory')
    return parser.parse_args()


def load_and_fix_annotations(input_dir, output_dir, mode):
    # Define the path to the dataset
    input_path = os.path.join(input_dir, mode, "annotations", f'{mode}.json')
    output_path = os.path.join(output_dir, mode, "annotations", f'{mode}.json')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Load the dataset
    with open(input_path, 'r') as file:
        data = json.load(file)
    
    # Reassign unique IDs to annotations and convert bbox format
    unique_id = 0
    for item in data['annotations']:
        item['id'] = unique_id
        unique_id += 1
    
    # Save the fixed dataset
    with open(output_path, 'w') as file:
        json.dump(data, file, indent=4)


def move_images(input_dir, output_dir, mode):
    input_path = os.path.join(input_dir, f'{mode}/images')
    output_path = os.path.join(output_dir, f'{mode}/images')
    os.makedirs(output_path, exist_ok=True)
    for file in os.listdir(input_path):
        copyfile(os.path.join(input_path, file), os.path.join(output_path, file))


def main():
    args = parse_args()
    # Load and fix annotations for all modes
    for mode in ['train', 'val', 'test']:
        move_images(args.input_dir, args.output_dir, mode)
        load_and_fix_annotations(args.input_dir, args.output_dir, mode)


if __name__ == '__main__':
    main()