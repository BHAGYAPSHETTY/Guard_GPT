import os
import json
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

client = InferenceClient(
    provider="novita",
    api_key=HF_TOKEN,
)


def ask_llama(prompt, system=""):
    if not system:
        system = "You are a helpful assistant."
    try:
        completion = client.chat.completions.create(
            model="meta-llama/llama-3.1-8b-instruct",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt},
            ],
            max_tokens=512,
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return "ERROR: " + str(e)


def ask_llama_json(prompt, system=""):
    system_with_json = system + "\nRespond ONLY with valid JSON. No extra text."
    raw = ask_llama(prompt, system_with_json)
    raw = raw.strip().replace("```json", "").replace("```", "").strip()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {"error": "Could not parse response", "raw": raw}


if __name__ == "__main__":
    print("Testing HuggingFace connection...")
    response = ask_llama("Say hello in one sentence.")
    print("Response:", response)