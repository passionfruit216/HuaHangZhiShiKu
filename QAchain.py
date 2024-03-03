from langchain.vectorstores import Chroma
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
import os
from ChatGLM3_LLM import ChatGLM3
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA


def load_chain():
    # 定义 Embeddings
    model_name = "BAAI/bge-large-zh-v1.5"
    embeddings = HuggingFaceEmbeddings(model_name=model_name)

    # 向量数据库持久化路径
    persist_directory = 'database/vector_db'

    # 加载数据库
    vectordb = Chroma(
        persist_directory=persist_directory, embedding_function=embeddings
    )
    # 加载 llm模型
    llm = ChatGLM3()
    llm.predict("你是谁")
    # 构建 QA问答链
    # 构建 问答模版  (后期可以修改)
    template = """使用以下上下文来回答最后的问题。如果你不知道答案，就说你不知道，不要试图编造答案。尽量使答案简明扼要。”。
    {context}
    问题: {question}
    有用的回答:"""
    # 调用 LangChain 的方法来实例化一个 Template 对象，该对象包含了 context 和 question 两个变量(对应模板中)，在实际调用时，这两个变量会被检索到的文档片段和用户提问填充
    QA_CHAIN_PROMPT = PromptTemplate(
        input_variables=["context", "question"], template=template
    )
    # 构建langchain 检索问答链
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=vectordb.as_retriever(),
        return_source_documents=True,
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
    )
    return qa_chain


class Model_center:
    """
    存储检索问答链的对象
    """

    def __init__(self):
        # 构造函数，加载检索问答链
        self.chain = load_chain()

    def qa_chain_self_answer(self, question: str, chat_history: list = []):
        """
        调用问答链进行回答
        """
        if question == None or len(question) < 1:
            return "", chat_history
        try:
            chat_history.append((question, self.chain({"query": question})["result"]))
            # 将问答结果直接附加到问答历史中，Gradio 会将其展示出来
            return "", chat_history
        except Exception as e:
            return e, chat_history
