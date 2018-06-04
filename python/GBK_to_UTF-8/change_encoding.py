#! /usr/bin/python3

import glob
import os

SOURCE_DIRECTORY = 'old'
SOURCE_FILES = []

TARGET_DIRECTORY = 'new'
if not os.path.exists(TARGET_DIRECTORY):
    os.mkdir(TARGET_DIRECTORY)

SOURCE_FILES = glob.glob(os.path.join(SOURCE_DIRECTORY, '*'))

for file in SOURCE_FILES:
    file_name = os.path.basename(file)
    with open(file, 'r', encoding='GBK') as sf:
        lines = sf.readlines()
        for line in lines:
            line = line.strip()
            with open(os.path.join(TARGET_DIRECTORY, file_name), 'a', encoding='utf-8') as tf:
                if line:
                    tf.write(line+'\n')
