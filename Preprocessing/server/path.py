import argparse
import os
import re


def filter_image_paths(image_paths: str):
    return list(
        filter(
            lambda path: re.match(r'^.*\.(jpe?g|png)$', path.lower()),
            image_paths
        )
    )


def get_image_paths(dir_path: str):
    file_paths = []
    for dir_or_file in os.scandir(dir_path):
        if os.path.isdir(dir_or_file.path):
            file_paths.extend(get_image_paths(dir_or_file.path))
        else:
            file_paths.append(dir_or_file.path)

    return filter_image_paths(file_paths)


if __name__ == '__main__':
    image_paths = get_image_paths('../images/')
