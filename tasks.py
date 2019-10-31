from invoke import task

@task
def clean():
    print("Cleaning")

@task(clean)
def build(c):
    print("Building!")
    
@task
def deploy(c):
    print("deploy parameters")
    # c.run("python setup.py sdist")
    # c.run("twine upload dist/*")
    