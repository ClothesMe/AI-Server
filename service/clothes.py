# import tensorflow as tf
# import cv2
import numpy as np
from colorthief import ColorThief
import tempfile
import os
import io
# from PIL import Image
# import common.white_balance as white_balance
from common import model as model
from common import color as color


async def getClothesType(image):

    # 새로운 이미지 전처리 및 예측
    preprocessed_image = preprocess_image(image)
    predictions = model.getTypeModel().predict(preprocessed_image)

    # 예측 결과 확인
    predicted_class = np.argmax(predictions)  # 가장 높은 확률을 가진 클래스 인덱스

    return predicted_class

def getClothesColor(image):

    clothes_color = color.getClothesMainColor(image)
    
    return clothes_color

async def getClothesPattern(image):

    # 새로운 이미지 전처리 및 예측
    preprocessed_image = preprocess_image(image)
    predictions = model.getPatternModel().predict(preprocessed_image)

    # 예측 결과 확인
    predicted_class = np.argmax(predictions)  # 가장 높은 확률을 가진 클래스 인덱스

    return predicted_class

# 이미지 전처리 함수
def preprocess_image(image):

    # RGB 형식으로 변환
    rgb_image = image.convert("RGB")
    # 이미지 크기를 (224, 224)로 조정
    resized_image = rgb_image.resize((224, 224))
    # 이미지를 배열로 변환
    array_image = np.array(resized_image)
    # 이미지를 모델이 예상하는 형태로 변환
    preprocessed_image = np.expand_dims(array_image, axis=0)

    return preprocessed_image