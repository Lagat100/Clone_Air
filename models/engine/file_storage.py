import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os.path as path

class FileStorage:
    __file_path = "file.json"
    __objects = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_objs = {}
        for key, obj in self.__objects.items():
            if isinstance(obj, BaseModel):
                serialized_objs[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objs, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, val in data.items():
                    class_name, obj_id = key.split('.')
                    cls = self.__objects.get(class_name)
                    if cls:
                        self.__objects[key] = cls(**val)
        except FileNotFoundError:
            pass
