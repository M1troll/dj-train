# Installing project for developing on local PC

You have to have the following tools installed prior initializing the project:

* [pyenv](https://github.com/pyenv/pyenv)
* [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

## Python interpreter

Currently, we're using `python 3.11`

The simplest way to configure proper Python version and virtual environment
is using [`pyenv`](https://github.com/pyenv/pyenv) and [`pyenv-virtualenv`](https://github.com/pyenv/pyenv-virtualenv).

### Prepare python env using pyenv-virtualenv

1. 
2. reate separate python virtual environment:

```bash
pyenv virtualenv-delete --force dj-train
pyenv install 3.11 --skip-existing
pyenv virtualenv `pyenv latest 3.11` dj-train
pyenv local dj-train
pyenv shell dj-train
```

2. Set up packages for using `invoke`

```bash
pip install -r requirements/local_build.txt
```

3. Start project initialization that will set up docker containers, python/system env:

```bash
inv project.init
```

4. Set environment variables

```bash
inv secrets.create-env
```

Open `.env` file in `config/settings/` dir and set values for variables.

`P.S.` In future it will be replaced on downloading credentials from cloud.

5. Run server for check that project is ready for work:

```bash
inv django.run
```
