"""
AI Project Manager Copilot

Prototype for turning project-management information
into structured project updates.
"""

from dataclasses import dataclass, field


@dataclass
class ProjectUpdate:
    """Structured project information."""

    project_name: str
    status: str
    risks: list[str] = field(default_factory=list)
    actions: list[str] = field(default_factory=list)
    blockers: list[str] = field(default_factory=list)
@dataclass
class Requirement:
    requirement_id: str
    description: str
    priority: str = "Medium"

def analyze_project_update(update: ProjectUpdate) -> dict:
    """
    Convert a ProjectUpdate into a structured dictionary.
    """

    return {
        "project_name": update.project_name,
        "status": update.status,
        "risks": update.risks,
        "actions": update.actions,
        "blockers": update.blockers,
    }
def analyze_requirements(requirements: list[str]) -> list[Requirement]:
    """Structure raw project requirements."""

    structured_requirements = []

    for index, requirement in enumerate(requirements, start=1):
        structured_requirements.append(
            Requirement(
                requirement_id=f"FR-{index:02d}",
                description=requirement.strip(),
            )
        )

    return structured_requirements

if __name__ == "__main__":
    project = ProjectUpdate(
        project_name="AI Project Manager Copilot",
        status="Building",
        risks=["Requirements may change"],
        actions=["Complete prototype"],
        blockers=[],
    )

    result = analyze_project_update(project)

    print("AI Project Manager Copilot")
    print("==========================")
    print(result)
