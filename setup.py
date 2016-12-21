#!/usr/bin/env python

from setuptools import setup, find_packages

SETUP = {
    'name': 'jujuplugins',
    'version': '0.0.0',
    'author': 'Juju Developers',
    'author_email': 'juju@lists.ubuntu.com',
    'description': 'Plugins for Juju command line client',
    'url': 'https://github.com/juju/plugins',
    'packages': find_packages(
        exclude=["setup.py"]),
    'scripts': [
        'juju-activate',
        'juju-clean',
        'juju-crashdump',
        'juju-debug',
        #'juju-debug-hooks-ext -> juju-dhx',  # TODO: make symlink
        'juju-dhx',
        'juju-flags',
        'juju-get-filter',
        'juju-git-charm',
        'juju-kill',
        #'juju-list',  # TODO: figure out where to put this non ascii bash script
        'juju-notify',
        'juju-notify-remote',
        'juju-pdb',
        'juju-pprint',
        'juju-public-ip',
        'juju-setall',
        'juju-set-all-the-things',
        'juju-sync-charm',
        'juju-sync-watch',
        'juju-unstick-upgrade',
        'juju-watch-status'
    ],
    'install_requires': ['PyYAML']
}

if __name__ == '__main__':
    setup(**SETUP)
