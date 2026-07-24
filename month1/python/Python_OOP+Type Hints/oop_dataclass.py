from dataclasses import dataclass,field
from typing import List,Optional

@dataclass
class ModelMetadata:
    name:       str
    version:    str
    accuracy:   float
    features:   List[str]
    description: Optional[str] = None       # default value
    tags:       List[str]     = field(default_factory=list)  # mutable default

    def is_production_ready(self) -> bool:
        return self.accuracy >= 0.90


# Python auto-generates __init__, __repr__, __eq__
m = ModelMetadata(
    name     = "iris_classifier",
    version  = "1.0.0",
    accuracy = 0.957,
    features = ["sepal_length", "sepal_width", "petal_length", "petal_width"],
    tags     = ["production", "iris"]
)

print(m)              # ModelMetadata(name='iris_classifier', ...)
print(m.accuracy)     # 0.957
print(m.is_production_ready())  # True

m2 = ModelMetadata(
    name="iris_classifier", version="1.0.0",
    accuracy=0.957,
    features=["sepal_length","sepal_width","petal_length","petal_width"]
)
print(m == m2)  