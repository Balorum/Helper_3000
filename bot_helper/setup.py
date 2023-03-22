from setuptools import setup, find_namespace_packages

setup(
    name="Helper3000",
    version="3",
    description="Joint project 'Bot Assistant'",
    url="https://github.com/Balorum/Helper_3000",
    author="Pypeople",
    author_email="",
    license="MIT",
    packages=find_namespace_packages(),
    entry_points={"console_scripts": ["Helper3000 = bot_helper.Bot:main"]},
    install_requires=[
        "colorama",
    ],
)
