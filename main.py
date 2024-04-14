import cv2
import socks
from fastapi import FastAPI

app = FastAPI()

@app.get("/socks")
def socks_color(socks_image_path):
    """
    메인 함수: 양말 이미지와 배경 이미지를 입력받아 양말의 색상을 판별하고 짝이 맞는지 확인
    :param socks_image_path: 양말 이미지 경로
    :return: None
    """

    # 이미지 로드
    socks_image = cv2.imread(socks_image_path)

    # 양말의 색상 판별
    left_color, right_color = socks.find_color_name(socks_image)

   
    # 결과 출력
    if left_color == right_color: 
         return {"왼쪽 양말의 색상은 ": left_color, "오른쪽 양말의 색상은 ": right_color, "양말의 짝이 ": "맞습니다."}
    else:
        return {"왼쪽 양말의 색상은 ": left_color, "오른쪽 양말의 색상은 ": right_color, "양말의 짝이 ": "맞지 않습니다."}