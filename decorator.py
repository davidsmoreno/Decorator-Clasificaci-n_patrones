from functools import wraps

class Utilities(object):

    @staticmethod 
    def logger(f): 
        @wraps(f)  
        def wrapper(self, *args, **kwargs): 
            print("Antes:", self.sonido)
            result = f(self, *args, **kwargs)
            print("Despues:", self.sonido)
            return result
        return wrapper

class Dog(object):
    def __init__(self):
        self.sonido = "Waaf!"

    @Utilities.logger
    def Correr(self):
        print("Corriendo")