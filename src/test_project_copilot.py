from project_copilot import analyze_project_update


def test_analyze_project_update():
    result = analyze_project_update(
        project_name="AI Project Manager Copilot",
        status="Building",
        risks=["Requirements may change"],
        actions=["Complete prototype"],
        blockers=[],
    )

    assert result["project_name"] == "AI Project Manager Copilot"
    assert result["status"] == "Building"
    assert "Requirements may change" in result["risks"]
    assert "Complete prototype" in result["actions"]
    assert result["blockers"] == []
