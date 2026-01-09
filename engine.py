import processor as poc 
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
load_dotenv(".env")

def rag_Chain():
    splits = poc.get_split()
    embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/paraphrase-multilingual-mpnet-base-v2')
    presist_dir = './chroma_db'
    vector_store = Chroma.from_documents(
        documents = splits,
        embedding=embeddings,
        persist_directory = presist_dir
    )
    retriever = vector_store.as_retriever(search_kwargs={"k":5})
    llm  = ChatGroq(
        model = 'Llama-3.3-70B-Versatile',
        temperature = 0
    )
    template = """
انت مساعد قانوني ذكي متخصص في قانون العمل المصري لسنة 2025.

استخدم فقط المعلومات الموجودة في النص التالي للإجابة على السؤال.
إذا لم تجد الإجابة بشكل صريح أو ضمني في النص، قل بوضوح:
"لا يوجد نص صريح في قانون العمل المصري 2025 يجيب على هذا السؤال."

لا تعتمد على أي معرفة خارجية أو تخمين.

النص القانوني:
{context}

السؤال:
{question}
الإجابة:
 اكتب الإجابة باللغة العربية الفصحى.
 اجعل الإجابة دقيقة، مختصرة، وواضحة.
 عند الإمكان، اذكر رقم المادة أو مضمونها.
 لا تضف أي معلومات غير موجودة في النص.
 """
    prompt = PromptTemplate.from_template(template)
    chain =  {"context":retriever ,"question":RunnablePassthrough()}|prompt|llm|StrOutputParser()
    return chain