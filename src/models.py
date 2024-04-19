from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

#aqui empiezo a añadir codigo---------------------------
class Planeta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)
    gravedad = db.Column(db.String(80), unique=False, nullable=False)
    poblacion = db.Column(db.String(80), unique=False, nullable=False)
    habitable = db.Column(db.String(80), unique=False, nullable=False)
    tipo = db.Column(db.String(250), unique=False, nullable=False)
    clima = db.Column(db.String(250), unique=False, nullable=False)
    
    

    def __repr__(self):
        return '<Planeta %r>' % self.planeta

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "gravedad": self.gravedad,
            "poblacion": self.poblacion,
            "habitable": self.habitable,
            "tipo": self.tipo,
            "clima": self.clima,
            # do not serialize the password, its a security breach
        }
    

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)
    raza = db.Column(db.String(80), unique=False, nullable=False)
    altura = db.Column(db.String(80), unique=False, nullable=False)
    peso = db.Column(db.String(80), unique=False, nullable=False)
    sexo = db.Column(db.String(80), unique=False, nullable=False)
    color_pelo = db.Column(db.String(80), unique=False, nullable=False)
    
    

    def __repr__(self):
        return '<People %r>' % self.people

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "raza": self.raza,
            "altura": self.altura,
            "peso": self.peso,
            "sexo": self.sexo,
            "color_pelo": self.color_pelo,
            # do not serialize the password, its a security breach
        }
    

class Vehiculos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)
    tipo = db.Column(db.String(80), unique=False, nullable=False)
    velocidad = db.Column(db.String(80), unique=False, nullable=False)
    peso = db.Column(db.String(80), unique=False, nullable=False)
    tripulacion = db.Column(db.String(80), unique=False, nullable=False)
    armamento = db.Column(db.String(80), unique=False, nullable=False)
    
    

    def __repr__(self):
        return '<Vehiculos %r>' % self.Vehiculos

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "tipo": self.raza,
            "velocidad": self.velocidad,
            "peso": self.peso,
            "tripulacion": self.tripulacion,
            "armamento": self.armamento,
            # do not serialize the password, its a security breach
        }