import gradio as gr
import torch

# Audio
torch.hub.download_url_to_file('https://github.com/ultralytics/yolov5/raw/master/data/images/zidane.jpg', 'zidane.jpg')
torch.hub.download_url_to_file('https://github.com/ultralytics/yolov5/raw/master/data/images/bus.jpg', 'bus.jpg')


description = "demo for HuBERT. To use it, simply add your audio or click one of the examples to load them. Read more at the links below."
article = "<p style='text-align: center'><a href='https://arxiv.org/abs/2004.05150'>HuBERT: Self-Supervised Speech Representation Learning by Masked Prediction of Hidden Units</a> | <a href='https://github.com/pytorch/fairseq/tree/master/examples/hubert'>Github Repo</a></p>"

gr.Interface.load("huggingface/facebook/hubert-large-ls960-ft", 
    description=description,
    article=article,
    examples=[
  ["./audio1.mp3"],
  ["./audio2.mp3"]
]).launch()
