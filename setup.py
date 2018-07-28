"""Setup for pytest-hammertime plugin."""

from setuptools import setup

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='pytest-hammertime',
    version='1.1.1',
    description='Display "🔨 " instead of "." for passed pytest tests.',
    url='https://github.com/zhammer/pytest-hammertime',
    author='Zach Hammer',
    author_email='zach.the.hammer@gmail.com',
    license='MIT License',
    py_modules=['pytest_hammertime'],
    install_requires=['pytest'],
    entry_points={'pytest11': ['hammertime = pytest_hammertime', ], },
    long_description=long_description,
    long_description_content_type='text/markdown'
)
