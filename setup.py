import setuptools


def _readme_from_file(filename):
    return open(filename).read()


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setuptools.setup(
    name="mo9mo9db",
    version="0.0.1",
    author="su-pleiades",
    author_email="su.impreza.itengineer@gmail.com",
    description="discord.guild[mo9mo9study]でDBと連携するために使用するモジュール",
    long_description=_readme_from_file('README.md'),
    long_description_content_type="text/markdown",
    url="https://github.com/cm-hirano-shigetoshi/python_sample_command",
    packages=setuptools.find_packages("mo9mo9db",
                                      exclude=['.env*']),
    python_requires='>=3.7',
    install_requires=_requires_from_file('requirements.txt'),
)
