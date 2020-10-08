'''
    A simple script to download the dataset, extract it into the right path for mmdetection
'''
import os
from os.path import join as osp
import utils
import wget
import zipfile
import shutil

TRAIN_URL = 'https://datasets.aicrowd.com/default/aicrowd-public-datasets/food-recognition-challenge/v0.4/train-v0.4.tar.gz'
VALID_URL = 'https://datasets.aicrowd.com/default/aicrowd-public-datasets/food-recognition-challenge/v0.4/val-v0.4.tar.gz'
# TEST_URL = 'https://datasets.aicrowd.com/default/aicrowd-public-datasets/food-recognition-challenge/v0.4/test_images-v0.4.tar.gz'
DATA_ROOT = './data'
TEMP_PATH = osp(DATA_ROOT, '.temp')


def download_extract(url, download_dest, extract_dest):
    '''
        This method downloads and extracts 'tar.gz' file
    '''
    # assert len(os.listdir(extract_dest)) == 0, f'{extract_dest} Not Empty'
    print(f'Downloading file from {url}')
    wget.download(url, download_dest)
    print(f'\nExtracting to {extract_dest}')
    with zipfile.ZipFile(download_dest, "r") as zip_ref:
        zip_ref.extractall(extract_dest)


if __name__ == '__main__':
    utils.mksubdir(TEMP_PATH)
    # download_extract(TRAIN_URL, osp(TEMP_PATH, 'train.tar.gz'), DATA_ROOT)
    download_extract(VALID_URL, osp(TEMP_PATH, 'val.tar.gz'), DATA_ROOT)
    # download_extract(TEST_URL, osp(TEMP_PATH, 'test.tar.gz'), DATA_ROOT)
    shutil.rmtree(TEMP_PATH)
