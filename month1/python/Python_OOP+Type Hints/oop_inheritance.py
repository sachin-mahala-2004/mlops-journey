# Parent class 
class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    
    def speak(self):
        return f"{self.name} says {self.sound}"
    
    def __str__(self):
        return f"Animal({self.name})"
    
# Child Class

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name,"Woof")
        self.breed = breed 
        
    def speak(self):
        return f"{self.name} barks: {self.sound}!"
    
    def fetch(self):
        return f"{self.name} fetches the ball!"
    
dog = Dog("Bruno","Labrador")
print(dog)
print(dog.speak())
print(Animal.speak(dog)) 
print(dog.name)   
print(dog.breed)
print(dog.fetch())

print(isinstance(dog,Dog))
print(isinstance(dog,Animal))
print(isinstance(Dog,Animal))
print(issubclass(Dog,Animal))
print(issubclass(Animal,Dog))

#Multi-level Inheritence 
class BaseModel:
    def __init__(self,name):
        self.name = name
    
    def train(self,data):
        raise NotImplementedError("Subclass must implement train()")
    
    def predict(self,x):
        raise NotImplementedError("Subclass must implement predict()")
    
    
class SklearnModel(BaseModel):
    def __init__(self,name,sklearn_estimator):
        super().__init__(name)
        self.estimator = sklearn_estimator
        self._trained = False
        
    def train(self, data):
        X, y = data
        self.estimator.fit(X, y)
        self._trained = True
        print(f"{self.name} trained successfully")

    def predict(self, x):
        if not self._trained:
            raise RuntimeError("Model not trained yet")
        return self.estimator.predict(x)


class LogisticModel(SklearnModel):
    def __init__(self):
        from sklearn.linear_model import LogisticRegression
        super().__init__("LogisticRegression", LogisticRegression())

    def predict_proba(self, x):
        return self.estimator.predict_proba(x)

X_train = [[8, 7], [2, 4], [7, 8], [3, 5]]
y_train = [1, 0, 1, 0]
training_data = (X_train,y_train)

model = LogisticModel()
model.train(training_data)
print(model.predict([[4,5]]))

