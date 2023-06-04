import os
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


database = os.getenv('DB_URI', "postgresql://juser:cfytr666131@localhost/jservicedb")


# Создание базы данных:
Base = declarative_base()
engine = create_engine(database)
Session = sessionmaker(autoflush=False, bind=engine)


class Questions(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False, default="")
    answer = Column(String, nullable=False, default="")
    date_of_question = Column(DateTime)


Base.metadata.create_all(bind=engine)
db = Session()

