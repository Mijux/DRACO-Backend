#!/usr/bin/env python3

from datetime import datetime, timezone
from model.base import Base
from sqlalchemy import String, Uuid, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Periodic(Base):
    __tablename__ = "periodic"

    id: Mapped[Uuid] = mapped_column(primary_key=True)
    task_id: Mapped[str] = mapped_column(
        ForeignKey("task.id"),
        String,
        nullable=False,
    )
    year_recursivity: Mapped[datetime] = mapped_column()
    month_recursivity: Mapped[datetime] = mapped_column()
    day_recursivity: Mapped[bool] = mapped_column(default=datetime.now(timezone.utc))
    periode_recursivity: Mapped[datetime] = mapped_column(
        default=datetime.now(timezone.utc)
    )
    at_hour: Mapped[int] = mapped_column()
    at_minute: Mapped[int] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now(timezone.utc), nullable=False
    )

    task = relationship("Task")
