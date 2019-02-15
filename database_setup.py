from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(32), nullable=False)
    email = Column(String(80), index=True)
    picture = Column(String(250))


class Genre(Base):
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in serialized format"""
        return {
            'id': self.id,
            'name': self.name
        }


class Movie(Base):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)
    year = Column(String(4))
    rating = Column(String(5))
    plot_summary = Column(String(250))
    poster_image = Column(String(250))
    genre_id = Column(Integer, ForeignKey('genre.id'))
    genre = relationship(Genre)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in serialized format"""
        return {
            'id': self.id,
            'title': self.title,
            'year': self.year,
            'rating': self.rating,
            'plot_summary': self.plot_summary,
            'poster_image': self.poster_image
        }


engine = create_engine('sqlite:///movies.db')


Base.metadata.create_all(engine)
