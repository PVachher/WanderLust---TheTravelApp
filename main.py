from flask import *
from modules import adding,check,getname,citydata,getdata
from random import *
from weather import coded
analytics1 = {}
for k in citydata():
    analytics1[k] = 0

analytics2 = {}

app = Flask(__name__,static_url_path='/static')

@app.route('/', methods=['GET','POST'])
def home():
    if 'username' in session:
        return redirect(url_for('loggedin'))
    if request.method == 'POST':
        return redirect(url_for('login'))
    return render_template('new.html',l1=citydata())

@app.route('/login', methods=['GET','POST'])
def login():
    error = ""
    if 'username' in session:
        return redirect(url_for('loggedin'))
    value = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        val = check(username.lower(),password)
        print val
        if val:
            session['username'] = request.form['username']
            return redirect(url_for('loggedin'))
        else:
            value = "Access Denied"
    return render_template('login.html',value = value)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/signup', methods=['GET','POST'])
def signup():
    v1=v2=v3=v4=v5=""
    error = ""

    if request.method == 'POST':
        if request.form['password'] == request.form['repassword']:
            adding(request.form['username'],request.form['FirstName'], request.form['LastName'],
                   request.form['password'],(request.form['mobile']), request.form['email'])
            return redirect(url_for('login'))
        else:
            error = 'Passwords dont Match'
            v1 = request.form['FirstName']
            v2 = request.form['LastName']
            v3 = request.form['username']
            v4 = request.form['mobile']
            v5 = request.form['email']
    return render_template('register.html', error=error, v1=v1, v2=v2, v3=v3, v4=v4, v5=v5)


@app.route('/loggedin', methods=['GET','POST'])
def loggedin():
    global analytics1
    error = ""
    if 'username' in session:
        username_session = escape(session['username']).capitalize()
        if request.method == 'POST':
            if 'logout' in request.form:
                print 'Logged Out'
                session.clear()
                return redirect(url_for("login"))
            else:
                if 'place' in request.form:
                    place = request.form['place']
                    dept= request.form['tata']
                    arr = request.form['hello']
                    if arr >= dept:
                        analytics1[place] += 1
                        if dept not in analytics2:
                            analytics2[dept] = 1
                        else:
                            analytics2[dept] += 1
                        if arr not in analytics2:
                            analytics2[arr] = 1
                        else:
                            analytics2[arr] += 1
                        return redirect('/data/' + request.form['place'])
                    else:
                        error = "Invalid Entry"
        return render_template('loggedin.html', fname=getname(username_session).capitalize(),l1=citydata(),error = error)
    else:
        return redirect(url_for("home"))



@app.route('/data/<variable>', methods=['GET','POST'])
def data(variable):
    if 'username' in session:
        username_session = escape(session['username']).capitalize()
        url = 'https://www.triphobo.com/tripplans/' + variable + '-itinerary-1-day'
        url1 = "https://www.makemytrip.com/hotels/"+variable[:-4]+"-hotels.html"
        url2 = "https://www.makemytrip.com/flights/"+variable[:-4]+"-flight-tickets.html"
        try:
            wo = coded(variable[:-4])
        except:
            wo = ""
        url3 = "https://weather.com/en-IN/weather/today/l/"+coded(variable[:-4])+":1:IN"
        print url3
        url5 = "https://maps.googleapis.com/maps/api/streetview?size=600x600&location=40.720032,-73.988354&fov=90&heading=235&pitch=10&key=AIzaSyB_TCBB2MFU35bfBDMeUGC14t1bP51KgIM"
        a = variable + "dia"
        a = a.replace(',', ' ')
        a = a.replace(' ', '%20')
        url4 = "https://www.google.com/maps/embed/v1/place?q="+a+"&key=AIzaSyB_TCBB2MFU35bfBDMeUGC14t1bP51KgIM"
        print url4
        if request.method == "POST":
            if 'logout' in request.form:
                print 'Logged Out'
                session.clear()
                return redirect(url_for("login"))
            if 'photu' in request.form:
                return redirect("/vr/"+variable)
        if variable in citydata():
            return render_template('place.html',name=variable,url=url,fname=getname(username_session).capitalize(),url1=url1,url2=url2,url3=url3,url4=url4,url5=url5)
        else:
            return "ERROR CANT LOAD"

    else:
        return redirect(url_for("home"))







@app.route('/weather/<variable>', methods=['GET','POST'])
def weather(variable):
    if 'username' in session:
        username_session = escape(session['username']).capitalize()

        if request.method == "POST":
            if 'logout' in request.form:
                print 'Logged Out'
                session.clear()
                return redirect(url_for("login"))

        if variable in citydata():
            return render_template('weather.html',name=variable)
        else:
            return "ERROR CANT LOAD"

    else:
        return redirect(url_for("home"))










@app.route('/test', methods=['GET','POST'])
def test():
    return render_template('test.html')














@app.route('/vr/<variable>', methods=['GET','POST'])
def vr(variable):

    if 'username' in session:
        username_session = escape(session['username']).capitalize()
        z = getdata(variable)
        import random
        k = random.randint(0, len(z) - 1)
        if request.method == "POST":
            if 'logout' in request.form:
                print 'Logged Out'
                session.clear()
                return redirect(url_for("login"))
            if 'back' in request.form:
                return redirect("/data/"+variable)
            else:
                print "YOU PRESSED THE BUTTON"
                k = random.randint(0,len(z)-1)
        print "THIS IS VARIABLE", variable
        if variable in citydata():
            print z[k][1], k, len(z)

            return render_template('vr.html',lat=z[k][1],long=z[k][2],name=z[k][3])
        else:
            return "ERROR CANT LOAD"

    else:
        return redirect(url_for("home"))



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)