import os
import json
import shutil
import random

# This script converts json annotations to YOLO format
# and moves the data in to following directory structure

# | - workingdir
#     | -- data
#         | -- train
#         | -- val
#     | -- labels
#         | -- train
#         | -- val

	
os.makedirs('labels', exist_ok=True)
os.makedirs('labels/train', exist_ok=True)
os.makedirs('labels/val', exist_ok=True)

os.makedirs('data', exist_ok=True)
os.makedirs('data/train', exist_ok=True)
os.makedirs('data/val', exist_ok=True)

# Function to parse COCO annotations and create YOLO format labels
def create_yolo_labels(coco_file):
    with open(coco_file) as f:
        coco = json.load(f)

    images = coco['images']
    annotations = coco['annotations']
    categories = {cat['id']: cat['name'] for cat in coco['categories']}


    for ann in annotations:
        image = next(img for img in images if img['id'] == ann['image_id'])
        width, height = image['width'], image['height']
        x_center = (ann['bbox'][0] + ann['bbox'][2] / 2) / width
        y_center = (ann['bbox'][1] + ann['bbox'][3] / 2) / height
        bbox_width = ann['bbox'][2] / width
        bbox_height = ann['bbox'][3] / height
        category_id = ann['category_id']
        image_id = ann['image_id']
        filename = image['file_name']
        label_filename = filename.split('.jpg')[0]
        label_path = os.path.join(f'{label_filename}.txt')
        with open(label_path, 'w') as f:
            line = f"{category_id} {x_center} {y_center} {bbox_width} {bbox_height}\n"
            f.write(line)

# Function to split images into train and val folders
def split_images_into_train_val(src_folder, train_ratio=0.8):
    file_names = [file for file in os.listdir(src_folder) if file.endswith('.txt')]
    random.shuffle(file_names)

    train_files = file_names[:int(len(file_names) * train_ratio)]
    val_files = file_names[int(len(file_names) * train_ratio):]

    for mode, files in [('train', train_files), ('val', val_files)]:
        for file in files:
            src_path = os.path.join(src_folder, file)
            dest_path = os.path.join('labels', mode, file)
            shutil.copy(src_path, dest_path)

            img = file.split('.txt')[0]+'.jpg'
            src_path_img = os.path.join(src_folder, img)
            dest_path_img = os.path.join('data', mode, img)
            shutil.copy(src_path_img, dest_path_img)

# Create YOLO format labels
coco_file = 'annotations_coco.json'
create_yolo_labels(coco_file)

# Split images into train and val folders
split_images_into_train_val('atlantic')
split_images_into_train_val('humpback')