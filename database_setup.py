
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()

class Car(Base):
    __tablename__ = 'Car'
    id = Column(Integer, primary_key= True)
    model = Column(String(250))
    color = Column(String(250))
    year = Column(Integer)
    license_plate = Column(String(8))

    @property
    def serialize(self):
        return {
            'id' : self.id,
            'model' : self.model,
            'color' : self.color,
            'year' : self.year,
            'license_plate' : self.license_plate
        }

engine = create_engine('sqlite:///cars.db')

Base.metadata.create_all(engine)