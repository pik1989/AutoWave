from setuptools import setup,find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]


setup(name="AutoWave",
version="0.1",
description="Package contains functionality for speech analysis",
long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read() ,
url='',  
author='Satyajit Pattnaik , Kalash Jindal, Nilesh Verma',
author_email='pattnaiksatyajit89@gmail.com , jindalkalash298@gmail.com, me@nileshverma.com‎',
license='MIT', 
classifiers=classifiers,
keywords='Speech',
packages=['AutoWave'],
install_requires=["pydub","librosa","soundfile","numpy","matplotlib","scipy","datetime"]
)