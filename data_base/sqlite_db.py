import sqlite3 as sql

base = sql.connect('vert_questions_base')
cur = base.cursor()


def sql_add_ARquestions():
    if base:
        print('Data base ARquestions connected!!')
    base.execute('CREATE TABLE IF NOT EXISTS ARquestions(namber TEXT PRIMARY KEY, ing TEXT, question TEXT)')
    base.commit()


def sql_add_INquestions():
    if base:
        print('Data base INquestions connected!!')
    base.execute('CREATE TABLE IF NOT EXISTS INquestions(namber TEXT PRIMARY KEY, ing TEXT, question TEXT)')
    base.commit()


def sql_add_answersAR():
    if base:
        print('Data base answers_Ar connected!!')
    base.execute('CREATE TABLE IF NOT EXISTS answers_Ar(name TEXT PRIMARY KEY, post TEXT, answers1 TEXT, answers2 TEXT)')
    base.commit()


def sql_add_answersIG():
    if base:
        print('Data base answers_IG connected!!')
    base.execute('CREATE TABLE IF NOT EXISTS answers_IG(name TEXT PRIMARY KEY, post TEXT, answers1 TEXT, answers2 TEXT)')
    base.commit()


async def sql_add_command_ARquestions(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO ARquestions VALUES (?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_add_command_INquestions(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO INquestions VALUES (?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_add_command_answersAR(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO answers_Ar VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_add_command_answersIG(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO answers_IG VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()