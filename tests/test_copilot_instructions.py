"""Test for copilot-instructions.md file."""

import os


def test_copilot_instructions_exists():
    """Test that copilot-instructions.md file exists."""
    copilot_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "copilot-instructions.md")
    assert os.path.exists(copilot_file), "copilot-instructions.md file should exist"


def test_copilot_instructions_content():
    """Test that copilot-instructions.md contains key sections."""
    copilot_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "copilot-instructions.md")
    
    with open(copilot_file, 'r') as f:
        content = f.read()
    
    # Check for key sections
    assert "Project Overview" in content
    assert "Cookiecutter template" in content
    assert "Template Variables" in content
    assert "cookiecutter.json" in content
    assert "Testing Commands" in content
    assert "Development Guidelines" in content