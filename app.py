import sqlite3
conn  = sqlite3.connect("database.db")
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS informations
(
    nom text,
    prenom text,
    email text,
    mdp text,
    confirm mdp text,  
)
""")

d = {"nom":"Kouaho", "prenom":"Jaheim", "email":"jaheimkouaho@gmail.com", "mdp":"Jaheim2002", "confirm mdp":"Jaheim2002"}
c.execute("INSERT INTO informations VALUES(:nom, :prenom, :email, :mdp , :confirm mdp", d)

conn.commit()
conn.close()