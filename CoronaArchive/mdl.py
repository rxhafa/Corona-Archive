from CoronaArchive import mydb, signin
from flask_login import UserMixin

@signin.user_loader
def vis(visitor_id):
    return Visitor.query.get(int(visitor_id))

class Visitor(mydb.Model, UserMixin):
    id = mydb.Column(mydb.Integer, primary_key = True)
    name = mydb.Column(mydb.String(20), unique = True, nullable = False)
    email = mydb.Column(mydb.String(70), unique = True, nullable = False)
    address = mydb.Column(mydb.String(100), nullable = False)
    password = mydb.Column(mydb.String(60), nullable = False)
    def __repr__(this):
        return f"Visitor('{this.name}, {this.email}, {this.address}')"

class PlaceOwner(mydb.Model, UserMixin):
    id = mydb.Column(mydb.Integer, primary_key = True)
    name = mydb.Column(mydb.String(20), unique = True, nullable = False)
    email = mydb.Column(mydb.String(70), unique = True, nullable = False)
    place = mydb.Column(mydb.String(50), unique = True, nullable = False)
    address = mydb.Column(mydb.String(100), nullable = False)
    # qr = mydb.Column(mydb.String(20), nullable = False, default = qrcode.make())
    password = mydb.Column(mydb.String(60), nullable = False)
    # visitor_id = mydb.Column(mydb.Integer, mydb.ForeignKey('visitor.id'))
    def __repr__(this):
        return f"PlaceOwner('{this.name}, {this.email}, {this.place}, {this.address}')"

# class HospitalOfficial(mydb.Model, UserMixin):
#     id = mydb.Column(mydb.Integer, primary_key = True)
#     name = mydb.Column(mydb.String(20), unique = True, nullable = False)
#     email = mydb.Column(mydb.String(70), unique = True, nullable = False)
#     hospital_name = mydb.Column(mydb.String(50), unique = True, nullable = False)
#     address = mydb.Column(mydb.String(100), nullable = False)
#     password = mydb.Column(mydb.String(60), nullable = False)
#     def __repr__(this):
#         return f"HospitalOfficial('{this.hospital_name}, {this.email}, {this.address}')"

# class Agent(mydb.Model, UserMixin):
#     id = mydb.Column(mydb.Integer, primary_key = True)
#     name = mydb.Column(mydb.String(20), unique = True, nullable = False)
#     email = mydb.Column(mydb.String(70), unique = True, nullable = False)
#     address = mydb.Column(mydb.String(100), nullable = False)
#     password = mydb.Column(mydb.String(60), nullable = False)
#     # viss = mydb.relationship('Visitor', lazy = True)
#     # pos = mydb.relationship('PlaceOwner', lazy = True)
#     # hps = mydb.relationship('Hospital', lazy = True)
#     def __repr__(this):
#         return f"HospitalOfficial('{this.name}, {this.email}, {this.address}')"