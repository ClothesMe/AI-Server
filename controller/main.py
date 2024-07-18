import cv2
import socks
from fastapi import FastAPI
from fastapi import File, UploadFile
import numpy as np
import clothes_info as ct
import matplotlib.pyplot as plt
from PIL import Image
import io
# import tensorflow
# from tensorflow.keras.models import load_model

app = FastAPI()

@app.post("/socks")
async def socks_color(file: UploadFile):
    """
    메인 함수: 양말 이미지와 배경 이미지를 입력받아 양말의 색상을 판별하고 짝이 맞는지 확인
    :param socks_image_path: 양말 이미지 경로
    :return: None
    """

    clothes_pattern = ['argyle', 'camouflage', 'checked', 'dot', 'floral', 'geometric', 'gradient','graphic', 'houndstooth', 'leopard', 'lettering', 'muji', 'paisley', 'snake_skin','snow_flake', 'stripe', 'tropical', 'zebra', 'zigzag']


    # 이미지 로드
    image_bytes = await file.read()
    np_img = np.frombuffer(image_bytes, np.uint8)
    socks_image = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    # 양말의 색상 판별
    left_color, right_color = socks.find_color_name(socks_image)

    # 양말의 패턴 판별
    left_pattern, right_pattern = socks.find_pattern(socks_image)

    # 양말의 짝 판별
    if left_color == right_color and left_pattern == right_pattern: 
        pairing_result = "맞습니다."
    else:
        pairing_result = "맞지 않습니다."

    # 결과 출력
    return {
        "status": "success",
        "code": "2000",
        "message": "Ok",
        "result": "왼쪽 양말의 색상은 " + left_color + ", " + "오른쪽 양말의 색상은 " + right_color + "이며, " 
                + "왼쪽 양말의 패턴은 " + clothes_pattern[left_pattern] + ", 오늘쪽 양말의 패턴은 " + clothes_pattern[right_pattern] + "입니다. " 
                + "양말의 짝이 " + pairing_result
    }

@app.post("/clothes")
async def read_clothes(file: UploadFile):
    UPLOAD_DIR = "./photo"  # 이미지를 저장할 서버 경로

    image = await file.read() # 이미지 파일 받아오는 부분
    image = Image.open(io.BytesIO(image))

    clothes_categories = ['Not sure', 'T-Shirt', 'Shoes', 'Shorts', 'Shirt', 'Pants', 'Skirt', 'Other', 'Top', 'Outwear', 'Dress', 'Body', 'Longsleeve', 'Undershirt', 'Hat', 'Polo', 'Blouse', 'Hoodie', 'Skip', 'Blazer']
    clothes_pattern = ['argyle', 'camouflage', 'checked', 'dot', 'floral', 'geometric', 'gradient','graphic', 'houndstooth', 'leopard', 'lettering', 'muji', 'paisley', 'snake_skin','snow_flake', 'stripe', 'tropical', 'zebra', 'zigzag']

    # 옷 배경 제거한 후 이미지 파일 넘겨주기
    removed_image = ct.remove_background(image) # 배경 제거
    pil_image = Image.fromarray(removed_image) # 이미지를 PIL 이미지로 변환

    # 옷 정보 받아오기
    color = ct.getClothesColor(pil_image)
    pattern = clothes_pattern[ct.getClothesPattern(pil_image)]
    clothes_type = clothes_categories[ct.getClothesType(pil_image)]

    return {
        "status": "success",
        "code": "2000",
        "message": "Ok",
        "result": color + " 의 " + pattern + " 패턴의 " + clothes_type + " 입니다."
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)