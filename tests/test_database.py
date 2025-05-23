DEFAULT_PROJECT = "api"


def test_default_postgres(cookies):
    result = cookies.bake()

    assert (result.project / "docker-compose.yml").exists()

    with open(result.project / "contrib" / "env-sample") as f:
        assert "DATABASE_URL=postgres://api:p4ssw0rd@localhost:5432/api" in f.read()

    with open(result.project / ".env") as f:
        assert "DATABASE_URL=postgres://api:p4ssw0rd@localhost:5432/api" in f.read()

    with open(result.project / "pyproject.toml") as f:
        assert "psycopg" in f.read()

    with open(result.project / "README.md") as f:
        assert "docker compose up -d" in f.read()

    with open(result.project / "Makefile") as f:
        content = f.read()
        assert "docker compose up -d" in content


def test_sqlite(cookies):
    result = cookies.bake(extra_context={"database": "SQLite"})

    assert not (result.project / "docker-compose.yml").exists()

    with open(result.project / "contrib" / "env-sample") as f:
        assert "DATABASE_URL=sqlite:///db.sqlite3" in f.read()

    with open(result.project / ".env") as f:
        assert "DATABASE_URL=sqlite:///db.sqlite3" in f.read()

    with open(result.project / "pyproject.toml") as f:
        assert "psycopg" not in f.read()

    with open(result.project / "README.md") as f:
        assert "docker compose up -d" not in f.read()

    with open(result.project / "Makefile") as f:
        content = f.read()
        assert "docker compose up -d" not in content
