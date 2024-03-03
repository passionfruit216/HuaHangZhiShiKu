# -*- coding: UTF-8 -*-
"""
此文件用于方便检测环境是否符合要求
"""
import nltk
nltk.download('punkt')
import torch
print(torch.__version__)
print(torch.cuda.is_available())
import langchain
print(langchain.__version__)
import gradio as gr
print(gr.__version__)