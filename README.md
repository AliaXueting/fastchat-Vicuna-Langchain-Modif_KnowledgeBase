# fastchat/Langchain/KnowledgeBase

## Deploy the fastchat
在AI studio云服务器上进行了部署了测试。 main.ipynb是LangChain部分的代码  products.txt文件是data

Deploy the fastchat on AI studio cloud server. main.ipynb is the code of the LangChain part and the products.txt file is data

step1  launch the controller: python3 -m fastchat.serve.controller

step2: python3 -m fastchat.serve.model_worker --model-names "gpt-3.5-turbo,text-davinci-003,text-embedding-ada-002" --model-path lmsys/vicuna-7b-v1.3 


![a857bc770a1bd9d6f09fcea006dc544](https://github.com/AliaXueting/fastchat/assets/96671351/b15ab77a-655b-4b0f-a004-53273e7f416c)

## Langchain Integration
step3 launch the RESTful API server: 

Set OpenAI base url: export OPENAI_API_BASE=http://localhost:8000/v1

Set OpenAI API key: export OPENAI_API_KEY=EMPTY

Exampel of modified data:
![image](https://github.com/AliaXueting/fastchat-Vicuna-Langchain-Modif_KnowledgeBase/assets/96671351/cc1b8659-a8f1-4ea0-934d-3f99a0e5b525)

LangChain/modify knowledge base part:
![71483767729b9a1f45e9659988b231b](https://github.com/AliaXueting/fastchat/assets/96671351/e4781242-cd3a-41a8-8e60-00f69e202c21)

Testing on the Gradio UI:


