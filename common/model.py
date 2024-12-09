import tensorflow as tf
# import keras
# from keras.models import load_model

# 옷 종류 모델 로드
saved_model_type = tf.keras.models.load_model("ai_models/mobilenetv3_1.keras", compile=False)
# 옷 패턴 모델 로드
saved_model_pattern = tf.keras.models.load_model("ai_models/pattern_model.h5")

def getPatternModel():
    return saved_model_pattern

def getTypeModel():
    return saved_model_type