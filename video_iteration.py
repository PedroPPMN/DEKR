import os
import glob

root = '/mnt/data/Unifall/dataset/T-set/'
output_dir = '/mnt/data/Unifall/modelos/dekr/output/'
os.makedirs(output_dir, exist_ok=True)
for file in glob.glob(root + '/vid*'):
    print('Cerregando: ' + file)
    file_name = file.split('vid-')[1] + '/'

    os.system(
    'python tools/inference_demo.py --cfg experiments/coco/inference_demo_coco.yaml \
    '+'--videoFile ' + file + ' \
    '+'--outputDir ' + output_dir + file_name + ' \
    '+'--visthre 0.3 \
    '+'TEST.MODEL_FILE ./model/pose_coco/pose_dekr_hrnetw32_coco.pth')


