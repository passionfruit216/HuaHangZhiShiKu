# -*- coding: UTF-8 -*-
import os
from tqdm import tqdm
from langchain.document_loaders import UnstructuredFileLoader
from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.document_loaders import UnstructuredImageLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from sentence_transformers import SentenceTransformer

# 完成 从本地获取指定文件读取
def get_files(file_path):
    file_list = []
    for root, dirs, files in os.walk(file_path):
        for file in files:
            # 判断 文件是否符合标准
            if file.endswith('.txt'):
                file_list.append(os.path.join(root, file))
            elif file.endswith('.md'):
                file_list.append(os.path.join(root, file))
            elif file.endswith('.pdf'):
                file_list.append(os.path.join(root, file))
            elif file.endswith('.jpg'):  # 添加图片 待测试功能
                file_list.append(os.path.join(root, file))

    return file_list


# 使用 langchain完成 文件文字内容提取
def get_text(file_path):
    # 调用定义的函数得到目标文件路径列表
    file_list = get_files(file_path)
    # docs 存放加载之后的纯文本对象
    docs = []
    for file in tqdm(file_list):
        file_type = file.split('.')[-1]
        if file_type == 'md':
            loader = UnstructuredMarkdownLoader(file)
        elif file_type == 'txt':
            loader = UnstructuredFileLoader(file)
        elif file_type == 'pdf':
            loader = UnstructuredPDFLoader(file)
        elif file_type == 'jpg':
            loader = UnstructuredImageLoader(file)
        else:
            # 如果是不符合条件的文件，直接跳过
            continue
        docs.extend(loader.load())
    return docs


# 加载目标文件 (后续可以写的更优雅一点)
file_path = 'C:\\Users\\15892\\Desktop\\owngpt\\owngpt\\sample'
docs = []
docs.extend(get_text(file_path))
# 使用langchain对文本进行分块
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=150)
split_docs = text_splitter.split_documents(docs)
# 加载开源词向量模型
model_name = "BAAI/bge-large-zh-v1.5"
embeddings = HuggingFaceEmbeddings(model_name=model_name)
# 构建向量数据库
persist_directory = 'database/vector_db'
# 加载数据库
vectordb = Chroma.from_documents(
    documents=split_docs,
    embedding=embeddings,
    persist_directory=persist_directory,  # 允许将persist_directory目录保存到磁盘上
)
# 将加载的向量数据库存到磁盘上
vectordb.persist()
