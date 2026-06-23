from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

llm = init_chat_model("groq:llama-3.3-70b-versatile", temperature=0)
