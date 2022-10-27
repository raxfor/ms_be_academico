from Repositorios.RepositorioEstudiante import RepositorioEstudiante
from Modelos.Estudiante import Estudiante

class ControladorEstudiante():
    def __init__(self):
        self.repositorioEstudiante = RepositorioEstudiante()

    def mostrar(self):
        return self.repositorioEstudiante.findAll()


    def crear(self, infoEstudiante):
        nuevoEstudiante = Estudiante(infoEstudiante)
        return self.repositorioEstudiante.save(nuevoEstudiante)

    def consultar(self, id):
        elEstudiante = Estudiante(self.repositorioEstudiante.findById(id))
        return elEstudiante.__dict__

    def actualizar(self, id, infoEstudiante):
        estudianteActual = Estudiante(self.repositorioEstudiante.findById(id))
        estudianteActual.cedula = infoEstudiante["cedula"]
        estudianteActual.nombre = infoEstudiante["nombre"]
        estudianteActual.apellido = infoEstudiante["apellido"]
        return self.repositorioEstudiante.save(estudianteActual)


    def eliminar(self, id):
        return self.repositorioEstudiante.delete(id)

