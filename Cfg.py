#!/usr/bin/env python

"""Cfg.py

Usage:
    Cfg.py [(-v|--verbose)] <arg>...
    Cfg.py (-h | --help)
    Cfg.py (--version)

Options:
    -v, --verbose                   Show execution details [default: False]
    -h --help                       Show this screen
    --version                       Show version

Example:
    ./Cfg.py -v Cfg.html.

Author: Jonathan D. Lettvin
LinkedIn: jlettvin
Date: 20141020
"""


from sys import (argv, path)
path.append('Dict')

from Dict import (Dict)
from pprint import (pprint)
from bs4 import (BeautifulSoup)

class Cfg(Dict):

    def __init__(self, **kw):
        argv = Dict(**kw)
        for arg in argv.arg:
            with open(arg) as source:
                soup = BeautifulSoup(source)
                print soup.prettify()
        """
        name = []
        self.section = []
        self.info = {}
        for arg in argv.arg:
            with open(arg) as source:
                self.lines = []
                for line in source.readlines():
                    line = line.strip()
                    if line and not line.startswith('#'):
                        self.lines += [line, ]
                for line in self.lines:
                    num = 0
                    while line[0] == '=' and line[-1] == '=':
                        num += 1
                        line = line[1:-1]
                    line = line.strip()
                    if num:
                        index = num - 1
                        N = len(self.section)
                        if N < num:
                            self.section += ['', ]
                            N += 1
                        assert N >= num, 'section jump > 1 forbidden'
                        self.section = self.section[:num]
                        self.section[index] = line
                    info = self.info
                    for section in self.section:
                        info[section] = self.info.get(section, {})
                        info = info[section]
                    if not num:
                        if info.has_key('text'):
                            info['text'] += '\n' + line
                        else:
                            info['text'] = line
                        print info['text']
                        print
                        #info['text'] = info.get('text', '') + '\n' + line
                    #print 'info: ', self.info
                pprint(self.info)
                print arg
        """
        print self

if __name__ == "__main__":
    from docopt import (docopt)

    kwargs = docopt(__doc__, version="0.0.1")
    cfg = Cfg(**kwargs)
