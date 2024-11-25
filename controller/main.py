import cv2
from service import socks as socks
from fastapi import FastAPI, Depends
from fastapi import File, UploadFile
import numpy as np
from service import clothes as ct
from common import label as label
import matplotlib.pyplot as plt
from PIL import Image
import io
from common import background as bg
from sqlalchemy.orm import Session
from db.database import Base, engine, SessionLocal
import db.database as database
import uuid

# 데이터베이스 초기화
database.Base.metadata.create_all(bind=engine)

app = FastAPI()

# 의존성 주입: DB 세션 생성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/socks")
async def socks_color(file: UploadFile):
    """
    메인 함수: 양말 이미지와 배경 이미지를 입력받아 양말의 색상을 판별하고 짝이 맞는지 확인
    """

    # 이미지 로드
    image_bytes = await file.read()
    np_img = np.frombuffer(image_bytes, np.uint8)
    socks_image = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    removedSocksImage = bg.remove_background(socks_image)
    left_socks, right_socks = socks.getSocksImage(removedSocksImage)

    # 양말의 색상 판별
    left_color, right_color = socks.find_color_name(left_socks, right_socks)

    # 양말의 패턴 판별
    left_pattern, right_pattern = socks.find_pattern(left_socks, right_socks)

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
                + "왼쪽 양말의 패턴은 " + label.clothes_pattern[left_pattern] + ", 오늘쪽 양말의 패턴은 " + label.clothes_pattern[right_pattern] + "입니다. " 
                + "양말의 짝이 " + pairing_result
    }

@app.post("/clothes")
async def read_clothes(file: UploadFile):

    image = await file.read() # 이미지 파일 받아오는 부분
    image = Image.open(io.BytesIO(image))

    # 옷 배경 제거한 후 이미지 파일 넘겨주기
    removed_image = bg.remove_background(image) # 배경 제거
    pil_image = Image.fromarray(removed_image) # 이미지를 PIL 이미지로 변환

    # 옷 정보 받아오기
    color = ct.getClothesColor(pil_image)
    pattern = label.clothes_pattern[ct.getClothesPattern(pil_image)]
    clothes_type = label.clothes_categories[ct.getClothesType(pil_image)]

    return {
        "status": "success",
        "code": "2000",
        "message": "Ok",
        "result": color + " 의 " + pattern + " 패턴의 " + clothes_type + " 입니다."
    }

# 회원가입
@app.post("/members")
def create_user(db: Session = Depends(get_db)):
    member_uuid = uuid.uuid4()
    database.create_member(db=db, uuid=member_uuid)
    return {
        "status": "success",
        "code": "2000",
        "message": "Ok",
        "result": member_uuid
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)