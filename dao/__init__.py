import psycopg2

def conectardb():
    con = psycopg2.connect(host='dpg-cl5v0ps72pts73af17m0-a.oregon-postgres.render.com', database='my_app_db_d3aj',
    user='my_app_user', password='MedlZen0ZlU6owtyW4AAPPsGijPvgfi8')

    return con

def listarUsuarios(conexao):
    cur = conexao.cursor()
    cur.execute('select * from newtable')
    recset = cur.fetchall()
    conexao.close()
    return recset

def inserirDB(login, senha, nome, conexao):
    cur = conexao.cursor()

    exito = False
    try:
        sql = f"insert into newtable values ('{login}', '{senha}', '{nome}')"
        cur.execute(sql)
    except psycopg2.IntegrityError:
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True

    conexao.close()
    return exito