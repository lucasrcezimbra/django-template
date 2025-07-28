import yaml


def test_cruft_update_workflow_exists(cookies):
    """Test that the cruft update workflow is included in the generated project."""
    result = cookies.bake()

    assert result.exit_code == 0

    workflow_path = result.project_path / ".github" / "workflows" / "cruft-update.yml"
    assert workflow_path.exists()


def test_cruft_update_workflow_content(cookies):
    """Test that the cruft update workflow has the correct configuration."""
    result = cookies.bake()

    assert result.exit_code == 0

    workflow_path = result.project_path / ".github" / "workflows" / "cruft-update.yml"

    with open(workflow_path) as f:
        workflow = yaml.safe_load(f)

    # Check workflow name
    assert workflow["name"] == "Cruft Update"

    # Check triggers
    assert "schedule" in workflow["on"]
    assert "workflow_dispatch" in workflow["on"]

    # Check schedule (daily at 2 AM UTC)
    schedule = workflow["on"]["schedule"]
    assert len(schedule) == 1
    assert schedule[0]["cron"] == "0 2 * * *"

    # Check job exists
    assert "cruft-update" in workflow["jobs"]
    job = workflow["jobs"]["cruft-update"]

    # Check runner
    assert job["runs-on"] == "ubuntu-latest"

    # Check steps
    steps = job["steps"]
    step_names = [step["name"] for step in steps]

    expected_steps = [
        "Checkout repository",
        "Set up Python",
        "Install cruft",
        "Check for template updates",
        "Update template",
        "Create Pull Request",
    ]

    for expected_step in expected_steps:
        assert expected_step in step_names

    # Check that cruft update step has skip-apply-ask flag
    update_step = next(step for step in steps if step["name"] == "Update template")
    assert "cruft update --skip-apply-ask" in update_step["run"]

    # Check that PR creation uses peter-evans/create-pull-request
    pr_step = next(step for step in steps if step["name"] == "Create Pull Request")
    assert pr_step["uses"] == "peter-evans/create-pull-request@v6"
