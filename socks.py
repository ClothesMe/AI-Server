import cv2
import color
import white_balance
from rembg import remove
from colorthief import ColorThief


def remove_background(socks_image):
    """
    배경 제거
    :param cloth_image: 배경 제거할 이미지
    :return: 배경이 제거된 이미지
    """   
    removed_background = remove(socks_image)
    
    cv2.imwrite('E:/clothesme/image_data/removed_background.jpg', removed_background)
    return removed_background

def find_color_name(socks_image):
    """
    양말 색상 판별
    :param socks_image: 양말 이미지
    :return: 양말의 왼쪽과 오른쪽 색상
    """

    # 배경 제거
    processed_image = remove_background(socks_image)

    # 화이트 밸런싱 적용
    white_balanced_image = white_balance.white_balance(processed_image)

    # 배경과 양말 객체 분리
    socks_mask = cv2.cvtColor(processed_image, cv2.COLOR_BGR2GRAY)
    _, socks_mask = cv2.threshold(socks_mask, 1, 255, cv2.THRESH_BINARY)
    socks_objects = cv2.bitwise_and(white_balanced_image, white_balanced_image, mask=socks_mask)

    # 좌우 양말로 나누기
    height, width, _ = socks_objects.shape
    cropped_left_image = socks_objects[0:height, 0:width // 2]
    cropped_right_image = socks_objects[0:height, width // 2:width]

    cropped_left_image_path = 'E:/clothesme/image_data/socks_left.jpg'
    cropped_right_image_path = 'E:/clothesme/image_data/socks_right.jpg'
    cv2.imwrite(cropped_left_image_path, cropped_left_image)
    cv2.imwrite(cropped_right_image_path, cropped_right_image)

    # 좌우 양말 주요 색상 추출
    dominant_color_left =  ColorThief(cropped_left_image_path).get_color(quality=1)
    dominant_color_right = ColorThief(cropped_right_image_path).get_color(quality=1)

    color_name_left = color.extract_color(dominant_color_left)
    color_name_right = color.extract_color(dominant_color_right)

    return color_name_left, color_name_right