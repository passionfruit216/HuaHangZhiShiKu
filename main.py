# -*- coding: UTF-8 -*-
from transformers import AutoTokenizer, AutoModel
# 加载 tokener
tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm3-6b", trust_remote_code=True)
# 加载模型 4 bit 量化
model = AutoModel.from_pretrained("THUDM/chatglm3-6b", trust_remote_code=True).quantize(4).cuda()
model = model.eval()
# history 是一个list 里面放元组  ('user的对话','chatglm的对话') 可以用于角色扮演功能
response, history = model.chat(tokenizer, "你好", history=[])
print(response)
