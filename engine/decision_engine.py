import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def make_decision(safety_result, intent_result):
    """
    Takes safety and intent results and decides what to do.
    Returns: ALLOW, WARN, or BLOCK
    """

    safety_label = safety_result.get("label", "SAFE")
    severity = safety_result.get("severity", "LOW")
    intent = intent_result.get("intent", "information_seeking")
    category = intent_result.get("category", "BENIGN")

    print("  [Decision] Safety:", safety_label, "| Intent:", intent, "| Category:", category)

    # Always block these intents no matter what
    always_block = ["harmful_request", "jailbreak", "data_extraction"]
    if intent in always_block:
        return {
            "action": "BLOCK",
            "risk_level": "CRITICAL",
            "reason": "Blocked intent detected: " + intent
        }

    # Block if unsafe and high severity
    if safety_label == "UNSAFE" and severity in ["HIGH", "CRITICAL"]:
        return {
            "action": "BLOCK",
            "risk_level": "HIGH",
            "reason": "Unsafe content detected: " + safety_result.get("reason", "")
        }

    # Warn if suspicious
    if category == "SUSPICIOUS" or severity == "MEDIUM":
        return {
            "action": "WARN",
            "risk_level": "MEDIUM",
            "reason": "Suspicious content detected"
        }

    # Warn if unsafe but low severity
    if safety_label == "UNSAFE" and severity == "LOW":
        return {
            "action": "WARN",
            "risk_level": "LOW",
            "reason": "Mildly unsafe content detected"
        }

    # Everything else is allowed
    return {
        "action": "ALLOW",
        "risk_level": "LOW",
        "reason": "Content is safe"
    }


def get_block_message(decision):
    """Returns a message to show the user when blocked."""
    action = decision.get("action")
    if action == "BLOCK":
        return "Sorry, I cannot help with that request as it violates safety guidelines."
    elif action == "WARN":
        return "Warning: This topic is sensitive. Please use this information responsibly."
    return ""


if __name__ == "__main__":
    print("--- Test 1: Safe message ---")
    safety = {"label": "SAFE", "severity": "LOW", "reason": "Safe content"}
    intent = {"intent": "information_seeking", "category": "BENIGN"}
    result = make_decision(safety, intent)
    print("Decision:", result)

    print("\n--- Test 2: Jailbreak attempt ---")
    safety = {"label": "UNSAFE", "severity": "HIGH", "reason": "Jailbreak detected"}
    intent = {"intent": "jailbreak", "category": "MALICIOUS"}
    result = make_decision(safety, intent)
    print("Decision:", result)

    print("\n--- Test 3: Suspicious message ---")
    safety = {"label": "SAFE", "severity": "LOW", "reason": "Safe"}
    intent = {"intent": "conversation", "category": "SUSPICIOUS"}
    result = make_decision(safety, intent)
    print("Decision:", result)