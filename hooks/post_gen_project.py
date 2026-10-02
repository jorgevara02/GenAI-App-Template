import subprocess
from pathlib import Path

UV_INIT_OPTIONS = [
    "--bare",
    "--package",
    "--name",
    "{{ cookiecutter.project_slug }}",
    "--description",
    "{{ cookiecutter.description }}",
    "--python",
    "{{ cookiecutter.python_version }}",
    "--vcs",
    "git",
]

DEPENDENCIES = [
    "langchain",
    "langchain-openai",
    "python-dotenv",
]

BUILD_BACKEND_CONFIG = """
[tool.uv.build-backend]
module-name = "src"
module-root = ""
"""


def init_uv_project() -> None:
    subprocess.run(["uv", "init", ".", *UV_INIT_OPTIONS], check=True)


def pin_python_version() -> None:
    subprocess.run(
        ["uv", "python", "pin", "{{ cookiecutter.python_version }}"], check=True
    )


def configure_src_module() -> None:
    """Use the `src` directory itself as the importable package (`import src`)."""
    with Path("pyproject.toml").open("a", encoding="utf-8") as f:
        f.write(BUILD_BACKEND_CONFIG)


def add_dependencies() -> None:
    subprocess.run(["uv", "add", *DEPENDENCIES], check=True)


def main() -> None:
    init_uv_project()
    pin_python_version()
    configure_src_module()
    add_dependencies()


if __name__ == "__main__":
    main()
