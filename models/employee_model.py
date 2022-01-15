from db import db

class EmployeeModel(db.Model):
    
    __tablename__ = "employees"
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    monday = db.Column(db.Integer)
    tuesday = db.Column(db.Integer)
    wednesday = db.Column(db.Integer)
    thursday = db.Column(db.Integer)
    friday = db.Column(db.Integer)
    
    def __init__(self, _id, name, email, workdays=(0, 0, 0, 0, 0)):
        self._id = _id
        self.name = name
        self.email = email
        self.monday = workdays[0]
        self.tuesday = workdays[1]
        self.wednesday = workdays[2]
        self.thursday = workdays[3]
        self.friday = workdays[4]
        
    def to_json (self):
        return {self._id: {"name": self.name,
                           "email": self.email,
                           "monday": self.monday,
                           "tuesday": self.tuesday,
                           "wednesday": self.wednesday,
                           "thursday": self.thursday,
                           "friday": self.friday
            }}
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    '''This class returns the object if name or id is found. Therefor no 
    updates on db are allowed, if object got returned with its name,
    because name can tecnically be the same on two rows'''
    @classmethod
    def get(cls, param):
        employee = cls.query.filter_by(_id=param).first()
        if employee:
            return employee
        emloyee = cls.query.filter_by(name=param).first()
        if employee:
            return employee
        
    @classmethod
    def get_all(cls):
        return cls.query.all()

