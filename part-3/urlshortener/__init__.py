from flask import Flask, redirect, url_for, flash, render_template, request
from flask_security import login_required, logout_user
from .config import Config
from .models import db, security, user_datastore, ShortUrl
from .oauth import blueprint
from .cli import create_db
import datetime


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(blueprint, url_prefix="/login")
app.cli.add_command(create_db)
db.init_app(app)
security.init_app(app, user_datastore)

counter = 1
list_original_urls= []
list_ids = []
list_short_urls = []
list_date = []

def urlshortcode(num):

    """This function will take in an ID to a URL and convert it"""

    def urlshortcode_help(num, num_ar):
        if num < 26:
            num_ar.append(chr(num + 97))

        elif num >= 26 and num < 52:
            num_ar.append(chr((num-26)+65))

        elif num >= 52 and num < 62:
            num_ar.append(str(num-52))

        elif num >= 62:
            urlshortcode_help( int(num/62), num_ar )
            urlshortcode_help(num % 62, num_ar)
        return num_ar
        #End of helper

    code_array = []
    short_code = ""
    urlshortcode_help(num, code_array)
    return short_code.join(code_array)

def orignalurl(changed):

    """This function will take in a converted ID and convert it back"""

    def orignalurl_help(string, list):
        count = 0

        for i in range(len(list)):
            if list[i].islower():
                count = count + (ord(list[i])-97)

            elif list[i].isupper():
                count = count + (ord(list[i])- 65 + 26)
            else:
                count = count + (int(list[i]) + 52)

        if len(list) > 1:
            return count + ( 61*( len(list)-1))

        return count
        #End of helper

    chan_list = []
    for i in range(len(changed)):
        chan_list.append(changed[i])

    return orignalurl_help(changed,chan_list)

@app.route('/')
def start():
    return redirect('/home')

@app.route('/home', methods=['GET','POST'])
def shorten():
    global counter
    global list_original_urls
    global list_ids
    global list_short_urls
    global list_date

    if request.method == 'POST':
        db.create_all()
        origin = request.form['name']
        db.session.add(ShortUrl(original_url = origin, short_url= urlshortcode(counter), date= datetime.date.today()))
        flash('Congrats your URL has been shortened')
        counter = counter + 1
        db.session.commit()

    return render_template('home.html')


@app.route('/list', methods=['GET','POST'])
def list():
    list_original_urls = [record.original_url for record in db.session.query(ShortUrl.original_url)]
    list_ids = [record.id for record in db.session.query(ShortUrl.id)]
    list_short_urls = [record.short_url for record in db.session.query(ShortUrl.short_url)]
    list_date = [record.date for record in db.session.query(ShortUrl.date)]
    final_list = []

    for i in range(len(list_ids)):
        final_list.append( {'id':list_ids[i], 'ori': list_original_urls[i], 'short': list_short_urls[i], 'date': list_date[i]} )

    return render_template('list.html', final = final_list)


@app.route('/delete/<given_id>', methods=['GET','POST'])
def delete_URL(given_id = 0):
    if ShortUrl.query.filter_by(id = given_id) != None:
        db.session.delete(ShortUrl.query.filter_by(id = given_id).first())
        db.session.commit()
    return redirect('/list')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have logged out")
    return redirect(url_for("index"))
