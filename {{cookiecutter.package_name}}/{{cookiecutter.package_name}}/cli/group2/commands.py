import click

context_settings = {
    'help_option_names': ['-h', '--help'],
    'show_default': True
}

# Command Group
@click.group(name='grp2', context_settings=context_settings)
def grp2():
    '''
    Description group 2.
    '''
    pass
#===============================================================================

# Command 1
@grp2.command(
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
@grp2.command(
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
