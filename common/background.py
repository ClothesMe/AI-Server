from rembg import remove
import numpy as np
from PIL import Image

async def remove_background(clothes_image):
    """
    배경 제거
    :param cloth_image: 배경 제거할 이미지
    :return: 배경이 제거된 이미지
    """   
    removed_background = remove(clothes_image)
        
    # numpy 배열로 변환
    removed_background_np = np.array(removed_background)

    return removed_background_np
