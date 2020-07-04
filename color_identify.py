import numpy as np
from cnocr import CnOcr
import cv2
from cnstd import CnStd
from identify import identify

global std,cn_ocr
kernel = np.ones((10,10),np.uint8)

std = CnStd(model_name='resnet50_v1b', root='C:/Users/HP/AppData/Roaming/Python/Python36/site-packages/cnstd')
cn_ocr = CnOcr(model_name="conv-lite-fc")

#颜色提取方法
def color_identify(name):
    #颜色范围
    lower = np.array([70, 110, 110])
    upper = np.array([130, 255, 255])

    raw = cv2.imread(name)
    original = cv2.imread(name)

    #中值滤波
    hsv_one = cv2.medianBlur(raw,5)
    hsv = cv2.cvtColor(hsv_one, cv2.COLOR_BGR2HSV)

    #颜色提取
    mask_blue = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(raw, raw, mask=mask_blue)
    res = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
    ret, iIMAGE= cv2.threshold(res, 0, 255,cv2.THRESH_OTSU)

    #查找轮廓
    con,hierarchy = cv2.findContours(iIMAGE, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    img = cv2.imread(name)

    for item in con:
        x,y,w,h = cv2.boundingRect(item)
        if w > (h * 2) and w > 100 and h > 100:
            # 裁剪区域图片
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            chepai = original[y:y + h, x:x + w]
            list = identify(chepai)
            print(list)
            if(len(list) > 3):
                cv2.resize(chepai,(300,100))
                cv2.imwrite("pai.jpg",chepai)
                return list
    return [0]