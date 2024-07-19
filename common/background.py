from rembg import remove
import numpy as np
from PIL import Image

# def remove_background(image):
#     """
#     배경 제거
#     :param cloth_image: 배경 제거할 이미지
#     :return: 배경이 제거된 이미지
#     """   
#     removed_background = remove(image)
        
#     # numpy 배열로 변환
#     removed_background_np = np.array(removed_background)

#     return removed_background_np

def remove_background(image: np.ndarray) -> np.ndarray:
    """
    배경 제거
    :param image: 배경 제거할 이미지 (numpy 배열)
    :return: 배경이 제거된 이미지 (numpy 배열, 투명 배경)
    """
    # numpy 배열을 PIL 이미지로 변환
    image_pil = Image.fromarray(image)

    # 배경 제거
    removed_background_pil = remove(image_pil)

    # PIL 이미지를 numpy 배열로 변환
    removed_background_np = np.array(removed_background_pil)

    return removed_background_np


# def remove_background(socks_image):
#     """
#     배경 제거
#     :param cloth_image: 배경 제거할 이미지
#     :return: 배경이 제거된 이미지
#     """   
#     removed_background = remove(socks_image)
    
#     # cv2.imwrite('./removed_background.jpg', removed_background)
#     return removed_background
