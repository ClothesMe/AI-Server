# ClothesMe AI-Server

시각장애인을 위한 AI 기반 패션 도우미 서비스 **클로즈미(ClothesMe)**의 AI 서버입니다.

## 기획 의도

시각장애인이 옷을 고를 때 쓸 수 있는 방법은 제한적입니다.

1. **점자 의류**: 2022년 한국장애인고용공단 장애인 고용패널 조사 결과, 시각장애인 중 63.6%가 점자를 해독하지 못합니다.
2. **RFID 태그 의류**: 위치와 의류 종류에 대해서만 제한적으로 정보를 제공합니다.

## 주요 기능

| 기능 | 분석 항목 |
| :--- | :--- |
| 의류 분석 | 종류 · 패턴 · 색상 |
| 양말 짝 판별 | 패턴 · 색상 |
| 날씨에 맞는 옷 추천 | 종류 · 색상 · 추천 |

## 시스템 환경

- **Server**: AWS EC2 위에서 Python · FastAPI 서버와 TensorFlow 모델 실행, Nginx 리버스 프록시
- **Storage**: Amazon S3, AWS RDS
- **Client**: Android 앱, OpenCV
- **음성 안내**: Google Cloud Text-to-Speech AI

## 서비스 과정

```
사용자: 의류 촬영
  → Android: 의류 분석 요청
  → AI-Server: 의류 종류 분류 모델 (양말 짝 판별 시 생략)
             → 의류 패턴 분류 모델
             → 색상 판별 알고리즘
             → 분석 결과 전달
  → 사용자: 분석 결과 음성 안내
```

## 모델 소개

### 1. 의류 종류 분류 모델 (정확도 약 85%)

| 구분 | 분류 |
| :--- | :--- |
| 상의 | 반팔, 긴팔, 셔츠, 외투, 폴로, 언더셔츠, 재킷, 후드, 탑 |
| 하의 | 바지, 반바지, 치마 |
| 그 외 | 신발, 드레스, 모자, 바디 |

### 2. 의류 패턴 분류 모델 (정확도 약 70%)

argyle, camouflage, checked, dot, floral, geometric, gradient, graphic, houndstooth, leopard, lettering, muji, paisley, snake skin, snow flake, stripe, tropical, zebra, zigzag

## 기대 효과

- 시각장애인의 의류 선택 과정의 어려움 해소
- 시각장애인의 적극적인 의류 문화 향유 유도
- 제한된 앱과 점자 오류로 인한 의류 선택의 어려움 해소
