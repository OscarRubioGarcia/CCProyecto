
import sys

from invoke import task


@task
def clean():
    print("Test clean task!")
	
@task
def build(clean=False):
    if clean:
        print("Clean before build!")
    print("Test build task!")
	
@task
def testNoticias(ctx):
    sys.argv.pop()
    main()
	
def main():
    import tests.testNoticiasModel
    import unittest
    unittest.main(module='tests.testNoticiasModel')

if __name__ == '__main__':
    main()

