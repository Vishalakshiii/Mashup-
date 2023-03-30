from distutils.core import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name = 'Mashup-Vishalakshi-102017189',
  packages = ['Mashup-Vishalakshi-102017189'],
  version = '0.0.1',      
  license='MIT',        
  description = 'Mashup of songs of your favorite singer with a single click.',
  long_description=long_description,
  long_description_content_type='text/markdown',   
  author = 'Vishalakshi',                   
  author_email = 'vvishalakshi_be20@gmail.com',   
  install_requires=[           
          'pytube',
          'pydub',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
