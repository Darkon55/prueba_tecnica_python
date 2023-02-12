import click

from options import commands as login_commands

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {};


cli.add_command(login_commands.all)