import cv2
import numpy as np

def white_balance(img):
    # LAB 색 공간으로 이미지 변환
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

    # 'a' 채널의 평균값 계산
    a_mean = np.mean(lab[:,:,1])

    # 'a' 채널을 조정하여 초록-마젠타 색상을 제거
    lab[:,:,1] = lab[:,:,1] - (128 - a_mean)

    # 조정된 'l'과 'a' 채널을 병합
    img_white_balanced = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

    return img_white_balanced