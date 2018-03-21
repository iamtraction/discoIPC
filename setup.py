from setuptools import setup, find_packages
from codecs import open

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='discoIPC',
    version='1.0.0',
    description='Connect to the local Discord IPC Socket, for features like Rich Presence.',
    long_description=readme,
    url='https://github.com/k3rn31p4nic/discoIPC',
    author='k3rn31p4nic',
    license='GPL-3.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    keywords='discord disco discoipc ipc rpc rich-presence presence activity wrapper library',
    packages=find_packages(),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
)
