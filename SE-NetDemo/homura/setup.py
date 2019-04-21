from setuptools import setup, find_packages

with open("README.md", encoding='UTF-8') as f:
    readme = f.read()

with open("requirements.txt") as f:
    requirements = f.read().split()

setup(name="homura",
      version="0.5.3",
      author="moskomule",
      author_email="hataya@nlab.jp",
      packages=find_packages(exclude=["test", "docs", "examples"]),
      url="https://github.com/moskomule/homura",
      description="support tool for research experiments",
      long_description=readme,
      license="Apache License 2.0",
      install_requires=requirements,
      )
