import cv2
from common import color as color
from common import white_balance as white_balance
from rembg import remove
from PIL import Image
import numpy as np
from colorthief import ColorThief
from common import model as model

def find_color_name(left_socks, right_socks):
    """
    양말 색상 판별
    :param socks_image: 양말 이미지
    :return: 양말의 왼쪽과 오른쪽 색상
    """

    color_name_left, color_name_right = color.getSocksMainColor(left_socks, right_socks)

    return color_name_left, color_name_right

def find_pattern(left_socks, right_socks):

    left_preprocessed_image = preprocess_image(left_socks)
    right_preprocessed_image = preprocess_image(right_socks)

    left_predictions = model.getPatternModel().predict(left_preprocessed_image)
    right_predictions = model.getPatternModel().predict(right_preprocessed_image)

    # 예측 결과 확인
    left_predicted_class = np.argmax(left_predictions)  # 가장 높은 확률을 가진 클래스 인덱스
    right_predicted_class = np.argmax(right_predictions)  # 가장 높은 확률을 가진 클래스 인덱스

    return left_predicted_class, right_predicted_class



# 공동 로직
def getSocksImage(removedSocksImage):

    # 화이트 밸런싱 적용
    white_balanced_image = white_balance.white_balance(removedSocksImage)

    # 배경과 양말 객체 분리
    socks_mask = cv2.cvtColor(removedSocksImage, cv2.COLOR_BGR2GRAY)
    _, socks_mask = cv2.threshold(socks_mask, 1, 255, cv2.THRESH_BINARY)
    socks_objects = cv2.bitwise_and(white_balanced_image, white_balanced_image, mask=socks_mask)

    # 좌우 양말로 나누기
    height, width, _ = socks_objects.shape
    cropped_left_image = socks_objects[0:height, 0:width // 2]
    cropped_right_image = socks_objects[0:height, width // 2:width]

    # cropped_left_image_path = './socks_left3.jpg'
    # cropped_right_image_path = './socks_right3.jpg'
    # cv2.imwrite(cropped_left_image_path, cropped_left_image)
    # cv2.imwrite(cropped_right_image_path, cropped_right_image)

    return cropped_left_image, cropped_right_image

def preprocess_image(image: np.ndarray) -> np.ndarray:
    # numpy.ndarray 객체를 PIL.Image 객체로 변환
    pil_image = Image.fromarray(image)
    # RGB로 변환
    rgb_image = pil_image.convert("RGB")
    # PIL.Image 객체를 다시 numpy.ndarray로 변환
    np_image = np.array(rgb_image)
    # 이미지 크기 조정 (모델 입력 크기에 맞게 조정, 예: 224x224)
    resized_image = cv2.resize(np_image, (224, 224))
    # 이미지 스케일링 (0-1 범위로)
    normalized_image = resized_image / 255.0
    # 배치 차원 추가
    batch_image = np.expand_dims(normalized_image, axis=0)
    return batch_image

