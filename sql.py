import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Sequence
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

# 数据库连接:
mysql_engine = create_engine("mysql://lee:1234@localhost/tudb")
Base.metadata.create_all(mysql_engine)
# 创建DBSession类型:
DBSession = sessionmaker(bind=mysql_engine)
session = DBSession()

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
