---

# 🤖 Q\&A Chatbot with Ollama, LangChain & Streamlit

This project is an AI-powered chatbot built using:

* 🧠 **Ollama** – Run open-source LLMs like Mistral or Gemma locally.
* 🔗 **LangChain** – Manage prompt templates and model interactions.
* 🌐 **Streamlit** – Build a fast and interactive user interface.

It allows users to ask any question and receive intelligent responses from local language models.

---

## 🚀 Features

* Chat interface using local LLMs via **Ollama**
* Clean UI with **Streamlit**
* Model switcher for **Mistral**, **Gemma**, and more
* Adjustable **temperature** and **response length**
* Modular architecture using **LangChain**'s chaining and prompt templating

---

## 🧰 Tech Stack

| Layer          | Tool           |
| -------------- | -------------- |
| LLM Runtime    | Ollama         |
| LLM Chaining   | LangChain      |
| Frontend UI    | Streamlit      |
| Prompt Parsing | LangChain Core |

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/KartikNimhan/QA-Chatbot-with-Ollama-LangChain-Streamlit.git
cd QA-Chatbot-with-Ollama-LangChain-Streamlit
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Start Ollama Locally

Make sure [Ollama](https://ollama.com) is installed and running:

```bash
ollama run mistral
```

You can also pull additional models like:

```bash
ollama pull gemma:2b
```

---

## 🧠 Supported Models

You can select these models from the sidebar in the app:

* `mistral`
* `gemma:2b`

✅ You can add more [Ollama-supported models](https://ollama.com/library) by editing the `selectbox()` in the code.

---

## 🛠 Running the App

Start the Streamlit app:

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📂 Project Structure

```
.
├── app.py              # Main Streamlit app
├── .env                # Optional environment variables
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 🔐 Environment Variables (Optional)

If you're using [LangSmith](https://www.langchain.com/langsmith) for tracing:

Create a `.env` file:

```env
LANGCHAIN_API_KEY=your_langsmith_api_key
```

---

## 🖼️ Screenshots

<details>
<summary>Click to expand</summary>

### Chatbot Interface Example
<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/fa5e7172-1e8b-4337-bc44-b17f2f978474" />

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/1739e9a6-93bc-43b9-9bef-514c76283328" />

</details>

---

## 👨‍💻 Author

Made with ❤️ by [Kartik Nimhan](https://github.com/KartikNimhan)

---

## 📜 License

This project is licensed under the **MIT License**.

---

