class Settings:
    def __init__(self):
        self.model_name = "iris classifier"
        
def get_settings()-> Settings:
    return Settings()

obj = Settings()
print(obj.model_name)