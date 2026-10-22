from datetime import datetime 
from decimal import Decimal
from database import Base
from sqlalchemy.orm import Mapped , mapped_column, relationship
from sqlalchemy import (
    String,func,DateTime,Numeric,ForeignKey,CheckConstraint,Index,
)
from sqlalchemy.dialects.postgresql import JSONB

class Student(Base):
    __tablename__ = "students"
    student_id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(100))
    email:Mapped[str] = mapped_column(String(200),unique=True)
    major:Mapped[str | None] = mapped_column(String(100))
    enrollment_year:Mapped[int|None]
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),server_default=func.now())
    grades:Mapped[list["Grade"]] = relationship(back_populates="student",cascade="all,delete-orphan")
    
    def __repr__(self):
        return f"Student id = {self.student_id} name = {self.name}"

class Course(Base):
    __tablename__ = "courses"
    course_id:Mapped[int]=mapped_column(primary_key=True)
    course_name:Mapped[str]=mapped_column(String(200))
    department:Mapped[str|None] = mapped_column(String(100))
    credits:Mapped[int|None]
    grades:Mapped[list["Grade"]] = relationship(back_populates="course")
    
    __table_args__ = (
        CheckConstraint("credits > 0" ,name="ck_courses_credits_positive")
    )
    def __repr__(self) -> str:
        return f"Course id = {self.course_id} name = {self.course_name}"
class Grade(Base):
    __tablename__ = "grades"
    grade_id:Mapped[int] = mapped_column(primary_key=True)
    grade:Mapped[Decimal|None] = mapped_column(Numeric(5,2))
    semester:Mapped[str | None] = mapped_column(String(100))
    student_id:Mapped[int] = mapped_column(ForeignKey("students.student_id",ondelete="CASCADE"))
    course_id:Mapped[int] = mapped_column(ForeignKey("courses.course_id",ondelete="RESTRICT"))
    student:Mapped["Student"] = relationship(back_populates="grades")
    course:Mapped["Course"] = relationship(back_populates="grades")
    
    __table_args__ = (
        CheckConstraint("grade >= 0 AND grade <= 100",name="ck_grades_range"),
        Index("idx_grades_student_course","student_id","course_id"),
        Index("idx_grades_course","course_id")
    )
    
    def __repr__(self):
        return f"Grade id = {self.grade_id} student = {self.student} value = {self.grade}"
    
class Prediction(Base):
    """Every prediction your service makes logs here."""
    __tablename__ = "predictions"
    
    prediction_id:Mapped[int] = mapped_column(primary_key=True)
    model_name:Mapped[int] = mapped_column(String(100))
    model_version:Mapped[int] = mapped_column(String(50))
    features:Mapped[dict] = mapped_column(JSONB)
    prediction:Mapped[float|None]
    confidence:Mapped[float|None]
    latency:Mapped[int|None]
    created_at:Mapped[datetime] = mapped_column(DateTime(timezone=True),server_default=func.now())
    
    __table_args__ = (
        CheckConstraint("confidence >=0 AND confidence <=1",name="ck_predictions_confidence"),
        Index("idx_pred_model_created_at","model_name","created_at"),
        Index("idx_pred_features","features",postgresql_using = "gin")
    )
    
    def __repr__(self):
        return (f"Prediciton id = {self.prediction_id}"
                f"model={self.model_name}:{self.model_version}")
        
        
