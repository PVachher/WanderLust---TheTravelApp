def creatingdb():
    import sqlite3
    conn = sqlite3.connect('vr.db')
    print "Opened database successfully";

    conn.execute('''CREATE TABLE exp
           (location CHAR(40)     NOT NULL,
           lat           CHAR(50)   PRIMARY KEY NOT NULL,
           long           CHAR(50)    NOT NULL,
           name           CHAR(50)    NOT NULL);''')
    print "Table created successfully";

    conn.close()
#creatingdb()


def adding(location,lat,long,name):
    import sqlite3

    conn = sqlite3.connect('vr.db')
    print "Opened database successfully";

    conn.execute("INSERT INTO exp (location,lat,long,name) \
          VALUES ('%s','%s','%s','%s')" % (location,lat,long,name));

    conn.commit()
    print "Records created successfully";
    conn.close()
'''
adding("New Delhi",'28.5240097','77.1854019','Qutab Minar')
adding("New Delhi",'28.6131894','77.2300824','India Gate')
adding("New Delhi",'28.6506941','77.2334528','Jama Masjid')
adding("New Delhi",'28.592915','77.2509268','Humanyuns Tomb')
adding("Mumbai",'18.9220194','72.8336444','Gateway of India')
adding("Mumbai",'19.06014','72.859686','NSE')
adding("Mumbai",'18.9255776','72.8182172','Sea')
adding("Bangalore",'12.9981903','77.5924588','Bangalore Palace')
adding("Bangalore",'12.981084','77.588659','Vidhana Soudha')
adding("Bangalore",'12.9733686','77.5947923','City')
adding("Bangalore",'12.8257278','77.5094782','Art Of Living Yoga and Meditation Centre')
adding("Bangalore",'12.972255','77.5959578','UB CITY')
adding("Kolkata",'22.5342525','88.3756546','Tijala')
adding("Kolkata",'22.5333333','88.3333333','Victoria Memorial')
adding("Kolkata",'22.571358','88.423333','Nicco Park')
adding("Kolkata",'22.50332','88.376367','Howrah Bridge')
adding("Agra",'27.173441','78.0423877','Taj Mahal')
adding("Agra",'27.1969689','78.0332608','Fatehpur Sikhri')
adding("Agra",'27.1789494','78.0218813','Diwan-e-Aam')
adding("Pondichery",'11.9311231','79.8359168','Rocky Beach')
adding("Vishakapatnam",'17.7286454','83.3202362','City')
adding("Chennai",'13.0551433','80.2416042','Valluvar Kottam')
adding("Chennai",'12.9791916','80.219289','Sai Sarovar')
adding("Jaipur",'26.9245377','75.8212255','City')
adding("Shimla",'31.1028958','77.14113','Viceroy Lodge')
adding("Shimla",'31.1021866','77.1534634','City')
adding("Mizoram",'23.6983294','92.6052838','Reiek')
adding("Mussoorie",'30.4669358','78.0949869','New Laal Tibba')
adding("Mussoorie",'30.4333333','78.0833333','Jaypee Residency Manor')
adding("Goa",'15.0532139','73.9797978','Agonda Beach')
'''
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

def getdata(location):
    location = location[:-4]
    print 'DATA NEEDED FOR', location
    import sqlite3
    conn = sqlite3.connect('vr.db')
    cursor = conn.execute("SELECT * FROM exp WHERE location = '%s'" % (location))
    r = []
    for k in cursor:
        r.append(k)
        print k
    return r
    conn.close()
#getdata('New Delhi')

#adding('pv','prateek','vachher','welcome','100','abc@gmail.com')
#print getname('pv')