# 🤖 Q&A Chatbot with Ollama, LangChain & Streamlit

This project is an **AI-powered chatbot** built using:

- 🧠 **Ollama** – for running open-source large language models locally  
- 🔗 **LangChain** – for chaining prompts and managing LLM interactions  
- 🌐 **Streamlit** – for building a fast, interactive UI

It enables users to ask any question and get smart, conversational responses using models like `mistral` and `gemma`.

---

## 🚀 Features

- Chat interface with local LLMs via [Ollama](https://ollama.com/)
- Streamlit-powered frontend for simple interaction
- Easily switch between models (e.g., `mistral`, `gemma`)
- Adjustable response temperature and character length
- LangChain-based prompt templating and chaining

---

## 🧰 Tech Stack

| Layer        | Tool          |
|--------------|---------------|
| LLM Runtime  | Ollama        |
| LLM Chaining | LangChain     |
| Frontend UI  | Streamlit     |
| Prompt Parsing | LangChain Core |

---
````markdown
## 📦 Installation

1. Clone the repo:

```bash
git clone https://github.com/KartikNimhan/QA-Chatbot-with-Ollama-LangChain-Streamlit.git
cd QA-Chatbot-with-Ollama-LangChain-Streamlit
````

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Start Ollama locally:**

Make sure Ollama is installed and running.

```bash
ollama run mistral
```

You can pull any supported model like:

```bash
ollama pull gemma:2b
```

---

## 🧠 Supported Models

You can select these models from the sidebar:

* `mistral`
* `gemma:2b`

> ✅ You can add more Ollama-supported models easily by updating the `selectbox()`.

---

## 🛠 Running the App

```bash
streamlit run app.py
```

Then go to:
[http://localhost:8501](http://localhost:8501)

---

## 📂 Project Structure

```
.
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

## 📌 Environment Variables (Optional)

If you want to enable LangSmith tracking:

```env
LANGCHAIN_API_KEY=your_langsmith_api_key
```

---



```

---

## 👨‍💻 Author

Made with ❤️ by [Kartik Nimhan](https://github.com/KartikNimhan)

---

## 📜 License

This project is licensed under the **MIT License**.

```
