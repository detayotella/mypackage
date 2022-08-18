from setuptools import setup, find_packages


setup(
    name="mypackage",
    version="0.1",
    packages=find_packages(exclude=["test*"]),
    license="MIT",
    description="ESDA example python package",
    long_description=open("README.md").read(),
    install_requires=["numpy"],
    url="https:github.com/detayotella/mypackage.git",
    author="Adetayo Tella",
    author_email="tellaadetayo7@yahoo.com"
)