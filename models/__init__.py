from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amnesty import Amnesty
from models.review import Review
from models.place import Place
from models.state import State
from models.city import City
from models.user import User


MODELS = {
    "Amnesty": Amnesty,
    "BaseModel": BaseModel,
    "City": City,
    "Review": Review,
    "Place": Place,
    "State": State,
    "User": User,
}

storage = FileStorage()
storage.reload()
