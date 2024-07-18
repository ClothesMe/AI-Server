import cv2
import numpy as np

# 색상을 나타내는 HSV 값과 색상 이름을 딕셔너리로 정의
HSV = {
    (4 / 2, 65*(255/100), 73*(255/100)): '빨간색',
    (3 / 2, 68*(255/100), 75*(255/100)): '선명한 빨강색',
    (4 / 2, 65*(255/100), 86*(255/100)): '밝은 빨강색',
    (359 / 2, 60*(255/100), 60*(255/100)): '진한 빨강색',
    (358 / 2, 42*(255/100), 69*(255/100)): '흐린 빨강색',
    (5 / 2, 56*(255/100), 57*(255/100)): '탁한 빨강색',
    (358 / 2, 34*(255/100), 39*(255/100)): '어두운 빨강색',
    (4 / 2, 16*(255/100), 57*(255/100)): '회적색',
    (4 / 2, 41*(255/100), 41*(255/100)): '어두운 회적색',
    (4 / 2, 20*(255/100), 33*(255/100)): '검정빛 빨강색',
    (11 / 2, 73*(255/100), 95*(255/100)): '주황색',
    (10 / 2, 73*(255/100), 95*(255/100)): '선명한 주황색',
    (15 / 2, 67*(255/100), 100*(255/100)): '밝은 주황색',
    (20 / 2, 80*(255/100), 85*(255/100)): '진한 주황색',
    (16 / 2, 69*(255/100), 88*(255/100)): '흐린 주황색',
    (20 / 2, 46*(255/100), 79*(255/100)): '탁한 주황색',
    (9 / 2, 75*(255/100), 85*(255/100)): '빨간 주황색',
    (9 / 2, 80*(255/100), 88*(255/100)): '선명한 빨간 주황색',
    (11 / 2, 74*(255/100), 88*(255/100)): '밝은 빨간 주황색',
    (9 / 2, 56*(255/100), 70*(255/100)): '탁한 빨간 주황색',
    (42 / 2, 92*(255/100), 100*(255/100)): '노란색',
    (39 / 2, 92*(255/100), 100*(255/100)): '진한 노란색',
    (44 / 2, 40*(255/100), 98*(255/100)): '연한 노란색',
    (39 / 2, 46*(255/100), 89*(255/100)): '흐린 노란색',
    (54 / 2, 16*(255/100), 95*(255/100)): '흰 노란색',
    (29 / 2, 21*(255/100), 86*(255/100)): '회황색',
    (33 / 2, 18*(255/100), 89*(255/100)): '밝은 회황색',
    (93 / 2, 67*(255/100), 76*(255/100)): '연두색',
    (98 / 2, 68*(255/100), 68*(255/100)): '선명한 연두색',
    (96 / 2, 42*(255/100), 83*(255/100)): '밝은 연두색',
    (93 / 2, 61*(255/100), 55*(255/100)): '진한 연두색',
    (96 / 2, 34*(255/100), 83*(255/100)): '연한 연두색',
    (97 / 2, 27*(255/100), 73*(255/100)): '흐린 연두색',
    (94 / 2, 39*(255/100), 64*(255/100)): '탁한 연두색',
    (67 / 2, 59*(255/100), 85*(255/100)): '노란 연두색',
    (68 / 2, 86*(255/100), 88*(255/100)): '선명한 노란 연두색',
    (69 / 2, 60*(255/100), 93*(255/100)): '밝은 노란 연두색',
    (55 / 2, 64*(255/100), 77*(255/100)): '진한 노란 연두색',
    (70 / 2, 48*(255/100), 88*(255/100)): '연한 노란 연두색',
    (62 / 2, 35*(255/100), 89*(255/100)): '겨자색',
    (53 / 2, 38*(255/100), 83*(255/100)): '탁한 노란 연두색',
    (100 / 2, 45*(255/100), 78*(255/100)): '녹연두색',
    (105 / 2, 53*(255/100), 76*(255/100)): '선명한 녹연두색',
    (99 / 2, 44*(255/100), 76*(255/100)): '밝은 녹연두색',
    (104 / 2, 26*(255/100), 86*(255/100)): '연한 녹연두색',
    (103 / 2, 23*(255/100), 74*(255/100)): '흐린 녹연두색',
    (102 / 2, 31*(255/100), 66*(255/100)): '탁한 녹연두색',
    (79 / 2, 14*(255/100), 91*(255/100)): '흰 연두색',
    (123 / 2, 13*(255/100), 63*(255/100)): '회연두색',
    (121 / 2, 15*(255/100), 82*(255/100)): '밝은 회연두색',
    (157 / 2, 69*(255/100), 49*(255/100)): '초록색',
    (142 / 2, 78*(255/100), 40*(255/100)): '선명한 초록색',
    (146 / 2, 60*(255/100), 58*(255/100)): '밝은 초록색',
    (146 / 2, 37*(255/100), 38*(255/100)): '진한 초록색',
    (144 / 2, 39*(255/100), 85*(255/100)): '연한 초록색',
    (147 / 2, 38*(255/100), 67*(255/100)): '흐린 초록색',
    (149 / 2, 39*(255/100), 47*(255/100)): '탁한 초록색',
    (157 / 2, 29*(255/100), 31*(255/100)): '어두운 초록색',
    (144 / 2, 18*(255/100), 93*(255/100)): '흰 초록색',
    (152 / 2, 16*(255/100), 49*(255/100)): '회녹색',
    (120 / 2, 15*(255/100), 80*(255/100)): '밝은 회녹색',
    (150 / 2, 6*(255/100), 30*(255/100)): '검정빛 초록색',
    (176 / 2, 100*(255/100), 44*(255/100)): '청록색',
    (178 / 2, 100*(255/100), 61*(255/100)): '밝은 청록색',
    (179 / 2, 66*(255/100), 35*(255/100)): '진한 청록색',
    (177 / 2, 42*(255/100), 77*(255/100)): '연한 청록색',
    (178 / 2, 36*(255/100), 67*(255/100)): '흐린 청록색',
    (180 / 2, 31*(255/100), 47*(255/100)): '탁한 청록색',
    (179 / 2, 19*(255/100), 31*(255/100)): '어두운 청록색',
    (180 / 2, 20*(255/100), 93*(255/100)): '흰 청록색',
    (163 / 2, 37*(255/100), 55*(255/100)): '밝은 청록색',
    (161 / 2, 22*(255/100), 30*(255/100)): '어두운 청록색',
    (209 / 2, 75*(255/100), 44*(255/100)): '청색',
    (206 / 2, 100*(255/100), 65*(255/100)): '선명한 청색',
    (207 / 2, 61*(255/100), 73*(255/100)): '밝은 청색',
    (206 / 2, 68*(255/100), 49*(255/100)): '진한 청색',
    (197 / 2, 52*(255/100), 91*(255/100)): '연한 청색',
    (204 / 2, 29*(255/100), 73*(255/100)): '흐린 청색',
    (204 / 2, 36*(255/100), 53*(255/100)): '탁한 청색',
    (204 / 2, 28*(255/100), 41*(255/100)): '어두운 청색',
    (205 / 2, 22*(255/100), 92*(255/100)): '흰 청색',
    (189 / 2, 24*(255/100), 87*(255/100)): '연청색',
    (191 / 2, 38*(255/100), 80*(255/100)): '선명한 연청색',
    (193 / 2, 39*(255/100), 87*(255/100)): '밝은 연청색',
    (190 / 2, 43*(255/100), 57*(255/100)): '진한 연청색',
    (191 / 2, 27*(255/100), 76*(255/100)): '흐린 연청색',
    (191 / 2, 23*(255/100), 60*(255/100)): '탁한 연청색',
    (194 / 2, 14*(255/100), 41*(255/100)): '어두운 연청색',
    (192 / 2, 23*(255/100), 59*(255/100)): '회청색',
    (194 / 2, 22*(255/100), 79*(255/100)): '밝은 회청색',
    (194 / 2, 18*(255/100), 45*(255/100)): '어두운 회청색',
    (273 / 2, 25*(255/100), 69*(255/100)): '보라색',
    (270 / 2, 38*(255/100), 65*(255/100)): '선명한 보라색',
    (276 / 2, 24*(255/100), 76*(255/100)): '밝은 보라색',
    (291 / 2, 40*(255/100), 47*(255/100)): '진한 보라색',
    (274 / 2, 16*(255/100), 83*(255/100)): '연한 보라색',
    (272 / 2, 21*(255/100), 81*(255/100)): '흐린 보라색',
    (277 / 2, 30*(255/100), 55*(255/100)): '탁한 보라색',
    (280 / 2, 30*(255/100), 39*(255/100)): '어두운 보라색',
    (275 / 2, 10*(255/100), 89*(255/100)): '흰 보라색',
    (289 / 2, 17*(255/100), 67*(255/100)): '회보라색',
    (290 / 2, 15*(255/100), 81*(255/100)): '밝은 회보라색',
    (288 / 2, 15*(255/100), 51*(255/100)): '어두운 회보라색',
    (343 / 2, 75*(255/100), 90*(255/100)): '분홍색',
    (342 / 2, 80*(255/100), 89*(255/100)): '선명한 분홍색',
    (342 / 2, 81*(255/100), 95*(255/100)): '밝은 분홍색',
    (339 / 2, 67*(255/100), 47*(255/100)): '진한 분홍색',
    (318 / 2, 34*(255/100), 95*(255/100)): '연한 분홍색',
    (326 / 2, 36*(255/100), 82*(255/100)): '흐린 분홍색',
    (335 / 2, 47*(255/100), 65*(255/100)): '탁한 분홍색',
    (329 / 2, 49*(255/100), 46*(255/100)): '어두운 분홍색',
    (315 / 2, 17*(255/100), 69*(255/100)): '회분홍색',
    (312 / 2, 18*(255/100), 81*(255/100)): '밝은 회분홍색',
    (320 / 2, 20*(255/100), 51*(255/100)): '어두운 회분홍색',
    (0, 0, 53*(255/100)): '회색',
    (0, 0, 75*(255/100)): '밝은 회색',
    (0, 0, 40*(255/100)): '진회색',
    (0, 0, 27*(255/100)): '어두운 회색',
    (0, 0, 13*(255/100)): '검정빛 회색',
    (0, 0, 0): '검정색',
    (0, 0, 100*(255/100)): '흰색'
}

hsv = list(HSV.keys())
hsv_len = len(hsv)

def extract_color(rgb):
    rgb = np.uint8([[rgb]])
    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)[0][0]

    minimum = float('inf')
    closest_color = None

    for hsv_value, color_name in HSV.items():
        chai = sum(abs(hsv[i] - hsv_value[i]) * (3 - i) for i in range(3))
        if chai == 0:
            chai += abs(hsv[2] - hsv_value[2])
        if chai < minimum:
            minimum = chai
            closest_color = color_name
    
    return closest_color