from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.state import State
from models.user import User


MODELS = {
    "BaseModel": BaseModel,
    "State": State,
    "User": User,
}

storage = FileStorage()
storage.reload()
