#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


def requirements_reader(f_name):
    requirements = []
    trash_prefixies = ('#', '-r')
    with open(f_name) as requirements_file:
        for i in requirements_file.read().split():
            r = i.strip()
            if not r:
                continue
            for prefix in trash_prefixies:
                if r.startswith(prefix):
                    continue
        requirements.append(r)
    return requirements


with open('README.md') as readme_file:
    readme = readme_file.read()


requirements = requirements_reader('requirements.txt')
test_requirements = requirements_reader('requirements_dev.txt')


setup(
    name='login_counter',
    version='0.1.0',
    description="login counter test task",
    long_description=readme,
    author="Roman Bondar",
    author_email='rombr5@gmail.com',
    url='https://github.com/rombr/login-counter-test-task',
    packages=[
        'src/login_counter',
    ],
    package_dir={'src':
                 'login_counter'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='login_counter',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='src/tests',
    tests_require=test_requirements
)
