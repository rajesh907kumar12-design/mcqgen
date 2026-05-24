from setuptools import find_packages,setup

setup(
    name='meqgenrator',
    version='0.0.1',
    author='rajesh',
    author_email='rajesh907kumar12@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","pyPDF2"],
    packages=find_packages()
)