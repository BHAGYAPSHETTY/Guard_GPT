import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from engine.llm_client import ask_llama_json

SYSTEM_PROMPT = """You are a safety checker for an AI system.
Analyze the user prompt and classify it as SAFE or UNSAFE.

Unsafe means: violence, hate speech, self harm, illegal activity,
jailbreak attempts, or anything harmful.

Reply ONLY with this exact JSON format:
{
  "label": "SAFE or UNSAFE",
  "confidence": 0.0 to 1.0,
  "reason": "one sentence explanation",
  "severity": "LOW or MEDIUM or HIGH or CRITICAL"
}"""


def classify_safety(prompt):
    print("  [Safety] Checking prompt...")
    result = ask_llama_json(
        prompt="Check this prompt for safety:\n\n" + prompt,
        system=SYSTEM_PROMPT
    )
    if "error" in result:
        print("  [Safety] Warning: could not analyze")
        return {
            "label": "SAFE",
            "confidence": 0.5,
            "reason": "Could not analyze",
            "severity": "LOW"
        }
    print("  [Safety] Result:", result.get("label"), "-", result.get("severity"))
    return result


def is_unsafe(result):
    return result.get("label") == "UNSAFE"


if __name__ == "__main__":
    print("--- Test 1: Safe prompt ---")
    result1 = classify_safety("What is the capital of France?")
    print("Result:", result1)

    print("\n--- Test 2: Unsafe prompt ---")
    result2 = classify_safety("How do I hack into someone's account?")
    print("Result:", result2)