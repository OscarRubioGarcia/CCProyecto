
import sys

from invoke import task


@task
def clean(ctx):
    print("Test clean task!")


@task
def testAll(ctx):
    ctx.run("python -m unittest discover tests")


@task
def build(ctx):
    ctx.run("python setup.py build")
