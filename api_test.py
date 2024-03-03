# -*- coding: UTF-8 -*-
import requests
import json
"""
文件用于测试 模型api的通讯
后续可能会有用？
"""
def chat(prompt,history):
    headers = {'Content-Type': 'application/json'}
    data = {"prompt": prompt, "history": history}
    response = requests.post(url='http://127.0.0.1:6006', headers=headers, data=json.dumps(data))
    # print(response)
    return response.json()['response']
history=[]
while True:
    response = chat(input("Enter your Question: "),history)
    print(response)