import sys
import argparse
from yolo import YOLO, detect_video
from PIL import Image

if __name__ == '__main__':
    # class YOLO defines the default value, so suppress any default here
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    '''
    Command line options
    '''
    parser.add_argument(
        '--image_list', type=str,
        help='path to list of images in yolo format (dev or test list)')

    FLAGS = parser.parse_args()

    yolo = YOLO()
    imagelist_filepath_and_name = FLAGS.image_list

    with open(imagelist_filepath_and_name, 'r') as f:
        names = f.readlines()
    for name in names:
        img_src = '.' + name.split()[0]
        image = Image.open(img_src)

        these_predictions = yolo.detect_image(image, img_src.split('/')[-1])
        img_filename = img_src.split('/')[-1]

        with open(f"../logs/000/detection-predictions/{img_filename}",'w') as f:
            f.write('\n'.join(these_predictions))
