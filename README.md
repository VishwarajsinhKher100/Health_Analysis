# 🩸 AI Blood Report Analyzer & Indian Diet Planner

An intelligent health companion that parses raw text from blood test reports using LangChain and Llama models to generate an easy-to-understand health summary and a personalized, culturally relevant Indian diet plan. Built with a clean Streamlit interface. 

⚠️ **CRITICAL MEDICAL DISCLAIMER:** This application is an educational AI tool designed to support wellness. It is NOT a diagnostic tool and does NOT provide professional medical advice, prescription, or treatment. Always consult a certified physician or clinical dietitian before making significant changes to your diet or health regimen based on a laboratory report.

---

## 🚀 Features
* **Raw Report Parsing:** Simply copy-paste the text from your laboratory blood report directly into the dashboard.
* **Llama-Powered Analysis:** Leverages local or API-driven Llama models to read complex medical jargon and break it down.
* **Smart Health Summary:** Translates biomarkers (e.g., Hemoglobin, Vitamin D3, Cholesterol, HbA1c) into a clear, plain-language health snapshot highlighting key areas of focus.
* **Customized Indian Diet Plan:** Dynamically builds a macro-friendly Indian meal plan (including traditional options like Roti, Dal, Sabzi, Idli, Poha, etc.) tailored to support the user's specific biomarker deficiencies or goals.
* **Zero Layout Friction:** Clean, intuitive, single-page Streamlit UI designed for fast input and immediate readability.

---

## 🛠️ Architecture Workflow

1. **User Input:** The user copy-pastes the text block of their blood test report into a Streamlit `st.text_area`.
2. **Environment & Context:** `python-dotenv` securely loads the required Llama endpoints and system configurations.
3. **LangChain Pipeline:** 
   * A tailored system prompt template instructs the Llama model to act as a supportive wellness assistant and an expert Indian nutritionist.
   * The text is piped into the Llama model using LangChain.
4. **Dual-Core Generation:** The LLM processes the data in two clear logical blocks:
   * **Part 1:** Plain-language health summary mapping flagged values.
   * **Part 2:** A balanced, practical 7-day or daily Indian diet plan incorporating regional whole foods.
5. **Streamlit UI Render:** Formats and prints the outputs into interactive markdown tabs for the user.

---

## 🛠️ Tech Stack & Dependencies

This application is built entirely using Python, utilizing modern AI framework layers for orchestration and a lightweight, responsive framework for the user interface.

*   **Orchestration Framework:** `LangChain` — Manages the LLM orchestration pipeline, system prompt templates, and structures the context passing.
*   **User Interface:** `Streamlit` — Powers the interactive web dashboard, text-input components, and responsive markdown rendering.
*   **AI Inference Engine:** `Llama 3` Model — Interprets the medical text payload to perform biomarker analysis and compute the personalized diet architecture.
*   **Configuration & Security:** `python-dotenv` — Securely loads environment variables and API endpoints from isolated `.env` environments.

---

## 📋 Prerequisites & Setup

### 1. Clone the Repository

```bash
git clone [https://github.com/VishwarajsinhKher100/Health_Analysis.git](https://github.com/VishwarajsinhKher100/Health_Analysis.git)
cd health_analysis
```

### 2. Environment Configuration

This project uses python-dotenv to manage model parameters and API configurations. Create a .env file in the root directory:

# 🦙 Llama Model Configuration (Update based on your environment: Groq, Replicate, Ollama, etc.)
# If using a cloud provider API (e.g., Groq for blazing fast Llama inference):
GROQ_API_KEY="your_groq_api_key_here"

# If using local Llama via Ollama, point your base URL here:
# OLLAMA_BASE_URL="http://localhost:11434"

# 🩺 Application Hyperparameters
MODEL_NAME="llama-3.3-70b-versatile"  # Example Llama model variant
TEMPERATURE="0.2"                    # Kept low to minimize hallucination of medical metrics

### 3. Installation

Set up a clean virtual environment and install the verified stack:

# Create and activate environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

## 💻 Usage

To launch the Streamlit server locally, run the following command in your terminal:

```bash
streamlit run main.py
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
