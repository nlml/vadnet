import numpy as np
import requests
from vadnet.utils import audio_from_file
import pickle


audio = audio_from_file("test_audio.wav")

r = requests.post(
    url='http://localhost:5001/predict',
    data=pickle.dumps(audio),
    headers={'Content-Type': 'application/octet-stream'}
)
print(r.json())
