import sys

from invoke import task


@task
def active(ctx):
    print("Invoke is Active!")


@task
def testAll(ctx):
    ctx.run("python -m unittest discover project/tests")


@task
def testNewsManual(ctx):
    ctx.run(
        "python -m unittest project/tests/testNoticiasModel.py project/tests/test_gestornoticias.py project/tests/test_api.py")


@task
def testAllCoverageManual(ctx):
    ctx.run(
        "coverage run -m unittest project/tests/testNoticiasModel.py project/tests/test_gestornoticias.py project/tests/test_api.py")


@task
def testNews(ctx):
    ctx.run("python -m unittest project/tests/testNoticiasModel.py project/tests/test_gestornoticias.py")


@task
def testNewsApi(ctx):
    ctx.run("python -m unittest project/tests/test_api.py")


@task
def runNews(ctx):
    ctx.run("python app.py")


@task
def build(ctx):
    ctx.run("python setup.py build")


@task
def runPython(ctx):
    ctx.run("python app.py")


@task
def runGunicorn(ctx):
    ctx.run("gunicorn -b 0.0.0.0:5000 app:api --reload")
