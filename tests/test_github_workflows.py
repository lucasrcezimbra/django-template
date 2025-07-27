import os
import yaml


def test_trigger_child_projects_workflow_exists():
    """Test that the trigger child projects workflow file exists."""
    workflow_path = ".github/workflows/trigger-child-projects.yml"
    assert os.path.exists(workflow_path), f"Workflow file {workflow_path} does not exist"


def test_trigger_child_projects_workflow_structure():
    """Test that the trigger child projects workflow has correct structure."""
    workflow_path = ".github/workflows/trigger-child-projects.yml"
    
    with open(workflow_path, 'r') as f:
        workflow = yaml.safe_load(f)
    
    # Test basic structure
    assert workflow['name'] == 'Trigger Child Projects'
    assert 'on' in workflow
    assert 'release' in workflow['on']
    assert workflow['on']['release']['types'] == ['published']
    
    # Test jobs structure
    assert 'jobs' in workflow
    assert 'trigger-child-projects' in workflow['jobs']
    
    job = workflow['jobs']['trigger-child-projects']
    assert job['runs-on'] == 'ubuntu-latest'
    assert 'steps' in job
    assert len(job['steps']) == 1
    
    # Test step structure
    step = job['steps'][0]
    assert 'name' in step
    assert step['name'] == 'Trigger child projects to update with cruft'
    assert 'run' in step


def test_workflow_contains_repository_dispatch():
    """Test that the workflow contains repository dispatch logic."""
    workflow_path = ".github/workflows/trigger-child-projects.yml"
    
    with open(workflow_path, 'r') as f:
        content = f.read()
    
    # Check for key components
    assert 'repository_dispatch' in content or 'dispatches' in content
    assert 'cruft_update' in content
    assert 'CHILD_REPOSITORIES' in content
    assert 'CHILD_PROJECTS_TOKEN' in content