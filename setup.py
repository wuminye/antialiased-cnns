from setuptools import setup, find_packages

setup(
	name='models_lpf',
	version='0.0.1',
	packages=find_packages(exclude=["weights"]),
	license='MIT'
)