from src.project_copilot import ProjectUpdate, analyze_project_update
from src.ai_workflow import build_project_context

def test_analyze_project_update():
    project = ProjectUpdate(
        project_name="AI Project Manager Copilot",
        status="Building",
        risks=["Requirements may change"],
        actions=["Complete prototype"],
        blockers=[],
    )

    result = analyze_project_update(project)

    assert result["project_name"] == "AI Project Manager Copilot"
    assert result["status"] == "Building"
    assert "Requirements may change" in result["risks"]
    assert "Complete prototype" in result["actions"]
    assert result["blockers"] == []
def test_build_project_context():
    project = ProjectUpdate(
        project_name="AI Project Manager Copilot",
        status="Building",
        risks=["Requirements may change"],
        actions=["Complete prototype"],
        blockers=[],
    )

    context = build_project_context(project)

    assert "AI Project Manager Copilot" in context
    assert "Building" in context
    assert "Requirements may change" in context
    assert "Complete prototype" in context
    assert "Blockers:" in context
