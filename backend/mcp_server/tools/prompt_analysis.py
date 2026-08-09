from models.schemas import (
    PromptAnalysisInput,
    PromptAnalysisOutput,
)


def analyze_prompt(data: PromptAnalysisInput) -> PromptAnalysisOutput:
    """
    Analyze a user prompt and classify it into one of the
    GuardGPT intent categories.
    """

    prompt = data.prompt.strip()
    prompt_lower = prompt.lower()

    # --------------------------------------------------------
    # Greeting detection
    # --------------------------------------------------------

    greeting_words = [
        "hello",
        "hi",
        "hey",
        "good morning",
        "good afternoon",
        "good evening",
    ]

    if any(word in prompt_lower for word in greeting_words):
        return PromptAnalysisOutput(
            intent="Greeting",
            risk_level="low",
            summary="The prompt appears to be a greeting.",
            requires_jailbreak_check=False,
        )

    # --------------------------------------------------------
    # Self-harm detection
    # --------------------------------------------------------

    self_harm_keywords = [
        "suicide",
        "kill myself",
        "hurt myself",
        "self harm",
        "self-harm",
        "end my life",
    ]

    if any(keyword in prompt_lower for keyword in self_harm_keywords):
        return PromptAnalysisOutput(
            intent="Self-Harm",
            risk_level="high",
            summary="The prompt contains language associated with self-harm.",
            requires_jailbreak_check=False,
        )

    # --------------------------------------------------------
    # Cybersecurity detection
    # --------------------------------------------------------

    cybersecurity_keywords = [
        "malware",
        "ransomware",
        "phishing",
        "exploit",
        "ddos",
        "sql injection",
        "xss",
        "penetration testing",
        "ethical hacking",
        "cybersecurity",
        "vulnerability",
        "hacking",
        "hack",
    ]

    if any(keyword in prompt_lower for keyword in cybersecurity_keywords):
        return PromptAnalysisOutput(
            intent="Cybersecurity",
            risk_level="medium",
            summary="The prompt is related to cybersecurity.",
            requires_jailbreak_check=True,
        )

    # --------------------------------------------------------
    # Programming detection
    # --------------------------------------------------------

    programming_keywords = [
        "python",
        "java",
        "javascript",
        "programming",
        "code",
        "coding",
        "function",
        "class",
        "api",
        "debug",
        "bug",
        "sql",
        "html",
        "css",
        "algorithm",
    ]

    if any(keyword in prompt_lower for keyword in programming_keywords):
        return PromptAnalysisOutput(
            intent="Programming",
            risk_level="low",
            summary="The prompt is related to programming or software development.",
            requires_jailbreak_check=False,
        )

    # --------------------------------------------------------
    # Suspicious prompt detection
    # --------------------------------------------------------

    suspicious_keywords = [
        "ignore previous instructions",
        "ignore all previous instructions",
        "bypass",
        "jailbreak",
        "system prompt",
        "reveal your instructions",
        "developer message",
        "hidden instructions",
        "override instructions",
    ]

    if any(keyword in prompt_lower for keyword in suspicious_keywords):
        return PromptAnalysisOutput(
            intent="Suspicious",
            risk_level="high",
            summary="The prompt contains language that may indicate an attempt to bypass or manipulate instructions.",
            requires_jailbreak_check=True,
        )

    # --------------------------------------------------------
    # General prompt
    # --------------------------------------------------------

    return PromptAnalysisOutput(
        intent="General",
        risk_level="low",
        summary="The prompt does not match a specific GuardGPT intent category.",
        requires_jailbreak_check=False,
    )