from abc import ABC, abstractmethod

class IInformacion(ABC):
    @abstractmethod
    def mostrar_info(self) -> str:
        pass

class Usuario(IInformacion, ABC):
    def __init__(self, nombre: str, correo: str):
        self.nombre = nombre
        self.correo = correo

    @abstractmethod
    def mostrar_info(self) -> str:
        pass
