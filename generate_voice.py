import os
from TTS.api import TTS

# 初始化語音模型（使用多語言多說話人模型）
tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=True, gpu=False)

# 要合成的文字
text = "你好，我是 E.M.T，很高興為你服務喔～"

# 輸出路徑
output_path = "output.wav"

# 執行語音合成
tts.tts_to_file(text=text, file_path=output_path)

print("✅ 已成功生成語音：" + output_path)
