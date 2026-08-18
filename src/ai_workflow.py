"""
AI workflow layer for the Project Manager Copilot.

This module prepares structured project information
for an AI system.
"""

import re

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

    action_items = []
    owners = []
    deadlines = []
    decisions = []
    follow_up_requirements = []

    for line in notes.splitlines():
        text = line.strip()
        lower = text.lower()

        if not text:
            continue

        if any(keyword in lower for keyword in [
            "action:",
            "action item:",
            "todo:",
            "to-do:",
        ]):
            action_items.append(text)

        if "owner:" in lower or "assigned to:" in lower:
            owners.append(text)

        if "deadline:" in lower or "due:" in lower:
            deadlines.append(text)

        if any(keyword in lower for keyword in [
            "decision:",
            "decided:",
            "agreed:",
        ]):
            decisions.append(text)

        if any(keyword in lower for keyword in [
            "follow-up:",
            "follow up:",
            "next step:",
        ]):
            follow_up_requirements.append(text)

    return {
        "action_items": action_items,
        "owners": owners,
        "deadlines": deadlines,
        "decisions": decisions,
        "follow_up_requirements": follow_up_requirements,
    }
