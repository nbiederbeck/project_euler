from setuptools import setup, find_packages

setup(
    name='Project_Euler',
    author='Noah Biederbeck',
    author_email='noah.biederbeck@tu-dortmund.de',
    description='Solutions for Project Euler',
    license='MIT',
    packages=find_packages(),
    # install_requires=[],
    # entry_points={},
    setup_requires=['pytest-runner'],
    test_requires=['pytest'],
)
