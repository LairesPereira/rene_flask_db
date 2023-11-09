import psycopg2

con = psycopg2.connect(host='dpg-cl5v0ps72pts73af17m0-a.oregon-postgres.render.com', database='my_app_db_d3aj',
user='my_app_user', password='MedlZen0ZlU6owtyW4AAPPsGijPvgfi8')

cur = con.cursor()

sql = "insert into newtable values ('lairespsoares@gmail.com','mypassword', 2)"
cur.execute(sql)
con.commit()

con.close()
