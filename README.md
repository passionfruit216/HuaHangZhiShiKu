# **使用指南**
### 配置环境
---
推荐使用anaconda

*下载anaconda*
>https://www.anaconda.com/download/

**安装时请勾选添加到环境变量中**


安装完毕后打开 Anaconda Powershell Prompt

*创建虚拟环境*

>conda create -n 你的环境名字(修改) python=3.10

等待安装完毕后输入

```
cd 项目路径
conda activate 你的环境名字
pip install -r requirements.txt
pip install -r requirements_web.txt

```
**注意pytorch需要自己安装GPU版本**


如何安装pytoch

**torch版本==2.1.2 其他版本未测试 eg. 2.2.0版本经过测试无法使用** 
>https://blog.csdn.net/qlkaicx/article/details/134577555

### 项目结构介绍
---
- database文件夹 存放词向量数据库
- flagged文件夹 存放运行日志
- sample文件夹 存放相关文档
- add_documents.py 运行可实现添加单个文档的功能 (测试功能)
- api.py 创建LLM大模型的api(服务器部署)
- api_test.py 运行api.py后可测试api通讯情况
- app.py 主程序
- ChatGLM3_LLM.py 实现LLM类，创建LLM模型
- create_db.py 自动加载sample文件夹内的文档，并且创建词向量数据库(未创建时运行)
- QAchain.py 基于Langchain用于创建QA问答链
- test.py 方便测试python环境情况


*其他文件均为未完成或测试用文件*

---
### 如何使用?

直接运行 *app.py* 即可,会自动下载模型(如果遇到网络问题，请参见常见问题)

想要添加文档进行知识库问答,运行 *add_documents.py* 即可

**使用时请一定注意网页下方的注意部分！！！**

---
## 常见问题

#### 下载速度慢？
**pip 换源**
>https://mirrors.tuna.tsinghua.edu.cn/help/pypi/


**conda 换源**
>https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/

#### 运行app.py时提示huggingface xxxxxxx错误?

科学上网

**仅供学术交流使用，禁止其他用途！**

>https://xfltd.net/login

自行注册或者使用账号

```
邮箱: 1589220751@qq.com
密码: 12345678
```
流量用完了联系weixin或QQ

