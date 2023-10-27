import os
import shutil
import zipfile
import kaggle

# Set up the dataset directory
DATASET_DIR = 'Dataset'
TRAIN_DIR = os.path.join(DATASET_DIR, 'train')
VALIDATION_DIR = os.path.join(DATASET_DIR, 'validation')
TEST_DIR = os.path.join(DATASET_DIR, 'test')

# Download the dataset
kaggle.api.dataset_download_files('mahmoudnoor/high-resolution-catdogbird-image-dataset-13000', path=DATASET_DIR, unzip=True)

# Create train, validation, and test directories
os.makedirs(TRAIN_DIR, exist_ok=True)
os.makedirs(VALIDATION_DIR, exist_ok=True)
os.makedirs(TEST_DIR, exist_ok=True)

# Define the categories
categories = ['cats', 'dogs', 'birds']

def split_data(SOURCE_DIR, TRAIN_DIR, VALIDATION_DIR, TEST_DIR, SPLIT_SIZE):
    all_files = os.listdir(SOURCE_DIR)
    all_files = [file for file in all_files if os.path.getsize(os.path.join(SOURCE_DIR, file)) > 0]
    
    n_files = len(all_files)
    split_train = int(n_files * SPLIT_SIZE[0])
    split_val = split_train + int(n_files * SPLIT_SIZE[1])

    train_files = all_files[:split_train]
    validation_files = all_files[split_train:split_val]
    test_files = all_files[split_val:]

    for file in train_files:
        shutil.copy(os.path.join(SOURCE_DIR, file), os.path.join(TRAIN_DIR, file))

    for file in validation_files:
        shutil.copy(os.path.join(SOURCE_DIR, file), os.path.join(VALIDATION_DIR, file))

    for file in test_files:
        shutil.copy(os.path.join(SOURCE_DIR, file), os.path.join(TEST_DIR, file))

for category in categories:
    SOURCE_DIR = os.path.join(DATASET_DIR, category)
    train_category_dir = os.path.join(TRAIN_DIR, category)
    validation_category_dir = os.path.join(VALIDATION_DIR, category)
    test_category_dir = os.path.join(TEST_DIR, category)

    os.makedirs(train_category_dir, exist_ok=True)
    os.makedirs(validation_category_dir, exist_ok=True)
    os.makedirs(test_category_dir, exist_ok=True)

    split_data(SOURCE_DIR, train_category_dir, validation_category_dir, test_category_dir, [0.8, 0.1, 0.1])
