from project_copilot import ProjectUpdate, analyze_project_update


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
