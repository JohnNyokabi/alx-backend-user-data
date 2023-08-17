#!/usr/bin/env python3
"""DB module"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError, NoResultFound

from user import Base, User

class DB:
    """DB class"""

    def __init__(self) -> None:
        """Initialize a new DB instance"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add a new user to the database and return the user object.
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """
        Find and return the first user found in the users table
        filtered by the given keyword arguments.
        """
        if not kwargs:
            raise InvalidRequestError("No filter criteria provided")
        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound("No user found with the given criteria")
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Update the attributes of a user based on the provided user_id
        and keyword arguments. Commit changes to the database.
        """
        user_to_update = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if not hasattr(user_to_update, key):
                raise ValueError(f"User has no attribute: {key}")
            setattr(user_to_update, key, value)
        self._session.commit()
