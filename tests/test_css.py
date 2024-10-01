DEFAULT_PROJECT = "api"


def test_bootstrap(cookies):
    result = cookies.bake(extra_context={"css": "Bootstrap"})

    core_app_path = result.project / DEFAULT_PROJECT / "core"
    assert (result.project / DEFAULT_PROJECT / "static" / "bootstrap.min.css").exists()
    assert (result.project / DEFAULT_PROJECT / "static" / "bootstrap.min.js").exists()

    with open(core_app_path / "templates" / "base.html") as f:
        content = f.read()
        assert (
            '<link href="{% static \'bootstrap.min.css\' %}" rel="stylesheet" async>'
            in content
        )
        assert (
            "<script src=\"{% static 'bootstrap.min.js' %}\" defer></script>" in content
        )


def test_no(cookies):
    result = cookies.bake(extra_context={"css": "No"})

    core_app_path = result.project / DEFAULT_PROJECT / "core"
    assert not (
        result.project / DEFAULT_PROJECT / "static" / "bootstrap.min.css"
    ).exists()
    assert not (
        result.project / DEFAULT_PROJECT / "static" / "bootstrap.min.js"
    ).exists()

    with open(core_app_path / "templates" / "base.html") as f:
        content = f.read()
        assert "bootstrap.min.css" not in content
        assert "bootstrap.min.js" not in content
