#used as example


from db import db
from model_utilities import is_in_range

class PresentModel(db.Model):
    
    __tablename__ = "presents";
    _id = db.Column(db.Integer, primary_key=True)
    
    kid_id = db.Column(db.Integer, db.ForeignKey("kids._id"))
    kid = db.relationship('KidModel')
    
    present_type = db.Column(db.Integer)
    is_done = db.Column(db.Boolean)
    year = db.Column(db.Integer)
    
    def __init__(self, kid_id, present_type, year, is_done):
        self.kid_id = kid_id
        self.present_type = present_type
        self.year = year
        self.is_done = is_done
                
    def to_json(self):
        if (self.kid == None):
            return {"id": self._id,
                "kid_id": self.kid_id,
                "present_type": self.present_type,
                "year": self.year,
                "is_done": self.is_done,
                "kid_name": "None, probably should delete this",
                "kid_birthday": "None, probably should delete this"}
        
        return {"id": self._id,
                "kid_id": self.kid_id,
                "present_type": self.present_type,
                "year": self.year,
                "is_done": self.is_done,
                "kid_name": self.kid.name,
                "kid_birthday": str(self.kid.birthday)}

    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def deleteMe(self):
        db.session.delete(self)
        db.session.commit()
        
    @classmethod
    def get (cls, _id):
        return cls.query.filter_by(_id=_id).first();
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def get_from_date_to_date(cls, start_date, end_date):
        if end_date:
            end_year = end_date.year
        else:
            end_year = 3000
        possible = db.session.query(cls).filter(cls.year < end_year + 1).all()
        return_body = []
        for present in possible:
            if is_in_range(present, start_date, end_date):
                return_body.append(present)
            
        return return_body
    
    
        
                