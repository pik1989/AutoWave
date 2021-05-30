from setuptools import setup,find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]


setup(name="PyAutoSpeech",
version="0.1",
description="Package contains functionality for speech analysis",
Long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
url='',  
author='Satyajit Pattnaik','Kalash Jindal'
author_email='pattnaiksatyajit89@gmail.com','jindalkalash298@gmail.com'
license='MIT', 
classifiers=classifiers,
keywords='Speech','audio' 
packages=['PyAutoSpeech'],find_packages(),
install_requires=["pydub",]
)