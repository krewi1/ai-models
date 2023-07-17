import argparse
import datetime
import numpy as np
import os
import os.path as osp
import glob
import cv2
import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image


assert insightface.__version__>='0.7'

parser = argparse.ArgumentParser(description='Face swap images.')

parser.add_argument('-s', type=str, help='File name of input file. Faces will be infered from this picture.')
parser.add_argument('-t', type=str, help='File name of target file. Faces will be applied into this picture.')
parser.add_argument('-o', type=str, help='Name of output file')
parser.add_argument('-i', type=int, help='Starting face index in input image.', default=0)

args = parser.parse_args()

source = args.s
target = args.t
output = args.o
start_index = args.i

assert source is not None, "-s source have to be defined"
assert target is not None, "-t target have to be defined"
assert output is not None, "-o output have to be defined"

if __name__ == '__main__':
    source_image = cv2.imread(source)
    target_image = cv2.imread(target)
    app = FaceAnalysis(name='buffalo_l')
    app.prepare(ctx_id=0, det_size=(640, 640))
    swapper = insightface.model_zoo.get_model('inswapper_128.onnx', download=True, download_zip=True)


    source_faces = app.get(source_image)
    target_faces = app.get(target_image)
    target_faces = sorted(target_faces, key = lambda x : x.bbox[0])
    res = target_image.copy()
    counter = start_index
    for face in target_faces:
        res = swapper.get(res, face, source_faces[counter], paste_back=True)
        counter = (counter + 1) % len(source_faces)
    cv2.imwrite(output, res)