# fastchat/Langchain/KnowledgeBase

## Deploy the fastchat
在AI studio云服务器上进行了部署了测试。 app.py是LangChain部分的代码  products.txt文件是data

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
![image](https://github.com/AliaXueting/fastchat-Vicuna-Langchain-Modif_KnowledgeBase/assets/96671351/69a27c71-7d5f-4705-bc91-1183a516bb88)


step4 launch the Gradio web server: python3 -m fastchat.serve.gradio_web_server

or create your own UI page, Reference https://www.bilibili.com/video/BV1rk4y137Ty?p=2&vd_source=2efcd8c571daa7543cf07149b1c07305

![image](https://github.com/AliaXueting/fastchat-Vicuna-Langchain-Modif_KnowledgeBase/assets/96671351/6964ae76-2c81-47d5-8f62-5622e3d769ba)

UI page 
![image](https://github.com/AliaXueting/fastchat-Vicuna-Langchain-Modif_KnowledgeBase/assets/96671351/6cb34dae-83ce-44f1-b9dc-ec322a7cdda8)


## Custom Prompts
Language Detection and Switching: Develop a language detection mechanism to identify whether the user input is in Mandarin or English. 
use pre-trained language detection libraries or models to accomplish this. Based on the detected language, switch the chatbot's responses accordingly.

Custom Response Templates: Design custom response templates that can be filled with language-specific content. For instance, create templates for greetings, acknowledgments, and common queries in both languages. The model can then use these templates to generate coherent responses.

Language-Specific Variations: Develop variations of your responses to account for cultural differences and language preferences. Certain phrases or concepts might not directly translate between Mandarin and English, so having language-specific variations can ensure more accurate and culturally sensitive interactions. such as Uesr "You got an apple", This sentence may refer to you having an iPhone in Chinese, not that you have an Apple

## Reference
fastchat:
https://github.com/lm-sys/FastChat

Langchain:
https://python.langchain.com/docs/use_cases/question_answering/ 
