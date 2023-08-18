import openai
import gradio as gr

from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator

#openai.api_key = "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"
messages = [{"role":"system", "content":"you are a helpful and kind AI Assistant"}]

embedding = OpenAIEmbeddings(model="text-embedding-ada-002")
loader = TextLoader("products.txt")
index = VectorstoreIndexCreator(embedding=embedding).from_loaders([loader])
llm = ChatOpenAI(model="gpt-3.5-turbo")

    
def chatbot(input):
    if input:
        messages.append({"role":"user", "content":input})
        answer = index.query(input, llm=llm)
        messages.append({"role": "assistant", "content": answer})
        return answer

inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot by AliaXueting",description="Ask anything you want",
theme="compact").launch(share=True)
