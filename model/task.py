#!/usr/bin/env python3

from datetime import datetime, timezone
from model.base import Base
from sqlalchemy import String, Uuid, ForeignKey, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Task(Base):
    __tablename__ = "task"

    id: Mapped[Uuid] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(), nullable=False)
    run_count: Mapped[int] = mapped_column(nullable=False, default=0)
    automaton_id: Mapped[str] = mapped_column(
        ForeignKey("automaton.id"),
        String,
        nullable=False,
    )
    args: Mapped[list[str]] = mapped_column(ARRAY(String))
    config_file: Mapped[str] = mapped_column(String())
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now(timezone.utc), nullable=False
    )

    automaton = relationship("Automaton")
