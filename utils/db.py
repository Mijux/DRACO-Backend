#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from uuid import uuid4

from model.base import Base
from model.user import User


def init_db():
    engine = create_engine("sqlite:///database.db", echo=True)
    Base.metadata.create_all(engine)

    return engine


def insert_test(engine):
    with Session(engine) as session:
        user1 = User(
            id=uuid4(),
            username="Mijux",
            password="password123",
            email="mijux@nogg.ovh",
            is_admin=1,
        )

        session.add_all([user1])
        session.commit()
