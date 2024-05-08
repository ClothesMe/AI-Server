import cv2
import socks
from fastapi import FastAPI
from fastapi import File, UploadFile
import numpy as np
import clothes_type as ct
import matplotlib.pyplot as plt
from PIL import Image
import io
# import tensorflow
# from tensorflow.keras.models import load_model

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
    

@app.post("/clothes")
async def read_clothes(file: UploadFile):
    UPLOAD_DIR = "./photo"  # 이미지를 저장할 서버 경로

    image = await file.read() # 이미지 파일 받아오는 부분
    image = Image.open(io.BytesIO(image))

    clothes_categories = ['Not sure', 'T-Shirt', 'Shoes', 'Shorts', 'Shirt', 'Pants', 'Skirt', 'Other', 'Top', 'Outwear', 'Dress', 'Body', 'Longsleeve', 'Undershirt', 'Hat', 'Polo', 'Blouse', 'Hoodie', 'Skip', 'Blazer']

    color = ct.getClothesColor(image)
    pattern = "muji"
    clothes_type = clothes_categories[ct.getClothesType(image)]

    return {
        "isSuccess": True,
        "code": "2000",
        "message": "Ok",
        "result": color + " 의 " + pattern + " 패턴의 " + clothes_type + " 입니다."
    }