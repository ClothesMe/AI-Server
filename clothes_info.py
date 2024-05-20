import tensorflow as tf
import cv2
import numpy as np
from rembg import remove
from colorthief import ColorThief
import color
import os
import io
from PIL import Image
import white_balance
import tempfile


def remove_background(clothes_image):
    """
    배경 제거
    :param cloth_image: 배경 제거할 이미지
    :return: 배경이 제거된 이미지
    """   
    removed_background = remove(clothes_image)
        
    # numpy 배열로 변환
    removed_background_np = np.array(removed_background)

    return removed_background_np

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

def getClothesType(image):
    # 옷 종류 모델 로드
    saved_model = tf.keras.models.load_model("./clothes_type_model_#7.h5")

    # 새로운 이미지 전처리 및 예측
    preprocessed_image = preprocess_image(image)
    predictions = saved_model.predict(preprocessed_image)

    # 예측 결과 확인
    predicted_class = np.argmax(predictions)  # 가장 높은 확률을 가진 클래스 인덱스

    return predicted_class

def getClothesColor(image):

    # 이미지 모드가 RGBA인 경우 RGB로 변환
    if image.mode == 'RGBA':
        image = image.convert('RGB')


    # 처리된 이미지를 저장할 임시 파일 생성
    with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as temp_image:
        temp_image_path = temp_image.name
        image.save(temp_image_path)

    # 옷 주요 색상 추출
    thief = ColorThief(temp_image_path)
    image_color = thief.get_color(quality=1)

    clothes_color = color.extract_color(image_color)

    # 이미지 파일을 삭제합니다.
    os.remove(temp_image_path)

    return clothes_color

def getClothesPattern(image):

    # 옷 패턴 모델 로드
    saved_model = tf.keras.models.load_model("./pattern_model.h5")

    # 새로운 이미지 전처리 및 예측
    preprocessed_image = preprocess_image(image)
    predictions = saved_model.predict(preprocessed_image)

    # 예측 결과 확인
    predicted_class = np.argmax(predictions)  # 가장 높은 확률을 가진 클래스 인덱스

    return predicted_class