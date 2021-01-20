import psycopg2


connection = psycopg2.connect(
      database = 'exampale', 
      user = 'postgres', 
      password = 12345, 
      port = 5432 ,
      host = 'localhost' 
      )

cursor = connection.cursor()

cursor.execute ('''
  CREATE TABLE table2 (
      id INTEGER PRIMARY KEY,
      completed BOOLEAN NOT NULL DEFAULT False
  );

''')
cursor.execute ('INSERT INTO table2 (id, completed) VALUES (1, true);')

connection.commit()

connection.close()
cursor.close()
print("connected ")

