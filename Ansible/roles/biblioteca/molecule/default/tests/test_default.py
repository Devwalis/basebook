from pathlib import Path


APP_DIR = Path("/tmp/sistema-biblioteca")
VENV_DIR = APP_DIR / "venv"


def test_diretorio_da_aplicacao_existe(host):
    app_dir = host.file(str(APP_DIR))
    assert app_dir.exists
    assert app_dir.is_directory


def test_ambiente_virtual_foi_criado(host):
    assert host.file(str(VENV_DIR)).exists
    assert host.file(str(VENV_DIR)).is_directory


def test_python_do_ambiente_virtual_existe(host):
    python = host.file(str(VENV_DIR / "bin/python"))
    assert python.exists
    assert python.is_file
    assert python.is_executable


def test_requirements_foi_copiado(host):
    requirements = host.file(str(APP_DIR / "requirements.txt"))
    assert requirements.exists
    assert requirements.is_file


def test_pacote_da_aplicacao_foi_copiado(host):
    pacote = host.file(str(APP_DIR / "biblioteca"))
    assert pacote.exists
    assert pacote.is_directory


def test_pasta_de_testes_foi_copiada(host):
    tests = host.file(str(APP_DIR / "tests"))
    assert tests.exists
    assert tests.is_directory
