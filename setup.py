from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["Flask", "coverage", "Flask-Injector", "Flask-RESTful", "gunicorn", "invoke",
                "waitress", "cassandra-driver"]

setup(
    name="campusDashboard",
    version="3.0.0",
    author="Oscar Rubio Garcia",
    description="Campus dashboard web service",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/OscarRubioGarcia/CCProyecto",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)