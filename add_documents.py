# -*- coding: UTF-8 -*-
import os
from tqdm import tqdm
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.document_loaders import UnstructuredFileLoader
from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain.document_loaders import UnstructuredHTMLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import gradio as gr


def add_documents(files_path):
    docs = []
    # 暂时将file_path 转化为 list (后续优化项)
    files_path = [files_path]
    # print(files_path)
    # print(type(files_path))
    # 加载文件 从列表里面
    for file in tqdm(files_path):
        if file.endswith('.pdf'):
            loader = UnstructuredPDFLoader(file)
        elif file.endswith('.txt'):
            loader = UnstructuredFileLoader(file)
        elif file.endswith('.md'):
            loader = UnstructuredMarkdownLoader(file)
        elif file.endswith('.html'):
            loader = UnstructuredHTMLLoader(file)
        else:
            continue
        docs.extend(loader.load())

    # 对文本进行分块
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=150)
    split_docs = text_splitter.split_documents(docs)
    print(type(split_docs))
    print(split_docs)
    # 加载开源词向量模型
    model_name = "BAAI/bge-large-zh-v1.5"
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    # 加载数据库 (可以换上自己的路径)
    # 构建向量数据库
    persist_directory = 'database/vector_db'
    db = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
    texts = [doc.page_content for doc in split_docs]
    db.add_texts(texts)
    db.persist()
    message = r"成功插入{}条数据".format(len(files_path))
    return message


# 可视化？
with gr.Blocks() as app:
    gr.Markdown(
        """提醒: <br>
    <b>1.本功能暂时未完善，请将所要添加的文档事先放到本项目的sample文件夹内<b><br>
    <b>2.非常建议使用相对路径<b><br>
    <b>3.支持添加PDF,TXT,MARKDOWN,HTML格式文档<b><br>
    """
    )
    inp = gr.Textbox(placeholder="请输入文件路径", label='文件路径')
    out = gr.Textbox(label='运行结果')
    button = gr.Button("提交")
    button.click(fn=add_documents, inputs=inp, outputs=out)

app.launch()
