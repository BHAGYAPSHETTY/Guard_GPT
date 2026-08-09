from models.schemas import (
    ContentModerationInput,
    ContentModerationOutput,
)


def moderate_content(
    data: ContentModerationInput,
) -> ContentModerationOutput:
    """
    Perform basic deterministic content moderation.

    This tool identifies potentially unsafe content categories.
    """

    prompt = data.prompt.strip()
    prompt_lower = prompt.lower()

    detected_categories: list[str] = []

    # --------------------------------------------------------
    # Self-harm
    # --------------------------------------------------------

    self_harm_patterns = [
        "kill myself",
        "end my life",
        "suicide",
        "self harm",
        "self-harm",
        "hurt myself",
    ]

    if any(
        pattern in prompt_lower
        for pattern in self_harm_patterns
    ):
        detected_categories.append("self_harm")

    # --------------------------------------------------------
    # Violence
    # --------------------------------------------------------

    violence_patterns = [
        "kill someone",
        "murder someone",
        "how to murder",
        "how to kill",
        "attack someone",
        "hurt someone",
    ]

    if any(
        pattern in prompt_lower
        for pattern in violence_patterns
    ):
        detected_categories.append("violence")

    # --------------------------------------------------------
    # Malware / malicious cyber activity
    # --------------------------------------------------------

    cyber_abuse_patterns = [
        "create malware",
        "write ransomware",
        "deploy ransomware",
        "steal passwords",
        "steal credentials",
        "keylogger",
        "ddos attack",
        "build a botnet",
    ]

    if any(
        pattern in prompt_lower
        for pattern in cyber_abuse_patterns
    ):
        detected_categories.append("malicious_cyber_activity")

    # --------------------------------------------------------
    # Credential theft / phishing
    # --------------------------------------------------------

    credential_theft_patterns = [
        "steal someone's password",
        "steal passwords",
        "steal login credentials",
        "phishing page",
        "phishing website",
        "capture passwords",
        "capture login credentials",
    ]

    if any(
        pattern in prompt_lower
        for pattern in credential_theft_patterns
    ):
        detected_categories.append("credential_theft")

    # --------------------------------------------------------
    # Determine severity
    # --------------------------------------------------------

    if not detected_categories:
        is_unsafe = False
        severity = "none"

    elif "self_harm" in detected_categories:
        is_unsafe = True
        severity = "high"

    elif (
        "violence" in detected_categories
        or "malicious_cyber_activity" in detected_categories
        or "credential_theft" in detected_categories
    ):
        is_unsafe = True
        severity = "high"

    else:
        is_unsafe = True
        severity = "medium"

    # --------------------------------------------------------
    # Explanation
    # --------------------------------------------------------

    if is_unsafe:
        explanation = (
            "The prompt contains content that matches one or more "
            "unsafe-content categories."
        )
    else:
        explanation = (
            "No known unsafe-content categories were detected."
        )

    return ContentModerationOutput(
        is_unsafe=is_unsafe,
        categories=detected_categories,
        severity=severity,
        explanation=explanation,
    )