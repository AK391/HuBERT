import gradio as gr



description = "demo for HuBERT. To use it, simply add your audio or click one of the examples to load them. Read more at the links below."
article = "<p style='text-align: center'><a href='https://arxiv.org/abs/2106.07447'>HuBERT: Self-Supervised Speech Representation Learning by Masked Prediction of Hidden Units</a> | <a href='https://github.com/pytorch/fairseq/tree/master/examples/hubert'>Github Repo</a></p>"

gr.Interface.load("huggingface/facebook/hubert-large-ls960-ft", 
    description=description,
    article=article,
    examples=[
  ["./audio1.mp3"],
  ["./audio2.mp3"]
]).launch()
