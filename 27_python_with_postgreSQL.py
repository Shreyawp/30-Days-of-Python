# Day 27: 30 Days of python programming

## Python with PostgreSQL

# open pgadmin and create new database 'demo'
# note the hostname, username, port_id, password of database to establish connection

## Install psycopg2 in terminal 
# >> pip install psycopg2

import psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'demo'
username = 'postgres'
pwd = 'testing#1'
port_id = 5432
conn = None
## Not required if using with clause
# cur = None

try:
    with psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    ) as conn:

        # dictionary cursor added to view record using key names
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            # excutes the defined SQL script
            cur.execute('DROP TABLE IF EXISTS employee')

            # the records manipulated here are visible in pgadmin too.

            # script to create new table
            create_script = ''' CREATE TABLE employee (
                                    id int PRIMARY KEY,
                                    name varchar(40) NOT NULL,
                                    salary int,
                                    dept_id varchar(30)
                                )
                            '''

            cur.execute(create_script)

            # insert values to table employee
            insert_script = 'INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s, %s)'
            insert_values = [(1, 'James', 12000, 'D1'), (2, 'Robin', 15000, 'D1'), (3, 'Xavier', 20000, 'D1')]
            
            # insert each record tuuple from given list
            for record in insert_values:
                cur.execute(insert_script, record)

            # update the salry column of each employee
            update_script = 'UPDATE employee SET salary = salary + (salary * 0.5)'
            cur.execute(update_script)

            # delete one record from table
            delete_script = 'DELETE FROM employee WHERE name = %s'
            delete_record = ('James',)
            cur.execute(delete_script, delete_record)

            # execute SQL command to display record 
            cur.execute('SELECT * FROM employee')

            # to display record in terminal
            # cur.fetchall()

            # display each record in terminal on new line using dictionary keys
            for record in cur.fetchall():
                print(record['name'], record['salary'])

            ## with clause take care of commit, if there are no exceptions
            # commits changes that are updated in PostgreSQL
            # conn.commit()

except Exception as error:
    print(error)
finally:
    ## cursor will close while using with clause
    # if cur is not None:
    #     cur.close()
    ## need to manually close connections
    if conn is not None:
        conn.close()
