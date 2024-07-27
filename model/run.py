#!/usr/bin/env python3

from datetime import datetime, timezone
from model.base import Base
from sqlalchemy import String, Uuid, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Run(Base):
    __tablename__ = "run"

    id: Mapped[Uuid] = mapped_column(primary_key=True)
    task_id: Mapped[str] = mapped_column(
        ForeignKey("task.id"),
        String,
        nullable=False,
    )
    status: Mapped[int] = mapped_column()
    value_returned: Mapped[str] = mapped_column(String())
    logfile: Mapped[str] = mapped_column(String(), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now(timezone.utc), nullable=False
    )

    task = relationship("Task")
