#!/usr/bin/env python3

from datetime import datetime, timezone
from model.base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID


class User(Base):
    __tablename__ = "user"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    is_admin: Mapped[int] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now(timezone.utc), nullable=False
    )
