#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 29.03.2021
# ----------------------------------------------------------------------------------------------------------------------
import argparse
import os
import re
import sys
import textwrap


def main():
    main_return_value = True
    # __________________________________________________________________________
    # command-line options, arguments
    try:
        # noinspection PyTypeChecker
        parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                         description=textwrap.dedent('''\
                                         Yet another alternative to envsubst.
                                         Substitutes the values of environment variables.
                                         By default, undefined variables are not substitute.'''))
        parser.add_argument('file', action='store', type=str,
                            metavar="<FILE>", help="Input file path")
        parser.add_argument("-f", "--fail", action='store_true', default=False,
                            help="exit with status code 1 if no environment variable is found")
        parser.add_argument("-u", "--undefined", action='store_true', default=False,
                            help="substitute undefined variables")
        args = parser.parse_args()  # <class 'argparse.Namespace'>
    except SystemExit:
        return False
    # __________________________________________________________________________
    re_variable = re.compile(r'(\${\w+}|\$\w+)+')
    with open(args.file) as f:
        for line in f:
            # print(line)
            # print(re_variable.findall(line))
            for x in set(re_variable.findall(line)):
                _tmp = re.sub(r'[\${}]', '', x)
                if args.undefined:
                    line = line.replace(x, os.getenv(_tmp, ''))
                else:
                    line = line.replace(x, os.getenv(_tmp, x))
                    if args.fail and os.getenv(_tmp) is None:
                        main_return_value = False
            # __________________________________________________________________
            sys.stdout.write(line)
            sys.stdout.flush()
    # __________________________________________________________________________
    return main_return_value


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
if __name__ == '__main__':
    sys.exit(not main())
