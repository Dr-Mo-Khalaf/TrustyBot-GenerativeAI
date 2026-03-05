# TrustyBot-GenerativeAI

**Safely validate generative AI responses using TrustGuard.** Supports schema checks, custom rules (profanity, PII), and AI judges for contextual safety. Ideal for chatbots, content moderation, and trustworthy LLM outputs.

---

## 🔖 Badges

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg" alt="Python 3.9+"/>
  <img src="https://img.shields.io/badge/LLM-HuggingFace-yellow.svg" alt="LLM HuggingFace"/>
  <img src="https://img.shields.io/badge/TrustGuard-PII%20Detection-purple.svg" alt="TrustGuard"/>
  <img src="https://img.shields.io/badge/Security-Data%20Protection-red.svg" alt="Security"/>
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License"/>
  <img src="https://img.shields.io/badge/Status-Active-success.svg" alt="Status"/>
</p>

---

# 🔐 Secure LLM Chatbot

A **privacy-first AI chatbot** integrating **HuggingFace LLMs** with **TrustGuard** to detect and block **PII** in both user inputs and model outputs.

---

# ✨ Features

* **PII Protection**: Detects emails, phone numbers, SSNs, and other personal identifiers.
* **Dual Guardrail System**: Input & Output validation using TrustGuard.
* **LLM Integration**: Default `openai/gpt-oss-20b` via HuggingFace Inference API.
* **Interactive CLI Chat**: Real-time secure messaging.
* **Environment-based Configuration**: API keys via `.env`.

---

# 🖥 Demo

**CLI Chat Example**

```bash
🤖 Chatbot with PII Detection + HuggingFace (type 'exit' to quit)

You: Hello
Bot: thinking
Hello! How can I assist you today?

You: My SSN is 123-45-6789
Bot: 🚫 Blocked (Input - PII): Sensitive information detected
```

---

# 📸 Screenshots

<img src="docs/screenshot-cli.png" width="700" alt="CLI Chat Interface"/>

*(Replace with actual screenshots)*

---

# 🏗 Architecture (Visual / Animated)

```mermaid
flowchart TD
    style A fill:#4caf50,stroke:#333,stroke-width:2px
    style B fill:#ff9800,stroke:#333,stroke-width:2px
    style C fill:#2196f3,stroke:#333,stroke-width:2px
    style D fill:#ff9800,stroke:#333,stroke-width:2px
    style E fill:#4caf50,stroke:#333,stroke-width:2px

    A[User Input] --> B[TrustGuard Input Validator<br/>(PII Detection)]
    B --> C[HuggingFace LLM<br/>(openai/gpt-oss-20b)]
    C --> D[TrustGuard Output Validator<br/>(PII Detection)]
    D --> E[Safe Response to User]
```

**Diagram Description:**

1. **User Input**
2. **TrustGuard Input Validator (PII Detection)**
3. **HuggingFace LLM (`openai/gpt-oss-20b`)**
4. **TrustGuard Output Validator (PII Detection)**
5. **Clean Response to User**

> Optional: replace with an animated GIF later for a premium effect.

---

# 📂 Project Structure

```text
secure-llm-chatbot
│
├── chatbot.py
├── .env
├── requirements.txt
├── README.md
│
└── docs
    └── screenshot-cli.png
```

---

# ⚙ Installation

## 1️⃣ Clone the repository

```bash
git clone hhttps://github.com/Dr-Mo-Khalaf/TrustyBot-GenerativeAI.git
cd TrustyBot-GenerativeAI
```

---

## 2️⃣ Create a virtual environment

Linux / Mac:

```bash
python -m venv venv
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

---

## 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```text
huggingface_hub
python-dotenv
trustguard
uvicorn  # optional for web deployment
```

---

# 🔑 Environment Setup

Create a `.env` file:

```text
HF_API_KEY=your_huggingface_api_key
```

Get a token from:

[https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

---

# 🚀 Usage

**CLI Mode**

```bash
python main.py
```

Exit anytime with:

```bash
exit
```


---

# 🧠 How It Works

### 1️⃣ Input Validation

User prompts are wrapped into structured JSON and validated by **TrustGuard**.

```python
input_guard = TrustGuard(
    schema_class=GenericResponse,
    custom_rules=[validate_pii]
)
```

If PII is detected:

```text
🚫 Blocked (Input - PII)
```

---

### 2️⃣ LLM Response Generation

The validated prompt is sent to HuggingFace:

```python
response = llm.chat_completion(
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ]
)
```

Default model:

```python
model="openai/gpt-oss-20b"
```

---

### 3️⃣ Output Validation

The response is validated again:

```text
TrustGuard → PII detection
```

If sensitive data appears:

```text
⚠ Blocked (Output - PII)
```

---

# 🔄 Switching Models

```python
llm = InferenceClient(
    model="deepseek-ai/DeepSeek-R1",
    token=HF_API_KEY
)
```

Other compatible models:

* Mistral
* Llama
* Mixtral
* DeepSeek

---

# 🔒 Security Design

| Layer            | Purpose                                      |
| ---------------- | -------------------------------------------- |
| Input Guard      | Prevent sensitive data from reaching the LLM |
| System Prompt    | Controls model behavior                      |
| Output Guard     | Prevents data leakage                        |
| Response Cleaner | Removes hidden reasoning tags                |

Defends against:

* Prompt injection
* Data leakage
* Sensitive data exposure
* Unsafe model outputs

---

# 📌 Use Cases

* Enterprise chatbots
* Privacy-aware AI assistants
* LLM security experimentation
* AI guardrail testing
* AI safety research

---

# 🧩 Dependencies

* `huggingface_hub`
* `trustguard`
* `python-dotenv`
* `json`
* `os`

---

# 📜 License

MIT License

---

# 🤝 Contributing

Pull requests are welcome.

1. Fork the repo
2. Create a new branch
3. Submit a PR

---

# ⭐ Support

If you find this project useful:

⭐ Star the repository
🍴 Fork the project
🛠 Contribute improvements


