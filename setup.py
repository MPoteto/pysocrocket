from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='pysocrocket',
  version='0.0.1',
  author='mpoteto',
  author_email='oleg.potetos@gmail.com',
  description='Неоффициальная API для SocRocket.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/MPoteto/pysocrocket',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='socrocket api ',
  project_urls={
    'GitHub': 'https://github.com/MPoteto/pysocrocket'
  },
  python_requires='>=3.6'
)
