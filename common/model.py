import tensorflow as tf

# 옷 종류 모델 로드
saved_model_type = tf.keras.models.load_model("models/clothes_type_model_#7.h5")
# 옷 패턴 모델 로드
saved_model_pattern = tf.keras.models.load_model("models/pattern_model.h5")

def getPatternModel():
    return saved_model_pattern

def getTypeModel():
    return saved_model_type