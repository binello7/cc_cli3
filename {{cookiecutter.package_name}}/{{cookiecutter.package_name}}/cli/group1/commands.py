import click

context_settings = {
    'help_option_names': ['-h', '--help'],
    'show_default': True
}

# Command Group
@click.group(name='grp1', context_settings=context_settings)
def grp1():
    '''
    Description group 1.
    '''
    pass
#===============================================================================

# Command 1
@grp1.command(
    name='command1',
    help='Help command1.',
    context_settings=context_settings
)
@click.option('-a',
    required=True,
    type=str,
    help='Help -a.'
)
@click.option('-b',
    type=int,
    default=1,
    help='Help -b'
)

def command1():
    '''
    Description command 1.
    '''
    pass
#-------------------------------------------------------------------------------

# Command 2
@grp1.command(
    name='command2',
    help='Help command2.',
    context_settings=context_settings
)
@click.option('-a',
    required=True,
    type=str,
    help='Help -a.'
)
@click.option('-b',
    type=int,
    default=1,
    help='Help -b'
)

def command2():
    '''
    Description command 2.
    '''
    pass
#-------------------------------------------------------------------------------
