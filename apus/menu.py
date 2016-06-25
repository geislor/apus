# -*- coding:utf-8 -*-

import click
from .users.models import Users, session


@click.command()
@click.option('--user', help='Iniciar configurações: (createuser: Adiciona '
                             'novo usuário. ')
# @click.option('--count', default=1, help='number of greetings.')
# @click.option('--name', prompt='Your name', help='The person to greet.')
def general(user):
    """
    Hello!
    """

    if user == 'create':
        print("Criar novo usuário")
        username = input('username: ')
        email = input('email: ')
        user = Users(username=username, email=email)
        user.save()

    elif user == 'listall':
        print("Listagem de usuários: ")
        usu = session.query(Users)
        for i, u in enumerate(usu.all()):
            print(i, u)
        pass

