"""
AI Project Manager Copilot

A lightweight prototype for turning project-management inputs
into structured outputs.
"""


def analyze_project_update(
    project_name,
    status,
    risks=None,
    actions=None,
    blockers=None,
):
    """
    Create a structured project update.

    Parameters:
        project_name: Name of the project.
        status: Current project status.
        risks: Current project risks.
        actions: Open action items.
        blockers: Current blockers.

    Returns:
        A structured dictionary containing the project update.
    """

    return {
        "project_name": project_name,
        "status": status,
        "risks": risks or [],
        "actions": actions or [],
        "blockers": blockers or [],
    }


if __name__ == "__main__":
    update = analyze_project_update(
        project_name="AI Project Manager Copilot",
        status="Building",
        risks=["Requirements may change"],
        actions=["Complete prototype"],
        blockers=[],
    )

    print("AI Project Manager Copilot")
    print("==========================")
    print(update)
