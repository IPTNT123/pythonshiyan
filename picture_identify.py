import cv2
import numpy as np
import pytesseract
from cnocr import CnOcr
import cv2
from cnstd import CnStd

from identify import identify

kernel = np.ones((10,10),np.uint8)
global std
global cn_ocr
std = CnStd(model_name='resnet50_v1b', root='C:/Users/HP/AppData/Roaming/Python/Python36/site-packages/cnstd')
cn_ocr = CnOcr(model_name="conv-lite-fc")

#图像处理方法
def picture_identify(name):
    original=cv2.imread(name)
    rawImage = cv2.imread(name)
    #高斯模糊
    image = cv2.GaussianBlur(rawImage, (3, 3), 0)
    #转为灰度图像
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    #Canny边缘检测
    image = cv2.Canny(image,100,300)
    #Sobel算子
    Sobel_x = cv2.Sobel(image, cv2.CV_16S, 1, 0)
    absX = cv2.convertScaleAbs(Sobel_x)
    image = absX

    #图像二值化
    ret, image = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)

    #闭操作
    kernelX = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 10))
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernelX,iterations = 1)

    # #膨胀腐蚀

    kernelX = cv2.getStructuringElement(cv2.MORPH_RECT, (19, 1))
    kernelY = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 19))

    image = cv2.dilate(image, kernelX)
    image = cv2.erode(image, kernelX)

    image = cv2.erode(image, kernelY)
    image = cv2.dilate(image, kernelY)

    #中值滤波
    image = cv2.medianBlur(image, 15)

    #查找轮廓
    contours,hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for item in contours:
        x,y,weight,height = cv2.boundingRect(item)
        if weight > (height * 2) and weight > 50 and height > 25:
            # 裁剪区域图片
            cv2.rectangle(image, (x, y), (x + weight, y + height), (0, 255, 0), 2)
            chepai = original[y:y + height, x:x + weight]
            list = identify(chepai)
            print(list)
            if (len(list) > 3):
                cv2.resize(chepai, (300, 100))
                cv2.imwrite("pai.jpg", chepai)
                return list
    return [0]

