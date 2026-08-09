from typing import Literal
from pydantic import BaseModel, Field


# ============================================================
# 1. PROMPT ANALYSIS
# ============================================================

class PromptAnalysisInput(BaseModel):
    prompt: str = Field(
        ...,
        description="The user's original prompt to analyze."
    )


class PromptAnalysisOutput(BaseModel):
    intent: Literal[
        "Greeting",
        "Self-Harm",
        "Programming",
        "Cybersecurity",
        "Suspicious",
        "General"
    ]

    risk_level: Literal[
        "low",
        "medium",
        "high"
    ]

    summary: str

    requires_jailbreak_check: bool


# ============================================================
# 2. JAILBREAK DETECTION
# ============================================================

class JailbreakDetectionInput(BaseModel):
    prompt: str = Field(
        ...,
        description="The user's prompt to check for jailbreak attempts."
    )


class JailbreakDetectionOutput(BaseModel):
    is_jailbreak: bool

    confidence: float = Field(
        ...,
        ge=0.0,
        le=1.0
    )

    risk_level: Literal[
        "low",
        "medium",
        "high"
    ]

    detected_patterns: list[str]

    explanation: str


# ============================================================
# 3. CONTENT MODERATION
# ============================================================

class ContentModerationInput(BaseModel):
    prompt: str = Field(
        ...,
        description="The user's prompt to check for unsafe content."
    )


class ContentModerationOutput(BaseModel):
    is_unsafe: bool

    categories: list[str]

    severity: Literal[
        "none",
        "low",
        "medium",
        "high"
    ]

    explanation: str


# ============================================================
# 4. AUDIT LOGGER
# ============================================================

class AuditLoggerInput(BaseModel):
    prompt: str = Field(
        ...,
        description="The original user prompt being logged."
    )

    tool_name: str = Field(
        ...,
        description="Name of the MCP tool that produced the result."
    )

    result: dict = Field(
        ...,
        description="Structured result returned by the tool."
    )


class AuditLoggerOutput(BaseModel):
    success: bool

    event_id: str

    message: str