import tensorflow as tf
import cv2
import numpy as np

# 이미지 전처리 함수
def preprocess_image(image):
    image = np.array(image)  # 이미지 객체를 NumPy 배열로 변환
    image = cv2.resize(image, (224, 224))  # 모델이 기대하는 이미지 크기로 조정
    image = np.expand_dims(image, axis=0)  # 배치 차원 추가
    return image

def getClothesType(image):
    # 옷 종류 모델 로드
    saved_model = tf.keras.models.load_model("./clothes_type_model_#7.h5")

    # 새로운 이미지 전처리 및 예측
    preprocessed_image = preprocess_image(image)
    predictions = saved_model.predict(preprocessed_image)

    # 예측 결과 확인
    predicted_class = np.argmax(predictions)  # 가장 높은 확률을 가진 클래스 인덱스

    return predicted_class