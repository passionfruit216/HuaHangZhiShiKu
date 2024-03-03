# -*- coding: UTF-8 -*-
import gradio as gr
def gradio_test(input):
    return "Hello World!"+ input+" ! "

demo = gr.Interface(fn=gradio_test,inputs='text',outputs='text')

demo.launch()