import os
from dotenv import load_dotenv
import streamlit as st

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

# Load environment variables (for LangSmith if needed)
load_dotenv()

# Optional LangSmith tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Q & A Chatbot with OLLAMA"

# Define the prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user queries."),
    ("user", "Question: {question}")
])

# Function to generate response using Ollama
def generate_response(question, model_name, temperature, max_tokens):
    # max_tokens is NOT supported by Ollama in LangChain, so we ignore it
    llm = Ollama(
        model=model_name,
        temperature=temperature
    )

    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})

    # Optional: truncate response manually (not actual token control)
    return answer[:max_tokens]

# Streamlit App Interface
st.title("🤖 Enhanced Q&A Chatbot with Ollama")
st.sidebar.title("Settings")

# Model selection
model_name = st.sidebar.selectbox(
    "🧠 Select an Ollama model:",
    [
        "mistral",        
        "gemma:2b",
        
    ]
)

# Response controls
temperature = st.sidebar.slider("🔥 Temperature", 0.0, 1.0, 0.7)
max_tokens = st.sidebar.slider("🔢 Max Characters (soft limit)", 50, 1000, 300)

# User input
st.write("💬 Ask a question:")
user_input = st.text_input("📝 Your Question:")

# Generate response
if user_input:
    try:
        response = generate_response(user_input, model_name, temperature, max_tokens)
        st.success("✅ Response:")
        st.write(response)
    except Exception as e:
        st.error("⚠️ Error generating response.")
        st.exception(e)
else:
    st.info("👈 Type a question to begin.")
