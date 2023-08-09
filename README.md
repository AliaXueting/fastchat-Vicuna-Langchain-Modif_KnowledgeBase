# fastchat
fastchat


step1  launch the controller: python3 -m fastchat.serve.controller
step2: python3 -m fastchat.serve.model_worker --model-names "gpt-3.5-turbo,text-davinci-003,text-embedding-ada-002" --model-path lmsys/vicuna-7b-v1.3 


![a857bc770a1bd9d6f09fcea006dc544](https://github.com/AliaXueting/fastchat/assets/96671351/b15ab77a-655b-4b0f-a004-53273e7f416c)

step3 launch the RESTful API server: 
Set OpenAI base url: export OPENAI_API_BASE=http://localhost:8000/v1
Set OpenAI API key: export OPENAI_API_KEY=EMPTY

LangChain part:
![71483767729b9a1f45e9659988b231b](https://github.com/AliaXueting/fastchat/assets/96671351/e4781242-cd3a-41a8-8e60-00f69e202c21)


