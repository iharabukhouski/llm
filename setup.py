from setuptools import setup #, find_packages

setup(
  name='llm',
  version='0.0.1',
  packages=['llm'],
  # package_dir={"": "src"},
  # packages=find_packages(where="src"),
  install_requires=[
    'openai==1.61.0',
    'anthropic==0.45.2',
  ],
)
