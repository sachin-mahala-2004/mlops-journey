# dunder = double underscore
# 1. __str__ and __repr__

class Model:
    def __init__(self, name, version, accuracy):
        self.name = name
        self.version = version
        self.accuracy = accuracy
    
    def __str__(self):
        # For humans - used by print()
        return f"Model: {self.name} v{self.version} (accuracy: {self.accuracy:.1%})"
    
    def __repr__(self):
        # For developers - used in console/debugger , should be unambiguous   
        return f"Model(name='{self.name}',version='{self.version}', accuracy={self.accuracy})"
    
m = Model("RandomForest","1.0",0.957)

print(m) 
print(repr(m))
print(f"{m}")

#--------------------------------------
# __len__ , __eq__ , __lt__ , __contains__ , __getitem__

class Dataset:
    def __init__ (self, name, data):
        self.name = name
        self.data = data
        
    def __len__ (self):
        return len(self.data)
    
    def __eq__(self, other):
        return len(self.data) == len(other.data)
    
    def __lt__(self, other):
        return len(self.data) < len(other.data)
    
    def __contains__(self, item):
        return item in self.data
    
    def __getitem__(self, index):
        return self.data[index]
    
ds1 = Dataset("train", [1,2,3,4,5])
ds2 = Dataset("test",[1,2,3])

print(len(ds1)) 
print(len(ds2))
print(ds1 == ds2)
print(ds1 > ds2)
print(3 in ds1)
print(ds1[0])
print(sorted([ds2,ds1]))


#-------------------------------------------------------
#PART 5 — @property

class Cirle:
    def __init__(self,radius):
        self._radius = radius
        
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self,value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @radius.deleter
    def radius(self):
        print("Deleting radius")
        del self._radius
        
    @property
    def area(self):
        #read-only computed property - no setter
        return 3.14 * (self._radius ** 2)
    
    @property
    def diameter(self):
        return 2* self._radius
    
c = Cirle(5)
print(c.radius)
print(c.area)
print(c.diameter)

c.radius = 10  #calls the setter
print(c.radius)

try:
    c.radius = -1  #ValueError : Radius cannot be negative
except ValueError as e:
    print(f"ValueError: {e}")
    
try:
    c.area = 100     # AttributeError - no setter defined (read-only)
except AttributeError as e:
    print(e)
    

#---------------------------------------------------------------------
# Real MLOps use case

class MLModel:
    def __init__(self,name):
        self.name = name
        self._loaded = False
        self._model = None
        
    @property
    def is_loaded(self):
        return self._loaded
    
    @property
    def model(self):
        if not self._loaded:
            raise RuntimeError("Model not loaded. Call load() first.")
        return self._model
    
    @model.deleter
    def model(self):
        self._model = None
        self._loaded = False
    
    def load(self,path):
        #simulate loading
        self._model = f"<model form {path}>"
        self._loaded = True

m = MLModel("Regression")
try:
   print(m.model)
except RuntimeError as e:
    print(f"RuntimeError: {e}")
    
print(m.is_loaded)
m.load("models/iris.pkl")
print(m.is_loaded)
print(m.model)
del m.model

try:
   print(m.model)
except RuntimeError as e:
    print(f"RuntimeError: {e}")
    
    
    
#---------------------------------------------------------
# @classmethod 
import json
class Config:
    def __init__ (self, host, port, debug, db_url):
        self.host = host 
        self.port = port 
        self.debug = debug 
        self.db_url = db_url
        
    @classmethod
    def from_dict(cls,data:dict):
        return cls(
            host = data.get("host","localhost"),
            port = data.get("port",8000),
            debug = data.get("debug",False),
            db_url = data.get("db_url","sqlite:///db.sqlite3")
        )
        
    @classmethod
    def from_json_file(cls,path:str):
        with open(path,"r") as f:
            data = json.load(f)
            return cls.from_dict(data)
        
    @classmethod 
    def development(cls):
        return cls("localhost",8000,True,"sqlite:///dev.db")
    
    @classmethod
    def __repr__(self):
        return f"Config(host={self.host},port={self.port},debug={self.debug})"
    