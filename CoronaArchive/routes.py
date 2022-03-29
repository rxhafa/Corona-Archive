from flask import Flask, render_template, url_for, redirect, flash
from CoronaArchive import app, mydb, encrypt
from CoronaArchive.forms import SignupVis, SignupPO, LoginForm
from CoronaArchive.mdl import Visitor, PlaceOwner
from flask_login import login_user

features = [
    {
        'test': 'Info',
        'title': 'Corona Archive',
        'content': 'We manage everything for you to enjoy your favourite places without a fuss.'
    }
]


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', features=features, title='Start')

@app.route("/imprint")
def imprint():
    return render_template('imprint.html', title='Imprint')

@app.route("/signup_visitor", methods=['GET', 'POST'])
def signup1():
    f1 = SignupVis()
    if f1.validate_on_submit():
        AuthPwd = encrypt.generate_password_hash(f1.password.data).decode('utf-8')
        vis = Visitor(name = f1.name.data, email = f1.email.data, address = f1.address.data, password = AuthPwd)
        mydb.session.add(vis)
        mydb.session.commit()
        flash(f'Congrats { f1.name.data }, you are officially in Corona Archive!!!', 'success')
        return redirect(url_for('index'))
    return render_template('signup1.html', title='Sign Up - Visitor', form=f1)

@app.route("/signup_place_owner", methods=['GET', 'POST'])
def signup2():
    f3 = SignupPO()
    if f3.validate_on_submit():
        AuthPwd = encrypt.generate_password_hash(f3.password.data).decode('utf-8')
        po = PlaceOwner(name = f3.name.data, email = f3.email.data, place = f3.place.data, address = f3.address.data, password = AuthPwd)
        mydb.session.add(po)
        mydb.session.commit()
        flash(f'Congrats { f3.name.data }, you are officially in Corona Archive!!!', 'success')
        return redirect(url_for('index'))
    return render_template('signup2.html', title='Sign Up - Place Owner', form=f3)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    f2 = LoginForm()
    if f2.validate_on_submit():
        vis = Visitor.query.filter_by(email = f2.email.data).first()
        po = PlaceOwner.query.filter_by(email = f2.email.data).first()
        # agent = Agent.query.filter_by(email = f2.email.data).first()
        # hp = HospitalOfficial.query.filter_by(email = f2.email.data).first()
        c1 = (vis and encrypt.check_password_hash(vis.password, f2.password.data))
        c2 = (po and encrypt.check_password_hash(po.password, f2.password.data))
        # c3 = (agent and encrypt.check_password_hash(agent.password, f2.password.data))
        # c4 = (hp and encrypt.check_password_hash(hp.password, f2.password.data))
        if c1:
            login_user(vis, remember = f2.rem.data)
            return redirect(url_for('index'))
        elif c2:
            login_user(po, remember = f2.rem.data)
            return redirect(url_for('index'))
        flash(f'Login was not possible :( Check the credentials', 'danger')
    return render_template('login.html', title='Login', form=f2)