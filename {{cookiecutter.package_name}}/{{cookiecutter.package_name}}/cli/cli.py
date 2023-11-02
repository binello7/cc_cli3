#!/usr/bin/env python3

import click

from {{ cookiecutter.package_name }}.cli.group1 import commands as group1
from {{ cookiecutter.package_name }}.cli.group2 import commands as group2

# Click setup
context_settings = {'help_option_names': ['-h', '--help']}
@click.group(context_settings=context_settings)
#-------------------------------------------------------------------------------

# Main functions
def main():
    '''
    My CLI-tool.
    '''

main.add_command(group1.grp1)
main.add_command(group2.grp2)
#-------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
