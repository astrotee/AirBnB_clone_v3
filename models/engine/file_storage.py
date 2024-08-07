#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from functools import reduce


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            return {k: v for k, v in FileStorage.__objects.items()
                    if isinstance(v, cls)
                    }
        return FileStorage.__objects

    def get(self, cls, id):
        """get a single object by id"""
        return FileStorage.__objects.get(cls.__class__ .__name__ + '.' + id)

    def count(self, cls=None):
        """count the number of objects in storage for given class"""
        if cls:
            return reduce(lambda a, b: a + 1 if isinstance(b, cls) else a,
                          FileStorage.__objects.values(), 0)
        return len(FileStorage.__objects)

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def delete(self, obj=None):
        """Deletes an object from storage dictionary"""
        if obj is None:
            return
        for k, v in FileStorage.__objects.items():
            if obj is v:
                break
        else:
            return
        del FileStorage.__objects[k]

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def close(self):
        """deserializing the JSON file to objects"""
        self.reload()
