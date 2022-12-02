import os

from fabric.api import local
from fabric.context_managers import lcd


PROJECT_NAME = "my-first-blog"
PROJECT_PATH = f"/home/salvi/deploys/{PROJECT_NAME}"
REPO_URL = "https://github.com/SalvadorPR97/my-first-blog.git"
VENV_PYTHON = f'{PROJECT_PATH}/.venv/bin/python'
VENV_PIP = f'{PROJECT_PATH}/.venv/bin/pip'

def clone():
    print(f'cloning repo {REPO_URL}')
    
    if os.path.exists(PROJECT_PATH):
        print("project already exists")
    else:
        local(f'git clone {REPO_URL} {PROJECT_PATH}')


def create_env():
    print ("creating venv...")
    
    with lcd(PROJECT_PATH):
        local("python3 -m venv .venv")


def install_requirements():
    print("installing requirements.txt....")

    with lcd(PROJECT_PATH):
        local(f"{VENV_PIP} install -r requirements.txt ")


def django_makemigrations():
    print("creating django migrations....")

    with lcd(PROJECT_PATH):
        local(f"{VENV_PYTHON} manage.py makemigrations ")
      

def django_migrate():
    print("executing django migrations....")

    with lcd(PROJECT_PATH):
        local(f"{VENV_PYTHON} manage.py migrate ")


def django_loaddata():
    print("loading initial data...")

    with lcd(PROJECT_PATH):
        local(f"{VENV_PYTHON} manage.py loaddata db.json")
      

def django_runserver():
    print("runing server...")

    with lcd(PROJECT_PATH):
        local(f"{VENV_PYTHON} manage.py runserver")
      

def deploy():
    clone()
    create_env()
    install_requirements()
    django_makemigrations()
    django_migrate()
    django_loaddata()
    django_runserver()
