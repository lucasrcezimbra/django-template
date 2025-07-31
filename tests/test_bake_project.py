DEFAULT_PROJECT = "api"


def test_bake_with_defaults(cookies):
    result = cookies.bake()

    assert result.project.isdir()
    assert result.exit_code == 0
    assert result.exception is None

    found_toplevel_files = {f.basename for f in result.project.listdir()}
    assert "pyproject.toml" in found_toplevel_files
    assert "api" in found_toplevel_files


def test_github_username(cookies):
    result = cookies.bake(extra_context={"github_username": "my_custom_username"})

    with open(result.project / "README.md") as f:
        assert "git clone git@github.com:my_custom_username/api.git" in f.read()


def test_makefile_has_update_template_command(cookies):
    result = cookies.bake()

    assert result.project.isdir()
    assert result.exit_code == 0

    makefile_path = result.project / "Makefile"
    assert makefile_path.isfile()

    with open(makefile_path) as f:
        makefile_content = f.read()
        assert "update-template:" in makefile_content
        assert "cruft update --skip-apply-ask" in makefile_content
        assert "update-template" in makefile_content.split(".PHONY:")[1].split("\n")[0]
