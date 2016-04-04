from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

engine = create_engine('sqlite:////home/bogdan/PycharmProjects/sandbox/lel.db')
Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)

    def __str__(self):
        return str(self.id) + ' ' + self.username


session = Session()

user1 = User(username='bushig')
session.add(user1)
session.commit()
first = session.query(User)
print(first)