from pydantic import BaseModel
from enum import IntEnum

class Departments(IntEnum):
  SCIENCE     = 0
  ENGINEERING = 1
  MEDICAL     = 2
  ARTS        = 3
  BUSINESS    = 4

class Genders(IntEnum):
  FEMALE = 0
  MALE = 1

class InboundRequest(BaseModel):
    age : int
    gender : Genders
    department : Departments
    cgpa : float
    sleep_duration : float
    study_hours : float
    social_media_hours : float
    physical_activity : float
    stress_level : int