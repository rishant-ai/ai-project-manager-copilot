from src.project_copilot import ProjectUpdate, analyze_project_update
from src.ai_workflow import build_project_context, extract_meeting_actions


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


def test_extract_meeting_actions():
    notes = """
    Rishant will complete the prototype by Friday.
    The team decided to use the current project structure.
    We will review progress next Monday.
    """

    result = extract_meeting_actions(notes)

    assert "action_items" in result
    assert "owners" in result
    assert "deadlines" in result
    assert "decisions" in result
    assert "follow_up_requirements" in result
