from ninja import Schema
from datetime import datetime
from workouts.schema import Exercise

class Equipament(Schema):
  name = str

class Muscles(Schema):
  name = str
  
  
class Exercise(Schema):
  name = str
  description = str
  gif_url = str
  category_id: int
  equipment_id: int
  
  class ExerciseMuscles(Schema):
    exercise_id: int
    muscle_id: int
    
class NotFoundSchema(Schema):
  message: str