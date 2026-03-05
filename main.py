import json
import os
from dotenv import load_dotenv

from huggingface_hub import InferenceClient

from trustguard import TrustGuard
from trustguard.schemas import GenericResponse
from trustguard.rules import validate_pii  # PII detection only

# =====================================
# 1️⃣ Load Environment Variables
# =====================================

load_dotenv()
HF_TOKEN = os.getenv("HF_API_KEY")
if not HF_TOKEN:
    raise ValueError("HF_API_KEY not found in environment variables.")

# =====================================
# 2️⃣ Create HuggingFace llm
# =====================================

llm = InferenceClient(
    model="openai/gpt-oss-20b",
    # model="deepseek-ai/DeepSeek-R1",
    token=HF_TOKEN
)

# =====================================
# 3️⃣ TrustGuard with PII Detection
# =====================================

input_guard = TrustGuard(schema_class=GenericResponse, custom_rules=[validate_pii])
output_guard = TrustGuard(schema_class=GenericResponse, custom_rules=[validate_pii])

# =====================================
# 4️⃣ Chat Function
# =====================================

def chat(user_message: str):
    user_message = user_message.strip()
    prompted_message = f"prompt: {user_message}"

    # ---- INPUT VALIDATION ----
    input_payload = json.dumps({
        "content": prompted_message,
        "sentiment": "neutral",
        "tone": "neutral",
        "is_helpful": True
    })

    input_result = input_guard.validate(input_payload)
    if not input_result.is_approved:
        return f"🚫 Blocked (Input - PII): {input_result.log}"

    # ---- LLM GENERATION ----
    system_prompt = (
        "You are a helpful AI assistant. "
        "Respond naturally, politely, and concisely. "
        "Do NOT output any internal reasoning, thinking steps, or <think> tags. "
        "Just provide the final reply only."
    )

    try:
        response = llm.chat_completion(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompted_message}
            ],
            max_tokens=1024,
            temperature=0.7,
        )
        reply = response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Model Error: {str(e)}"

    reply = (reply or "").strip()
    if not reply:
        return "⚠️ Model returned empty output."

    # ---- OUTPUT VALIDATION ----
    output_payload = json.dumps({
        "content": reply,
        "sentiment": "neutral",
        "tone": "neutral",
        "is_helpful": True
    })

    output_result = output_guard.validate(output_payload)
    if not output_result.is_approved:
        return f"⚠️ Blocked (Output - PII): {output_result.log}"

    # ---- Remove any <think> blocks and prefix with "thinking" ----
    clean_reply = output_result.data['content'].replace("<think>", "").replace("</think>", "").strip()

    return f"thinking\n{clean_reply}"

# =====================================
# 5️⃣ CLI Chat Loop
# =====================================

if __name__ == "__main__":
    print("🤖 Chatbot with PII Detection + HuggingFace (type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        print("Bot:", chat(user_input))