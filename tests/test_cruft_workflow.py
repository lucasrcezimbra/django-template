def test_cruft_update_workflow_exists(cookies):
    """Test that the cruft update workflow is included in the generated project."""
    result = cookies.bake()

    assert result.exit_code == 0

    workflow_path = result.project_path / ".github" / "workflows" / "cruft-update.yml"
    assert workflow_path.exists()
