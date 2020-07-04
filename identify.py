import numpy as np
from cnocr import CnOcr
from cnstd import CnStd
kernel = np.ones((10,10),np.uint8)
global std
global cn_ocr
std = CnStd(model_name='resnet50_v1b', root='C:/Users/HP/AppData/Roaming/Python/Python36/site-packages/cnstd')
cn_ocr = CnOcr(model_name="conv-lite-fc")

#检测车牌号
def identify(image):
    std = CnStd(model_name='resnet50_v1b', root='C:/Users/HP/AppData/Roaming/Python/Python36/site-packages/cnstd')
    global cn_ocr
    box_info_list = std.detect(image)

    ocr_res=[]
    for box_info in box_info_list:
        cropped_img = box_info['cropped_img']
        ocr_res.extend(cn_ocr.ocr_for_single_line(cropped_img))
        print('ocr result1: %s' % ''.join(ocr_res))
    return ocr_res