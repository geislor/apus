# -*-coding:utf-8-*-

import sqlite3
from .settings import PACKAGE_DIR, DATABASE_NAME, USERNAME, FIRST_NAME, \
    LAST_NAME, EMAIL


def db_create():
    conn = sqlite3.connect("{}/{}".format(PACKAGE_DIR, DATABASE_NAME))
    cursor = conn.cursor()

    # cria tabela de usuários
    cursor.execute("""CREATE TABLE users
                     (username TEXT,
                     first_name TEXT,
                     last_name TEXT,
                     email TEXT)
                  """)

    # Adiciona dados do usuário primário
    cursor.execute(
        "INSERT INTO users VALUES ("
        "'geislor', "
        "'Geislor', "
        "'Crestani', "
        "'geislor@gmail.com')"
    )
    conn.commit()
    return "Database: {} - Craida com sucesso!".format(DATABASE_NAME)
