import nox


@nox.session()
def lint(session):
    session.install("-r", "requirements-dev.txt")
    session.run("black", "modelkit_imdb", "tests", "--check")
    session.run("isort", "--profile", "black", "modelkit_imdb", "tests", "--check-only")
    session.run("flake8", "modelkit_imdb", "tests")
    session.run("mypy", "modelkit_imdb")


@nox.session()
def test(session):
    session.install("-r", "requirements-dev.txt")
    session.run("pytest")


@nox.session()
def coverage(session):
    session.install("-r", "requirements-dev.txt")

    session.run("coverage", "run", "-m", "pytest", "--junitxml=junit.xml")
    session.run("coverage", "report", "-m")
    session.run("coverage", "xml")
    session.run("coverage", "html", "-d", "docs/coverage")

    # Generate README badges using genbadge, junit.xml and coverage.xml
    session.install("genbadge[coverage,tests]")
    session.run(
        "genbadge",
        "coverage",
        "-i",
        "coverage.xml",
        "-o",
        "docs/badges/coverage.svg",
    )
    session.run("genbadge", "tests", "-i", "junit.xml", "-o", "docs/badges/tests.svg")
