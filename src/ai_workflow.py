"""
AI workflow layer for the Project Manager Copilot.

This module prepares structured project information
for an AI system.
"""

from .project_copilot import ProjectUpdate


def build_project_context(update: ProjectUpdate) -> str:
    """Convert project information into AI-ready context."""

    risks = "\n".join(f"- {risk}" for risk in update.risks) or "- None"
    actions = "\n".join(f"- {action}" for action in update.actions) or "- None"
    blockers = "\n".join(f"- {blocker}" for blocker in update.blockers) or "- None"

    return f"""
Project: {update.project_name}
Status: {update.status}

Risks:
{risks}

Actions:
{actions}

Blockers:
{blockers}
""".strip()

def extract_meeting_actions(notes: str) -> dict:
    """Extract actionable information from meeting notes."""

    return {
        "action_items": [],
        "owners": [],
        "deadlines": [],
        "decisions": [],
        "follow_up_requirements": [],
    }
