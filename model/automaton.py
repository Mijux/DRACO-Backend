#!/usr/bin/env python3

from datetime import datetime, timezone
from model.base import Base
from sqlalchemy import String, Uuid
from sqlalchemy.orm import Mapped, mapped_column


class Automaton(Base):
    __tablename__ = "automaton"

    id: Mapped[Uuid] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(), nullable=False)
    executable: Mapped[str] = mapped_column(String(), nullable=False)
    version: Mapped[str] = mapped_column(String(), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now(timezone.utc), nullable=False
    )
