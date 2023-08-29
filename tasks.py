import inspect

# hack to support `invoke` for python 3.11
# https://github.com/pyinvoke/invoke/issues/833
if not hasattr(inspect, "getargspec"):
    inspect.getargspec = inspect.getfullargspec

from invoke.collection import Collection

from invocations import (
    django,
    git,
    linters,
    project,
    tests,
)

ns = Collection(
    django,
    git,
    linters,
    project,
    tests,
)

# Configurations for run command
ns.configure({"run": {"pty": True, "echo": True}})
