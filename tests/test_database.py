DEFAULT_PROJECT = "api"


def test_default_postgres(cookies):
    result = cookies.bake()

    assert (result.project / "docker-compose.yml").exists()

    with open(result.project / "contrib" / "env-sample") as f:
        assert "DATABASE_URL=postgres://api:p4ssw0rd@localhost:5432/api" in f.read()

    with open(result.project / ".env") as f:
        assert "DATABASE_URL=postgres://api:p4ssw0rd@localhost:5432/api" in f.read()


def test_sqlite(cookies):
    result = cookies.bake(extra_context={"database": "SQLite"})

    assert not (result.project / "docker-compose.yml").exists()

    with open(result.project / "contrib" / "env-sample") as f:
        assert "DATABASE_URL=sqlite:///db.sqlite3" in f.read()

    with open(result.project / ".env") as f:
        assert "DATABASE_URL=sqlite:///db.sqlite3" in f.read()
