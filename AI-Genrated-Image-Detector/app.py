import gradio as gr
import numpy as np
from tensorflow.keras.models import load_model


model = load_model("large_model_3lakh_v1.h5")

title = "🧠 AI IMAGE DETECTOR BY ELITEX"

description = "THROUGH THIS APPLICATION YOU CAN INPUT AN IMAGE AND THE WEBSITE WILL TELL WHETHER THE IMAGE IS AI GENERATED OR NOT."
list_num = [0, 1]
# 0 is fake 1 is true


def closest(lst, K):
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i] - K))]


def hell(image):
    pred = model.predict(np.expand_dims(image / 255, 0))
    result = closest(list_num, pred[0])
    if result == 0:
        return "The image is generated by AI"
    if result == 1:
        return "The Image is not generated by AI"


demo = gr.Interface(
    fn=hell,
    inputs=[gr.Image(shape=(256, 256))],
    outputs=["text"],
    # Pass through title and description
    title=title,
    description=description,
    # Set theme and launch parameters
    theme="finlaymacklon/boxy_violet",
)

demo.launch()
