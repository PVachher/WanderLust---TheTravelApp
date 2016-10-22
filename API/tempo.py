def creatingdb():
    import sqlite3
    conn = sqlite3.connect('user.db')
    print "Opened database successfully";

    conn.execute('''CREATE TABLE user
           (username CHAR(40) PRIMARY KEY     NOT NULL,
           firstname           CHAR(50)    NOT NULL,
           lastname           CHAR(50)    NOT NULL,
           password           CHAR(50)    NOT NULL,
           mobilenumber           CHAR(50)    NOT NULL,
           email           CHAR(50)    NOT NULL);''')
    print "Table created successfully";

    conn.close()

def adding(username,first,last,passw,mob,email):
    import sqlite3

    conn = sqlite3.connect('user.db')
    print "Opened database successfully";

    conn.execute("INSERT INTO user (username,firstname,lastname,password,mobilenumber,email) \
          VALUES ('%s','%s','%s','%s','%s','%s')" % (username.lower(),first,last,passw,mob,email));


    conn.commit()
    print "Records created successfully";
    conn.close()

def check(username,passw):
    import sqlite3
    conn = sqlite3.connect('user.db')
    print "Opened database successfully";

    cursor = conn.execute("SELECT password from user WHERE username='%s'"%(username))
    for k in cursor:
        if k[0] == passw:
            return True
        else:
            return False
    print "Operation done successfully";
    conn.close()

def getname(username):
    import sqlite3
    conn = sqlite3.connect('user.db')
    cursor = conn.execute("SELECT firstname FROM user WHERE username = '%s'" % (username.lower()))
    for k in cursor:
        return k[0]
    #print "Operation done successfully";
    conn.close()

def citydata():
    a = open('Data/wow.txt', 'r')
    z = []
    data = a.readlines()
    for k in data:
        z.append(k.split(',')[-1][:-1] + ', IN')
    return z


#adding('pv','prateek','vachher','welcome','100','abc@gmail.com')
#print getname('pv')