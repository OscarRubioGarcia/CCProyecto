
import sys

from invoke import task


@task
def active(ctx):
    print("Invoke is Active!")


@task
def testAll(ctx):
    ctx.run("python -m unittest discover tests")
    

@task
def testNews(ctx):
    ctx.run("python -m unittest tests/testNoticiasModel.py tests/test_gestornoticias.py")


@task
def testNewsApi(ctx):
    ctx.run("python -m unittest tests/test_api.py")


@task
def build(ctx):
    ctx.run("python setup.py build")
