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
        ctx.run("gunicorn -b 127.0.0.1:%s \"project.app:create_app()\" " % port)
    else:
        ctx.run("gunicorn -b 127.0.0.1:%s \"project.app:create_app()\" " % port)


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


@task(help={'port': "Port number that gunicorn will use when deploying the microservice. (Usable for Linux)"})
def runGunicornAsyncParams(ctx, port="5000"):
    ctx.run("python project/scripts/Regenerator.py")
    time.sleep(3)
    if port == "DEFAULT":
        port = 5000
        # --workers=5 --threads=2
        # --worker-class gevent --workers=3
        ctx.run("gunicorn -b 0.0.0.0:%s --workers=5 --threads=25 \"project.CassandraLaunch:create_app()\" " % port)
    else:
        ctx.run("gunicorn -b 0.0.0.0:%s --workers=5 --threads=25 \"project.CassandraLaunch:create_app()\" " % port)


@task(help={'port': "Port number that waitress will use when deploying the microservice. (Usable for Windows)"})
def callWaitress(ctx, port="5000"):
    if port == "DEFAULT":
        port = 5000
        ctx.run("waitress-serve --port=%s project.app:app" % port)
    else:
        ctx.run("waitress-serve --port=%s project.app:app" % port)


@task(help={'port': "Port number that waitress will use when deploying the microservice. (Usable for Windows)"})
def callWaitressCassandra(ctx, port="5000"):
    ctx.run("python project/scripts/Regenerator.py")
    # Wait for DB Regeneration
    time.sleep(3)
    if port == "DEFAULT":
        port = 5000
        ctx.run("waitress-serve --port=%s --threads=25 project.CassandraLaunch:app" % port)
    else:
        ctx.run("waitress-serve --port=%s --threads=25 project.CassandraLaunch:app" % port)

# ------------------------------------------Service Commments Tasks----------------------------------------------------


@task(help={'port': "Port number that waitress will use when deploying the microservice comments. "
                    "(Usable for Windows)"})
def callWaitressCassandraComments(ctx, port="5050"):
    ctx.run("python project2/scripts/Regenerator.py")
    # Wait for DB Regeneration
    time.sleep(4)
    if port == "DEFAULT":
        port = 5050
        ctx.run("waitress-serve --port=%s --threads=25 project2.CassandraLaunchComments:app" % port)
    else:
        ctx.run("waitress-serve --port=%s --threads=25 project2.CassandraLaunchComments:app" % port)


@task(help={'port': "Port number that gunicorn will use when deploying the microservice comments. "
                    "(Usable for Linux)"})
def runGunicornAsyncParamsComments(ctx, port="5050"):
    if port == "DEFAULT":
        port = 5050
        ctx.run("gunicorn -b 0.0.0.0:%s --workers=5 --threads=25 \"project2.CassandraLaunchComments:create_app()\" " % port)
    else:
        ctx.run("gunicorn -b 0.0.0.0:%s --workers=5 --threads=25 \"project2.CassandraLaunchComments:create_app()\" " % port)


@task()
def regenerateCassandra(ctx):
    ctx.run("python project2/scripts/Regenerator.py")
    ctx.run("python project/scripts/Regenerator.py")
