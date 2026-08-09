import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

from models.schemas import (
    AuditLoggerInput,
    AuditLoggerOutput,
)


# Store audit logs outside the tools directory.
BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "data"
LOG_FILE = LOG_DIR / "audit.log"


def log_audit_event(
    data: AuditLoggerInput,
) -> AuditLoggerOutput:
    """
    Record an MCP security-tool event in a JSON Lines audit file.
    """

    try:
        # Make sure the data directory exists.
        LOG_DIR.mkdir(parents=True, exist_ok=True)

        # Generate a unique event ID.
        event_id = str(uuid.uuid4())

        # Create a UTC timestamp.
        timestamp = datetime.now(timezone.utc).isoformat()

        # Build the audit record.
        audit_record = {
            "event_id": event_id,
            "timestamp": timestamp,
            "tool_name": data.tool_name,
            "prompt": data.prompt,
            "result": data.result,
        }

        # Append one JSON object per line.
        with LOG_FILE.open(
            "a",
            encoding="utf-8",
        ) as file:
            file.write(
                json.dumps(audit_record, ensure_ascii=False)
                + "\n"
            )

        return AuditLoggerOutput(
            success=True,
            event_id=event_id,
            message="Audit event recorded successfully.",
        )

    except Exception as exc:
        return AuditLoggerOutput(
            success=False,
            event_id="",
            message=f"Failed to record audit event: {exc}",
        )