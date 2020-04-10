import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Float, Date, Integer, Sequence
from sqlalchemy.ext.declarative import declarative_base





print(sqlalchemy.__version__) 

#创建模型
# 创建对象的基类:
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))
    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                                self.name, self.fullname, self.nickname)

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer,  primary_key=True)
    p0 = Column(Integer)
    p1 = Column(Integer)
    p2 = Column(Integer)
    p3 = Column(Integer)
    p4 = Column(Integer)
    p5 = Column(Integer)
    p6 = Column(Integer)
    p7 = Column(Integer)
    p8 = Column(Integer)
    p9 = Column(Integer)
    p10 = Column(Integer)
    p11 = Column(Integer)
    n1 = Column(Integer)
    n2 = Column(Integer)
    n3 = Column(Integer)
    n4 = Column(Integer)
    n5 = Column(Integer)
    n6 = Column(Integer)
    n7 = Column(Integer)
    n8 = Column(Integer)
    n9 = Column(Integer)
    n10 = Column(Integer)
    n11 = Column(Integer)
    def __repr__(self):
        return "<User(name='%d')>" % (self.id,)

class sql_ops:      
    def __init__ ( self ):
        # 数据库连接:
        mysql_engine = create_engine("mysql://lee:1234@localhost/tudb")
        Base.metadata.create_all(mysql_engine)

        # 创建DBSession类型:
        DBSession = sessionmaker(bind=mysql_engine)
        session = DBSession()
    def add_grade(self):
        

'''
# session 
ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
session.add(ed_user)

session.add_all([
    User(name="Wendy", fullname="Wendy Williams", nickname="foobar"),
    User(name="mary", fullname="Mary Contrary", nickname="xxg527"),
    User(name="fred", fullname="Fred Flinstone", nickname="blah")
])

session.commit()

our_user = session.query(User).filter_by(name='fred').first() 
print(our_user)
'''


