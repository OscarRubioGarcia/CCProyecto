
import sys

from invoke import task


@task
def clean():
    print("Test clean task!")
	
@task
def build(ctx):
    ctx.run("pip install -r requirements.txt")
	
@task
def testAll(ctx):
    ctx.run("python -m unittest discover tests")
    
@task
def testNoticiasModel(ctx):
    sys.argv.pop()
    main()
	
def main():
    import tests.testNoticiasModel
    import unittest
    unittest.main(module='tests.testNoticiasModel')

if __name__ == '__main__':
    main()

