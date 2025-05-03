from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="meu_investimento-package",
    version="1.0.0",
    packages=find_packages(),
    description="Pacote para calcular o retorno de investimento em ações.",
    author="Aaron Lesbão Dumont",
    author_email="aarondmt@gmail.com",
    url="",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
