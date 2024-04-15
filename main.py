import cv2
import socks
from fastapi import FastAPI
from fastapi import File, UploadFile

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
    # filename = f"{str(uuid.uuid4())}.jpg"  # uuid로 유니크한 파일명으로 변경
    # with open(os.path.join(UPLOAD_DIR, filename), "wb") as fp:
    #     fp.write(content)  # 서버 로컬 스토리지에 이미지 저장 (쓰기)

    return {"isSuccess": True,
            "code": "2000",
            "message": "Ok",
            "result": color + "의 " + pattern + "패턴의 " + clothes_type + " 입니다."
    }