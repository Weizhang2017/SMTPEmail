import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SMTPEmail",
    version="0.2",
    author="Zhang Wei",
    author_email="zhangw1.2011@gmail.com",
    description="send MIME message via SMTP server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Weizhang2017/SMTPEmail",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)