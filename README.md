# Health Analysis using LLM API 🩺🤖

An AI-powered health analysis application that leverages Large Language Models (LLMs) to provide insights, summarize medical notes, and analyze health-related queries. 

> **⚠️ MEDICAL DISCLAIMER:** This application is for informational and educational purposes only. It is not intended to be a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.

---

## 🚀 Features

- **Medical Report Summarizer:** Upload complex medical lab results and get an easy-to-understand summary.
- **Diet Plan Recommendation:** Recomment diet plan according medial report.

## 🛠️ Tech Stack

- **Language:** Python 3.14
- **Framework:** Streamlit
- **LLM API:** Groq llama
- **Libraries:** LangChain, Dotenv

---

## ⚙️ Getting Started

### Prerequisites

Make sure you have Python installed, and you will need an API key from [OpenAI/Google/Anthropic].

### Installation

1. **Clone the repository:**

    ```bash
    git clone [https://github.com/VishwarajsinhKher100/Health_Analysis.git](https://github.com/VishwarajsinhKher100/Health_Analysis.git)
    cd health_analysis
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

# Environment Setup

Create a .env file in the root directory of your project and add your API keys:

```bash
LLM_API_KEY=your_actual_api_key_here
```

Note: The .env file is included in .gitignore to protect your API keys.

# 💻 Usage

To run the application locally, execute the following command:

```bash
streamlit run app.py
```

# 🔒 Security & Privacy

Data Masking: This application attempts to strip out personally identifiable information (PII) before sending data to the LLM API.

API Usage: Ensure your API provider's data policy aligns with health data regulations (e.g., checking if data is used for model training).

# 📄 License

Distributed under the MIT License. See LICENSE for more information.
