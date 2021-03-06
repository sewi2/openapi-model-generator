import os
import re

from setuptools import setup, find_packages

dependency_links = []
dependency_links_pattern = re.compile(r".*(?P<url>https?://[^\s]+)")

with open('README.md') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = [
        line.rstrip(f'{os.linesep}') for line in f.readlines()
        if line and not line.startswith(('#', '-e', 'git+'))
    ]

with open('requirements.txt') as f:
    for line in f.readlines():
        matched = dependency_links_pattern.match(line)
        if matched:
            dependency_links.append(matched.group("url"))

with open('VERSION') as version_file:
    version = version_file.read().strip()

setup(
    name='openapi_model_generator',
    packages=find_packages(),
    version=version,
    url='https://github.com/sewi2/openapi-model-generator',
    download_url='https://github.com/sewi2/openapi-model-generator/archive/refs/tags/0.1.15.tar.gz',
    license='MIT',
    description='This library allows us to generate django models and drf serializers using an OpenAPI schema',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Dmitry Nikolaev',
    author_email='sewi0018@gmail.com',
    keywords=['openapi', 'models', 'serializers', 'generator', ],
    install_requires=requirements,
    dependency_links=dependency_links,
    include_package_data=True,
    python_requires='~=3.6',
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
