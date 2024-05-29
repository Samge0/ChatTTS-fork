import os
import time
import wave

import numpy as np
import scipy
import ChatTTS


start_time = time.time()

chat = ChatTTS.Chat()
chat.load_models()
print(f"load ChatTTS model time: {time.time() - start_time}s")

start_time = time.time()
inputs_cn = """
chat T T S 真是是一款强大的对话式文本转语音模型啊！它有中英混读和多说话人的能力，听起来非常自然。
chat T T S 不仅能够生成自然流畅的语音，还能控制[laugh]笑声啊[laugh]，
停顿啊[uv_break]语气词啊等副语言现象[uv_break]。这个韵律超越了许多开源模型[uv_break]。
请注意，chat T T S 的使用应遵守法律和伦理准则，避免滥用的哦~ [uv_break]'
""".replace('\n', '')

params_refine_text = {
  'prompt': '[oral_2][laugh_0][break_4]'
} 
audio_array_cn = chat.infer(inputs_cn, params_refine_text=params_refine_text)

# 保存 WAV 文件
cache_dir = '.cache'
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)
output_path = f'{cache_dir}/result.wav'
scipy.io.wavfile.write(filename = output_path, rate = 24_000, data = audio_array_cn[0].T)

print(f"Audio file saved as {output_path}")
print(f"ChatTTS infer time: {time.time() - start_time}s")