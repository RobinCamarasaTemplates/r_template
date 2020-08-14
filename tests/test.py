"""
**Author** : Robin Camarasa

**Institution** : Erasmus MC

**Position** : PhD student

**Contact** : r.camarasa@erasmusmc.nl

**Date** : 2020-08-14

**Project** : r_template

**Test r_template project **

"""
import sys
import os
from datetime import datetime
import pytest
import shutil
from pathlib import Path
from cookiecutter import main
import subprocess


ROOT = Path(__file__).parents[1]
TESTS_ROOT = ROOT / 'test_output'
EXTRA_CONTEXT = {
    "project_name": "Awesome test",
    "description": "Description",
    "remote_url": "github.com",

    "author_name": "John Doe",
    "author_institution": "john.doe@lambda.com",
    "author_position": "Intern",
    "author_github": "https://github.com/JohnDoe"
}


def test_generate_project() -> None:
    """
    Test project generation

    :return: None
    """
    # Clean
    if TESTS_ROOT.exists():
        shutil.rmtree(TESTS_ROOT)
    TESTS_ROOT.mkdir()

    # Get path
    output_dir = TESTS_ROOT.resolve()

    # Launch project generation
    main.cookiecutter(
        str(ROOT),
        no_input=True,
        extra_context=EXTRA_CONTEXT,
        output_dir=output_dir
    )

    # Test project generation
    project_name = 'awesome-test'
    assert (TESTS_ROOT / project_name).exists()

    assert (TESTS_ROOT / project_name / 'data').exists()
    assert (TESTS_ROOT / project_name / 'data' / '.gitkeep').exists()
    assert (TESTS_ROOT / project_name / 'results').exists()
    assert (TESTS_ROOT / project_name / 'results' / '.gitkeep').exists()
    assert (TESTS_ROOT / project_name / 'src').exists()
    assert (TESTS_ROOT / project_name / 'src' / 'Makefile').exists()
    assert (TESTS_ROOT / project_name / 'src' / 'main.R').exists()
    assert (TESTS_ROOT / project_name / 'src' / 'functions.R').exists()
    assert (TESTS_ROOT / project_name / 'src' / 'functions.R').exists()
    assert (TESTS_ROOT / project_name / 'README.md').exists()

    process = subprocess.Popen(
        ['make'],
        cwd=(TESTS_ROOT / project_name / 'src')
    )
    process.wait()
    assert process.returncode == 0

