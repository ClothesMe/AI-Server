from rembg import remove
import numpy as np

def remove_background(image):
    """
    배경 제거
    :param cloth_image: 배경 제거할 이미지
    :return: 배경이 제거된 이미지
    """   
    removed_background = remove(image)
        
    # numpy 배열로 변환
    removed_background_np = np.array(removed_background)

    return removed_background_np

# def remove_background(socks_image):
#     """
#     배경 제거
#     :param cloth_image: 배경 제거할 이미지
#     :return: 배경이 제거된 이미지
#     """   
#     removed_background = remove(socks_image)
    
#     cv2.imwrite('./removed_background.jpg', removed_background)
#     return removed_background
