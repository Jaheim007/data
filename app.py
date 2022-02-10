import sqlite3

conn  = sqlite3.connect("database.db")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS informations(   
        nom text,
        prenom text,
        email text, 
        mdp text, 
        confirm text 
    )""")

d = {"nom": "Kouaho" , "prenom" : "Jaheim" , "email":"jaheimkouaho@gmail.com", "mdp":"hj", "confirm":"hj"}
c.execute("INSERT INTO informations VALUES(:nom, :prenom, :email, :mdp, :confirm)", d)

c.execute("SELECT * FROM informations ")
donnes = c.fetchall()
print(donnes)


conn.commit()
conn.close()