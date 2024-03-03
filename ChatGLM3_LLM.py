# -*- coding: UTF-8 -*-

from langchain.llms.base import LLM
from typing import Any, List, Optional
from langchain.callbacks.manager import CallbackManagerForLLMRun
from transformers import AutoTokenizer, AutoModel

# 从 LangChain.llms.base.LLM 类继承一个子类
# 重写构造函数与 _call 函数
class ChatGLM3(LLM):
    # 基于本地 InternLM 自定义 LLM 类
    tokenizer: AutoTokenizer = None
    model: AutoModel = None

    def __init__(self, model_path="THUDM/chatglm3-6b"):
        super().__init__()
        print("正在加载模型")
        # 加载分词器和模型
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_path, trust_remote_code=True
        )
        # 注意 4bit量化仅供测试 服务器部署可以改成 fp16
        self.model = (
            AutoModel.from_pretrained(model_path, trust_remote_code=True)
            .quantize(4)
            .cuda()
        )
        self.model = self.model.eval()
        print("完成模型的加载")

    # 重载 _call 函数

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any
    ):
        # 重写调用函数
        response, history = self.model.chat(self.tokenizer, prompt, history=[])
        return response

    @property
    def _llm_type(self) -> str:
        return "ChatGLM3-6B"
