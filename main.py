from sqlalchemy import String, Integer, Column, create_engine, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///hospital.db', echo=True)

connector_table = Table(
    'location_table',
    Base.metadata,
    Column('patient_id', ForeignKey('patients.id')),
    Column('ward_id', ForeignKey('wards.id'))
)


class Doctor (Base):
    __tablename__ = 'doctors'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    specialization = Column(String(), nullable=False)
    email = Column(String())

    def __repr__(self):
        return f"Doctor name: {self.name}, Specialization: {self.specialization}"
    

class Nurse(Base):
    __tablename__ = 'nurses'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    shift = Column(String(), nullable=False)


    def __repr__(self):
        return f"Nurse name: {self.name}, Shift: {self.shift}"
    
class Patient (Base):
    __tablename__ = 'patients'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    arrival_time = Column(String())
    assigned_doctor = Column(Integer(), ForeignKey('doctors.id'))
    ward = Column(Integer(), ForeignKey('wards.id'))


    def __repr__(self):
        return f"Patient name: {self.name}, Waiting Number: {self.id}, Assigned Doctor: {self.assigned_doctor}"
    
class Ward(Base):
    __tablename__ = 'wards'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)

    def __repr__(self):
        return f"Name: {self.name}"
    
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)