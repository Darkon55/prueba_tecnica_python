import click

from options.services import EdnpointService
from options.models import Endpoint

@click.group()
def login():
    """Tool to perform test with the "login" api"""
    pass


@login.command()
@click.option('-n', '--username',
            type=str,
            prompt=True,
            help='The user name')
@click.option('-p', '--password',
            type=str,
            prompt=True,
            help='The user password')
@click.option('-u', '--url',
            type=str,
            prompt=True,
            help='The user password')
@click.pass_context
def test(ctx, username, password, url):
    """Test login endpoint"""
    params = Endpoint(username, password, url)
    endpoint_service = EdnpointService(ctx)

    click.echo(endpoint_service.post_login(params).json())
    pass


all = login
