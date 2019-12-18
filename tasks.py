import sys
import time

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
def build(ctx):
    ctx.run("python setup.py build")


@task
def runGunicorn(ctx):
    ctx.run("gunicorn \"project.app:create_app()\" ")


@task(help={'port': "Port number that gunicorn will use when deploying the microservice. (Usable for Linux)"})
def runGunicornParams(ctx, port="5000"):
    if port == "DEFAULT":
        port = 5000
        ctx.run("gunicorn -b 0.0.0.0:%s \"project.app:create_app()\" " % port)
    else:
        ctx.run("gunicorn -b 0.0.0.0:%s \"project.app:create_app()\" " % port)


@task(help={'port': "Port number that gunicorn will use when deploying the microservice. (Usable for Linux)"})
def runGunicornCassandraParams(ctx, port="5000"):
    ctx.run("./apache-cassandra-3.11.4/bin/cassandra -R")
    # Wait for DB setup
    time.sleep(7)
    ctx.run("python project/scripts/Regenerator.py")
    # Wait for DB Regeneration
    time.sleep(3)
    if port == "DEFAULT":
        port = 5000
        ctx.run("gunicorn -b 0.0.0.0:%s \"project.CassandraLaunch:create_app()\" " % port)
    else:
        ctx.run("gunicorn -b 0.0.0.0:%s \"project.CassandraLaunch:create_app()\" " % port)


@task(help={'port': "Port number that waitress will use when deploying the microservice. (Usable for Windows)"})
def callWaitress(ctx, port="5000"):
    if port == "DEFAULT":
        port = 5000
        ctx.run("waitress-serve --port=%s project.app:app" % port)
    else:
        ctx.run("waitress-serve --port=%s project.app:app" % port)


@task(help={'port': "Port number that waitress will use when deploying the microservice. (Usable for Windows)"})
def callWaitressCassandra(ctx, port="5000"):
    if port == "DEFAULT":
        port = 5000
        ctx.run("waitress-serve --port=%s project.CassandraLaunch:app" % port)
    else:
        ctx.run("waitress-serve --port=%s project.CassandraLaunch:app" % port)


@task()
def regenerateDB(ctx):
    ctx.run("python project/scripts/Regenerator.py")
