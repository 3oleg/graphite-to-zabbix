#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='graphite-to-zabbix',
      version = '0.3',
      description = 'This tool allow handle alerts based on graphite metrics. It works as a proxy between graphite and zabbix. It use graphite as data source and zabbix as an alerting system.',
      author = 'tgavriltg',
      author_email = 'tgavriltg@gmail.com',
      url = 'https://github.com/tgavriltg/graphite-to-zabbix',
      install_requires = ["argparse","py-zabbix","PyYAML"],
      scripts = ['g2zproxy'],
      packages = find_packages(),
     )
