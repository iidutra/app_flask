
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime(6), nullable=False)
    last_update = db.Column(db.DateTime(6), nullable=True)
    active = db.Column(db.Boolean(), default=1, nullalbe=False)
    role = db.Column(db.Integer(), db.ForeignKey(Role.id), nullable=False)

    def __repr__(self):
        return '%s - %s' % (self.id, self.username)

    def set_password(self, password):
        self.password = pbkdf2_sha256.hash(password)

    def hash_password(self, password):
        try:
            return pbkdf2_sha256.hash(password)
        except Exception as e:
            print("Erro ao criptografar senha %s" % e)

    def verify_password(self, password_no_hash, password_database):
        try:
            return pbkdf2_sha256.verify(password_no_hash, password_database)
        except ValueError:
            return False


class State(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class DiseaseState(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)

    def __repr__(self):
        return self.name


disease_patient = db.Table('disease_patient',
                           db.Column('disease_id', db.Integer, db.ForeignKey('disease_id')),
                           db.Column('patient_id', db.Integer, db.ForeignKey('patient_id'))
                           )


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(40), unique=True, nullable=False)
    state = db.Column(db.Integer, db.ForeignKey(State.id), nullable=False)
    diseaseState = db.Column(db.Integer, db.ForeignKey(DiseaseState.id), nullable=False)
    estado = relationship(State)
    last_state = db.Column(db.Date, nullable=True)
    estadoSaude = relationship(DiseaseState)
    diseases = db.relationship('Disease', secondary=disease_patient, backref=db.backref('patients', lazy=True))

    def __repr__(self):
        self.name


class Disease(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(40), unique=True, nullable=False)

    def __repr__(self):
        self.name
