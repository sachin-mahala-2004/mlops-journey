from sqlalchemy import String
from sqlalchemy.orm import Mapped , mapped_column, relationship
from datetime import datetime
from sqlalchemy import DateTime,func
from sqlalchemy import ForeignKey,Numeric
from decimal import Decimal

from database import Base

class Student(Base):
    __tablename__ = "students"
    student_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255),unique=True,index=True)
    major: Mapped[str| None] = mapped_column(String(100))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),server_default=func.now())
    grades : Mapped[list["Grade"]] = relationship(back_populates="student",cascade="all,delete-orphan")
    
class Grade(Base):
    __tablename__= "grades"
    grade_id: Mapped[int] = mapped_column(primary_key=True)
    grade: Mapped[Decimal|None] = mapped_column(Numeric(5,2))
    student_id:Mapped[int] = mapped_column(ForeignKey("students.student_id",ondelete="CASCADE"))
    student: Mapped["Student"] = relationship(back_populates="grades")