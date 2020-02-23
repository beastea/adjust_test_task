from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='randomizer',
    version='0.0.1',
    author="Anatoly Lebedev",
    author_email='beastea@gmail.com',
    description='A small package that returns string of randomized numbers from 1 to 10',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/beastea/adjust_test_task",
    packages=['randomizer'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    entry_points={
        'console_scripts': [
            'randomizer = randomizer.__main__:main'
        ]
    },
)
