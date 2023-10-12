from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = 'And blood black nothingness began to spin. A series of cells interlinked within cells interlinked within cells interlinked within one stem'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/perpus_calvin'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models import *
from routes import *

### models ###

# class Room_bookings(db.Model):
#     id = db.Column('id',db.Integer,primary_key=True)
#     student_id = db.Column(db.Integer,db.ForeignKey('students.nim'))
#     booking_date = db.Column(db.Date)
#     booking_time = db.Column(db.Time)
#     end_time = db.Column(db.Time)
#     room_name = db.Column(db.String(200))

# class Students(db.Model):
#     nim = db.Column('nim',db.Integer,primary_key=True)
#     full_name = db.Column(db.String)
#     password = db.Column(db.String)
#     fine = db.Column(db.Float,default=0.0)
#     room_bookings = db.relationship('Room_bookings',backref='room_bookings')
#     peminjaman_ongoing = db.relationship('Peminjaman_ongoing',backref='peminjaman_ongoing')

# class Peminjaman_ongoing(db.Model):
#     id_peminjaman = db.Column('id_peminjaman',db.Integer,primary_key=True)
#     id_buku = db.Column(db.Integer,db.ForeignKey('catalogue.id_buku')) 
#     nim_peminjam = db.Column(db.Integer,db.ForeignKey('students.nim'))
#     tanggal_peminjaman = db.Column(db.Date)
#     waktu_peminjaman = db.Column(db.Time)

# class Peminjaman_done(db.Model):
#     id_peminjaman = db.Column('id_peminjaman',db.Integer,primary_key=True)
#     id_buku = db.Column(db.Integer,db.ForeignKey('catalogue.id_buku')) 
#     nim_peminjam = db.Column(db.Integer,db.ForeignKey('students.nim'))
#     tanggal_peminjaman = db.Column(db.Date)
#     tanggal_pengembalian = db.Column(db.Date)

# class Catalogue(db.Model):
#     id_buku = db.Column('id_buku',db.Integer,primary_key=True)
#     nama_buku = db.Column(db.String(200))
#     deskripsi_buku = db.Column(db.String(255))
#     tanggal_masuk = db.Column(db.Date)
#     tanggal_terbit = db.Column(db.Date)
#     author = db.Column(db.String(255))
#     genre = db.Column(db.String(255))
#     status = db.Column(db.String(255))

### models ###

if __name__ == '__main__':
    app.run(debug=True)
    


